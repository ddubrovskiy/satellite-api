variable "yc_token" {
  description = "PAuth token for YC"
  type = string
  sensitive = true
}

variable "yc_cloud_id" {
  description = "YC Cloud ID"
  type = string
}

variable "yc_foler_id" {
  description = "YC Foled ID"
  type = string
}

variable "vm_name" {
  description = "VM instance name"
  type = string
  default = "satellite-api-vm"
}
