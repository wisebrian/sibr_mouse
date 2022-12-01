setup:
	sudo apt-get update && sudo apt-get upgrade -y
	sudo apt-get install -y build-essential
	sudo apt-get install -y checkinstall
	sudo apt-get install -y libreadline-gplv2-dev
	sudo apt-get install -y libncurses5-dev
	sudo apt-get install -y libncursesw5-dev
	sudo apt-get install -y libssl-dev
	sudo apt-get install -y libsqlite3-dev
	sudo apt-get install -y tk-dev
	sudo apt-get install -y libgdbm-dev
	sudo apt-get install -y libc6-dev
	sudo apt-get install -y libbz2-dev
	sudo apt-get install -y libnss3-dev
	sudo apt-get install -y zlib1g-dev
	sudo apt-get install -y openssl
	sudo apt-get install -y libffi-dev
	sudo apt-get install -y python3-dev
	sudo apt-get install -y python3-setuptools
	sudo apt-get install -y wget
	wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz
	tar -xzvf Python-3.10.8.tgz
	cd Python-3.10.8/
	./configure --enable-optimizations
	sudo make altinstall
	sudo rm /usr/bin/python3
	sudo ln -s /usr/local/bin/python3.10 /usr/bin/python3
	pip3 install flask websockets smbus explorerhat