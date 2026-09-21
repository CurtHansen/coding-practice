# A function to count the number of consecutive characters in a string.


def count_consecutive_chars(string):

    n = len(string)
    idx = 0
    currchar = string[idx]
    charcount = 0
    characters = []
    counts = []
    while idx < n:
        if string[idx] == currchar:
            charcount += 1
        else:
            characters.append(currchar)
            counts.append(charcount)
            charcount = 1
            currchar = string[idx]
        idx += 1
    characters.append(currchar)
    counts.append(charcount)

    return characters, counts


if __name__ == '__main__':
    print(count_consecutive_chars('aaabbcdddde'))









if __name__ == '__main__':
    count_consecutive_chars('ssammmple')