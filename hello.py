#coding=utf-8
import re
a = raw_input()
a = map(eval,re.findall('\d+',a))
N,M = a[0],a[1]
task =[]
for i in range(N):
    a = raw_input()
    a = map(eval,re.findall('\d+',a))
    task.append(a)
Ai = []
a = raw_input()
Ai= map(eval,re.findall('\d+',a))
print Ai
for p in Ai:
    lists = [ i for i in task if i[0]<=p]
    salary = [i[1] for i in lists]
    print max(salary)
