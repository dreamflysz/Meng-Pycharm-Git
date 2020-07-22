def next_number(s):
    res = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        res.append(str(count) + s[i])
        i += 1
    return ''.join(res)


s = "12312334356756865796780"
n = 4

for i in range(n):
    s = next_number(s)
    print(s)
