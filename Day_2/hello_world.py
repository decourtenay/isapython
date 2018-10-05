# Do oznaczania stringów możemy używać
# dwóch rodzajów znaków ' i "
print("Hello \"world\"!")
print('Hello "world"!')

hello = "Hello"
world = "world"
ex = "!"

# Konkatenacja stringów
sign = hello + " " + world + ex
print(sign)

# Możemy stosować metodę (capitalize)
# na wyniku funkcji (input)
name = input("Jak masz na imię? ").capitalize()
greeting = hello.upper() + " " + name + ex.upper()
print(greeting)