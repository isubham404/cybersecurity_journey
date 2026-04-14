text = input("Enter text: ")
shift = 3

choice = input("Type 'e' to encrypt or 'd' to decrypt: ")

result = ""

for char in text:
    if char.isalpha():
        if choice == 'e':
            new_char = chr(ord(char) + shift)
        elif choice == 'd':
            new_char = chr(ord(char) - shift)
        else:
            new_char = char
        result += new_char
    else:
        result += char

print("Result:", result)