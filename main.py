class Parent1:
    def __init__(self):
        self.attribute1 = "Атрибут з sem"

    def method1(self):
        print("Метод з lili")


class Parent2:
    def __init__(self):
        self.attribute2 = "Атрибут з karl"

    def method2(self):
        print("Метод з loli")


class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)

    def method_child(self):
        print("Метод з Child")


child_instance = Child()

print(child_instance.attribute1)
print(child_instance.attribute2)

child_instance.method1()
child_instance.method2()
child_instance.method_child()
