from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column
from sqlalchemy import func
from .models import Beverage, Ingredient, Order, OrderDetail, Size, db
from .serializers import (
    BeverageSerializer,
    IngredientSerializer,
    OrderSerializer,
    SizeSerializer,
    ma,
)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(
        cls,
        order_data: dict,
        ingredients: List[Ingredient],
        beverages: List[Beverage],
    ):
        new_order = cls.model(**order_data)

        ingredients_details = (
            OrderDetail(
                order_id=new_order._id,
                ingredient_id=ingredient._id,
                ingredient_price=ingredient.price,
                total_detail_price=ingredient.price,
            )
            for ingredient in ingredients
        )

        beverages_details = (
            OrderDetail(
                order_id=new_order._id,
                beverage_id=beverage._id,
                beverage_price=beverage.price,
                total_detail_price=beverage.price,
            )
            for beverage in beverages
        )

        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all(ingredients_details)
        cls.session.add_all(beverages_details)
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f"Method not suported for {cls.__name__}")


class IndexManager(BaseManager):
    @classmethod
    def test_connection(cls):
        cls.session.query(column("1")).from_statement(text("SELECT 1")).all()


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        query = cls.session.query(cls.model)
        return query.filter(cls.model._id.in_(set(ids))).all() or []


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        query = cls.session.query(cls.model)
        return query.filter(cls.model._id.in_(set(ids))).all() or []


class ReportManager:
    session = db.session

    @classmethod
    def get_most_requested_ingredient(cls):
        return (
            cls.session.query(
                Ingredient,
                func.count(OrderDetail.ingredient_id),
            )
            .join(OrderDetail)
            .group_by(Ingredient)
            .order_by(func.count(OrderDetail.ingredient_id).desc())
            .first()
        )

    @classmethod
    def get_most_requested_beverage(cls):
        return (
            cls.session.query(
                Beverage,
                func.count(OrderDetail.beverage_id),
            )
            .join(OrderDetail)
            .group_by(Beverage)
            .order_by(func.count(OrderDetail.beverage_id).desc())
            .first()
        )

    @classmethod
    def get_month_with_more_revenue(cls):
        return (
            cls.session.query(
                Order.date,
                func.sum(Order.total_price),
            )
            .group_by(Order.date)
            .order_by(func.sum(Order.total_price).desc())
            .first()
        )

    @classmethod
    def get_top_three_customers(cls):
        return (
            cls.session.query(
                Order,
                func.sum(Order.total_price),
            )
            .group_by(Order.client_dni)
            .order_by(func.sum(Order.total_price).desc())
            .limit(3)
            .all()
            or []
        )

    @classmethod
    def get_report(cls):
        ingredient, counted_ingredients = cls.get_most_requested_ingredient()
        beverage, counted_beverages = cls.get_most_requested_beverage()
        top_date, total_revenue = cls.get_month_with_more_revenue()
        top_3_customers = cls.get_top_three_customers()

        return {
            "most_requested_ingredient": {
                "name": ingredient.name,
                "price": ingredient.price,
                "count": counted_ingredients,
            },
            "most_requested_beverage": {
                "name": beverage.name,
                "price": beverage.price,
                "count": counted_beverages,
            },
            "month_with_more_revenue": {
                "name": top_date.strftime("%B"),
                "total": round(total_revenue, 2),
            },
            "top_3_customers": [
                {
                    "dni": customer.client_dni,
                    "name": customer.client_name,
                    "address": customer.client_address,
                    "phone": customer.client_phone,
                    "total_spent": round(spent, 2),
                }
                for customer, spent in top_3_customers
            ],
        }
