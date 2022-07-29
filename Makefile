.PHONY: install
.PHONY: run-server
.PHONY: dev-frontend watch-frontend build-frontend

install:
	cd frontend && yarn install
	pip install -r requirements.txt

run-server:
	FLASK_ENV=development python main.py

dev-frontend:
	cd frontend && yarn run dev

watch-frontend:
	cd frontend && yarn run watch

