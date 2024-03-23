# Grade Calculator in Python
print("Enter Marks Obtained in 5 Subjects:")

# Hardcoded marks for demonstration
total1 = 44
total2 = 67
total3 = 76
total4 = 99
total5 = 58

# Calculate the total marks
total_marks = total1 + total2 + total3 + total4 + total5

# Calculate the average percentage
average_percentage = total_marks / 5

# Assign letter grades
if 91 <= average_percentage <= 100:
    print("Your Grade is A1")
elif 81 <= average_percentage < 91:
    print("Your Grade is A2")
elif 71 <= average_percentage < 81:
    print("Your Grade is B1")
elif 61 <= average_percentage < 71:
    print("Your Grade is B2")
elif 51 <= average_percentage < 61:
    print("Your Grade is C1")
elif 41 <= average_percentage < 51:
    print("Your Grade is C2")
elif 33 <= average_percentage < 41:
    print("Your Grade is D")
elif 21 <= average_percentage < 33:
    print("Your Grade is E1")
elif 0 <= average_percentage < 21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")