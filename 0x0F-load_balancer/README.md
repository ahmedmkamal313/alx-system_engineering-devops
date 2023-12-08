# 0x0F. Load balancer
This project is a demonstration of load balancing skills. The project involves configuring a load balancer for two web servers using HAProxy and Nginx. The project uses two Bash scripts that automate the installation and configuration of the load balancer and the web servers.
### Prerequisites
To run the scripts, you need to have:
- Three Linux machines running Ubuntu 14.04 LTS
- One machine acting as the load balancer and two machines acting as the web servers
- A non-root user with sudo privileges on each machine
- A domain name pointing to the load balancer’s IP address
### Installation
To install the scripts, clone this repository to each machine:
```
$ git clone https://github.com/ahmedmkamal313/alx-system_engineering-devops.git
```
Then, navigate to the `0x0F-load_balancer` directory and make the scripts executable:
```
$ cd alx-system_engineering-devops/0x0F-load_balancer
$ chmod +x *.sh
```
### Usage
To run the scripts, execute them with sudo privileges on the appropriate machines:
- [0-custom_http_response_header](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0F-load_balancer/0-custom_http_response_header): This script installs Nginx on the web servers and configures it to serve a custom HTTP response header.
- [1-install_load_balancer](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x0F-load_balancer/1-install_load_balancer): This script installs HAProxy on the load balancer and configures it to balance the traffic between the web servers.

For example, to run the first script on the web servers, you can use the following command:
```
$ sudo ./0-custom_http_response_header
```
The script will perform the following tasks:
- Check if Nginx is installed and install it if not
- Check if Nginx is running and start it if not
- Check if Nginx is listening on port 80 and enable it if not
- Modify the Nginx configuration file to add a custom HTTP response header called X-Served-By with the hostname of the server
- Reload Nginx to apply the changes

After running the script, you should be able to see the custom HTTP response header by visiting your domain name in a web browser and inspecting the network tab.

Dependencies
The scripts depend on the following packages:

- `nginx`: A web server that can also be used as a reverse proxy, load balancer, and HTTP cache.
- `haproxy`: A reliable, high performance TCP/HTTP load balancer.
- `curl`: A command-line tool for transferring data with URL syntax.
