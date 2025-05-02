import datetime
import signal
import sys
from scapy.all import *
import subprocess


interface = 'wlan0'
monitor_interface = 'wlan0mon'
probeReqs = []

def enable_mon_mode():
    subprocess.run(['airmon-ng', 'start', interface], stdout=subprocess.DEVNULL)

def disable_mon_mode():
    subprocess.run(['airmon-ng', 'stop', monitor_interface], stdout=subprocess.DEVNULL)

def cleanup(signum, frame):
    print("\n[!] Stopping sniffing and restoring interface...")
    disable_mon_mode()
    sys.exit(0)

def sniffProves(p):
    if p.haslayer(Dot11ProbeReq):
        netName = p.getlayer(Dot11ProbeReq).info.decode(errors='ignore')
        macAddr = p.addr2

        if netName not in probeReqs:
            probeReqs.append(netName)
            log_entry = f"[{datetime.datetime.now()}] SSID: {netName}, MAC: {macAddr}"
            print("[+] Detected New Probe Request: " + log_entry)
            with open("probe_requests.log", "a") as log_file:
                log_file.write(log_entry + "\n")

#Ctrl+C to clean up
signal.signal(signal.SIGINT, cleanup)

print("[*] Enabling monitor mode...")
enable_mon_mode()

print("[*] Starting sniffing on", monitor_interface)
sniff(iface=monitor_interface, prn=sniffProves)
