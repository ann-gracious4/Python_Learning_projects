#Program Title
print("=================================") 
print("PYTHON STUDY PROGRESS TRACKER") 
print("=================================") 

#Create a Starting Number 
completed_topics = 1 
while completed_topics <= 10: 
    print("Completed Topics:", completed_topics) 
    completed_topics += 1

print("You have completed 10 Python topics!") 
print("Keep learning and growing!")

#Use a List
topics = ["Syntax", "Variables", "List", "Set", "Tuple"] 
print(topics) 

#Create Another while Loop 
index = 0
while index < 5:
    print("Topic:", index+1, topics[index])
    index += 1

#Bonus Challenge
password = "" 
while password != "python123": 
    password = input("Enter password: ")

print("Access Granted!") 
print("Welcome to your Python learning journey!")