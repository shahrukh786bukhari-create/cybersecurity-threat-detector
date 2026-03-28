import logging
from collections import defaultdict

# Setup logging
logging.basicConfig(filename='alerts.log', level=logging.INFO, format='%(asctime)s - %(message)s')

failed_attempts = defaultdict(int)

def login_attempt(ip, success):
    if not success:
        failed_attempts[ip] += 1
    else:
        failed_attempts[ip] = 0

    if failed_attempts[ip] >= 5:
        alert = f"⚠️ ALERT: Possible brute-force attack from {ip}"
        print(alert)
        logging.info(alert)

# Simulate attacks
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)
