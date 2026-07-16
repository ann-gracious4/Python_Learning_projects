#Title
print("================================")
print("STUDENT REGISTRATION SYSTEM")
print("================================")

#Create These Tuples
student = ("Ann Agipu Aaron", 25, "Female", "Nigeria")
course = ("Python", "Beginner", "Completed")
scores = (85, 90, 78, 95, 88)
skills = ("HTML", "CSS", "Python", "Problem Solving")

#Display Information
print("Student Name\t:", student[0])
print("Age\t:", student[1]) 
print("Gender\t:", student[2]) 
print("Country\t:", student[3]) 

#Course Information
print("Programming Language\t:", course[0]) 
print("Level\t:", course[1]) 
print("Status\t:", course[2])

#Tuple Unpacking
(name, age, gender, country) = student 

print("Welcome", name, "!")

#Membership Operator
print("'Python' in skills =", "Python" in skills)
print("'Java' in skills =", "Java" in skills)

#Length 
print("Number of Scores\t:", len(scores))
print("Number of Skills\t:", len(skills))

#Highest and Lowest Score (though i haven't gone through this topic yet)
print("Highest Score\t:", max(scores))
print("Lowest Score\t:", min(scores))

#Summary 
print("================")
print("SUMMARY") 
print("================")

print("Student Successfully Registered!")
print("Python Course Completed!")
print("Ready for Next Topic!")


#Bonus Challenge
colors = ("Red", "Green", "Blue", "Yellow", "Black") 
(first, *middle, last) = colors 

print("First Color\t:", first)
print("Middle Colors\t:", middle) 
print("Last Color\t:", last)