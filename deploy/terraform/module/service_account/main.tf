resource "google_service_account" "gke_cluster_sa" {
  account_id   = "gke-cnk-sa"
  display_name = "GKE SA for ${var.label} Project"
}
