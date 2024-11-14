#Caesar's Cypher
##Define the function
def caesar_cipher(text, shift):

  result = ""
  abc = "abcdefghijklmnopqrstuvwxyz"
  for char in text:
    if char in abc:
        index = abc.find(char)
        index = (index + shift) % 26
        char = abc[index]
        result += char
    else:
        result += char
  return result

#Ask user for input
text = input("Please enter a sentence: ")
text_lower = text.lower()
shift = int(input("Please enter the number of places to shift: "))
encrypted_text = caesar_cipher(text_lower, shift)

#Display the encrypted text
print("Encrypted text:", encrypted_text)