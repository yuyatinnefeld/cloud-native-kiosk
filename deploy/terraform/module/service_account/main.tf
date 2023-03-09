resource "google_service_account" "gke_cluster_sa" {
  account_id   = "cnk-gke"
  display_name = "GKE SA | PROJECT: ${var.label}"
}

resource "google_service_account" "cloud_run_sa" {
  account_id   = "cnk-cloud-run"
  display_name = "CLOUD RUN SA | PROJECT: ${var.label}"
}
