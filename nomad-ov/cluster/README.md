# Nomad 集群搭建

## Nomad 安装

* 推荐使用二进制编译安装，具体地址：https://developer.hashicorp.com/nomad/install#linux
* 具体命令

```shell
# Server 端操作
## 启动
# ./nomad agent -server -config server.hcl
./nomad agent -config ./base.hcl -config ./server.hcl
## 查看
./nomad server members


# Client 端操作
## 启动
# ./nomad agent -client -config client.hcl
./nomad agent -config ./base.hcl -config ./client.hcl
## 查看
./nomad node status
./nomad node status 2dae95d3
## 安装GPU插件
### 插件重新构建
cd ./cluster/plugins/nomad-device-nvidia
export NOMAD_PLUGIN_DIR=/tmp/nomad-bootcamp/nomad-ov/cluster/data/plugins
make compile
### 安装指导
https://developer.hashicorp.com/nomad/plugins/devices/nvidia
### go-nvml最新版本
https://github.com/NVIDIA/go-nvml
### 解决问题
https://github.com/hashicorp/nomad-device-nvidia/issues/34
https://github.com/hashicorp/nomad-device-nvidia/issues/35

```


## UI 界面

* nomad支持可视化页面，对任务、集群进行查看和管理
* 具体地址：URL：http://*.*.*.*:4646/ui/jobs


## nomad-device-nvidia 自动构建

go 版本 1.22
go mod download
make compile
