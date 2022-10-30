from sys import stdin, argv

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encode(message):
    return(" ".join(MORSE_CODE_DICT[c] for c in message))

def decode(morse):
    return("".join(list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(m)] for m in morse.split()))

def main(d=False):
    inp = stdin.read().strip()
    if d:
        print(decode(inp))
    else:
        print(encode(inp.upper()))

def print_help():
    print("Decode or encode morse")
    print("No flag will encode")
    print("-d to decode")
    print("echo ABC | morse")
    print("echo .- -... -.- | morse -d")
    
if __name__ == "__main__":
    if "-h" in argv[1:] or "--help" in argv[1:]:
        print_help()
    else:
        main("-d" in argv[1:])

