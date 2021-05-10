#Numerical to Roman Convertor
"""
It works using the algo which is taught to
a grade 5 student who learns about Roman 
number system in school, by reducing the 
bigger number into smaller and smaller
"""
def Check(n):
    if n < 4:
        Roman = ""
        for x in range(n):
            Roman += "I"
        return Roman
    if n == 4:
        return "IV"
    if n < 9:
        Roman = "V"
        Roman += Check(n % 5)
        return Roman
    if n == 9:
        return "IX"
    if n < 40:
        Roman = ""
        rang = int(n/10)
        for x in range(rang):
            Roman += "X"
        Roman += Check(n % 10)
        return Roman
    if n < 50:
        Roman = "XL"
        Roman += Check(n % 40)
        return Roman
    if n < 90:
        Roman = "L"
        Roman += Check(n % 50)
        return Roman
    if n < 100:
        Roman = "XC"
        Roman += Check(n % 90)
        return Roman
    if n < 400:
        Roman = ""
        rang = int(n/100)
        for x in range(rang):
            Roman += "C"
        Roman += Check(n % 100)
        return Roman
    if n < 500:
        Roman = "CD"
        Roman += Check(n % 400)
        return Roman
    if n < 900:
        Roman = ""
        rang = int(n/500)
        for x in range(rang):
            Roman += "D"
        Roman += Check(n % 500)
        return Roman
    if n < 1000:
        Roman = "CM"
        Roman += Check(n % 900)
        return Roman
    if n < 4000:
        Roman = ""
        rang = int(n/1000)
        for x in range(rang):
            Roman += "M"
        Roman += Check(n % 1000)
        return Roman


num = int(input("Enter a number : "))
if num < 1 or num > 3999:
    print("Roman doesn't exist")
else:
    print(Check(num))
