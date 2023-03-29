resource "google_storage_bucket" "gcs_vault_bucket" {
  name                        = "yuyatinnefeld-${var.env}-vault-secrets"
  location                    = var.region
  uniform_bucket_level_access = true
  labels = {
    created = "terraform"
  }
}
