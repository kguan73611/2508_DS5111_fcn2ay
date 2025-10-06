<pre>
1) Create init.sh with the following base tooling and update.
	sudo apt update
	sudo apt install make -y
	sudo apt install python3.12-venv -y
	sudo apt install tree
Run:
	chmod +x init.sh
	bash init.sh
test:
	make
	tree
2) Create init_git_config.sh so configs are proper tagged
	!#/usr/bin/bash

	USER=<your github email>
	NAME=<your github user name>

	git config --global --list

	git config --global user.email ${USER} 
	git config --global user.name  ${NAME} 

	git config --global --list
Run:
	chmod +x init_git_creds.sh
	./init_git_creds.sh
test:
	cat .gitconfig
3) Clone Repository
Run:
	git clone git@github.com:<your-username>/<repo-name>.git
Organize Scripts:
	mkdir scripts
	cd scripts/
	mv /home/ubuntu/init.sh .
	mv ~/init_git_config.sh .
	cd ..
Save to github:
	git add scripts/
	git commit -m "Saving our two init files"
	git push
Test periodically:
	git status
4) Create makefile 
	default:
		@cat makefile

	env:
		python3 -m venv env; . env/bin/activate; pip install --upgrade pip

	update: env
		. env/bin/activate; pip install -r requirements.txt
Create requirements.txt
	pandas
	numpy
Run:
	make update
Verify:
	pip list
	python --version
	which python
Save makefile and requirements:
	git add .
	git commit -m "makefile and requirements."
	git push
</pre>
[![Feature Validation](https://github.com/kguan73611/2508_DS5111_fcn2ay/actions/workflows/validations.yml/badge.svg)](https://github.com/kguan73611/2508_DS5111_fcn2ay/actions/workflows/validations.yml)
