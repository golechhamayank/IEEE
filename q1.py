s1 = 'technology'
s2 = 'science'

for i in s1:
    if i not in s2:
        print('Strings are not balanced')
        break
    else:
        print('Strings are balanced')
