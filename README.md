# Tournament Database

This project contains all files necessary to the creation and management of a database designed to store , access and manipulate data for a tournament held in a swiss pairing mode. 

### Table of Contents

* Install
* Getting Started with Udacity UD-197 course material
* What's Included

### Install

> Tournament Database requires Python 2.7 or higher and postgre to be installed on your computer in order to be executed.
> Please make sure that Python 2.7 or higher is installed on your computer or download and install it.
* [Windows](https://www.python.org/ftp/python/2.7/python-2.7.amd64.msi)
* [Mac](https://www.python.org/ftp/python/2.7/python-2.7-macosx10.5.dmg)

> Linux user should have a version of ython already installed. Please refer to appropriate distribution documentation
> and upgrade to a newer version if needed.

> Please make sure that PostgreSQL is installed on your computer or download and install it following the instructions at:
* [PostgreSQL](http://www.postgresql.org/download/)

> Python 2.7 DB-API for PostgreSQL is psycopg2. Please refer to the following for download and installation on your system
* [psycopg](http://initd.org/psycopg/)

### Getting Started with Udacity UD-197 course material

The following instructions are for Udacity course UD-197 setup:
* Install Vagrant VM as descibed [here](https://www.udacity.com/wiki/ud197/install-vagrant)
* Download the tournament project from [GitHub](https://github.com/marscar)
* extract it on your local machine. **Keep all files in the same folder!**
* Open a terminal (Mac, Linux) or Putty (Windows)
* Crawl to the VM folder
```sh
$ cd /home/../path_to_VM_folder/fullstack/vagrant
```
type 
```sh
$ vagrant up
$ vagrant ssh
```
to launch your virtual machine andd log into it;

* Crawl to the project folder
```sh
$ cd /vagrant/tournament
```

Now you have three options

1) type
```sh
$ python tournament_test.py
```
if you want to run the test file.

2) create, connect to and interact with tournament database using PostgreSQL
```sh
$ psql
$ \i tournament
```

3) Use psycopg2 and the functions defined by tournament.py:
```sh
$ python
$ from tournament import *
```

### What's Included
```sh
tournament/
|--tournament.py
|--tournament.pyc
|--tournament.sql
|--tournament_test.py
|--README.md
```

### Author
Marcello Scarnecchia

