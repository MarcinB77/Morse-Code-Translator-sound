import json
import time

from pygame import mixer
mixer.init()
sound = mixer.Sound("beep.wav")


class Converter:
    def __init__(self):
        with open("morse-code.json") as alphabet:
            self.morse_dict = json.load(alphabet)
            self.r_morse_dict = {value: key for (key, value) in self.morse_dict.items()}

    def convert_to_morse(self, list_of_chars):
        new_list = [self.morse_dict[char] + " " for char in list_of_chars if char in self.morse_dict]
        mess = ""
        mess = mess.join(new_list)
        print(f"Your message: {mess}")
        for char in mess:
            time.sleep(0.1)
            if char == ".":
                time.sleep(0.1)
                sound.play()
                time.sleep(0.05)
                sound.stop()
                time.sleep(0.3)
            elif char == "-":
                time.sleep(0.3)
                sound.play()
                time.sleep(0.4)
            else:
                time.sleep(0.8)

    def convert_to_string(self, list_of_str):
        new_list = [self.r_morse_dict[string] for string in list_of_str if string in self.r_morse_dict]
        mess = ""
        print(f"Your message: {mess.join(new_list)}")

    def encode(self, msg):
        list_of_chars = [char for char in msg]
        self.convert_to_morse(list_of_chars)

    def decode(self, msg):
        list_of_chars = msg.split(" ")
        self.convert_to_string(list_of_chars)

