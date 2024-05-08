"""
Это примеры работы со строками
"""
# Учимся писать строки!

s = "Hell'o, 'wo'rl'd!"

s = 'He"llo, wo"rld!'

s = 'Hello, \' "world!'

s = "Hello,\" world!"

s = """Hello,"''""'' world!"""

s = '''He
llo, 
world
!'''

print(s)

s = "Hello, \nworld!"
print(s)

s = """Hello, 
world!"""
print(s)

s = "Hello, " \
    "world!"

s = ("Hello, "
     "world")

print("-----")
print(s)

# Сырые строки

s = "Hello, \\nworld!"
print(s)

s = r"Hello, \nworld!"
print(s)

# Индексы и слайсы

email = "user@domain.com"

print(email[1])

print(email[-2])

print(email[0:5])
print(email[:5])

print(email[0:10:2])
print(email[0:10:1])

print(email[::-1])

print(email[0:51])

# Оперируем


assert email.endswith("@domain.com")


# Форматируем

a = "Hello"
b = "World"

print(a + ", " + b + "!")

print("{a}, {b}!".format(a=a, b=b))

print(f"{a}, {b}!")

print(f"{a}, {b.upper()}!")

print(f"{a=}, {b=}!")

print("%s, %s!" % (a, b))


url_template = "https://yourservice.com/v1/api/{}"

users_url = url_template.format("users")
groups_url = url_template.format("groups")

# Строку в число, и наоборот

s = "1234"
n = 1234

assert s.isdigit()

# assert s == n
assert s == str(n)
assert int(s) == n
