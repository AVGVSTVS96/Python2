import random
import string

# Generate passwords by specifying the length, types of characters, and which side of the keyboard to use

def password_generator(length, uppercase, lowercase, numbers, symbols, left_side):
  password = ""
  # Set of characters to choose from
  chars = ""
  if uppercase:
    chars += string.ascii_uppercase
  if lowercase:
    chars += string.ascii_lowercase
  if numbers:
    chars += string.digits
  if symbols:
    chars += string.punctuation

  # Generate the password
  for i in range(length):
    if left_side:
      # Use only keys from the left side of the QWERTY keyboard
      if uppercase:
        password += random.choice("QWASZXEDCRFV")
        continue
      if lowercase:
        password += random.choice("qwaszxedcrfv")
        continue
      if numbers:
        password += random.choice("123045")
        continue
      if symbols:
        password += random.choice("!@#$%^")
        continue
    else:
      # Use only keys from the right side of the QWERTY keyboard
      if uppercase:
        password += random.choice("PLOKMIJNUHBY")
        continue
      if lowercase:
        password += random.choice("plokmiijnuhby")
        continue
      if numbers:
        password += random.choice("6789")
        continue
      if symbols:
        password += random.choice("&*()_+")
        continue

  return password

def main():
  # Get input from the user
  length = int(input("Enter the length of the password: "))
  uppercase = bool(input("Include uppercase characters? (True/False): "))
  lowercase = bool(input("Include lowercase characters? (True/False): "))
  numbers = bool(input("Include numbers? (True/False): "))
  symbols = bool(input("Include symbols? (True/False): "))
  left_side = bool(input("Use only keys from the left side of the QWERTY keyboard? (True/False): "))

  # Generate the password
  password = password_generator(length, uppercase, lowercase, numbers, symbols, left_side)
  print("Your password is:", password)

  # Rate the password's strength
  if length < 8:
    print("Password strength: weak (1/6)")
  elif length < 12:
    print("Password strength: medium (2/6)")
  elif length < 16:
    print("Password strength: strong (3/6)")
  elif uppercase and lowercase and numbers and symbols:
    print("Password strength: very strong (5/6)")
  else:
    print("Password strength: secure (4/6)")

if __name__ == "__main__":
  main()

# Ask if the user wants to generate another password
while True:
    again = input("Generate another password? (y/n): ")
    if again.lower() == "y":
        main()
        continue

    elif again.lower() == "n":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue
