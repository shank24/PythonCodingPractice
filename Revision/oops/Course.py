class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings

    def average(self):
        numberOfRatings=len(self.ratings)
        avg = sum(self.ratings)/numberOfRatings
        return avg


c1=Course("Python",[1,2,3,4,5])

print(c1.name,c1.ratings)

print('Avg Ratings for ' , c1.name, c1.average())
