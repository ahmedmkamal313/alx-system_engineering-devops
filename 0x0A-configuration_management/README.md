# Project 0x0A. Configuration management
This project is about using Puppet to automate the configuration management of servers. It uses Puppet manifests to define the desired state of the server and apply the changes to the server using the puppet apply command. It also uses the file and file_line resource types to manage files and their contents.

## Installation
To install this project, you need to have Puppet installed on your system.
### Install puppet
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
### Install puppet-lint
```
$ gem install puppet-lint
```
### Usage
To use this project, you can clone this repository to your local machine using:

```
$ git clone https://github.com/ahmedmkamal313/alx-system_engineering-devops.git
```

Then, you can navigate to the project folder using:
```
$ cd alx-system_engineering-devops/0x0A-configuration_management
```
### Files:
There, you will find several Puppet manifest files that perform different tasks, such as:

- [0-create_a_file.pp](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0A-configuration_management/0-create_a_file.pp): Creates a file in /tmp.
- [1-install_a_package.pp](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0A-configuration_management/1-install_a_package.pp): Installs the flask package.
- [2-execute_a_command.pp](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0A-configuration_management/2-execute_a_command.pp): Creates a manifest that kills a process named killmenow.

```
$ sudo puppet apply <manifest file>
```
For example, to apply the `0-create_a_file.pp` manifest, you can run:
```
$ sudo puppet apply 0-create_a_file.pp
```
This command will create a file named `school` in the /tmp directory with the permissions `0744` and the content **I love Puppet.**
