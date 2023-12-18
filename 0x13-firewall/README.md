# 0x13. Firewall
This project is about setting up and configuring a firewall using UFW on Ubuntu servers.

## Files
- [0-block_all_incoming_traffic_but](): install UFW and Block all incoming traffic, except the following TCP ports: 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP)
- [100-port_forwarding](): Redirect port 8080/TCP to port 80/TCP
