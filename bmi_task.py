#TASK2
#Ask the user to enter their weight in kg and their height in m
#Use the formula below to calculate the user's BMI:BMI = (weight in kg) / ((height in m)*(height in m))
#If the user’s BMI is 30 or greater the user is obese
#If the user’s BMI is 25 or greater the user is overweight
#If the user’s BMI is 18.5 or greater the user is normal
#If the user’s BMI is less than 18.5 the user is underweight
#Display the user’s BMI and whether they are obese, overweight, normal or underweight.

print("Welcome to the BMI Calculator!\n")
input("Press any key to continue...")

weight = float(input("please enter your weight in kg"))
height = float(input("please enter your height in m"))

BMI = (weight)/(height*height)
#just change the formula as mmy tutor correct me, the formula was wrong it make sense becaosue it told em i was obesse lol
print(BMI)

if BMI >= 30:
    print ("Your BMI is obese.")
    

elif BMI >25:
    print("Your BMI is overweight.")
    
    
    
elif BMI >= 18.5:
    print("Your BMI is normal.")
    
    
   
else:
    print("Your BMI is underweight.")

