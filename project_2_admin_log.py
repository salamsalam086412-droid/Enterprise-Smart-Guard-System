def admin_login():
    admin_credentials = {"username": "admin123", "password": "SecurePassword@2026"}
    failed_attempts = 0
    max_attempts = 3
    while failed_attempts < max_attempts:
        input_user = input("Enter Username:")
        input_pass = input("Enter Password:")
        if input_user == admin_credentials["Username"] and input_pass == admin_credentials["password"]:
            print("[+] Access Granted: Welcome back, Admin.")
            return True
        else:
            failed_attempts += 1
            remaining = max_attempts - failed_attempts
            print(f"[-] Invalid credentials. Remaining attempts: {remaining}")
    print("\n[!] CRITICAL ALERT: System Locked due to too many failed attempts.")
