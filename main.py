from morse_converter import Converter

conv = Converter()

print("Welcome to Morse Code Translator \n")
dec = ""
while dec != 'xxx':
    dec = input("Encode - type '1', Decode - type '2', To stop type 'xxx'\n")
    if dec == '1':
        message = input("\nPlease type your message to encode: ")
        conv.encode(message.lower())
    elif dec == '2':
        coded_message = input("\nPlease type your message to decode: ")
        conv.decode(coded_message)


