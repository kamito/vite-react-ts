.PHONY: install
.PHONY: dev-server
.PHONY: dev-frontend build-frontend
.PHONY: build-docker run-docker
.PHONY: build run
.PHONY: version

VERSION = $(shell cat ./VERSION | sed 's/ //g')
GCP_PROJECT := blocks-gn-kamito
DOCKER_URL := gcr.io/$(GCP_PROJECT)/appname

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
	docker build -t $(DOCKER_URL):$(VERSION) .

run-docker:
	docker run -t -i -p 8080:8080 --env-file ./.env --env IS_LOCAL=true $(DOCKER_URL):$(VERSION)

build: build-docker

run: run-server

version:
	@echo $(VERSION)
