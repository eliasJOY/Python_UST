import datetime
class person:
    def __init__(self,*args):
        if len(args)>=3:
            self.name=args[0]
            self.age=args[1]
            self.email=args[2]
        else:
            raise ValueError("Pass required values")
    
    def display(self):
        print(f"Name:{self.name}, age:{self.age}, email:{self.email}")

obj= person("elias",22,"eiasjoy@gmail.com")
obj.display()

#inheritance

class vehicle():
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

class car(vehicle):
    def __init__(self,brand,model,price,speed,color):
        super().__init__(brand,model,price)
        self.speed=speed
        self.color=color

    def display(self):
        print(f"Brand:{self.brand}, Model:{self.model}, Price:{self.price}, Speed:{self.speed}, Color:{self.color}")
    
obj=car("BMW","i8","4cr","230kmph","Red")
obj.display()

# muti level inheritance

class org:
    def __init__(self,company_name):
        self.company_name=company_name

class emp(org):
    def __init__(self,company_name,emp_id):
        super().__init__(company_name)
        self.emp_id=emp_id

class manager(emp):
    def __init__(self,company_name,emp_id,dep):
        super().__init__(company_name,emp_id)
        self.dep=dep
    def display(self):
        print(f"Company:{self.company_name} EmpId:{self.emp_id} Department:{self.dep}")

obj = manager("ust",26474,"data engineering")
obj.display()


#hierarchial

class phone:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class android(phone):
    def __init__(self,brand,model,os):
        super().__init__(brand,model)
        self.os=os
    def andDisp(self):
        print(f"Brand:{self.brand} Model:{self.model} Android OS:{self.os}")

class ios(phone):
    def __init__(self,brand,model,iOS):
        super().__init__(brand,model)
        self.iOS=iOS

    def iosDisp(self):
        print(f"Brand:{self.brand} Model:{self.model}  IOS:{self.iOS}")

apple=ios("Apple","15Pro","iOS 18")
andr=android("Samsung","S23","OneUI")

#multiple inheritance

class vehicle:
    def __init__(self,brand,model,mileage):
        self.brand=brand
        self.model=model
        self.mileage=mileage
class electric_vehcle:
    def __init__(self,battery,range):
        self.battery=battery
        self.range=range
        
class hybrid_car(vehicle,electric_vehcle):
    def __init__(self,brand,model,mileage,battery,range,tot_mileage):
        vehicle.__init__(self,brand,model,mileage)
        electric_vehcle.__init__(self,battery,range)
        self.tot_mileage=tot_mileage
    
    def display(self):
        print(f"Brand:{self.brand} Model:{self.model} Mileage:{self.mileage} Battery:{self.battery} Range:{self.range} Total Mileage:{self.tot_mileage}")

obj=hybrid_car("BMW","i8",20,"Amron",45,65)
obj.display()

