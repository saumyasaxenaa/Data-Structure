def reverse(s):
    if len(s) < 2:
        return None
    backwards = []
    totalitems = len(s) - 1
    for i in range(totalitems, -1, -1):
        backwards.append(s[i])
    print(backwards)
    return ''.join(backwards)

x = reverse('My name is Saumya')
print(x)