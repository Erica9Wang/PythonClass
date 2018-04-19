"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records." """

all_numbers = [];
for index in range(len(texts)):
    all_numbers.append(texts[index][0])
    all_numbers.append(texts[index][1])

for index in range(len(calls)):
    all_numbers.append(calls[index][0])
    all_numbers.append(calls[index][1])

print('here are {} different telephone numbers in the records.'.format(len(set(all_numbers))))
