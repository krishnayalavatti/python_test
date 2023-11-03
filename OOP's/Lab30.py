# Class and Objects in Python.

# Person
# Attributes - name,age,phone_no,gender
# Methods - run(),sleep(),talk(),learn(),fight()

# Objects
# Krishna
# Ram

class Person:
    # Attributes
    name = None
    age = None
    phone_no = None
    gender = None
    profession = None

    # Methods
    def talk(self):
        print("talk")

    def sleep(self):
        print("sleep")

    def walking(self):
        return "I am walking"


krishna_object = Person()
krishna_object.name="Krishna"
krishna_object.age = 27
krishna_object.phone_no = "22775544"

print(krishna_object)
krishna_object.sleep()
