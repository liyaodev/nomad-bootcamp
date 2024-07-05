# Nomad 集群搭建

## 安装

* 推荐使用二进制编译安装，具体地址：https://developer.hashicorp.com/nomad/install#linux

## 环境

* 基础版本：
    - Nomad: 1.8.1
    - nomad-device-nvidia: 0cb6b6d03a7b48acbbe92b8b264db5512f94a633
    - Go: 1.22

## 命令

### Server 端
```shell
# 启动
./nomad agent -config ./base.hcl -config ./server.hcl
# 查看
./nomad server members

```

### Client 端

```shell
# 启动
./nomad agent -config ./base.hcl -config ./client.hcl
# 查看
./nomad node status
./nomad node status 2dae95d3

```


### 安装GPU插件

* 安装文档：https://developer.hashicorp.com/nomad/plugins/devices/nvidia
* 文档中（[go-nvml](https://github.com/NVIDIA/go-nvml)）导致的坑：
    - https://github.com/hashicorp/nomad-device-nvidia/issues/34
    - https://github.com/hashicorp/nomad-device-nvidia/issues/35
* 重新编译安装（最新版本）
```shell
cd ./cluster/plugins/nomad-device-nvidia

# 指定编译路径
export NOMAD_PLUGIN_DIR=/tmp/nomad-bootcamp/nomad-ov/cluster/data/plugins

# 执行编译
make compile

# 编译验证
make hack

```


## UI 界面

* nomad支持可视化页面，对任务、集群进行查看和管理
* 具体地址：URL：http://*.*.*.*:4646/ui/jobs

## Job 任务执行

* 通过 UI 界面直接 Upload 任务文件
    - [测试任务](./test-job.hcl)
    - [omicverse GPU 任务](../docker/ov-job.hcl)

