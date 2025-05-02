# Python-network-sniffer

Wi-Fi Probe Request Sniffer A Python script that captures Wi-Fi probe requests in real-time using scapy. It automatically enables monitor mode on your wireless interface, logs unique SSIDs (network names) and device MAC addresses, and stores them in a file with timestamps.

Features Enables monitor mode automatically on wlan0 Sniffs probe requests from nearby devices Logs SSID, MAC address, and timestamp Avoids duplicate entries Saves logs to probe_requests.log Gracefully exits and restores interface to managed mode

Requirements Python 3.x scapy aircrack-ng (for airmon-ng) A wireless adapter that supports monitor mode

how to install: sudo apt update sudo apt install python3-pip aircrack-ng pip3 install scapy

How to Use: Make sure your wireless card supports monitor mode and no other network manager is interfering. sudo python3 Script.py

It will: Enable monitor mode (wlan0 → wlan0mon)

Begin sniffing probe requests Log new SSIDs and MACs to probe_requests.log Output Example [2025-05-02 14:21:10.487563] SSID: Home, MAC: 84:3a:4b:12:3f:9c [2025-05-02 14:21:33.672349] SSID: Galaxy_S20, MAC: f4:12:fa:aa:bc:3d Graceful Exit Press Ctrl + C to stop sniffing. The script will automatically: Stop monitor mode on wlan0mon Restore wlan0 to managed mode

Note: Use responsibly and legally. Capturing Wi-Fi traffic without permission may violate privacy or laws in your country. For best results, ensure no other network tools interfere with the interface (like NetworkManager or wpa_supplicant). This script is provided for educational and research purposes only. Use it ethically.
