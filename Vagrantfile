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
   sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   sudo apt-key fingerprint 0EBFCD88
   sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
   sudo apt-get -y update
   sudo apt-get -y install docker-ce
   curl -L https://github.com/docker/compose/releases/download/1.13.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   sudo docker-compose -f /vagrant/docker-compose.yml up --build -d
  SHELL
end
