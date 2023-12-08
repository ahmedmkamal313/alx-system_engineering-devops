# 0x10. HTTPS SSL
This project is a demonstration of HTTPS SSL skills. The project involves configuring HTTPS using Let’s Encrypt and certbot on your web server. The project uses two Bash scripts that automate the installation and configuration of the SSL certificate and the Nginx web server.
### Prerequisites
To run the scripts, you need to have:
- A Linux machine running Ubuntu 14.04 LTS
- A non-root user with sudo privileges
- A web server installed (preferably Nginx)
- A domain name pointing to your server’s IP address
### Installation
To install the scripts, clone this repository to your server:
```
$ git clone https://github.com/ahmedmkamal313/alx-system_engineering-devops.git
```
Then, navigate to the `0x10-https_ssl` directory and make the scripts executable:
```
$ cd alx-system_engineering-devops/0x10-https_ssl
$ chmod +x *.sh
```
### Usage
To run the scripts, execute them with sudo privileges on your server:
- [0-world_wide_web](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x10-https_ssl/0-world_wide_web): script displays information about the subdomains of your domain name. 
- [1-haproxy_ssl_termination](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x10-https_ssl/1-haproxy_ssl_termination): This script configures HAProxy to enable SSL termination. The script assumes that you have already obtained a SSL certificate and key from Let’s Encrypt using certbot.
- [100-redirect_http_to_https](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x10-https_ssl/100-redirect_http_to_https): This  script configures Nginx to redirect all HTTP traffic to HTTPS using a 301 redirection.
### Dependencies
The scripts depend on the following packages:
- `nginx`: A web server that can also be used as a reverse proxy, load balancer, and HTTP cache.
- `openssl`: A toolkit for the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols.
- `certbot`: A tool to automatically obtain and renew SSL certificates from Let’s Encrypt.
- `dig`: A command-line tool for querying DNS servers.
