Task 1 
marks = [
    [85, 90, 78],   
    [76, 88, 95],   
    [92, 81, 85]    
]

print("Task 1: Total and Average Marks")
for i, student_marks in enumerate(marks, start=1):
    total = sum(student_marks)
    average = total / len(student_marks)
    print(f"Student {i} - Total: {total}, Average: {average:.2f}")
print()
