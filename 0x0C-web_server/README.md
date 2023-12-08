# 0x0C. Web server
This project is a collection of Bash scripts that automate the process of setting up a web server using Nginx on Ubuntu 14.04 LTS. The scripts perform tasks such as installing Nginx, configuring Nginx to serve static files, setting up a custom domain name, enabling SSL with Let’s Encrypt, and redirecting HTTP traffic to HTTPS.

### Prerequisites
To run the scripts, you need to have:

- A Linux machine running Ubuntu 14.04 LTS
- A non-root user with sudo privileges
- A domain name pointing to your server’s IP address
### Installation
To install the scripts, clone this repository to your server:
```
$ git clone https://github.com/ahmedmkamal313/alx-system_engineering-devops.git
```
Then, navigate to the 0x0C-web_server directory and make the scripts executable:
```
$ cd alx-system_engineering-devops/0x0C-web_server
$ chmod +x *.sh
```
### Usage
To run the scripts, execute them in the following order:

- [0-transfer_file.sh](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0C-web_server/0-transfer_file): This script transfers a file from your local machine to your server using scp.
- [1-install_nginx_web_server.sh](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0C-web_server/1-install_nginx_web_server): This script installs Nginx on your server and configures it to listen on port 80.
- [2-setup_a_domain_name.sh](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0C-web_server/2-setup_a_domain_name): This script sets up a custom domain name for your server using the dig command.
- [3-redirection.sh](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0C-web_server/3-redirection): This script configures Nginx to redirect all HTTP traffic to HTTPS using a 301 redirection.
- [4-not_found_page_404.sh](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0C-web_server/4-not_found_page_404): This script configures Nginx to serve a custom 404 error page.
For example, to run the first script, you can use the following command:
```
$ ./0-transfer_file.sh /path/to/file user@server_ip:/path/to/destination
```
### Dependencies
The scripts depend on the following packages:

- `nginx`: A web server that can also be used as a reverse proxy, load balancer, and HTTP cache.
- `openssl`: A toolkit for the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols.
- `certbot`: A tool to automatically obtain and renew SSL certificates from Let’s Encrypt.
- `dig`: A command-line tool for querying DNS servers.
