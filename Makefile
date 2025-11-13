APP_NAME=jlapp
STACK_FILE=stack.yml

build:
	docker build -t jlimg:latest .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml quinto

rm:
	docker stack rm quinto

ps:
	docker service ls

restart:
	make rm
	sleep 5
	make build
	make deploy
