APP_NAME=JLapp
STACK_FILE=stack.yml

build:
	docker build -t JLimg:latest .

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
