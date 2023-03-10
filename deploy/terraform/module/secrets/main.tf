resource "google_secret_manager_secret" "webhook_url_slack_error" {
  secret_id = "webhook_url_slack_error"

  labels = {
    label = var.label
  }

  replication {
    user_managed {
      replicas {
        location = var.region
      }
    }
  }
}

resource "google_secret_manager_secret" "webhook_url_teams_error" {
  secret_id = "webhook_url_teams_error"

  labels = {
    label = var.label
  }

  replication {
    user_managed {
      replicas {
        location = var.region
      }
    }
  }
}
