if __name__ == '__main__':
    s = input()
    line1 = False
    line2 = False
    line3 = False
    line4 = False
    line5 = False
    for i in range(len(s)):
        if s[i].isalnum() == True:
            line1 = True
        if s[i].islower() == True:
            line2 = True
            line4 = True
        if s[i].isupper() == True:
            line2 = True
            line5 = True
        if s[i].isdigit() == True:
            line3 = True
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
            