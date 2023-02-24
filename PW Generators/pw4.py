import random

def generate_password():
    # ask the user which side of the keyboard they want the keys to be from
    side = input("Which side of the keyboard do you want the keys to be from? (left/right) ")

    choices = []
    options = {
        'lower': 'abcdefghijklmnopqrstuvwxyz',
        'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'numeric': '0123456789',
        'symbols': '!@#$%^&*()-_=+[]{}\\|;:\'",.<>/?'
    }
    for option, keys in options.items():
        if input(f"Include {option} in the password? (y/n) ").lower() == 'y':
            choices.extend(list(keys))

    # filter the choices based on the side of the keyboard the user specified
    if side == 'left':
        choices = [key for key in choices if key in 'qwertasdfgzxcvb12345!@#$%QWERASDFGZXCVB']
    elif side == 'right':
        choices = [key for key in choices if key in 'yuiophjklnmYUIOPHJKLNM67890^&*()-_=+[]{};:\'",.<>/?']

    # generate the password
    password_length = int(input("Enter the desired length of the password: "))
    password = ''.join(random.choices(choices, k=password_length))

    return password

# main loop
while True:
    password = generate_password()
    print(f"Your password is: {password}")
    again = input("Generate another password? (y/n) ").lower()
    if again != 'y':
        break

print("Goodbye!") 