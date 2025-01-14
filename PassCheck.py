import re


def check_password(password):
    if len(password) < 16:
        print("Password is too short.")
        return False

    if not re.search(r'[A-Z]', password):
        print("Password does not contain an uppercase letter.")
        return False

    if not re.search(r'[a-z]', password):
        print("Password does not contain a lowercase letter.")
        return False

    if not re.search(r'\d', password):
        print("Password does not contain a digit.")
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Password does not contain a special character.")
        return False

    print("Password is valid.")
    return True

if __name__ == "__main__":

    password = input("Input your password: ")
    is_valid = check_password(password)

    if is_valid:
        print("Password is valid.")
    else:
        print("Password is not accepted.")
