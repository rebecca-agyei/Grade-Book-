last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# Create Some Lists:
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# print(gradebook)

# Add More Subjects:
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modify The Gradebook:
gradebook[-1][1] = 98
gradebook[2].remove(85)
gradebook[2].append("Pass")

print("GRADEBOOK:")
print(gradebook)

# One Big Gradebook!
full_gradebook = last_semester_gradebook + gradebook 
print("FULL GRADEBOOK:")
print(full_gradebook)

