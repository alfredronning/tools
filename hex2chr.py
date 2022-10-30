from sys import stdin, argv

def main():
    inp = stdin.read().strip()
    print("".join(chr(int(inp[i*2:i*2+2], 16)) for i in range(len(inp)//2)))

def print_help():
    print("hex to string")
    print("echo 616263 | hex2chr")

if __name__ == "__main__":
    if "-h" in argv[1:] or "--help" in argv[1:]:
        print_help()
    else:
        main()
