#Program Title
print("=========================")
print("STUDENT CLASS MANAGER")
print("=========================")

#Create lists
students = ["Ann", "Grace", "John", "David", "Mary"] 
courses = ["Python", "Java", "HTML", "CSS", "JavaScript"] 
scores = [85, 92, 78, 88, 95] 
passed = [True, True, False, True, True] 

#Display the lists 
print("Students\t:", students) 
print("Courses\t:", courses)
print("Scores\t:", scores)
print("Passed\t:", passed) 

#Access List Items
print("First Student\t:", students[0]) 
print("Last Student\t:", students[-1])
print("Third Course\t:", courses[2])
print("Second Score\t:", scores[1]) 

#Change List Items
students[2] = "James"
scores[2] = 80 

print(students) 
print(scores)

#Add New Items 
students.append("Sarah")
scores.append(90)

print(students) 
print(scores) 

#Remove Items 
students.remove("Grace") 
passed.remove(False)

print(students) 
print(passed) 

#List Information 
print("Number of students\t:", len(students))
print("Number of courses\t:", len(courses)) 
print("Number of scores\t:", len(scores)) 

#Membership Operator 
print("'Ann' in students =", "Ann" in students) 
print("'Peter' in students =", "Peter" in students) 
print("'Python' in courses =", "Python" in courses) 
print("'C++' in courses=", "C++" in courses) 

#Final Summary 
print("==================") 
print("SUMMARY") 
print("==================")

print("Total Students\t:", len(students)) 
print("Total Courses\t:", len(courses)) 

print("Class Successfully Updated!")

