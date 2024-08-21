#abstraction

from abc import ABC, abstractmethod

class Bill(ABC):
    def printSlip(self,amt):
        print("Price:",amt)

    @abstractmethod
    def bill(self,amt):
        pass
class Debit(Bill):
    def bill(slef,amt):
        print("debit of:",amt)

absObj = Debit()
absObj.printSlip(1000)
absObj.bill(1000)
