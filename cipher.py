#Python program to generate Cipher Text(Encrypted text).

print("Welcome to our program in which we generate cipher text.")
print()
def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters acc. to ASCII character value.
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters acc. to ASCII character value.
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
 
    return result
 
#check the above function
text = input("Enter which you want to write:\n")
#s=no. of shift.
s = 5
print ("Text  : " + text)
print ("Shift : " + str(s))        
print ("Cipher: " + encrypt(text,s))
