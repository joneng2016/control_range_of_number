f = open("number_to_read")
contentStrings = f.read().split(',')

numbers = list()
numbersToCall = list()
stringToRegister=''

for element in contentStrings:
    numbers.append(int(element))

for number in range(0,100):
    numberFirst = numbers[0]
    numberToRegister = number + numberFirst      
    numbersToCall.append({"number":numberToRegister,"status":"not-call"})

for numberRegis in numbersToCall:
    stringToRegister = stringToRegister + "numero: " + str(numberRegis['number']) + " status:" + numberRegis['status'] + "\n"

print("Numeros Gerados em numbers_to_call")
f = open("numbers_to_call","w")
f.write(stringToRegister)
f.close()