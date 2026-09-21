def print_formatted(number):
    slen = len(bin(number)[2:])
    for i in range(1,number+1):
        binary = bin(i)[2:]
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        line = " ".join([str(i).rjust(slen, ' '), hexadecimal.rjust(slen, ' '), octal.rjust(slen, ' '), binary.rjust(slen, ' ')])
        print(line)


if __name__ == '__main__':
    print_formatted(17)