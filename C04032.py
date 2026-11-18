import sys

def check(s):
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            return False
    return True

a = [x for line in sys.stdin for x in line.split()]
freq = {}
for x in a:
    if check(x):
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1


sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
for val, count in sorted_items:
    print(val, count)