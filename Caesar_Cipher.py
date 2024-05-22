from art import logo #impoting logo from the art.py
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1 #shift amount is negative
  for char in start_text: #loop through each letter in the start_text
    if char in alphabet: #if char is in the alphabets
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else: #if it is not in the alphabet
       end_text += char #just add it to the endtext with out encoding or decoding
  print(f"Here's the {cipher_direction}d result: {end_text}")

#if the user wants to encode or decode again
another_operation = True
while another_operation:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25: #if shift is greater than 25
        shift = shift %26 #getting the remainder 
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    operation = input('Will you like to encode or decode again?(yes/no): ')
    if operation == 'no':
        another_operation = False
        print('GoodBye.')
