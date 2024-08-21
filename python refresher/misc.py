import datetime

print("Today's date:",datetime.date.today())
# print(datetime.datetime.now())

class person:
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob
    def age(self):
        today=datetime.date.today()
        age = today.year- self.dob.year
        if today<datetime.date(today.year,self.dob.month,self.dob.day):
            age-=1
        return age
    
man = person("elias",datetime.date(2002,5,8))
print("Age:",man.age())
