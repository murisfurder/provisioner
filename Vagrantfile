# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.define "vm0" do |vm0|
    vm0.vm.hostname = "vm0.local"
    vm0.vm.network "private_network", ip: "192.168.33.10"
  end

  config.vm.define "vm1" do |vm1|
    vm1.vm.hostname = "vm1.local"
    vm1.vm.network "private_network", ip: "192.168.33.11"
  end

  config.vm.define "vm2" do |vm2|
    vm2.vm.hostname = "vm2.local"
    vm2.vm.network "private_network", ip: "192.168.33.12"
  end

  config.vm.provision "shell", inline: <<-SHELL
    echo -e "foobar123\nfoobar123" | sudo passwd vagrant
  SHELL
end
