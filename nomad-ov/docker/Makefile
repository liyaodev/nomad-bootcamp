
build:
	docker build -f ./Dockerfile -t liyaodev/base-ov-gpu:v1.0.0 .

start:
	docker run --runtime=nvidia --gpus '"device=0"' --name ov-gpu -p 8080:8080 -p 8888:8888 -v ./:/app -it liyaodev/base-ov-gpu:v1.0.0

stop:
	docker rm ov-gpu

dev:
	docker exec -it ov-gpu /bin/bash

clean:
	docker rm ov-gpu
	docker rmi liyaodev/base-ov-gpu:v1.0.0
