# Project 0x0B. SSH
This project is about using SSH to securely connect to a remote server. It uses SSH keys to authenticate with the server without typing a password. It also uses the SSH configuration file to customize the SSH client settings.

### Installation
To install this project, you need to have SSH installed on your system.

### Usage
To use this project, you can clone this repository to your local machine using:
```
$ git clone https://github.com/ahmedmkamal313/alx-system_engineering-devops.git
```
Then, you can navigate to the project folder using:
```
$ cd alx-system_engineering-devops/0x0B-ssh
```
### files
There, you will find several files that perform different tasks, such as:

- [0-use_a_private_key](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0B-ssh/0-use_a_private_key): A Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.
- [1-create_ssh_key_pair](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0B-ssh/1-create_ssh_key_pair): A Bash script that creates an RSA key pair.
- [2-ssh_config](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0B-ssh/2-ssh_config): A SSH configuration file that uses the private key ~/.ssh/school and refuses to authenticate using a password.
- [100-puppet_ssh_config.pp](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0B-ssh/100-puppet_ssh_config.pp): A Puppet manifest that configures the SSH client configuration file to use the private key ~/.ssh/school and refuse to authenticate using a password.

You can use any of these files to connect to your server using SSH keys, like this:
```
$ ./<file name>
```
For example, to use the 0-use_a_private_key script, you can run:
```
$ ./0-use_a_private_key
```
This command will connect you to your server using the private key ~/.ssh/school and the user ubuntu.
