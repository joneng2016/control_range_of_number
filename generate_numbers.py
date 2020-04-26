numbers = list()
numbersToCall = list()
stringToRegister=''
stringMsgToSend=''

f = open("msng_to_send_by_user")
stringMsgToSend = f.read()

f = open("number_to_read")
contentStrings = f.read().split(',')

for element in contentStrings:
    numbers.append(int(element))

for number in range(0,100):
    numberFirst = numbers[0]
    numberToRegister = number + numberFirst      
    numbersToCall.append({"number":numberToRegister,"status":"not-call","msgToSend":stringMsgToSend})

for numberRegis in numbersToCall:
    stringToRegister = stringToRegister + str(numberRegis['number']) + "#" + numberRegis['status'] + "#" + numberRegis['msgToSend'] + "\n" 


print("Numeros Gerados em numbers_to_call")

f = open("numbers_to_call.csv","w")
f.write(stringToRegister)
f.close()
