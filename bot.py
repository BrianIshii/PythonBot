#import aiml
#import os
import time, sys
#import pyttsx
#import warnings
import speech as s

def main():
    listening()


# ->
# listens for prompt
def listening():
    while True:
        inp = s.listen(prompt=True)
        if inp == "hey Siri":
            print("Hey Siri")
            return
    
if __name__ == '__main__':
    main()

