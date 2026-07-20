#Program Title 
print("=========================================")
print("STUDENT INFORMATION MANAGEMENT SYSTEM")
print("=========================================")

#Create a Dictionary
student = {
    "name": "Ann Agipu Aaron",
    "age": 25,
    "gender": "Female", 
    "country": "Nigeria", 
    "course": "Python",
    "level": "Beginner"
}

#Display Student Information
print("Name\t:", student["name"]) 
print("age\t:", student["age"]) 
print("Gender\t:", student["gender"])
print("Country\t:", student["country"]) 
print("Course\t:", student["course"]) 
print("Level\t:", student["level"]) 

#Update Information 
student.update({"level" : "Intermediate"})
print("Updated Level:", student["level"])

#Add New Information
student.update({"university" : "University of Port Harcourt"}) 
student.update({"state" : "Benue"}) 
student.update({"learning_python" : True})

print("University\t:", student["university"])
print("State\t:", student["state"]) 
print("Learning_Python\t:", student["learning_python"]) 

#Remove One Item 
student.pop("gender") 
print(student)

#Dictionary Methods
print(student.keys()) 
print(student.values()) 
print(student.items()) 

#Membership Checks 
print("'name' in student =", "name" in student) 
print("'phone' in student =", "phone" in student) 
print("'course' in student =", "course" in student) 

#Number of Items
print("Total Information Stored\t:", len(student)) 

#Summary
print("============") 
print("SUMMARY") 
print("============")

print("Student Record Updated!") 
print("Dictionary Operations Completed!") 
print("Ready for Next Topic!") 

#Bonus Challenge
course = {
    "title": "Python Programming",
    "duration": "3 Months", 
    "completed": True
} 

print("Title\t:", course["title"]) 
print("Duration\t:", course["duration"]) 
print("Completed\t:", course["completed"])

#Dictionaries store information as key-value pairs.