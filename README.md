# FTP to HTTP Exploit Chain (Python) 🐍🔓

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Category](https://img.shields.io/badge/Category-Network%20Exploitation-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Educational-green?style=for-the-badge)

## 📜 Overview
This script automates a multi-protocol attack chain. It was developed during **Day 23** of my `#90_days_locked_in_cs` challenge to demonstrate how information leakage in one service (FTP) can lead to the compromise of another (HTTP).

Instead of manually interacting with `netcat` or GUI tools, this tool:
1.  **Connects** to a misconfigured FTP server.
2.  **Exfiltrates** sensitive internal files.
3.  **Parses** the file to extract a secret `User-Agent` string.
4.  **Weaponizes** that secret to bypass HTTP access controls and dump the hidden web page.

## ⚡ The Attack Logic
The script logic follows the "Kill Chain" concept:
1.  **Reconnaissance/Access:** Log into FTP as `anonymous`.
2.  **Collection:** Download `Note-From-IT.txt`.
3.  **Weaponization:** Read the file locally and extract the specific "Server Administrator" string.
4.  **Execution:** Craft a custom HTTP GET request using `requests` with the spoofed header.
5.  **Exfiltration:** Print the restricted website content (flag/data).

## 🛠️ Usage

### Prerequisites
* Python 3.x
* `requests` library

```bash
pip install requests
