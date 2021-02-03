# Course: CS261 - Data Structures
# Student Name: Jeremy Vernon
# Assignment: 2
# Description: Creates a stack
# Last revised: 03 Feb 21

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da[i]) for i in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    # ------------------------------------------------------------------ #

    def push(self, value: object) -> None:
        """
        Adds value to the end of the stack
        """
        self.da.append(value)

    def pop(self) -> object:
        """
        Removes top of the stack
        """
        # checks that there is at least one element in the stack
        if self.size() < 1:
            raise StackException
        # gets value of the top of the stack, then removes and returns the element
        else:
            last_pos = self.size() - 1
            stack = self.da.get_at_index(last_pos)
            self.da.remove_at_index(last_pos)
            return stack

    def top(self) -> object:
        """
        Returns the value at the top of the stack
        """
        # checks that there is at least one element in the stack
        if self.size() < 1:
            raise StackException
        # gets value of the top of the stack, then returns it
        else:
            last_pos = self.size() - 1
            stack = self.da.get_at_index(last_pos)
            return stack


# BASIC TESTING
if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))

    for value in [1, 2, 3, 4, 5]:
        s.push(value)

    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
