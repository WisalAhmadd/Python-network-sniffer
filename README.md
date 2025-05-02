# Python-network-sniffer

A Python script that captures Wi-Fi probe requests in real-time using scapy. It automatically enables monitor mode on your wireless interface, logs unique SSIDs (network names) and device MAC addresses, and stores them in a file with timestamps.

Requirements

Python 3.x

scapy

aircrack-ng (for airmon-ng)

A wireless adapter that supports monitor mode


Installation

sudo apt update

sudo apt install python3-pip aircrack-ng

pip3 install scapy



How to run:

sudo python3 Scrpt.py



Note:
Use responsibly and legally. Capturing Wi-Fi traffic without permission may violate privacy or laws in your country.
For best results, ensure no other network tools interfere with the interface (like NetworkManager or wpa_supplicant).
This Script is provided for educational and research purposes only. Use it ethically.

