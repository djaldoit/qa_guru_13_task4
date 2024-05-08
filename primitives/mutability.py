# Списки, словари и множества - изменяемые!

from copy import deepcopy

l1 = [1, 2, 3, [5, 6, 7]]
# l2 = l1.copy()
l2 = deepcopy(l1)
l2[-1].append(8)
l2.append(4)

print(l1)
print(l2)

# Кортежи, frozenset - нет


t1 = (1, 2, 3, 4, 5)
t2 = t1

frozenset({1, 2, 3, 4, 5, 5, 5})
