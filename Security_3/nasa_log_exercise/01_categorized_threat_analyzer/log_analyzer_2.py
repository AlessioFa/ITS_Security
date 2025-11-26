import re
from collections import Counter, defaultdict


def analyze_threats_categorized(file_path):
    """
    Intermediate Log Analyzer for Security+ Study.
    Focus: Threat Classification & Attack Signatures.
    
    Concept: Instead of just finding keywords, we group them by 'Intent'.
    This helps an analyst understand WHAT the attacker is trying to achieve.
    """
    
    # 1. SETUP REGEX (Standard CLF Format)
    log_pattern = re.compile(r'(\S+) - - \[(.*?)\] "(.*?)" (\d{3}) (\S+)')

    ip_counter = Counter()
    error_counter = Counter()
    
    # 'defaultdict(list)' is a dictionary that automatically creates a list
    # for a new key. Useful for grouping events under categories like "SQL Injection" or "Traversal".
    suspicious_events = defaultdict(list)

    # 2. DEFINE ATTACK SIGNATURES (The "Rules")
    # In a SIEM (Security Information and Event Management), these would be your detection rules.
    attack_signatures = {
        # ATTACK TYPE: Directory Traversal
        # Intent: Escape the web root to access system files.
        'Traversal & System Files': [
            '../', '..\\',       # The classic "dot-dot-slash" move
            '/etc/passwd',       # Unix user database
            'win.ini',           # Old Windows config
            'boot.ini'           # Windows boot loader
        ],
        
        # ATTACK TYPE: Remote Code Execution (RCE) / Shell
        # Intent: Execute commands on the server to take control.
        'Command Execution (RCE)': [
            '/bin/sh',           # Unix Shell
            'cmd.exe',           # Windows Command Prompt
            'phf',               # A famous 90s exploit for CGI scripts
            'test-cgi'           # Often left open by default on servers
        ],
        
        # ATTACK TYPE: Information Disclosure
        # Intent: Find leftover files that shouldn't be public.
        'Suspicious Extensions (Backup/Config)': [
            '.bak', '.old',      # Backup files (often contain source code)
            '.orig', '.config',  # Configuration files
            '.sql', '.db'        # Database dumps
        ],
        
        # ATTACK TYPE: Privilege Escalation / Admin Hunt
        # Intent: Find the login portal to brute-force it.
        'Admin/Privileged Access': [
            'admin', 'root', 'manager', 'webmaster'
        ]
    }

    print(f"--- Starting Categorized Threat Analysis on: {file_path} ---")

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                match = log_pattern.match(line)
                if match:
                    ip = match.group(1)
                    request = match.group(3)
                    status = match.group(4)
                    
                    # Basic stats still useful for context
                    ip_counter[ip] += 1
                    if status.startswith('4') or status.startswith('5'):
                        error_counter[ip] += 1

                    # 3. ENHANCED DETECTION LOGIC
                    # Check the request against EACH category of signatures.
                    for category, patterns in attack_signatures.items():
                        for pattern in patterns:
                            if pattern in request:
                                # We found a match!
                                event_desc = f"[{category}] Pattern '{pattern}' found from IP {ip}"
                                suspicious_events[category].append(event_desc)
                                # Break inner loop to avoid double-counting the same line for the same category
                                break 

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    # 4. GENERATE CATEGORIZED REPORT
    print("\n" + "="*60)
    print("THREAT INTELLIGENCE REPORT (CATEGORIZED)")
    print("="*60)

    # We skip the basic volume stats here to focus on threats, 
    # but you could include them if you want.

    print("\n[+] DETECTED THREATS BY CATEGORY")
    print("    Insight: This breakdown helps prioritize which vulnerability to fix first.")
    print("-" * 60)

    if not suspicious_events:
        print("No suspicious patterns detected based on current signatures.")
    else:
        for category, events in suspicious_events.items():
            # count total events in this category
            count = len(events)
            print(f"\n>>> Category: {category} (Total Attempts: {count})")
            
            # De-duplicate events to show unique attackers/patterns only
            unique_events = list(set(events))
            
            # Show first 10 unique events
            for event in unique_events[:10]:
                print(f"    {event}")
            
            if len(unique_events) > 10:
                print(f"    ... and {len(unique_events) - 10} more unique variations.")


if __name__ == "__main__":
    analyze_threats_categorized('NASA_access_log_Aug95')
