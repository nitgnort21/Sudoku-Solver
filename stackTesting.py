import unittest
from stack import stack

class Testing(unittest.TestCase):
    def testPush(self):
        myStack = stack()
        myStack.push(9)
        self.assertEqual(myStack.getSize(), 1)
        self.assertEqual(myStack.top(), 9)
    

    def testPushWithStings(self):
        try:
            myStack = stack()
            myStack.push(9)
            myStack.push("a b c")
        except Exception as exp:
            self.assertTrue(exp.args[0].startswith("Error"), "The type doesn't fit with the type of the first item in myStack")


    def testPushWithFloats(self):
        try:
            myStack = stack()
            myStack.push(9)
            myStack.push(3.4)
        except Exception as exp:
            self.assertTrue(exp.args[0].startswith("Error"), "The type doesn't fit with the type of the first item in myStack")
        

    def testTopAndTestGetSize(self):
        myStack = stack()
        myStack.push(3)
        myStack.push(9)
        myStack.push(4)

        self.assertEqual(myStack.top(), 4)

        self.assertEqual(myStack.getSize(), 3)


    def testPop(self):
        myStack = stack()
        myStack.push(4)
        myStack.push(6)
        myStack.push(10)

        self.assertEqual(myStack.top(), 10)
        self.assertEqual(myStack.getSize(), 3)

        myStack.pop()

        self.assertEqual(myStack.top(), 6)
        self.assertEqual(myStack.getSize(), 2)


    def testPopEmptyList(self):
        try:
            myStack = stack()
            myStack.pop()
        except Exception as exp:
            self.assertTrue((exp.args[0].startswith("Error")))


    def testIsEmpty(self):
        myStack = stack()
        self.assertTrue(myStack.isEmpty())

        myStack.push(4)
        self.assertFalse(myStack.isEmpty())


    def testDisplay(self):
        myStack = stack()
        myStack.push(4.5)
        myStack.push(6.2)
        myStack.push(10.9)

        self.assertEqual(myStack.display(), "4.5\n6.2\n10.9")


    def testGetTypeFloats(self):
        myStack = stack()
        myStack.push(4.5)
        myStack.push(6.2)
        myStack.push(10.9)

        self.assertIs(myStack.getType(), float)


    def testGetTypeInt(self):
        myStack = stack()
        myStack.push(4)
        myStack.push(6)
        myStack.push(10)

        self.assertIs(myStack.getType(), int)


    def testGetTypeString(self):
        myStack = stack()
        myStack.push("4")
        myStack.push("6")
        myStack.push("10")

        self.assertIs(myStack.getType(), str)


if __name__ == '__main__':
    unittest.main()
