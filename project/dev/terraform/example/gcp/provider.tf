
provider "google" {
  credentials = file("./key.json")
  project     = "aline-financial"
  region      = "us-west1"
  version     = "~> 2.5.0"
}