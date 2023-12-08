# 0x0D. Web stack debugging #0
This project is a demonstration of web stack debugging skills. The project involves fixing a web server that is not listening on port 80 and making it respond to HTTP requests. The project uses a Bash script that automates the debugging process and applies the necessary changes to the server configuration.
### Prerequisites
To run the script, you need to have:
- A Linux machine running Ubuntu 14.04 LTS
- A non-root user with sudo privileges
- A web server installed (preferably Nginx)
### Installation
To install the script, clone this repository to your server:
```
# git clone https://github.com/ahmedmkamal313/alx-system_engineering-devops.git
```
Then, navigate to the 0x0D-web_stack_debugging_0 directory and make the script executable:
```
$ cd alx-system_engineering-devops/0x0D-web_stack_debugging_0
$ chmod +x 0-give_me_a_page
```
### Usage
To run the script, execute it with sudo privileges:
```
$ sudo ./0-give_me_a_page
```
The script will perform the following tasks:

- Check if Nginx is installed and install it if not
- Check if Nginx is running and start it if not
- Check if Nginx is listening on port 80 and enable it if not
- Check if the default Nginx page is served and fix it if not
- After running the script, you should be able to access the default Nginx page by visiting your server’s IP address in a web browser.

### Dependencies
The script depends on the following packages:

- `nginx`: A web server that can also be used as a reverse proxy, load balancer, and HTTP cache.
- `curl`: A command-line tool for transferring data with URL syntax.
