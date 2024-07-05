name = "nomad-server"

datacenter = "dc1"

server {
  enabled = true

  bootstrap_expect = 1
}

ports {
  http = 4646
  rpc  = 4647
  serf = 4648
}
