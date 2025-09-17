import socket

def scan_ports(target, ports=[21,22,23,25,53,80,443,8080]):
    print(f"Scanning target: {target}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

if __name__ == "__main__":
    target = input("Enter host to scan (e.g., 127.0.0.1): ")
    scan_ports(target)
