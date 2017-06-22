# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.host_name = 'restpy'
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network :forwarded_port, host: 80, guest: 8000
  config.vm.network :forwarded_port, host: 5000, guest: 8080
  config.vm.provider "virtualbox" do |vb|
     vb.memory = "2048"
   end
   config.vm.provision "shell", inline: <<-SHELL
     sudo apt-get -y update
     sudo apt-get -y upgrade
     sudo apt-get -y install python3-pip
     sudo apt-get -y install build-essential libssl-dev libffi-dev python-dev
     sudo apt-get -y install python-virtualenv
   SHELL
end
