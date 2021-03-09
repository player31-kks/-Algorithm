from collections import Counter
string = "hello my name is sparta".replace(" ","")
c = Counter(string)
print(c.most_common(1)[0])
