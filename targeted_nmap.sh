#!/bin/bash

# Check if a target IP address was provided as an argument
if [ -z "$1" ]; then
    echo "[-] Error: No target IP specified."
    echo "[*] Usage: $0 <IP_ADDRESS>"
    echo "[*] Example: $0 10.10.10.5"
    exit 1
fi

TARGET=$1

echo "[*] Target set to: $TARGET"
echo "[*] Stage 1: Fast scanning all 65,535 ports to find open ports..."

# Run a fast scan on all ports (-p-)
# Extract the open port numbers and format them as a comma-separated list
OPEN_PORTS=$(nmap -p- --min-rate=1000 -T4 -n "$TARGET" | grep -E "^[0-9]+/tcp.*open" | cut -d '/' -f 1 | tr '\n' ',' | sed 's/,$//')

# Check if any ports were found
if [ -z "$OPEN_PORTS" ]; then
    echo "[-] No open ports found on $TARGET. The host might be down or blocking ping/probes."
    exit 1
fi

echo "[+] Open ports found: $OPEN_PORTS"
echo "[*] Stage 2: Running Aggressive scan (-A) on targeted ports..."

# Define an output file name based on the target IP
OUTPUT_FILE="scan_results_${TARGET}.txt"

# Run the aggressive scan on the discovered ports and save the output
nmap -p "$OPEN_PORTS" -A "$TARGET" -oN "$OUTPUT_FILE"

echo "[+] Scan complete!"
echo "[+] Results saved to: $OUTPUT_FILE"
