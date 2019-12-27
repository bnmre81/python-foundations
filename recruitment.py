skills = ['python', 'Django', 'C#', 'unity']

cv = {}

name = input("What is you name: ")
cv['name'] = name
age = input("How old are you: ")
cv['age'] = age
experience = input("How many years of experience do you have: ")
cv['experience'] = experience
cv['skills'] = []

print('''
	1.{}
	2.{}
	3.{}
	4.{}'''.format(skills[0], skills[1], skills[2], skills[3]))

skill_1 = input("Choose a skill from above by entering its number: ")

if skill_1 == '1':
	cv['skills'].append(skills[0])
elif skill_1 == '2':
	cv['skills'].append(skills[1])
elif skill_1 == '3':
	cv['skills'].append(skills[2])
elif skill_1 == '4':
	cv['skills'].append(skills[3])

skill_2 = input("Choose another skill from above by entering its number: ")

if skill_2 == '1':
	cv['skills'].append(skills[0])
elif skill_2 == '2':
	cv['skills'].append(skills[1])
elif skill_2 == '3':
	cv['skills'].append(skills[2])
elif skill_2 == '4':
	cv['skills'].append(skills[3])

print(cv)
if int(cv['age']) > 24 and int(cv['experience']) > 4 and 'python' in cv['skills'] and 'Django' in cv['skills']:
	print("You have been accepted " + name)
else:
	print("Sorry, you do not meet the reuirments for acceptance!")


