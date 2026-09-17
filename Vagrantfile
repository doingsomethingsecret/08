Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/focal64"
    config.vm.hostname = "assignment08"

    config.vm.network "private_network", ip: "192.168.56.10"

    config.vm.network "forwarded_port", guest: 5000, host: 5000

    config.vm.provider "virtualbox" do |vb|
        vb.name = "assignment08"
        vb.memory = "1024"
        vb.cpus = 2
    end
end

