class Person:

    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge

        self.age = initialAge
        if self.age < 0:
            self.age = 0
            print(f'Age is not valid, setting age to {self.age}.')

    def amIOld(self):

        if self.age<13:
            print("You are young")
        elif self.age>= 13 and self.age<18:
            
            print("You are a teenager")
        
        elif self.age>=18:
            print("You are old")
    
    def yearPasses(self):
        # Increment the age of the person in here
        self.age = self.age + j

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
