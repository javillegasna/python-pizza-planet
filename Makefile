create_environment:
	python3 -m venv .venv

install:
	poetry install

install_dependencies:
	. .venv/bin/activate && pip install -r requirements.txt

uninstall_dependencies:
	. .venv/bin/activate && pip uninstall -r requirements.txt -y

start_server:
	. .venv/bin/activate && python3 manage.py run

start_server_hot_reload:
	. .venv/bin/activate && python3 manage.py hot-reload

start_database:
	. .venv/bin/activate && python3 manage.py db init
	. .venv/bin/activate && python3 manage.py db migrate
	. .venv/bin/activate && python3 manage.py db upgrade

delete_database:
	rm -r migrations
	rm -r pizza.sqlite

run_tests:
	. .venv/bin/activate && pytest -v app/test/ 

run_lint:
	. .venv/bin/activate && flake8 app/

run_coverage_report:
	. .venv/bin/activate && pytest --cov-config=.coveragerc --cov=app app/test/ 

save_coverage_report:
	. .venv/bin/activate && pytest --cache-clear --cov-config=.coveragerc --cov=app app/test/ > pytest-coverage.txt

migrate_poetry:
	. .venv/bin/activate && pip install poetry && poetry init --no-interaction && cat requirements.txt | xargs poetry add