#In order to use time.sleep() to wait
import time
#Change 'x' value in order to get a different end number
#'x' value must be even!
x = int(2)
print("Think of a number between one and ten.")
print("Once you have your number, type it and press enter.")
A = int(input())
print("Now, multiply your number by two.")
int(input())
print ("Add", x, "to your product.")
int(input())
print ("Divide the new number by two.")
D = int(input())
print ("Now, subtract your original number from the result in your head.")
input("Press enter when ready.")
y = D - A
print ("And your number is...")
time.sleep(2.5)
print (y)

#Method source: http://www.wikihow.com/Read-Someone%27s-Mind-With-Math-(Math-Trick)
#"Divide by half" trick
