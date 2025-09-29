# Python program to overload equality
# and less than operators

class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a < other.a):
            return "obj1 is less than obj2"
        else:
            return "obj2 is less than obj1"
    def __eq__(self, other):
        if(self.a == other.a):
            return"Obj1 is equal to Obj2"
        else:
            return"Obj1 is not equal to Obj2"
        
obj1 = A(2)
obj2 = A(3)
print(f"Passed out values: {obj1.a} and {obj2.a}")
print(obj1 < obj2)

obj3 = A(4)
obj4 = A(4)
print(f"Passed out values: {obj3.a} and {obj4.a}")
print(obj3 == obj4)
