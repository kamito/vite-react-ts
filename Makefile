.PHONY: install
.PHONY: dev-server
.PHONY: dev-frontend build-frontend
.PHONY: build-docker run-docker
.PHONY: build run

install:
	cd frontend && yarn install
	pip install -r requirements.txt

dev-frontend:
	cd frontend && yarn run dev

build-frontend:
	cd frontend && yarn run build

dev-server:
	FLASK_ENV=development python main.py

run-server:
	gunicorn --bind=:8080 --workers=1 --threads=4 --timeout=0 main:app

build-docker:
	echo "TODO: build-docker"

run-docker:
	echo "TODO: run-docker"

build: build-docker

run: build-frontend run-server
