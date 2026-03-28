import logging
from collections import defaultdict

# Setup logging
logging.basicConfig(filename='alerts.log', level=logging.INFO, format='%(asctime)s - %(message)s')

failed_attempts = defaultdict(int)
blocked_ips = set()  # Track blocked IPs

MAX_ATTEMPTS = 5  # Threshold for brute-force

def login_attempt(ip, success):
    if ip in blocked_ips:
        print(f"🚫 Access denied for blocked IP: {ip}")
        return

    if not success:
        failed_attempts[ip] += 1
    else:
        failed_attempts[ip] = 0

    if failed_attempts[ip] >= MAX_ATTEMPTS:
        alert = f"⚠️ ALERT: Possible brute-force attack from {ip}"
        print(alert)
        logging.info(alert)
        blocked_ips.add(ip)
        print(f"🚫 IP {ip} has been blocked")

# Simulate activity
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)

# Test blocked IP
login_attempt("192.168.1.1", False)
# Simulate multiple IP login attempts
test_ips = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4"
]

# Simulate login activity
login_attempts_sequence = [
    ("192.168.1.1", False),
    ("192.168.1.2", False),
    ("192.168.1.1", False),
    ("192.168.1.3", False),
    ("192.168.1.2", False),
    ("192.168.1.1", False),
    ("192.168.1.4", False),
    ("192.168.1.1", False),
    ("192.168.1.2", False),
    ("192.168.1.1", False),  # This should trigger block
]

for ip, success in login_attempts_sequence:
    login_attempt(ip, success)
