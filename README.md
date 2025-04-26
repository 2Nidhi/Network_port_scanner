# Network Port Scanner
A simple and multi-threaded Python tool for scanning open TCP ports on multiple hosts, identifying common services, and logging the results.
# Features
•Multi-threaded port scanning for faster results.
•Service and protocol detection for known ports (e.g., HTTP, SSH, FTP).
•Supports scanning multiple IP addresses at once.
•Customizable port range (default 1–65535).
•Saves scan results automatically to a timestamped log file.

# Requirements
Python 3.x
(Uses only built-in libraries: socket, threading, argparse, logging, datetime)

# How It Works
For each host, the script scans the given range of ports.
If a port is open, it identifies the service (e.g., SSH, HTTP).
Results are printed (debug mode) and saved to a .log file.
Each scan uses threading to improve speed.

# Log Files
Log files are automatically created in the same directory.
Format: scan_results_YYYY-MM-DD_HH-MM-SS.log

# Usage
Run the Scanner: python scanner.py --hosts<ip> --start <port> --end<port>
(if multiple hosts than the list of IP should be comma-seperated.)

