'''def srt(string1, string2):
    if string1 == "":
        return 0
    if string1[0] == string2[0]:
        return 1 + srt(string1[1:], string2[0:])
    elif string1[0] == string2[1]:
        return 1 + srt(string1[1:], string2[1:])
    else:
        return srt(string1[0:], string2[1:])'''
def sub(string1, string2):
    if string1[0] == string2[0]:
        return 1 + sub(string1[0:], string2[1:])
    if string1[0] == string2[1]:
        return 1 + sub(string1[0:],string2[2:])
    else:
        return sub(string1[1:], string2[0:])
print(sub('aaa', 'bba'))

    
