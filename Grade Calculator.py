import math
print("This is a code script that computes your average grade and give you your honor ranking based on your semestral grade" )
CPAR = (input("CPAR "))
PE = (input("PE "))
English = (input("English "))
III = (input("III "))
Biology = (input("Biology "))
Chemistry = (input("Chemistry "))
Physics = (input("Physics "))
Capstone = (input("Capstone "))

TotGenAve = (int(CPAR)+int(PE)+int(English)+int(III)+int(Biology)+int(Physics)+int(Chemistry)+int(Capstone))
GenAve = (int(TotGenAve)/8)

if round(GenAve) in range(97, 101):
    print((GenAve) + " Your grade is", round(GenAve), "and you are with Highest Honor")
if round(GenAve) in range(94, 98):
    print("Your grade is", round(GenAve), "and you are with High Honor")
if round(GenAve) in range(89, 95):
    print("Your grade is", round(GenAve), "and you are with Honor")
if round(GenAve) in range(84, 90):
    print("You have passed the school year with a grade of", round(GenAve))
if round(GenAve) < 85:
    print("You have failed this school year")
if GenAve > 100:
    print("please check your input values again because the total grade is higher than 100")
    