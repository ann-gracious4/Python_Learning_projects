#Program Title
print("==============================")
print("SMART STUDENT CALCULATOR")
print("==============================")

#Student Information
student_name = "Ann Agipu Aaron"
print("Student Name\t:", student_name) 

course = "Python Programming"
print("Course\t:", course)

#Calculator Section
num1 = 25
num2 = 8 

print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)
print(num1, "//", num2, "=", num1 // num2)
print(num1, "%", num2, "=", num1 % num2)
print(num1, "**", num2, "=", num1 ** num2)

#Assignment Operators
score = 50 

print("Initial:", score)

score += 20
print(score)

score -= 10
print(score)

score *= 2
print(score) 

score /= 4
print(score) 

score //= 2
print(score) 

score %= 3 
print(score)

#Comparison Operators
print(num1, ">", num2, "=", num1 > num2)
print(num1, "<", num2, "=", num1 < num2)
print(num1, ">=", num2, "=", num1 >= num2)
print(num1, "<=", num2, "=", num1 <= num2)
print(num1, "==", num2, "=", num1 == num2) 
print(num1, "!=", num2, "=", num1 != num2) 

#Logical Operator
passed_math = True 
passed_python = False 

print(passed_math and passed_python)
print(passed_math or passed_python)
print(not passed_python)

#Identity Operators
x = 100 
y = 100 
z = 200 

print(x is y)
print (x is not z)

#Membership Operators 
course = "Python Programming"

print("Python" in course)
print("Java" in course)
print("Programming" in course)
print("HTML" not in course)

#Summary 
print("=========================") 
print("OPERATOR SUMMARY") 
print("=========================")

print("Arithmetic\t:", '+')
print("Assignment\t:", '+=')
print("Comparison\t:", '>')
print("Logical\t:", 'and')
print("Identity\t:", 'is')
print("Membership\t:", 'in')