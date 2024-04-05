name1 = input("please enter your name: ")
name2 = input("please enter her name: ")

name = (name1 + name2).lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

true = t + r + u + e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = l + o + v + e

true_love = int(str(true) + str(love))

print(f"True love percent is {true_love}")
