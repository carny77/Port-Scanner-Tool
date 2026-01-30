import socket
import threading

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}

print_lock = threading.Lock()


def scan_port(target: str, port: int, timeout: float = 1.0) -> bool:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((target, port))
        sock.close()

        return result == 0
    except:
        return False


def grab_banner(target: str, port: int, timeout: float = 2.0):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((target, port))

        banner = sock.recv(1024)
        sock.close()

        banner_text = banner.decode(errors="ignore").strip()
        return banner_text if banner_text else None
    except:
        return None


def worker(target: str, port: int, service_name: str, do_banner: bool):
    is_open = scan_port(target, port)

    with print_lock:
        if is_open:
            print(f"[OPEN]   Port {port:<5} ({service_name})")
            if do_banner:
                banner = grab_banner(target, port)
                if banner:
                    print(f"        Banner: {banner}")
                else:
                    print(f"        Banner: (no banner / blocked / silent)")
        else:
            print(f"[CLOSED] Port {port:<5} ({service_name})")


def main():
    print("\n🔍 Python Port Scanner (Beginner)")
    print("----------------------------------")

    target = input("Enter IP or domain: ").strip()

    banner_choice = input("Enable banner grabbing? (y/n): ").strip().lower()
    do_banner = banner_choice == "y"

    print(f"\nScanning target: {target}\n")

    threads = []
    for port, service_name in COMMON_PORTS.items():
        t = threading.Thread(target=worker, args=(target, port, service_name, do_banner))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n✅ Scan Completed!\n")


if __name__ == "__main__":
    main()
