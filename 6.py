print(list(range(16, 2, -3)))
names = ["chanan", "tom", "zack", "aharon"]

for i in range(7):
    print(names[i])

for i in range(7):
    names[i] = "dotan"

for name in names:
    if name == "zack":
        continue
        print(name)

for name in names:
    if name == "zack":
        break
    else:
        pass
        print(name)

for name in names:
    print(name)

a = 0
while a < 5:
    print(a)
    a = a + 1








