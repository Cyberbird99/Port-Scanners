import nmap

# Firtst put the target in a variable
target_host = "10.20.10.10"

# Identify beginning and ending ports for the scan
port_beginning = 1
port_ending = 150

# And create the scanner object
port_scanner = nmap.PortScanner()

print("scanning {0}".format(target_host))
# Loop through each port and scan.
for port in range(port_beginning, port_ending + 1):
    result = port_scanner.scan(target_host,str(port))
    port_status = result['scan'] [target_host] ['tcp'] [port] ['state']
    print("\tPort: {0} is (1)".format(port, port_status))