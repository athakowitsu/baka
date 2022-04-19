s = input()
s = s.lower()
for c in range(ord('a'),ord('z')+1):
    freq = s.count(chr(c))
    if freq > 0:
        print(chr(c),freq)