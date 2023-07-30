alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(input_text, shift_amount, direction):
    
    output_text = ""
    shift = shift_amount
    if direction == "decode":
        shift *= -1
    for letter in input_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            if new_position >= len(alphabet):
                new_position -= len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += letter
    print(f"The {direction}d text is {output_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(input_text=text, shift_amount=shift, direction=direction)