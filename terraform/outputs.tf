output "vm_public_ip" {
  value = yandex_compute_instance.vm.network_interface[0].nat_ip_address
}

output "ssh-command" {
  value = "ssh -i ~/.ssh/git-key_ed25519 ubuntu@${yandex_compute_instance.vm.network_interface[0].nat_ip_address}"
}
