output "gke_cluster_sa_email" {
  value       = google_service_account.gke_cluster_sa.email
  description = "Email of the GKE Cluster Service Account"
}
