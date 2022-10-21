# Including commands
run-django-server:
	poetry run task server

run-quasar:
	quasar dev

install-frontend:
	yarn

install-backend:
	poetry run pip install -U setuptools
	poetry install --no-root

.PHONY: clear
clear:
	poetry run task clear

.PHONY: createadmin
createadmin:
	poetry run task createsuperuser

.PHONY: migrate
migrate:
	poetry run task migrate

.PHONY: migrations
migrations:
	poetry run task makemigrations

# Primary commands
.PHONY: install
install:
	@make -j 2 install-backend install-frontend
	poetry run task initconfig --debug
	@make migrate
	poetry run task defaultadmin
	poetry run task defaultfixtures

.PHONY: install-prod
install-prod:
	poetry run pip install -U pip
	@make -j 2 install-backend install-frontend
	poetry run task initconfig

.PHONY: docker
docker:
	python docker/initconfig.py --debug --docker
	cd docker && docker-compose up

.PHONY: run
run:
	@make -j 2 run-django-server run-quasar

.PHONY: build
build:
	quasar build
	poetry run task collectstatic
	@make migrate
	poetry run task defaultadmin
	poetry run task defaultfixtures

.PHONY: deploy
deploy:
	@make build
	sudo systemctl restart gunicorn
	sudo systemctl restart nginx

