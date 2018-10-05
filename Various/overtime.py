# Pobrać liczbę przepracowanych godzin w tygodniu
# Pobrać stawkę bazową za godzinę
# Standardowy czas pracy 35h w tygodniu
# Stawka za nadgodziny <= 10 sb * 1.5
# Stawka > 10 to sb * 2
# Obliczyć wypłatę za tydzień pracy

basic_rate = input("Podaj swoją stawkę bazową ")
basic_rate = int(basic_rate)

hours = input("Podaj liczbę przepracowanych godzin ")
hours = int(hours)

standard_time = 35
overtime_1_time = 10
overtime_1_factor = 1.5
overtime_2_factor = 2

if hours <= standard_time:
    standard_pay = basic_rate * hours
    overtime_pay_1 = 0
    overtime_pay_2 = 0
elif hours <= standard_time + overtime_1_time:
    standard_pay = basic_rate * \
                   standard_time
    overtime_pay_1 = basic_rate * \
                     overtime_1_factor * \
                     (hours - standard_time)
    overtime_pay_2 = 0
else:
    standard_pay = basic_rate * standard_time
    overtime_pay_1 = basic_rate * \
                     overtime_1_factor * \
                     overtime_1_time
    overtime_pay_2 = basic_rate * \
                     overtime_2_factor * \
                     (hours - standard_time - overtime_1_time)
pay = standard_pay + overtime_pay_1 + overtime_pay_2
print(pay)
print("Twoja wypłata to: {:.2f}".format(pay))

