import winsound
import time
import morse

def main():
    string_to_morse("Hello World")
    
def string_to_morse(string: str):
    '''
    Converts a string to morse code.
    string: The string to be converted.
    returns: None
    '''
    print(f'"{string}" in Morse Code is: ', end='')
    for char in string:
        if char.isalpha():
            char = char.upper()
            print(morse.CODES.get(char), end='')
        elif char.isdigit():
            print(morse.CODES.get(char), end='')
        elif char in morse.CODES:
            print(morse.CODES.get(char), end='')
        else:
            print('Invalid character')
        
        print(' ', end='')
        beep(char)
        
    print()
        
def beep(char: str, single_unit_duration: int = 50):
    '''
    Sounds the morse code for a single character.
    char: The character to be sounded.
    single_unit_duration: The duration of a single unit of the morse code.
    returns: None
    '''
    short_sound = single_unit_duration
    long_sound = single_unit_duration * 3
    element_space = single_unit_duration / 1000 # convert miliseconds to seconds
    letter_space = (single_unit_duration * 3) / 1000 # convert miliseconds to seconds
    word_space = (single_unit_duration * 7) / 1000 # convert miliseconds to seconds
    DEFAULT_FREQUENCY = 600 # Hz
    
    if char.isalpha():
        char = char.upper()
        
    for symbol in morse.CODES.get(char):
        if symbol == '.':
            winsound.Beep(DEFAULT_FREQUENCY, short_sound)
            time.sleep(element_space)
        elif symbol == '-':
            winsound.Beep(DEFAULT_FREQUENCY, long_sound)
            time.sleep(element_space)
        elif symbol == ' ':
            time.sleep(word_space)
            return
        else:
            print('Invalid character')
            time.sleep(letter_space)
            
    time.sleep(letter_space)
    
if __name__ == '__main__':
    main()