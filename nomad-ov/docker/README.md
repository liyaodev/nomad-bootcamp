# omicverse gpu docker 

## 环境

* 基于 [omicverse](https://github.com/Starlitnightly/omicverse.git)构建的基础 GPU 镜像
* 基础环境：
    - Nvidia: nvidia/cuda:12.1.0-cudnn8-devel-ubuntu20.04
    - Python: 3.10.10
    - torch: 2.3.1
    - omicverse: 1.6.3
    - rapids_singlecell: 0.10.6

## 镜像命令

```shell

# 构建
make build
# 启动
make start
# 停止
make stop

```


