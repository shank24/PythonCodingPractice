class Course:

    def __init__(self,name,ratings):
        self.name=name
        self.rating=ratings

    def average(self):
        numberofratings = len(self.rating)
        average = sum(self.rating)/numberofratings
        print('Average ratings for ', self.name, 'Is ', average)



c1 = Course('Java Course',[1,2,3,4,5])
c1.average()

c2 = Course('Python Course',[5,5,5,5,5])
c2.average()

print(c1.name, c1.rating)
print(c2.name, c2.rating)
