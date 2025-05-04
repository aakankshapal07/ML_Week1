 # Task 3 :
student_dict = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}

def search_student(roll_number):
    return student_dict.get(roll_number, "Student not found")

print("Task 3: Student Search")
print(search_student(102))  
print()

# Task 4: 
football_players = {"Alice", "Bob", "David"}
cricket_players = {"Bob", "Charlie", "Eve"}

both = football_players & cricket_players
only_one = (football_players ^ cricket_players)
none = set(student_dict.values()) - (football_players | cricket_players)

print("Task 4: Sports Participation")
print(f"Play both: {both}")
print(f"Play only one: {only_one}")
print(f"Play none: {none}")
