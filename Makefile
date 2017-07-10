default: up

build:
	docker-compose build

rebuild:
	docker-compose build --no-cache

up: build
	docker-compose up &

shell:
	docker exec -it manual50_web bash -l
