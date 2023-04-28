'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''

def ceasar_cracker(text, key):
    """
    This function takes 2 parameters.
    :param text: text that needs to be deciphered.
    :param key: key to shifiting the alphabet

    returns the decyphered message.
    """
     # define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # shift the alphabet by the key to create the cipher
    cipher = alphabet[key:] + alphabet[:key]
    
    # initialize the result string
    result = ''

    for char in text:
        # if the character is a letter, encrypt or decrypt it
        if char.isalpha():
            index = alphabet.find(char.lower())
            # decrypt the coded caracter
            if char.isupper():
                result += alphabet[index - key].upper()
            else:
                result += alphabet[index - key]
        # if the character is not a letter, leave it as is
        else:
            result += char
            
    return result



text = input("Enter the message to crack: ")

for i in range(1, 26):
    print(ceasar_cracker(text, i))