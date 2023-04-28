'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''


def caesar_cipher(text, key, mode):
    """

    Function that takes 3 arguments.
    :param text: string that ahs to be coded or decoded
    :param key: number that shifts the alphabet
    :mode: decryption or encryption

    """

    # define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # shift the alphabet by the key to create the cipher
    cipher = alphabet[key:] + alphabet[:key]
    
    # initialize the result string
    result = ''
    
    # loop through each character in the text
    for char in text:
        # if the character is a letter, encrypt or decrypt it
        if char.isalpha():
            index = alphabet.find(char.lower())
            if mode == 'e':
                # add coded character
                if char.isupper():
                    result += cipher[index].upper()
                else:
                    result += cipher[index]
            else:
                # decrypt the coded caracter
                if char.isupper():
                    result += alphabet[index - key].upper()
                else:
                    result += alphabet[index - key]
        # if the character is not a letter, leave it as is
        else:
            result += char
            
    return result


# get user input
mode = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ")
key = int(input("Please enter the key (0 to 25) to use.\n> "))
text = input("Enter the message to {}\n> ".format("encrypt" if mode == 'e' else "decrypt"))

# encrypt or decrypt the text using the Caesar cipher
result = caesar_cipher(text, key, mode)

# print the result
print(result)
