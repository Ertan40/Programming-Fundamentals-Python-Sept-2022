def validates_password(some_password):
    password_is_valid = True
    if not 6 <= len(some_password) <= 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False
    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False
    digit_counter = 0
    for current_character in some_password:
        if current_character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False
    return password_is_valid


password = input()
password_is_valid = validates_password(password)
if password_is_valid:
    print("Password is valid")
