job "nginx" {
  datacenters = [
    "dc1"
  ]
  type = "service"

  update {
    max_parallel = 1
    min_healthy_time = "10s"
    healthy_deadline = "2m"
    progress_deadline = "5m"
    auto_revert = true
  }

  group "nginx" {
    count = 1

    constraint {
      operator = "distinct_hosts"
      value = "true"
    }

    restart {
      attempts = 1
      interval = "5m"
      delay = "25s"
      mode = "delay"
    }

    task "nginx" {
      driver = "docker"

      config {
        image = "nginx:1.19.1-alpine"

        port_map {
          http = 80
        }

        volumes = [
          "local:/etc/nginx/conf.d",
        ]
      }

      resources {
        cpu = 10
        memory = 256

        network {
          mbits = 10
          port "http" {}
        }
      }
    }
  }
}
