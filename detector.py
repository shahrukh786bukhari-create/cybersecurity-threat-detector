from collections import defaultdict

failed_attempts = defaultdict(int)

def login_attempt(ip, success):
    if not success:
        failed_attempts[ip] += 1
    else:
        failed_attempts[ip] = 0

    if failed_attempts[ip] >= 5:
        print(f"⚠️ ALERT: Possible brute-force attack from {ip}")

# Simulate activity
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)
login_attempt("192.168.1.1", False)
