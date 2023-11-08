# Multilevel Inheritance
# Level - GF -> F -> S


class Grandfather:
    def grandfather_method(self):
        return "Grandfather method "


class Father(Grandfather):
    def father_method(self):
        return "Father method"


class Child(Father):
    def child_method(self):
        return "child's method"


child = Child()
print(child.grandfather_method())
print(child.father_method())
print(child.child_method())
