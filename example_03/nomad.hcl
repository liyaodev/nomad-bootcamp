# data_dir 为绝对路径，可自行修改
data_dir  = "/Users/xxx/nomad-bootcamp/example_03/data"

bind_addr = "0.0.0.0"

server {
  enabled          = "true"
  bootstrap_expect = 1
}

client {
  enabled = "true"
  servers = ["0.0.0.0"]
}
