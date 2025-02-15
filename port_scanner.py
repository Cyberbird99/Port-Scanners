import nmap

# Define the target IP address to scan
target_ip = "10.20.10.10"

# Specify the starting and ending ports for the scan
start_port = 1
end_port = 200

# Create an instance of the nmap.PortScanner class
scanner = nmap.PortScanner()

# Print a message indicating which host is being scanned
print(f"Scanning {target_ip}...")

# Iterate over the range of ports to scan
for port in range(start_port, end_port + 1):
    # Perform the scan for the current port
    scan_result = scanner.scan(target_ip, str(port))
    
    # Extract the state (open/closed) of the current port
    port_state = scan_result['scan'][target_ip]['tcp'][port]['state']
    
    # Output the port number and its state
    print(f"\tPort {port} is {port_state}")
