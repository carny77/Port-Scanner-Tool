
#Step 1: Import socket
#Tamil explanation
#  socket na OS-oda network phone 📞
#   Computer-ku computer pesura bridge.

import socket

# Step 2: Define common ports
# Common ports to scan
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}

# Key = port number
# Value = service name
# Easy-ah output readable.

# Step 3: Port scan function

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
     #Explanation:
     #AF_INET → IPv4
     #SOCK_STREAM → TCP

     #settimeout(1) →

     # 1 second wait, illatti hang aagum 😅

      # Step 4: Try connecting 
      #  
        result = sock.connect_ex((target, port))
        sock.close()

        #VERY IMPORTANT

# connect_ex() returns:

# 0 → SUCCESS → port OPEN

# non-zero → FAIL → CLOSED

# Step 5: Check result

        if result == 0:
            return True
        else:
            return False
    except Exception:
        return False

# Simple logic.
# Security tools simple logic + powerful idea.

# Step 6: Main program

def main():
    target = input("Enter IP or domain: ")

    print(f"\nScanning {target}...\n")

    #User input = reconnaissance target 🎯

    # Step 7: Loop through ports

    for port, service in COMMON_PORTS.items():
        if scan_port(target, port):
            print(f"[OPEN]   Port {port} ({service})")
        else:
            print(f"[CLOSED] Port {port} ({service})")

if __name__ == "__main__":
    main()

# One by one doors check pannrom
# Output clearly visible

# Banner grabbing function (optional)
# banner grabbing helps identify services running on open ports and versions.

def grab_banner(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return None

# modify the scan output

if scan_port(target, port):
    banner = grab_banner(target, port)
    print(f"[OPEN] Port {port} ({service})")
    if banner:
        print(f"       Banner: {banner}")

# Faster Scanning with Threading ⚡

# Threading = scan multiple ports at once.

        import threading

def threaded_scan(target, port, service):
    if scan_port(target, port):
        print(f"[OPEN] Port {port} ({service})")

threads = []

for port, service in COMMON_PORTS.items():
    t = threading.Thread(target=threaded_scan, args=(target, port, service))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

