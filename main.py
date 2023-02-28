# Define a class Person
class Person:
    # Define constructor
    def __init__(self, name, age, gender):
        # Declare attributes
        self.name = name
        self.age = age
        self.gender = gender

    # Define methods
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

# Main function
def main():
    # Create a list of Person objects
    people = [Person("Alice", 25, 'F'), Person("Bob", 30, 'M'), Person("Charlie", 35, 'M')]

    # Use a loop to print out the details of each person
    for p in people:
        print(p.getName() + " is " + str(p.getAge()) + " years old and " + p.getGender())

# Call the main function
if __name__ == "__main__":
    main()
