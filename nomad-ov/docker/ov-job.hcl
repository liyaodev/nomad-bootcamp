job "ov_job" {
  datacenters = ["dc1"]

  group "ov_job" {
    count = 1

    network {
      port "http" {
        static=8888
        to = 8888
      }
    }

    task "ov_job" {
      driver = "docker"

      config {
        image = "liyaodev/base-ov-gpu:v1.0.0"
        ports = ["http"]
      }

      resources {
        cores = 2
        memory = 8192 # MB

        device "nvidia/gpu" {
          count = 1

          # Add an affinity for a particular model
          affinity {
            attribute = "${device.model}"
            value     = "NVIDIA GeForce RTX 3060"
            // weight    = 50
          }
        }
      }

      env {
        PYTHONUNBUFFERED = 1
        CUDA_VISIBLE_DEVICES = "0"
      }
    }
  }
}
