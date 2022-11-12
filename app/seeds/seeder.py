from random import randrange
from datetime import timedelta, datetime
from flask_seeder import Seeder, Faker, generator
from app.repositories.models import (
    Size,
    Beverage,
    Ingredient,
    Order,
    OrderDetail,
)


class SizeSeeder(Seeder):
    def run(self):
        faker = Faker(
            cls=Size,
            init={
                "_id": generator.Sequence(start=1, end=5),
                "price": generator.Integer(start=8, end=25),
                "name": generator.String(
                    "(Personal|Medium|Familiar|MegaFamiliar|GigaFamiliar)",
                ),
            },
        )
        for size in faker.create(5):
            self.db.session.add(size)


class IngredientSeeder(Seeder):
    def run(self):
        faker = Faker(
            cls=Ingredient,
            init={
                "_id": generator.Sequence(start=1, end=5),
                "price": generator.Integer(start=1, end=2),
                "name": generator.String(
                    "("
                    + "Chedar|Cottage|Meat|Bacon|Salami|Mushrooms|"
                    + "Onion|Pineapple|Chicken|Peperoni"
                    + ")"
                ),
            },
        )
        for ingredient in faker.create(5):
            self.db.session.add(ingredient)


class BeverageSeeder(Seeder):
    def run(self):
        faker = Faker(
            cls=Beverage,
            init={
                "_id": generator.Sequence(start=1, end=5),
                "price": generator.Integer(start=2, end=5),
                "name": generator.String(
                    "(Coca Cola|Stripe|Water|Coffee|Capuchino|Orange Juice)",
                ),
            },
        )

        for ingredient in faker.create(5):
            self.db.session.add(ingredient)


class OrderSeeder(Seeder):
    def run(self):
        faker = Faker(
            cls=Order,
            init={
                "_id": generator.Sequence(start=1, end=100),
                "size_id": generator.Integer(start=1, end=5),
                "client_name": generator.String(
                    "(Jon|Alexander|Maria|Ana|juan|Javier)",
                ),
                "client_dni": generator.String("1[0-9]{9}"),
                "client_address": generator.String(
                    "("
                    + "Street-1 Interception-1|Street-2 Interception-2|"
                    + "Street-3 Interception-3|Street-4 Interception-4|"
                    + "Street-5 Interception-5"
                    + ")",
                ),
                "client_phone": generator.String("09[0-9]{8}"),
                "date": Date(),
                "total_price": generator.Integer(start=5, end=50),
            },
        )

        for order in faker.create(100):
            self.db.session.add(order)


class OrderDetailSeeder(Seeder):
    def run(self):

        faker = Faker(
            cls=OrderDetail,
            init={
                "_id": generator.Sequence(start=1, end=500),
                "order_id": generator.Integer(start=1, end=100),
                "beverage_id": generator.Integer(start=1, end=5),
                "ingredient_id": generator.Integer(start=1, end=10),
                "beverage_price": generator.Integer(start=2, end=5),
                "ingredient_price": generator.Integer(start=1, end=5),
                "total_detail_price": generator.Integer(start=1, end=2),
            },
        )

        for order_detail in faker.create(500):
            self.db.session.add(order_detail)


class Date(generator.Generator):
    def random_date(self, start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    def generate(self):
        date_start = datetime.strptime("1/1/2022 1:30 PM", "%m/%d/%Y %I:%M %p")
        date_end = datetime.strptime("1/1/2023 4:50 AM", "%m/%d/%Y %I:%M %p")
        return self.random_date(date_start, date_end)
