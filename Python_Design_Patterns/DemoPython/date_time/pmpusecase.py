from datetime import *

class Project:

    def __init__(self,name,stDate,enDate):
        self.name=name
        self.stDate=stDate
        self.enDate=enDate
        self.tasks=[]


    def addTask(self,task):
        self.tasks.append(task)

class Task:

    def __init__(self,name,duration):
        self.name=name
        self.duration=duration
        self.resources=[]

    def addResource(self,resource):
        self.resources.append(resource)


class Resource:

    def __init__(self,name,skill):
        self.name=name
        self.skill=skill


p=Project('AI',date(2021,1,1),date(2022,1,1))
t=Task('Creating a Bot',90)
r=Resource('John','Python')

t.addResource(r)
p.addTask(t)

for eachTask in p.tasks:
    print(eachTask.name)
    for eachRes in eachTask.resources:
        print(eachRes.name)
        print(eachRes.skill)
