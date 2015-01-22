from Registration import *


purdue = School('Purdue University')
purdue.loadData('students.txt')

print('About the Current School')
print('-----------------------')
print('-----------------------')
print(purdue)
print()
print('Students in the School:')
print('-----------------------')
print('-----------------------')

for name, student in purdue.students.items():
    print(student)
    print('---------------------------------')

print()
print('Transcripts of All Students in the School:')
print('-----------------------')
print('-----------------------')
print(purdue.generateAllTranscripts())
