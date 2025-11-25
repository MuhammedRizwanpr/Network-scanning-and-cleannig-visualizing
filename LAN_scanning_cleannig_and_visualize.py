from scapy.all import sniff, IP
import pandas as pd
import matplotlib.pyplot as plt
import re


print("\n[+] Capturing network traffic for 15 seconds...")

packets = sniff(timeout=15)   

data = []

for pkt in packets:
    if IP in pkt:
        data.append({
            "src_ip": pkt[IP].src,
            "dst_ip": pkt[IP].dst,
            "proto": pkt[IP].proto
        })

raw_df = pd.DataFrame(data)
raw_df.to_csv("raw_traffic.csv", index=False)

print("[+] Traffic captured. Saved as raw_traffic.csv")
print(raw_df.head())


print("\n[+] Cleaning captured traffic...")

df = raw_df.copy()

df = df.drop_duplicates()

df = df.dropna(subset=['src_ip', 'dst_ip'])

def valid_ip(ip):
    pattern = r'\b\d{1,3}(\.\d{1,3}){3}\b'
    if not re.match(pattern, ip):
        return False
    return all(0 <= int(p) <= 255 for p in ip.split('.'))

df = df[df['src_ip'].apply(valid_ip)]
df = df[df['dst_ip'].apply(valid_ip)]

protocol_map = {6: "TCP", 17: "UDP", 1: "ICMP"}
df['proto'] = df['proto'].map(protocol_map).fillna("OTHER")

df.to_csv("cleaned_traffic.csv", index=False)

print("[+] Cleaned traffic saved as cleaned_traffic.csv")
print(df.head())


print("\n[+] Visualizing traffic...")

def visualizing_traffic():
    src_count = df['src_ip'].value_counts()

    plt.figure(figsize=(10,4))
    bars = src_count.plot(kind="bar")
    plt.title("Top Source IPs")
    plt.xlabel("Source IP")
    plt.ylabel("Packet Count")

    for i, v in enumerate(src_count):
        plt.text(i, v + 0.05, str(v), ha="center")

    plt.tight_layout()
    plt.show()

    proto_count = df['proto'].value_counts()

    plt.figure(figsize=(6,4))
    bars = proto_count.plot(kind="bar")
    plt.title("Protocol Distribution")
    plt.xlabel("Protocol")
    plt.ylabel("Count")

    for i, v in enumerate(proto_count):
        plt.text(i, v + 0.05, str(v), ha="center")

    plt.tight_layout()
    plt.show()

    print("\n[+] Visualization complete!")
    
print("You need to visualizing it (Yes or no) ")
choies = input()
if choies.lower() == "yes":
    visualizing_traffic()
elif choies.lower() == "no":
    print("Thank you for using tool")
else:
    print("Wrong choiese..")
