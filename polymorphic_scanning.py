from abc import ABC, abstractmethod  # Import ABC and abstractmethod for creating abstract base classes
import socket  # Import socket module for network connections
import random  # Import random module for simulating vulnerability scanning
import subprocess  # Import subprocess module for running shell commands

# Define the Interface Using an Abstract Base Class
class Scanner(ABC):
    @abstractmethod
    def scan(self, target: str):
        """
        Abstract method to be implemented by all scanners.
        :param target: The target to scan (e.g., IP address or hostname)
        :return: Result of the scan
        """
        pass

# Implement Port Scanning Technique
class PortScanner(Scanner):
    def __init__(self, start_port: int = 1, end_port: int = 1024):
        """
        Initialize PortScanner with a range of ports.
        :param start_port: The starting port number for the scan (default is 1)
        :param end_port: The ending port number for the scan (default is 1024)
        """
        self.start_port = start_port
        self.end_port = end_port

    def scan(self, target: str):
        """
        Scans for open ports on the target.
        :param target: The IP address or hostname to scan
        :return: List of open ports
        """
        open_ports = []  # Initialize an empty list to store open ports
        for port in range(self.start_port, self.end_port + 1):  # Iterate over the specified range of ports
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
            sock.settimeout(1)  # Set a timeout of 1 second for the connection attempt
            result = sock.connect_ex((target, port))  # Try to connect to the target on the given port
            if result == 0:  # If connection is successful (result == 0)
                open_ports.append(port)  # Add the port to the list of open ports
            sock.close()  # Close the socket connection
        return open_ports  # Return the list of open ports

# Implement Vulnerability Scanning Technique
class VulnerabilityScanner(Scanner):
    def scan(self, target: str):
        """
        Simulates a vulnerability scan on the target.
        :param target: The IP address or hostname to scan
        :return: List of found vulnerabilities
        """
        vulnerabilities = ["SQL Injection", "Cross-Site Scripting", "Buffer Overflow"]  # List of possible vulnerabilities
        found_vulnerabilities = random.sample(vulnerabilities, random.randint(0, len(vulnerabilities)))  
        # Randomly select some vulnerabilities to simulate a scan
        return found_vulnerabilities  # Return the list of found vulnerabilities

# Implement Network Scanning Technique
class NetworkScanner(Scanner):
    def scan(self, target: str):
        """
        Performs a network scan by pinging the target.
        :param target: The IP address or hostname to scan
        :return: Output from the ping command or an error message if access is denied
        """
        try:
            result = subprocess.run(['ping', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # Execute the ping command
            return result.stdout.decode()  # Decode and return the output of the ping command
        except PermissionError:
            return "Access denied. Administrative privileges are required to run ping."

# Function to Perform a Scan Using Any Scanner
def perform_scan(scanner: Scanner, target: str):
    """
    Perform a scan using the given scanner and target.
    :param scanner: An instance of a class that implements the Scanner interface
    :param target: The target to scan (e.g., IP address or hostname)
    """
    result = scanner.scan(target)  # Call the scan method of the scanner
    print(f"\nResults for {target}: {result}")  # Print the results of the scan

# Example usage
if __name__ == "__main__":
    target = input("Enter the target IP address or hostname: ")  # Get the target IP address or hostname from the user
    
    # Perform Port Scanning
    start_port = int(input("Enter the starting port for the port scan: "))  # Get the starting port from the user
    end_port = int(input("Enter the ending port for the port scan: "))  # Get the ending port from the user
    port_scanner = PortScanner(start_port, end_port)  # Create an instance of PortScanner with the specified range

    import auto_scan_loading
    perform_scan(port_scanner, target)  # Perform the port scan on the target

    # Perform Vulnerability Scanning
    vuln_scanner = VulnerabilityScanner()  # Create an instance of VulnerabilityScanner
    perform_scan(vuln_scanner, target)  # Perform the vulnerability scan on the target

    # Perform Network Scanning
    network_scanner = NetworkScanner()  # Create an instance of NetworkScanner
    perform_scan(network_scanner, target)  # Perform the network scan on the target
