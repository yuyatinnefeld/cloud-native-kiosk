terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}


module "api" {
  source     = "./module/api"
  project_id = var.project_id
}


module "gke" {
  source   = "./module/gke"
  region   = var.region
  sa_email = module.service_account.gke_cluster_sa_email
  label    = format("%s-%s", var.label, var.env)
  depends_on = [
    module.api, module.service_account
  ]
}


module "service_account" {
  source = "./module/service_account"
  label  = format("%s-%s", var.label, var.env)
  depends_on = [
    module.api
  ]
}
