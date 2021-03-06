# Course: CS261 - Data Structures
# Student Name: Jeremy Vernon
# Assignment: 2
# Description: Creates a bag
# Last revised: 03 Feb 21

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds elements to bag
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes item from bag
        """
        for index in range(self.size()):
            if self.da.get_at_index(index) == value:
                self.da.remove_at_index(index)
                return True

        return False

    def count(self, value: object) -> int:
        """
        Counts the instances of a given element in a bag
        """
        count = 0
        for index in range(self.da.size):
            if self.da.get_at_index(index) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clears the bag
        """
        self.da = DynamicArray()

    def equal(self, second_bag: object) -> bool:
        """
        Checks if two bags contain the same elements.
        If they do, returns True. Else, returns False.
        """
        # checks if elements have the same number of elements
        if self.size() == second_bag.size():
            for index1 in range(self.size()):
                value = self.da.get_at_index(index1)
                bag_a = self.count(value)  # finds the count of the element in the first array,
                bag_b = second_bag.count(value)  # then compares to count of the element in the second array.
                if bag_a != bag_b:  # if the two counts (instances) do not match, returns False.
                    return False
            return True  # if array search completes without returning False, returns True.
        return False




# BASIC TESTING
if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# equal example 2")
    bag1 = Bag([1, 2, 2])
    bag2 = Bag([1, 1, 2])
    print(bag1, bag2, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print("expected result: False, False")
    bag1 = Bag([10, 20, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10, 60])
    print(bag1, bag2, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print("expected result: False, False")
    bag1 = Bag([10, 20, 60, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10, 60])
    print(bag1, bag2, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print("expected result: True, True")
