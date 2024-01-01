# Lab3_Question No: 1
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
print("Addition is Commutative", A+B==B+A)

# Lab3_Question No: 2
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
C = int(input("Enter a number:"))
print("Addition is Associative", A+(B+C)==(A+B)+C)

# Lab3_Question No: 3
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
print("A>B is", A>B)
print("A<B is",A<B)
print("A>=B is",A>=B)
print("A<=B is",A<=B)
print("A!=B is",A!=B)
print("A==B is",A==B)

# Lab3_Question No: 4
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
# Both Numbers are Psitive
print("Both Numbers are Psitive:",A>0 and B>0)
# Atleast one of them is positive
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
print("Atleast one of them is positive:",A>0 or B<0)
# Both Numbers are Nagetive
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
print("both numbers are nagetive:",A<0 and B<0 )
# Atleast one of them is Nagetive
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
print("Atleast one of them is nagetive:",A>0 or B<0)
# Both Numbers are Even
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
print("Both numbers are even:", A%2==0 and B%2==0)
# Atleast one of them is Even
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
print("Atleast one of them is Even:", A%2==0 or B%2==1)
# Both Numbers are odd
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
print("Both numbers are odd:", A%2==1 and B%2==1)
# Atleast one of them is odd
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
print("Atleast one of them is odd:", A%2==1 or B%2==0)
# Multiple of 3
A = int(input("Enter a number:"))
print("Multiple of 3:", A%3==0)
# Atleast one of them is multiple of 3
A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
print("Atleast one of them is multiple of 3:", A%3==0 or B%3==1)

# Lab4_Question No: 1
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("Even")
elif num % 2 ==1:
    print("odd")
else:
    print(0)

# Lab4_Question No:2
character = input("Enter a character:")
vowel = "a","e","i","o"
if character in vowel:
    print(character, "is a vowel")
else:
    print("Constant")

# Lab4_Question No:3
age = int(input("enter your age:"))
if age < 25:
    print("You are not allowed to take insurance")
elif age > 40:
    print("Your monthly payment: 1500PKR/month")
else:        ### age is 25-40
    e_status = input("enter your employment status as e or u")
    m_status = input("enter your martial status as m or u")
    if e_status == "u" and m_status == "u":
        print("Your monthly payment: 1400PKR/month")
    elif e_status == "e" and m_status == "u":
        print("Your monthly payment: 800PKR/month") 
    elif e_status == "u" and m_status == "m":
        print("Your monthly payment: 1200PKR/month") 
    elif e_status == "e" and m_status == "m":
        print("Your monthly payment: 1000PKR/month") 
    else:
        print("invalid input")

# Lab4_Question No: 4
marks = int(input("Enter your marks"))
if marks < 40:
    print("fail")
elif 41 < marks < 50:
    print("D grade")
elif 51 < marks < 60:
    print("C grade")
elif 61 < marks < 70:
    print("B grade")
elif 71 < marks < 80:
    print("A grade")
elif marks > 80:
    print("A-1 grade")
else:
    print("invalid input")
                            







        
