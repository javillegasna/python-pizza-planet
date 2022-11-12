VENV_ACTIVATE = . .venv/bin/activate
create_environment:
	python3 -m venv .venv && $(VENV_ACTIVATE) && pip install poetry 


install:
	$(VENV_ACTIVATE) && poetry install --no-interaction --no-root

start_server:
	$(VENV_ACTIVATE) && python3 manage.py run

start_server_hot_reload:
	$(VENV_ACTIVATE) && python3 manage.py hot_reload

start_database:
	$(VENV_ACTIVATE) && python3 manage.py db init
	$(VENV_ACTIVATE) && python3 manage.py db migrate
	$(VENV_ACTIVATE) && python3 manage.py db upgrade

delete_database:
	rm -r migrations
	rm -r pizza.sqlite

run_seeder:
	$(VENV_ACTIVATE) && python3 manage.py seed run --root app/seeds

run_tests:
	$(VENV_ACTIVATE) && pytest -v app/test/ 

run_lint:
	$(VENV_ACTIVATE) && flake8 app/

run_coverage_report:
	$(VENV_ACTIVATE) && pytest --cov-config=.coveragerc --cov=app app/test/ 

save_coverage_report:
	$(VENV_ACTIVATE) && pytest --cache-clear --cov-config=.coveragerc --cov=app app/test/ > pytest-coverage.txt

migrate_poetry:
	$(VENV_ACTIVATE) && pip install poetry && poetry init --no-interaction && cat requirements.txt | xargs poetry add