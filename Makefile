FILES = poetry.lock docker-compose.yml Dockerfile

all: run

.PHONY: run
run:
	poetry run pip freeze > requirements.txt
	docker-compose up -d --build

.PHONY: run-logs
run-logs:
	poetry run pip freeze > requirements.txt
	docker-compose up --build

.PHONY: migrate
migrate:
	docker-compose exec web python manage.py makemigrations
	docker-compose exec web python manage.py migrate

.PHONY: down
down:
	docker-compose down
