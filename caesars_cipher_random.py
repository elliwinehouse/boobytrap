s = input('введи зашифрованную строку: ')
d = 'abcdefghijklmnopqrstuvwxyz'

for k in range(25):
    b = ''
    for i in range(len(s)):
        if not s[i].isalpha():
            b += s[i]
        else:
            if s[i].isupper():
                b += (d[d.find(s[i].lower())-k]).upper()
            else:
                b += d[d.find(s[i].lower())-k]
    print(b)
