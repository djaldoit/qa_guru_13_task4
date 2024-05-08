# Делаем списки!

l = [1, 2, 3, "a", "b", "c", [4, 5, 6]]

print(l[0])
print(l[-1])

print(l[-1][0])

print(l[::-1])

# Функции списков

l.append("new element")
l.extend(["elem", "another elem"])
len(l)
l.reverse()

l[0] = 200

print(l)


# Множества

s1 = {1, 2, 3, 4, 5, 5, 5, 5, 5}
s2 = {1, 2, 5, 5}

print(s1)
print(s2)

s1.intersection(s2)

print(list(set([1, 2, 3, 4, 5, 5, 5])))
