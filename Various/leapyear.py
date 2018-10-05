# podzielny przez 400
# jednocześnie podzielny przez 4 i niepodzielny przez 100

year = input("Podaj rok: ")
year = int(year)

message_true = "Rok jest przestępny"
message_false = "Rok nie jest przestępny"

if year % 400 == 0:
    print(message_true)
elif year % 4 == 0 and year % 100 != 0:
    print(message_true)
else:
    print(message_false)
