name = "nomad-client"

datacenter = "dc1"

client {
  enabled = true

  servers = ["127.0.0.1:4647"]

  # 配置网络接口和速度
  // network_interface = "eth0"
  network_interface = "lo"
  // network_speed = 100
  

  gc_disk_usage_threshold = 95 # 将阈值提高到 95%

  options {
    "docker.privileged.enabled" = "true"
    "driver.raw_exec.enable"    = "1"
    "driver.raw_exec.enable_networking" = "1"
  }

  // reserved_ports = "8000-9000" # 开放端口范围（静态和动态端口）

}

ports {
  http = 5656
}

// plugin "docker" {
//   config {
//     volumes {
//       enabled = true
//     }
//   }
// }

plugin "nomad-device-nvidia" {
  config {
    enabled            = true
    // ignored_gpu_ids    = ["GPU-f9442e5b]
    fingerprint_period = "1m"
  }
}

// plugin "raw_exec" {
//   config {
//     enabled = true
//   }
// }


