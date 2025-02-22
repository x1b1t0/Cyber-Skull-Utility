# Cyber-Skull-Utility

## Description

**Cyber-Skull-Utility** is a cybersecurity tool developed in Python that provides various utilities for network scanning, SMB share enumeration, firewall rule checking, network traffic sniffing, and SSH brute force attacks (for authorized testing only).

## Features

- **Network Scan (Nmap)**: Performs a network scan using Nmap to detect services and versions.
- **Enumerate SMB Shares**: Enumerates SMB shares of a target.
- **Check Firewall Rules**: Checks firewall rules on Windows or Linux systems.
- **Sniff Network Traffic (tcpdump)**: Captures network traffic on any interface.
- **SSH Brute Force (Hydra)**: Attempts a brute-force attack on SSH using Hydra (for authorized testing only).

## Requirements

- Python 3.x
- [colorama](https://pypi.org/project/colorama/)
- Nmap
- smbclient
- netsh (for Windows)
- ufw (for Linux)
- tcpdump
- Hydra

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/x1b1t0/Cyber-Skull-Utility.git
   cd Cyber-Skull-Utility
   ```

2. Install Python dependencies:
   ```bash
   pip install colorama
   ```

3. Ensure the following programs are installed on your system:
   - Nmap
   - smbclient
   - netsh (for Windows)
   - ufw (for Linux)
   - tcpdump
   - Hydra

## Usage

1. Run the main script:
   ```bash
   python cyber_skull_utility.py
   ```

2. Follow the on-screen instructions to select the desired utility.

## Important Note

**Cyber-Skull-Utility** is intended for educational purposes and authorized testing only. Do not use this tool for illegal activities or without explicit permission from the target owner. The misuse of this tool is solely the user's responsibility.

## Contributing

Contributions are welcome! If you wish to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Development Status

This project is currently under development. New features and improvements are being added regularly. Stay tuned for updates!
