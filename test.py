import random

def generate_password():
  # ask the user which side of the keyboard they want the keys to be from
  side = input("Which side of the keyboard do you want the keys to be from? (left/right) ")
  
  # ask the user which types of characters they want to use in the password
  choices = []
  if input("Include lowercase letters in the password? (y/n) ").lower() == 'y':
    choices.extend(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
  if input("Include uppercase letters in the password? (y/n) ").lower() == 'y':
    choices.extend(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  if input("Include numbers in the password? (y/n) ").lower() == 'y':
    choices.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
  if input("Include symbols in the password? (y/n) ").lower() == 'y':
    choices.extend(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?'])
  
  # filter the choices based on the side of the keyboard the user specified
  if side == 'left':
    choices = [key for key in choices if key in ['ba', 'be', 'ca', 'ce', 'da', 'de', 'fa', 'fe', 'ga', 'ge', 'qa', 'qe', 'ra', 're', 'sa', 'se', 'ta', 'te', 'va', 've', 'wa', 'we', 'za', 'ze', '5', '4', '3', '2', '1', '%', '$', '#', '@', '!']]
  elif side == 'right':
    choices = [key for key in choices if key in ['hi', 'ho', 'hu', 'ji', 'jo', 'ju', 'ki', 'ko', 'ku', 'li', 'lo', 'lu', 'mi', 'mo', 'mu', 'ni', 'no', 'nu', 'pi', 'po', 'pu', 'yi', 'yo', 'yu', '6', '7', '8', '9', '0', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', ';', ':', '\'', ',', '<', '.', '>', '/', '?']]
  
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
