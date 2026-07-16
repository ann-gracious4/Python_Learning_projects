#Title
print("===================================")
print("STUDENT CLUB MANAGEMENT SYSTEM")
print("===================================")

#Create Sets
science_club = {"Ann", "Grace", "John", "David"}
tech_club = {"Ann", "James", "Mary"} 
sports_club = {"John", "Grace", "Peter"} 
skills = {"Python", "HTML", "CSS"} 

#Display the Sets
print("Science Club\t:", science_club)
print("Tech Club\t:", tech_club)
print("Sports Club\t:", sports_club) 
print("Skills\t:", skills) 

#Add One New Student
science_club.add("Sarah") 

#Add Multiple Skills 
new_skills = ["JavaScript", "Git", "Problem Solving"]
skills.update(new_skills)

#Remove One Student
science_club.discard("David") 

#Membership Check 
print("'Ann' in science_club =", "Ann" in science_club) 
print("'Peter' in science_club =", "Peter" in science_club) 
print("'Python' in skills =", "Python" in skills) 
print("'Java' in skills =", "Java" in skills) 

#Number of Items
print("Number of Science Club Members\t:", len(science_club)) 
print("Number of Tech Club Members\t:", len(tech_club)) 
print("Number of Skills\t:", len(skills)) 

#Duplicate Demonstration 
students = {"Ann", "Grace", "Ann", "John", "Grace"}
print(students)
print(len(students))  

#Summary
print("=====================") 
print("SUMMARY")
print("=====================")

print("Science Club Updated!") 
print("Skills Updated!") 
print("Project Completed Successfully!")


#Bonus Challenge
#Because Set does not allow duplicate items.