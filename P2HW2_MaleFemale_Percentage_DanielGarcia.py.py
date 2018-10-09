
# Write that uses user input to calculate the percentage
# of female and male students
# 10/8/2018
# CTI-110 P2HW2_MaleFemale_Percentage
# Daniel Garcia

males=int(input('Enter the number of Males registered in the class: '))
females=int(input('Enter the number of Females registered in the class: '))
class_size= males + females

M=males / class_size
F=females / class_size

print ('the percentage of males is', M, 'and the percentage of females is', F)
