#fractionToBinary takes a base 10 decimal number that is less than one and created the base 2 binary representation

def fractionToBinary(number):
	if(number == 0):
		return ""
	if(int(number * 2) == 0):
		return "0" + fractionToBinary((number * 2)) 
	else:
		return "1" + fractionToBinary((number * 2) - 1)

#decimalToBinary takes a whole integer and converts it to base 2 binary

def decimalToBinary(number):
	if(number == 0):
		return "0"
	elif(number == 1):
		return "1"
	elif (number % 2 == 0):
		return decimalToBinary(number / 2) + "0"
	else:
		return decimalToBinary((number - 1) / 2) + "1"

#fullBinaryConversion calls both decimalToBinary and fractionToBinary and concatentates them to return a full
# conversion of a base 10 number that can be greater than zero and include decimal fraction values.

def fullBinaryConversion(number):
	return decimalToBinary(int(number)) + "." + fractionToBinary(number - int(number))



print(fullBinaryConversion(8.125))