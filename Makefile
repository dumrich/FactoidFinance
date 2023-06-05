FILES = poetry.lock docker-compose.yml Dockerfile

.PHONY: run
run:
	pip freeze > requirements.txt
	docker-compose up -d --build


