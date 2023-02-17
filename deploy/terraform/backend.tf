terraform {
  backend "gcs" {
    bucket = "yuyatinnefeld-dev-tf-state"
    prefix = "state/all-resources"
  }
}
