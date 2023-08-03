# 0x07. Networking basics #0 🚀
This project is about learning the basics of networking, such as the OSI model, LAN, WAN, Internet, IP address, TCP/UDP, and ports. It’s a fun and exciting way to explore the world of networks and how they work. 😎

![network](https://pbs.twimg.com/media/C4uVCMaUEAAcAA-?format=jpg&name=900x900)

## OSI Model 🔥
The OSI model is a conceptual framework that describes how different network protocols interact and communicate with each other. It consists of seven layers: physical, data link, network, transport, session, presentation, and application. Each layer has a specific function and responsibility in the network communication process. For more details on the OSI model, see this [article](https://en.wikipedia.org/wiki/OSI_model).

## LAN 💡
LAN stands for Local Area Network. It is a network that connects devices within a small geographical area, such as a home, office, or school. LANs typically use Ethernet or Wi-Fi technologies to transmit data. LANs are usually faster and more secure than WANs.

## WAN 🌐
WAN stands for Wide Area Network. It is a network that connects devices across a large geographical area, such as a country or continent. WANs typically use routers and switches to route data over long distances. WANs are usually slower and less secure than LANs.

## Internet 🌎
The Internet is a global network of interconnected networks that use the TCP/IP protocol suite to communicate. The Internet enables the exchange of information and services among billions of devices worldwide. The Internet consists of many components, such as servers, clients, routers, ISPs, DNS servers, etc.

## IP address 📧
An IP address is a unique identifier that is assigned to each device on a network. It consists of four numbers separated by dots (for IPv4) or eight groups of hexadecimal digits separated by colons (for IPv6). An IP address allows devices to locate and communicate with each other on a network.

There are two types of IP addresses: static and dynamic. A static IP address does not change and is manually assigned to a device by an administrator. A dynamic IP address changes periodically and is automatically assigned to a device by a DHCP server.

## Localhost 🏠
Localhost is a special IP address that refers to the local device itself. It is usually represented by 127.0.0.1 (for IPv4) or ::1 (for IPv6). Localhost can be used to test network applications or access local services without going through the network.

## Subnet 🗂️
A subnet is a logical subdivision of a network that allows devices to communicate more efficiently and securely. A subnet is defined by a subnet mask, which is a number that indicates which part of an IP address belongs to the network and which part belongs to the host.

## IPv6 🆕
IPv6 is the latest version of the Internet Protocol that was created to replace IPv4 due to the exhaustion of available IP addresses. IPv6 uses 128-bit addresses instead of 32-bit addresses, which allows for more devices to connect to the Internet. That’s a lot of addresses! 😱

## TCP/UDP ⚙️
TCP and UDP are two of the most commonly used transport layer protocols for IP networks. They are responsible for delivering data from one application to another across the network.

TCP stands for Transmission Control Protocol. It is a reliable and connection-oriented protocol that ensures that data is delivered in order and without errors. TCP uses mechanisms such as acknowledgments, retransmissions, and flow control to achieve reliability.

UDP stands for User Datagram Protocol. It is an unreliable and connectionless protocol that does not guarantee that data is delivered in order or without errors. UDP does not use any mechanisms to achieve reliability, but it is faster and more efficient than TCP.

## Port 🔌
A port is a number that identifies a specific application or service on a device. A port allows multiple applications or services to share the same IP address without interfering with each other. Ports range from 0 to 65535, but only ports from 0 to 1023 are reserved for well-known services.

Some common port numbers are:

SSH: 22
HTTP: 80
HTTPS: 443
Tool/protocol for checking network connectivity 📡
One of the most common tools or protocols for checking if a device is connected to a network is ping. Ping is a command-line utility that sends a series of ICMP (Internet Control Message Protocol) packets to a specified IP address or hostname and measures the round-trip time and packet loss. Ping can be used to test the reachability and latency of a network device. Ping pong! 🏓

## Files 📁
This project contains the following files:

- [0-OSI_model](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x07-networking_basics/0-OSI_model): A file that contains the answers to some questions about the OSI model.
- [1-types_of_network](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x07-networking_basics/1-types_of_network): A file that contains the answers to some questions about LAN, WAN, and Internet.
- [2-MAC_and_IP_address](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x07-networking_basics/2-MAC_and_IP_address): A file that contains the answers to some questions about MAC and IP addresses.
- [3-UDP_and_TCP](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x07-networking_basics/3-UDP_and_TCP): A file that contains the answers to some questions about TCP and UDP.
- [4-TCP_and_UDP_ports](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x07-networking_basics/4-TCP_and_UDP_ports): A Bash script that displays listening ports for TCP and UDP.
- [5-is_the_host_on_the_network](https://github.com/ahmedmkamal313/alx-system_engineering-devops/blob/master/0x07-networking_basics/5-is_the_host_on_the_network): A Bash script that pings an IP address passed as an argument and displays if the host is alive or not.
