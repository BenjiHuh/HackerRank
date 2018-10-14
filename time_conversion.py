def timeConversion(s):
    string = s.split(":")
    hours = int(string[0])
    minutes = int(string[1])
    seconds = int(string[2][:2])
    ampm = string[2][2:]
    # Handle special case
    if hours == 12 and ampm == "AM":
        hours = 0    
    elif hours == 12 and ampm == "PM":
        hours = 12
    elif ampm == "PM":
        hours += 12
    return "{:02}:{:02}:{:02}".format(hours,minutes,seconds)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()