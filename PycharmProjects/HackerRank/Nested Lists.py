#Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
list_all_student = []
list_std_name = []
list_std_grade = []
list_output_student = []

#this is for loop to creat the list of all student grade
for loop in range(N):
    student_name = str(raw_input())
    student_grade = float(raw_input())
    list_all_student.append([student_name, student_grade])
    list_std_name.append(student_name)
    list_std_grade.append(student_grade)

#delete the minimum grade from list
minimum_grade = min(list_std_grade)
while minimum_grade in list_std_grade:
    list_std_name.remove(list_std_name[list_std_grade.index(min(list_std_grade))])
    list_std_grade.remove(min(list_std_grade))


#check the lowest student grade and append tham to the list
for loop in range(len(list_std_grade)):
    if list_std_grade[loop] == min(list_std_grade):
        list_output_student.append(list_std_name[loop])


#print the student name with the lowest grade:
list_output_student.sort()
for name in range(len(list_output_student)):
    print list_output_student[name]