#Sufiyah Sajan
#September 22 2022
#input, processing, output homework

#part A
print("Hello. This program will project how much you can earn by investing money in a high-yield savings account over a 3-month period.")

print()

initial_deposit = input("To begin, enter how much money you would like to initially invest: ")
interest_rate = input("Next, enter your projected annual interest rate as a decimal: ")

print()

print("Calculating...")

print()

a = format("Month", '<20s')
b = format("Statring Balance", '<20s')
c = format("Interest", '<20s')
d = format("Ending Balance", '<20s')
print(a, b, c, d,end = '\n')

print()

mon1 = format("1", '<20s')
mon1sb = format(initial_deposit, '<20s')
e = float(interest_rate) / 12
e2 = (float(initial_deposit) * e)
f = format(e2, '.2f')
mon1i = format(str(f), '<20s')
g = e2 + float(initial_deposit)
g2 = format(g, '.2f')
mon1eb = format(str(g2), '<20s')
print(mon1, mon1sb, mon1i, mon1eb, end = '\n')

print()

mon2 = format("2", '<20s')
mon2sb = format(mon1eb, '<20s')
h = (float(mon1eb) * e)
i = format(h, '.2f')
mon2i = format(str(i), '<20s')
j = h + float(mon1eb)
j2 = format(j, '.2f')
mon2eb = format(str(j2), '<20s')
print(mon2, mon2sb, mon2i, mon2eb, end = '\n')

print()

mon3 = format("3", '<20s')
mon3sb = format(mon2eb, '<20s')
k = (float(mon2eb) * e)
l = format(k, '.2f')
mon3i = format(str(l), '<20s')
m = k + float(mon2eb)
m2 = format(m, '.2f')
mon3eb = format(str(m2), '<20s')
print(mon3, mon3sb, mon3i, mon3eb, end = '\n')

