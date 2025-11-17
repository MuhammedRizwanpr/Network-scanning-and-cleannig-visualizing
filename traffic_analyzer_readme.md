# Network Traffic Analyzer

A beginner-friendly cybersecurity tool that **captures live network traffic**, **cleans the captured data**, and **visualizes it** using Pandas and Matplotlib.

This project is designed to help learners understand the full workflow:

```
Raw Packet Capture → Cleaning → Analysis → Visualization → Insights
```

---

## 🚀 What This Tool Does

This tool automatically handles an entire end-to-end process:

### **1. Capture Traffic (like Wireshark)**

- Sniffs live packets from your network
- Extracts:
  - Source IP
  - Destination IP
  - Protocol number
- Saves raw data into a CSV file (`raw_traffic.csv`)

### **2. Clean the Captured Logs (Pandas)**

The tool cleans the raw sniffed traffic by:

- Removing duplicates
- Removing packets without IP headers
- Removing invalid IP addresses
- Converting protocol numbers to names (TCP, UDP, ICMP)
- Saving a final cleaned dataset (`cleaned_traffic.csv`)

### **3. Visualize the Cleaned Data (Matplotlib)**

The tool produces clear visual charts:

- **Top Source IPs (bar chart)**
- **Protocol distribution (TCP vs UDP vs ICMP)**

These graphs help you understand which devices are talking the most and what protocols dominate your network.

---

## 📥 How to Download This Project

### **Option 1 — Download ZIP (Easy)**

1. Open the GitHub repository.
2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Extract the folder on your system.

### **Option 2 — Clone Using Git (Recommended)**

```
git clone https://github.com/MuhammedRizwanpr/Network-scanning-and-cleannig-visualizing.git
```

---

## ⚙️ How It Works (Simple Explanation)

### **Step 1 — Packet Capture**

The tool uses Scapy to sniff network packets for a few seconds.

### **Step 2 — Save Raw Scan**

Raw captured packet info is saved into:

```
raw_traffic.csv
```

### **Step 3 — Cleaning**

Cleaning steps include:

- removing invalid or blank rows
- removing bad IP formats
- converting protocol numbers to readable names (like TCP, UDP)

Cleaned data is saved into:

```
cleaned_traffic.csv
```

### **Step 4 — Visualization**

Two charts are generated:

- Traffic by top source IPs
- Protocol usage graph

---

## 📦 Requirements

Install the required libraries:

### **APT (Recommended)**

```
sudo apt install python3-scapy python3-pandas python3-matplotlib
```

### **PIP (Alternate)**

```
pip install scapy pandas matplotlib --break-system-packages
```

---

## ▶️ How to Run the Tool

1. Open the project folder.
2. Run the analyzer using:

```
sudo python3 network_analyzer.py
```

3. The script will:
   - capture live traffic
   - clean the captured packets
   - show graphs on your screen

---

## 📸 Screenshot

Add a screenshot of your tool:

```
![Traffic Analyzer Output](/screenshot/.png)
```

---

## 📝 Notes

- This tool is for educational and analysis purposes.
- You can increase sniffing time or filter protocols.
- Works best on networks where multiple devices are active.

---

## ⭐ Future Improvements

You can upgrade this project by adding:

- Packet size analysis
- Live dashboard
- GeoIP lookup for public IPs
- Port scanning statistics
- Saving graphs automatically

---

## 👨‍💻 Author

Created as a simple cybersecurity project to help beginners learn packet capture, cleaning, and visualization.

