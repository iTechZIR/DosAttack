> # DosAttack Tool - Denial of Service

# Description

A stress testing tool for evaluating server resilience against repeated HTTP requests. This tool is designed for educational purposes and testing your own servers only.
⚠️ Legal Warning

    Any illegal use of this tool is strictly prohibited

    Using it to attack others' servers is considered a crime

    This tool should only be used for testing personal servers or with explicit server owner permission

# Features

    Sends repeated HTTP/HTTPS requests

    Automatic port detection (80 for HTTP, 443 for HTTPS)

    Random User-Agent selection from text file

    Real-time request status display

    Detailed packet logging

# Installation
# Prerequisites

    Python 3.6 or higher

    Internet connection

# Install Required Library
```bash
pip install requests
```
# Usage
1. Prepare User-Agent File

Create a file named __user_agent__.txt in the same directory as the script. Add one User-Agent per line:
```bash

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
```
2. Run the Script
```bash

python dos_attack.py
```
3. Enter Required Information
```bash

╔══════════════════════════════════════════════════════╗
║                     DosAttack                        ║
║                 Denial of Service                    ║
║                                                      ║
║            Version: 1.0    Creator: 2yt              ║
╚══════════════════════════════════════════════════════╝

please enter url (https or http): https://example.com
please enter loop count number: 100
```
# Output Example
```bash

PACKET: 0 URL: https://example.com PORT: 443 STATUS: SUCCESS
PACKET: 1 URL: https://example.com PORT: 443 STATUS: SUCCESS
PACKET: 2 URL: https://example.com PORT: 443 STATUS: SUCCESS
```

# How It Works
1. User-Agent Selection

Reads random User-Agent from __user_agent__.txt
2. Port Detection

    https:// → Port 443

    http:// → Port 80

    Other → "UNKNOWN"

3. Status Checking

    200 → "SUCCESS"

    Other codes → "FAILED: [code]"

    Connection errors → "ERROR: [message]"

4. Attack Execution

Sends specified number of requests with random User-Agent
# Security Notes

    Use responsibly and ethically

    Only test servers you own or have explicit permission to test

    Be aware of your country's cyber laws

    Consider using dedicated testing environments

# Troubleshooting
# Common Issues:

    "File not found" error

        Ensure __user_agent__.txt exists in the same directory

    Connection errors

        Check internet connection

        Verify URL format (include http:// or https://)

    Module not found

        Install requests: pip install requests

# File Structure
```bash

dos_attack.py                    # Main script
__user_agent__.txt  # User-Agent database
README.md                        # This file
```
# Contact & Support

    Creator: 2yt

    Channel: @iTechZIR

    Channel: @dev_2yt_code_c

# License

For educational purposes only. Use at your own risk

REMINDER: This tool demonstrates basic HTTP request concepts. Misuse may result in legal consequences. Always obtain proper authorization before testing any server.