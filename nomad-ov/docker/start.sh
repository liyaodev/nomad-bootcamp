#!/bin/bash

sleep 1

# ###### 启动服务 ##########
# cd /app && tail -f /dev/null
# Start Jupyter Lab with --allow-root and any passed in arguments
exec jupyter-lab --ip=0.0.0.0 --port=8888 --allow-root "$@"
