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

module "service_account" {
  source = "./module/service_account"
  label  = format("%s-%s", var.label, var.env)
  depends_on = [
    module.api
  ]
}

module "secrets" {
  source = "./module/secrets"
  region = var.region
  label  = format("%s-%s", var.label, var.env)
  depends_on = [
    module.api
  ]
}

module "cloud_storage" {
  source = "./module/storage"
  region = var.region
  env    = var.env
}

# module "gke" {
#   source   = "./module/gke"
#   region   = var.region
#   sa_email = module.service_account.gke_cluster_sa_email
#   label    = format("%s-%s", var.label, var.env)
#   depends_on = [
#     module.api, module.service_account
#   ]
# }

# module "cloud_sql" {
#   source            = "./module/cloud_sql"
#   region            = var.region
#   sql_version       = var.sql_version
#   sql_instance_name = var.sql_instance_name
#   db_name           = var.db_name
#   db_user           = var.db_user
#   db_password       = var.db_password
# }
