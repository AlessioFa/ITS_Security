import re
from collections import Counter


def analyze_logs_basic(file_path):
    """
    Basic Log Analyzer for Security+ Study.
    Focus: Volume anomalies, Error rates, and Known suspicious keywords.
    """
    
    # 1. SETUP REGEX PATTERN
    # We use a Regular Expression to parse the 'Common Log Format' (CLF).
    # Group 1 (\S+): IP Address
    # Group 2 \[(.*?)\]: Timestamp
    # Group 3 "(.*?)": The actual HTTP Request (Method + URL + Protocol)
    # Group 4 (\d{3}): HTTP Status Code (e.g., 200, 404)
    log_pattern = re.compile(r'(\S+) - - \[(.*?)\] "(.*?)" (\d{3}) (\S+)')

    # 2. INITIALIZE COUNTERS
    # 'Counter' is a high-performance dictionary for counting items.
    # ip_counter: Tracks total requests per IP (Volume Analysis).
    # error_counter: Tracks 4xx/5xx responses per IP (Error Analysis).
    ip_counter = Counter()
    error_counter = Counter()
    
    # List to store full details of suspicious requests found
    suspicious_requests = []

    # 3. DEFINE THREAT SIGNATURES
    # A basic list of strings that should rarely appear in normal traffic.
    # These indicate attempts to access system files or admin panels.
    suspicious_keywords = [
        '/etc/passwd',  # Unix password file (Critical)
        'cmd.exe',      # Windows command prompt (Remote Code Execution)
        'root',         # Superuser account
        'admin',        # Administrative panels
        '..',           # Directory Traversal attempts
        '/cgi-bin/'     # Common target for exploits in the 90s
    ]

    print(f"--- Starting Basic Analysis on: {file_path} ---")

    try:
        # Open file with 'utf-8' and ignore errors to handle binary junk safely
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            
            # STREAM PROCESSING LOOP
            # We read line by line to handle large files without using too much RAM.
            for line in f:
                match = log_pattern.match(line)
                if match:
                    # Extract data using the regex groups defined above
                    ip = match.group(1)
                    request = match.group(3)
                    status = match.group(4)
                    
                    # --- METRIC A: TRAFFIC VOLUME ---
                    # Every request counts towards the IP's total volume.
                    # High volume in short time = DoS or heavy scanning.
                    ip_counter[ip] += 1

                    # --- METRIC B: ERROR RATE ---
                    # Status codes starting with '4' (Client Error) or '5' (Server Error).
                    # High error count = Blind scanning or seeking vulnerabilities.
                    if status.startswith('4') or status.startswith('5'):
                        error_counter[ip] += 1

                    # --- METRIC C: SIGNATURE MATCHING ---
                    # Check if the request contains any bad keywords.
                    for keyword in suspicious_keywords:
                        if keyword in request:
                            # Log the finding
                            suspicious_requests.append(f"DETECTED: '{keyword}' from IP {ip} -> {request}")
                            # Stop checking other keywords for this specific line
                            break

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return

    # 4. GENERATE REPORT
    print("\n" + "="*50)
    print("BASIC SECURITY ANALYSIS REPORT")
    print("="*50)

    # Report 1: Top Talkers (Volume)
    print("\n[1] High Volume Traffic (Top 5 IPs):")
    print("    Insight: Look for automated bots or potential DoS sources.")
    for ip, count in ip_counter.most_common(5):
        print(f"    - {ip}: {count} requests")

    # Report 2: Top Error Generators
    print("\n[2] High Error Rates (Top 5 IPs):")
    print("    Insight: These IPs are likely scanning for non-existent files.")
    for ip, count in error_counter.most_common(5):
        print(f"    - {ip}: {count} errors")

    # Report 3: Suspicious Signatures
    print(f"\n[3] Suspicious Keyword Matches (Total: {len(suspicious_requests)}):")
    print("    Insight: Direct evidence of malicious intent or probing.")
    # Show only the first 10 to keep the output clean
    for item in suspicious_requests[:10]:
        print(f"    {item}")


if __name__ == "__main__":
    analyze_logs_basic('NASA_access_log_Aug95')