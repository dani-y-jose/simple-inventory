# variables
provider "google" {
  project = var.project
  region  = var.region
}

variable "project" {
  type        = string
  description = "Google Cloud Project ID"
}

variable "region" {
  type        = string
  default     = "us-central1"
  description = "Google Cloud Region"
}

variable "service" {
  type        = string
  default     = "simple-inventory"
  description = "The name of the service"
}