text = input("Enter the text : ")
shift = 3
result = ""

for char in text:
    if char.isalpha():
        new_char = chr(ord(char) + shift)
        result+=new_char
    else :
        result+=char

print("encrypted text is :", result)