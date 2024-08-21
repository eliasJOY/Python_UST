# Private and protected

class emp:
    _name1 = None

    def __init__(self,name):
        self._name=name
    
    def _disp(self):
        print("Employee name:",self._name)



    