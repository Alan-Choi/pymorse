import winsound
import time
import morse

def main():
    sample_string = 'Hello World'
    morse_code = string_to_morse(sample_string)
    print(f'"{sample_string}" in Morse Code is: {morse_code}')
    string = morse_to_string(morse_code)
    print(f'"{morse_code}" in English is: {string}')
    sounds = morse_sound(morse_code)
    print(f'"{morse_code}" sounds like: \n{sounds}')
        
def string_to_morse(string: str) -> str:
    '''
    Converts a string to morse code.
    string: The string to be converted.
    returns: 
    '''
    morse_code = ''
    for char in string:
        if char.isalpha():
            char = char.upper()
            
        if char in morse.CODES:
            morse_code += morse.CODES.get(char)
        else:
            print('Invalid character')
            return
        
        morse_code += ' '
        # beep(char)
    
    return morse_code
    
def morse_to_string(morse_code: str) -> str:
    letters = morse_code.split(' ')
    s = ''
    for l in letters:
        for k, v in morse.CODES.items():
            if v == l:
                s += k
                # beep(k)
                break
        s += ' '
    return s
        
def morse_sound(morse_code: str) -> str:
    s = morse_to_string(morse_code)
    
    letters = s.split(' ')
    sound = ''
    for l in letters:
        for k, v in morse.SOUNDS.items():
            if k == l:
                sound += v
                beep(l)
                break
        sound += ' '
    return sound  
            
def beep(char: str, single_unit_duration: int = 50) -> None:
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