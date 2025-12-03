from scapy.all import sniff, IP
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
import sys
def captuer_traffic():
    flag = 0
    print("\n[+] Capturing network traffic for 5 seconds...")
        
    packets = sniff(timeout=5)   

    data = []
    for pkt in packets:
        if IP in pkt:
            data.append({"src_ip": pkt[IP].src,"dst_ip": pkt[IP].dst, "proto": pkt[IP].proto})
    raw_df = pd.DataFrame(data)
    
    if os.path.exists("/home/rizwan/Documents/scripts/lan-scan-and-clean-and-visual"):
        raw_df.to_csv("/home/rizwan/Documents/scripts/lan-scan-and-clean-and-visual/raw_traffic.csv", index=False)
    else:
        print("there is no folder to save 'raw_traffic.csv' file..")
        sys.exit()
    print("[+] Traffic captured. Saved as raw_traffic.csv")
    print(raw_df.head())


    print("\n[+] Cleaning captured traffic...")

    df = raw_df.copy()

    df = df.drop_duplicates()

    df = df.dropna(subset=['src_ip', 'dst_ip'])

    def valid_ip(ip):
        pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        if not re.match(pattern, ip):
            return False
        return all(0 <= int(p) <= 255 for p in ip.split('.'))

    df = df[df['src_ip'].apply(valid_ip)]
    df = df[df['dst_ip'].apply(valid_ip)]

    protocol_map = {6: "TCP", 17: "UDP", 1: "ICMP"}
    df['proto'] = df['proto'].map(protocol_map).fillna("OTHER")

    if os.path.exists("/home/rizwan/Documents/scripts/lan-scan-and-clean-and-visual"):
        df.to_csv("/home/rizwan/Documents/scripts/lan-scan-and-clean-and-visual/cleaned_traffic.csv", index=False)
    else:
        print("there is no any folder to save 'cleaned_traffic.csv'file..")
    print("[+] Cleaned traffic saved as cleaned_traffic.csv")
    print(df.head())

    print("You need to visualizing it (Yes or no) ")
    choies = input()
    if choies.lower() == "yes":
        flag = 1
    elif choies.lower() == "no":
        print("Thank you for using tool")
        return 0
    else:
        print("Wrong choiese..")
        return 0
    if flag == 1:
        print("\n[+] Visualizing traffic...")

        src_count = df['src_ip'].value_counts()

        plt.figure(figsize=(10,4))
        bars = src_count.plot(kind="bar")
        plt.title("Top Source IPs")
        plt.xlabel("Source IP")
        plt.ylabel("Packet Count")
        plt.tight_layout()
        plt.show()

        proto_count = df['proto'].value_counts()
        plt.figure(figsize=(6,4))
        bars = proto_count.plot(kind="bar")
        plt.title("Protocol Distribution")
        plt.xlabel("Protocol")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()

        print("\n[+] Visualization complete!")

try:
    captuer_traffic()
except PermissionError:
    print("Run the script should use 'sudo'")
