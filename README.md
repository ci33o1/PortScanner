# PortScanner
Multi-Threaded Port Scanner With Python

# Port Scanner

This is a simple Python-based port scanner that allows you to scan a range of ports on a given IP address or domain. It supports multi-threading for faster scans, customizable port ranges, and an option to input user-defined IPs and threads.

## Features

- **Scan IP/Domain**: You can scan both IP addresses and domain names.
- **Port Range**: Customizable port range for scanning (default: all ports from 0 to 65535).
- **Multi-threading**: Fast scans with adjustable thread count (default: 35 threads).
- **Service Mapping**: Displays the common service name associated with each open port.
- **User Input and Argument Parsing**: Supports both command-line arguments and interactive user input for flexibility.

## Requirements

Before using this port scanner, ensure you have the following installed:

- Python 3.7+
- The following Python libraries:
  - `socket`
  - `argparse`
  - `concurrent.futures`
  - `time`
  - `sys`

These are part of Python's standard library, so no extra installation should be needed for the dependencies.

## Installation

1. Clone this repository or download the files to your local machine.
2. Make sure you have Python 3.7+ installed.
3. You can run the script directly by navigating to the project directory and using the following command in your terminal:

    ```bash
    python portscanner.py
    ```

### Default Arguments

By default, the scanner will attempt to:

- Scan all ports from 0 to 65535.
- Use 35 threads for scanning.

If you want to customize the port range or threads, you can pass the relevant arguments through the command line. Alternatively, if you prefer to use the default settings, simply press Enter when prompted for the port range or threads, and the default values will be used.


### Command Line Arguments

You can use the following command-line arguments to configure the scanner:

- `-ip`, `--ip`: The IP address or domain name to scan.
- `-p`, `--ports`: The port range to scan (e.g., `80 100`).
- `-t`, `--threads`: The number of threads to use for scanning (default is 35).

Example usage:

```bash
python portscanner.py --ip example.com --ports 0 1000 --threads 50
```
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjRkNG8wazVmNDR1aDMyYXBpaXEzNmI2MmJ1bXJma3lkbHI1N3hvNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/49t2xI2qDWfPNk6esL/giphy.gif" width=1000>
