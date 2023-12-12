import hashlib
import getpass
import os
def register_account(account, password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    key = hashlib.sha256(salt + pwdhash).hexdigest().encode('ascii')

    try:
        with open('password_storage.txt', 'x') as f:
            f.write(key)
            print('Account successfully registered!')
    except FileExistsError:
        print('An account is already registered. Please delete the password_storage.txt file if you want to register a new account.')


def verify_account(account, password):
    try:
        with open('password_storage.txt', 'r') as f:
            key = f.readline().strip()
    except FileNotFoundError:
        print('No account registered. Please register an account.')
        return False

    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    entered_key = hashlib.sha256(salt + pwdhash).hexdigest().encode('ascii')

    if key == entered_key:
        return True
    else:
        print('Invalid password.')
        return False
def register_password(password):
    with open('password_storage.txt', 'a') as f:
        f.write(f' {password}')
        print('Password successfully registered!')
def verify_password(password):
    try:
        with open('password_storage.txt', 'r') as f:
            stored_passwords = f.read().split()
            if password in stored_passwords:
                return True
            else:
                print('Invalid password.')
                return False
    except FileNotFoundError:
        print('No passwords registered. Please register a password.')
        return False
def main():
    print("Welcome to Secure Password Manager!")
    action = input("Enter 'register' to register an account or 'verify' to verify an existing account: ")

    if action == 'register':
        password = getpass.getpass('Enter a password: ')
        register_account('user', password)
    elif action == 'verify':
        password = getpass.getpass('Enter your password: ')

        if verify_account('user', password):
            while True:
                action = input("\nEnter 'register' to register a password or 'verify' to verify a password: ")

                if action == 'register':
                    password_to_register = getpass.getpass('Enter a password to register: ')
                    register_password(password_to_register)

                elif action == 'verify':
                    password_to_verify = getpass.getpass('Enter a password to verify: ')
                    verify_password(password_to_verify)

                else:
                    print('Invalid action. Please enter either "register" or "verify".')
    else:
        print('Invalid action. Please enter either "register" or "verify".')
if __name__ == "__main__":
    main()