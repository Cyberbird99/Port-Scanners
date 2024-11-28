import nmap

# Define the target IP address to scan
target_ip = "10.20.10.10"

# Specify the port range for the scan (inclusive)
start_port = 1
end_port = 150

# Initialize the Nmap PortScanner object
scanner = nmap.PortScanner()

# Function to scan ports and return the state of each port
def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} from port {start_port} to port {end_port}...")

    # Loop through each port in the specified range
    for port in range(start_port, end_port + 1):
        try:
            # Perform the scan on the current port
            scan_result = scanner.scan(target_ip, str(port))

            # Check if the scan was successful and extract the port state
            port_state = scan_result['scan'][target_ip]['tcp'][port]['state']
            print(f"\tPort {port} is {port_state}")

        except KeyError:
            # Handle cases where the port is not found or the scan fails
            print(f"\tPort {port}: Scan failed or no data available")
        except Exception as e:
            # Handle any unexpected errors during scanning
            print(f"\tPort {port}: Error occurred - {e}")

# Call the scan_ports function to start scanning
scan_ports(target_ip, start_port, end_port)
