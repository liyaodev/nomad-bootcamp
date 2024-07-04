
build:
	docker build -f ./Dockerfile -t liyaodev/base-ov-gpu:v1.0.0 .

start:
	docker run --runtime=nvidia --gpus '"device=2"' --name ov-gpu -v ./:/app -it liyaodev/base-ov-gpu:v1.0.0

stop:
	docker rm ov-gpu

dev:
	docker exec -it ov-gpu /bin/bash

clean:
	docker rm ov-gpu
	docker rmi liyaodev/base-ov-gpu:v1.0.0
