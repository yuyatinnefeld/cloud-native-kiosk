data "google_compute_network" "mein_network" {
  name = "vpc-mainnet"
}

resource "google_sql_database_instance" "instance" {
  name                = var.sql_instance_name
  region              = var.region
  database_version    = var.sql_version
  deletion_protection = false

  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled    = true
      private_network = data.google_compute_network.mein_network.id
    }
  }
}

resource "google_sql_user" "users" {
  name     = var.db_user
  instance = google_sql_database_instance.instance.name
  host     = "ckn.com"
  password = var.db_password
}


resource "google_sql_database" "database" {
  name     = var.db_name
  instance = google_sql_database_instance.instance.name
}
