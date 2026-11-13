# Conditional statements in Python -> if and else
# used to check the given condition is satisfied or not with variables

# using if condition, check whether the number is positive or not
x = int(input("Enter a number : "))
if x>0:
    print(x, "is positive")

print("=================================================================")

# using if and else check whether a candidate is eligible for vote or not
y = int(input("Enter a number : "))
if y>18:
    print("Eligible for Vote")
else:
    print("Not Eligible for Vote")
    
print("================================================================")

# using if elif and else, check the grade of student according to his percentage
z = float(input("Enter Student Percentage : "))
if z >= 85.0 and z <= 100.0:
    print("A Grade")
elif z >= 70.0 and z < 85.0:
    print("B Grade")
elif z >= 60.0 and z < 70:
    print("C Grade")
else:
    print("Fail")