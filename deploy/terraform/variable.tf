variable "label" {
  type    = string
  default = "cnk"
}

variable "region" {
  type    = string
  default = "europe-west1"
}

variable "zone" {
  type    = string
  default = "europe-west1-b"
}

variable "sql_instance_name" {
  type    = string
  default = "cnk-sql-instance"
}

variable "sql_version" {
  type    = string
  default = "POSTGRES_14"
}

variable "db_name" {
  type    = string
  default = "cnk-db"
}

variable "db_user" {
  type    = string
  default = "postgres"
}

variable "env" {
  type = string
}

variable "project_id" {
  type = string
}

variable "db_password" {
  type = string
}
