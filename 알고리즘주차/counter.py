from collections import Counter

a = input()
b=Counter(a)
print(b)
print(b['s'])
print(b.most_common(1))