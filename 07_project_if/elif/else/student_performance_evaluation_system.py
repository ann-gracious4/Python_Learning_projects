#Program Title
print("===========================================")
print("STUDENT PERFORMANCE EVALUATION SYSTEM")
print("===========================================")

#Create a Dictionary 
student = {
    "name": "Ann Agipu Aaron",
    "course": "Python Programming", 
    "score": 78,
    "attendance": 85
}

#Display Student Information 
print("Student Name\t:", student["name"]) 
print("Student Course\t:", student["course"]) 
print("Student Score\t:", student["score"]) 
print("Student Attendance\t:", student["attendance"])

#Determine Pass or Fail 
if student["score"] >= 50: 
    print("PASS")
else: 
    print("FAIL")

#Assign Grade
if student["score"] >= 70: 
    print("Grade: A") 
elif student["score"] >= 60: 
    print("Grade: B")
elif student["score"] >= 50: 
    print("Grade: C") 
else:
    print("Grade: F")

#Attendance Check 
if student["attendance"] >= 75: 
    print("Attendance Status: Eligible for Exam")
else: 
    print("Attendance Status: Not Eligible for Exam")

#Scholarship Eligibility 
if student["score"] >= 80 and student["attendance"] >= 90: 
    print("Scholarship: Eligible") 
else: 
    print("Scholarship: Not Eligible")

#Best Performer 
scores = [78, 85, 92, 67, 88]
print("Highest Score:", max(scores))
print("Lowest Score:", min(scores)) 

#Summary
print("==========") 
print("SUMMARY") 
print("==========")

print("Student Evaluation Completed!") 
print("Decision Making Successful!") 
print("Ready for Next Topic!")

#Bonus Challenge
if student["score"] >= 90:
    print("Outstanding Performance!")
else: 
    print("Keep Improving!")