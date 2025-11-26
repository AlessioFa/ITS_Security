import re
from collections import defaultdict


def analyze_confirmed_incidents(file_path):
    """
    Advanced Log Analyzer for Security+ Study.
    Focus: Incident Verification (Successful Exploits).
    
    Concept: A 'threat' becomes an 'incident' ONLY if the attack succeeds.
    We filter for specific attack patterns that received a 200 OK status code.
    """
    
    # 1. SETUP REGEX
    log_pattern = re.compile(r'(\S+) - - \[(.*?)\] "(.*?)" (\d{3}) (\S+)')

    # Dictionary to store ONLY confirmed breaches
    confirmed_breaches = defaultdict(list)

    # 2. DEFINE CRITICAL SIGNATURES
    # We use the same categories, but now we only care if they WORKED.
    attack_signatures = {
        'Traversal & System Files': [
            '../', '..\\', '/etc/passwd', 'win.ini', 'boot.ini'
        ],
        'Command Execution (RCE)': [
            '/bin/sh', 'cmd.exe', 'phf', 'test-cgi'
        ],
        'Sensitive Config/Backup': [
            '.bak', '.old', '.orig', '.config', '.db'
        ],
        # We look for successful logins to admin pages
        'Admin Access (Potential Compromise)': [
            '/admin', '/root', '/manager'
        ]
    }

    print(f"--- Starting Incident Verification on: {file_path} ---")
    print("--- FILTER: Searching for Status Code 200 (Success) ONLY ---")

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                match = log_pattern.match(line)
                if match:
                    ip = match.group(1)
                    timestamp = match.group(2)
                    request = match.group(3)
                    status = match.group(4)
                    
                    # 3. CRITICAL FILTER: STATUS 200 OK
                    # If the status is NOT 200, the attack failed (blocked by server/permissions).
                    # We only care about "Success" (200) here.
                    if status == '200':
                        
                        # Check against our threat signatures
                        for category, patterns in attack_signatures.items():
                            for pattern in patterns:
                                if pattern in request:
                                    # INCIDENT CONFIRMED
                                    # Create a detailed evidence string
                                    evidence = f"IP: {ip} | Time: {timestamp} | File: {request}"
                                    confirmed_breaches[category].append(evidence)
                                    break 

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    # 4. GENERATE INCIDENT REPORT
    print("\n" + "!"*60)
    print("CRITICAL INCIDENT REPORT (CONFIRMED BREACHES)")
    print("!"*60)

    if not confirmed_breaches:
        print("\nGood News: No successful attacks detected.")
        print("Attackers tried, but the server returned errors (403/404).")
    else:
        print(f"\n[!!!] ALERT: {len(confirmed_breaches)} Categories with Confirmed Incidents!")
        print("    Action Required: Immediate Remediation.")
        
        for category, events in confirmed_breaches.items():
            print(f"\n>>> Incident Type: {category}")
            # Show all events because confirmed incidents are rare and critical
            for event in events:
                print(f"    [EVIDENCE] {event}")


if __name__ == "__main__":
    analyze_confirmed_incidents('NASA_access_log_Aug95')
