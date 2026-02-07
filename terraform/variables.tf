variable "yc_token" {
  description = "PAuth token for YC"
  type = string
  sensitive = true
}

variable "yc_cloud_id" {
  description = "YC Cloud ID"
  type = string
}

variable "yc_folder_id" {
  description = "YC Foled ID"
  type = string
}

variable "vm_name" {
  description = "VM instance name"
  type = string
  default = "satellite-api-vm"
}

variable "public_ssh_key" {
  description = "Public SSH key for VM access"
  type = string
}