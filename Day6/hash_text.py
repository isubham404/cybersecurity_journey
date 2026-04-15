import hashlib 
text = input("Enter the text : ")
hash_object = hashlib.sha256(text.encode())
hash_value = hash_object.hexdigest()
print("The hashed text is -\n",hash_value)