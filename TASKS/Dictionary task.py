# Write a program that: 
# Creates a dictionary where keys are subject names (e.g., Math, Science) and values are the marks (e.g., 90, 85). 
# Adds a new subject with its mark to the dictionary. 
# Updates the mark for one subject. 
# Prints the average marks.

subjects= {
    'English': 89,
    'Math': 91,
    'Physics': 86
}
print(f'Given subjects and marks: {subjects}')

new_sub=input('Enter new subject name: ')
new_mark=int(input('Enter its mark: '))

subjects.update({new_sub:new_mark})

print(f'Updated subjects: {subjects}')

avg= sum(subjects.values())/len(subjects)
print(f'Average marks: {avg}')

