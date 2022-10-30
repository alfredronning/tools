from sys import stdin, argv

A = ord("A")
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decode(inp, key):
    res = ""
    keyindex = 0
    for i in range(len(inp)):
        if not inp[i] in ALPHABET:
            res += inp[i]
        else:
            res += chr((ord(inp[i])-ord(key[keyindex%len(key)])+26)%26+A)
            keyindex += 1
    return res

def encode(inp, key):
    res = ""
    keyindex = 0
    for i in range(len(inp)):
        if not inp[i] in ALPHABET:
            res += inp[i]
        else:
            res += chr((ord(inp[i])+ord(key[keyindex%len(key)])-2*A)%26+A)
            keyindex += 1
    return res

def main(d=False):
    inp = stdin.read().strip().upper()
    key = argv[1].upper()
    if d:
        print(decode(inp, key))
    else:
        print(encode(inp, key))

def print_help():
    print("Decode or encode vingenere")
    print("No flag will encode")
    print("-d to decode")
    print("vingenere {key}")
    print("echo ABCDEFG | vingenere {key}")
    print("echo ABCDEFG | vingenere {key} -d")

if __name__ == "__main__":
    if "-h" in argv[1:] or "--help" in argv[1:]:
        print_help()
    else:
        main("-d" in argv[1:])
