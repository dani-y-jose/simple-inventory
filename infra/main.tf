data "google_project" "project" {
  project_id = var.project
}

# custom service account
resource "google_service_account" "django" {
  account_id = "django"
}

# bucket
resource "google_storage_bucket" "media" {
  name     = "${var.project}-images"
  location = "US"
}

# cloud run service
resource "google_cloud_run_service" "service" {
  name                       = var.service
  location                   = var.region
  autogenerate_revision_name = true

  template {
    spec {
      service_account_name = google_service_account.django.email
      containers {
        image = "gcr.io/${var.project}/${var.service}"
      }
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "1"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# cloud build trigger
resource "google_cloudbuild_trigger" "service-trigger" {
  name = "${var.project}-trigger"

  github {
    owner = "dani-y-jose"
    name =
    push {
      branch = "^main$"
    }
  }
  filename = "cloudbuild/build_deploy.yaml"
}


# final output
output "superuser_password" {
  value     = google_secret_manager_secret_version.superuser_password.secret_data
  sensitive = true
}

output "service_url" {
  value = google_cloud_run_service.service.status[0].url
}
