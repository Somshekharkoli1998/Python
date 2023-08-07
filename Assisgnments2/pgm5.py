class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

def test_string_manipulator():
    manipulator = StringManipulator()
    manipulator.getString()
    manipulator.printString()

if __name__ == "__main__":
    test_string_manipulator()