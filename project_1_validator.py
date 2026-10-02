def validate_password(password):
    
    if len(password) < 8:
        print("[-] Security Error: Password must be at least 8 characters long.")
        return False
          # Step 2: Check for at least one digit
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        print("[-] Security Error: Password must contain at least one number.")
        return False
          # Step 3: Check for at least one special character
    special_characters = "@#$%^&+=!"
    has_special = any(char in special_characters for char in password)
    if not has_special:
        print("[-] Security Error: Password must contain at least one special character (@#$%^&+=!).")
        return False

    return True
  # Test the validator
print(validate_password("Test1234@"))
