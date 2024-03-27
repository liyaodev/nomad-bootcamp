job "web_nginx" {
  datacenters = ["dc1"]

  group "web_nginx" {
    count = 1

    task "web_nginx" {
      driver = "docker"
      config {
        image = "nginx:latest"
        port_map {
          http = 80
        }
      }
      resources {
        cores = 1
        memory = 512
      }
      env {
      }
    }
  }
}