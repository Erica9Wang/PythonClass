# how_many_snakes = 1
# snake_string = """
# Welcome to Python3!
#
#              ____
#             / . .\\
#             \  ---<
#              \  /
#    __________/ /
# -=:___________/
#
# <3, Juno
# """
#
#
# print(snake_string * how_many_snakes)

names = input('Enter names separated by commas:')
assignments = input('Enter assignments separated by commas:')
grades = input('Enter grades separated by commas:')

names = names.split(',')
assignments = assignments.split(',')
grades = grades.split(',')

for index in range(len(names)):
    print('Hi {},\nThis is a reminder that you have [insert number of missing assignments] '+
    'assignments left to submit before you can graduate. Your current grade is {} and can increase to {} '+
    'if you submit all assignments before the due date.'.format(names[index], assignments[index], int(grades[index])+ int(assignments[index]*2)))
