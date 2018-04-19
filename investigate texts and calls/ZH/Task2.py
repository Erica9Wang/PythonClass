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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分
（计算主叫时间同时加上其他电话打进来的被叫时间）。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

telephone_time_dic = {}
#dictionary: key: telephone number / value: total time
for call in calls:
    if call[0] in telephone_time_dic:
        telephone_time_dic[call[0]] += int(call[3])
        if call[1] in telephone_time_dic:
            telephone_time_dic[call[1]] += int(call[3])
        else:
            telephone_time_dic[call[1]] = int(call[3])
    else:
        telephone_time_dic[call[0]] = int(call[3])
        if call[1] in telephone_time_dic:
            telephone_time_dic[call[1]] += int(call[3])
        else:
            telephone_time_dic[call[1]] = int(call[3])


telephone_time=[]
for telephone_number in telephone_time_dic:
    telephone_time.append(telephone_time_dic[telephone_number ])

longest_time = max(telephone_time)
longest_time_number = ''
for telephone_number in telephone_time_dic:
    if telephone_time_dic[telephone_number] == longest_time:
        longest_time_number = telephone_number

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_time_number, longest_time))
