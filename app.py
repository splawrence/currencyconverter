infile = open("Static/Exchrate.txt", 'r')
O = [line.rstrip().split(',') for line in infile]
infile.close()

print("")
print("5.8 (a)")
country = str(input("Enter the name of a country: "))

for i in O:
    if i[0] == country:
        print("Currency: ", i[1])
        print("Exchange rate: ", i[2])

print("")
print("5.8 (b)")

def takeSecond(elem):
    return elem[2]

sorted_list = []
with open('Static/Exchrate.txt', 'r') as f:
    for item in O:
        sorted_list.append(item)
        sorted_list.sort(key=takeSecond, )#reverse=True)
        #print(sorted_list[O.index(item)][0])
    #for item in sorted_list:
    #    f.write("%s\n" %",".join(item))

for j in sorted_list:
    print(sorted_list[sorted_list.index(j)][0])
    if sorted_list.index(j) > 1:
        break

print("")
print("5.8 (c)")
val1 = 0
val2 = 0

first_country = str(input("Enter the name of first country: "))
second_country = str(input("Enter the name of second country: "))
convert_amount = int(input("Amount of money to convert: "))
resulting_amount = 0
#first_country = first_country * 100
#resulting_amount = second_country * first_country

def get_exchange(country):
    for i in O:
        if i[0] == country:
            return(i[2])

def get_currency(country):
    for i in O:
        if i[0] == country:
            return(i[1])

val1 = float(get_exchange(first_country))
val2 = float(get_exchange(second_country))

if val1 < val2:
    val1 = val1*convert_amount
    resulting_amount = float(val1) * float(val2)
else:
    resulting_amount = (float(val2)/float(val1)) * convert_amount

print('%s %s(s) from %s equals %s %s(s) from %s' % (convert_amount, get_currency(first_country), first_country, round(resulting_amount,2), get_currency(second_country), second_country))


