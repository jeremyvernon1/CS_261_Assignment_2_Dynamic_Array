# Course: CS261 - Data Structures
# Student Name: Jeremy Vernon
# Assignment: 2
# Description: Creates a Dynamic Array
# Last revised: 03 Feb 21


from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # ------------------------------------------------------------------ #

    def resize(self, new_capacity: int) -> None:
        """
        Resizes the array and imports elements from the old array
        """
        # checks that new capacity is greater than 0, and is not less than the filled array
        if new_capacity > 0 and new_capacity >= self.size:
            # creates a new array, and copies the elements from the old array
            new_array = StaticArray(new_capacity)
            for index in range(self.capacity):
                if self.data.get(index) is not None:
                    new_array.set(index, self.data.get(index))
            self.data = new_array
            self.capacity = new_capacity

    def append(self, value: object) -> None:
        """
        Adds element to the end of the array
        """
        # checks if array is full, and if so, resizes
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        # adds element to the end of the array
        self.data[self.length()] = value
        self.size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a value at the given index.
        If the position is full, the elements to the right are shifted right
        """
        last_pos = self.size
        # checks if index position is valid
        if index < 0 or index > last_pos:
            raise DynamicArrayException
        else:
            # checks if array is full, and if so, resizes
            if last_pos == self.capacity:
                self.resize(self.capacity * 2)
            # checks if index is occupied, and if so shifts existing elements right
            if self.data.get(index) is not None:
                iteration_count = (self.size - index)
                while iteration_count > 0:
                    self.data.set(last_pos, self.data.get(last_pos - 1))
                    last_pos -= 1
                    iteration_count -= 1
            # adds new element
            self.data.set(index, value)
            self.size += 1

    def remove_at_index(self, index: int) -> None:
        """
        Removes element at the given index position.
        If capacity is greater than 10 elements, and size < 1/4 capacity,
        resized to twice the number of filled elements.
        Shifts elements to the right.
        """
        # checks for valid index position
        if index < 0 or index > (self.size - 1) or self.data.get(index) is None:
            raise DynamicArrayException
        # checks if capacity is greater than 10 and if size is less than 1/4 capacity
        # if meets, resizes to reduce
        if self.capacity > 10 and self.size < (self.capacity / 4):
            # checks that array will not be reduced lower than a size of 10
            lowest_array_size = 10
            double = self.size * 2
            if double > lowest_array_size:
                self.resize(double)
            else:
                self.resize(lowest_array_size)
        # shifts elements to the right to the left to fill in the empty space
        shift_count = (self.capacity - index) - 1  # subtracts 1 to account for zero base
        while shift_count > 0:
            self.data.set(index, self.data.get(index + 1))
            index += 1
            shift_count -= 1
        self.size -= 1

    def slice(self, start_index: int, size: int) -> object:
        """
        Creates a new dynamic array and appends (size) number of elements starting at start_index
        """
        # checks for valid start index and size
        array_size = self.size
        if \
                start_index < 0 or \
                start_index > (array_size - 1) or \
                size < 0 or \
                size > (array_size - start_index):
            raise DynamicArrayException

        # create a new array and copy sliced elements into it
        slice_new_array = DynamicArray()
        for index in range(start_index, (start_index + size)):
            slice_value = self.data.get(index)
            if slice_value is not None:
                slice_new_array.append(slice_value)

        return slice_new_array

    def merge(self, second_da: object) -> None:
        """
        Appends elements from the second array into the first array.
        """
        second_da_size = second_da.size
        if second_da_size > 0:  # checks that second array is not empty.
            for index in range(second_da_size):
                self.append(second_da.get_at_index(index))

    def map(self, map_func) -> object:
        """
        Creates a new dynamic array with the original elements mapped to the results of a function
        """
        # creates result array
        map_new_array = DynamicArray()

        # runs map_func from parameter on each element, then adds to result array
        for index in range(self.size):
            map_value = map_func(self.get_at_index(index))
            map_new_array.append(map_value)

        return map_new_array

    def filter(self, filter_func) -> object:
        """
        Creates a new dynamic array with only the elements that pass filter_func
        """
        # creates result array
        filter_new_array = DynamicArray()

        # runs filter_func from parameter on each element, then adds to result array
        for index in range(self.size):
            if filter_func(self.get_at_index(index)):
                filter_value = self.get_at_index(index)
                filter_new_array.append(filter_value)

        return filter_new_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Creates a new dynamic array with the elements after reduce_func has run on the element
        """
        # checks for empty array
        if self.size == 0:
            return initializer

        # sets initializer and whether to start at index 0 or index 1
        start_range = 0
        if initializer is None:
            initializer = self.get_at_index(0)
            start_range = 1

        # runs reduce_func from parameter on each element and accumulates the initializer
        for index in range(start_range, self.size):
            initializer = reduce_func(initializer, self.get_at_index(index))

        return initializer




# BASIC TESTING
if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)
    da.resize(8)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)
    da = DynamicArray([-91865, -12502, 91702])
    print(da)
    da.insert_at_index(1, -70756)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# remove at index - example 5")
    da = DynamicArray(["CokxWyd", "aROXptjK"])
    try:
        da.remove_at_index(2)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)
    da = DynamicArray([44683, 19377, 90480, -89559])
    try:
        da.remove_at_index(4)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")
    da = DynamicArray([1])
    da_slice = da.slice(0, 1)
    print(da, da_slice, sep="\n")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(2, 3)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# merge example 3")
    da = DynamicArray([1])
    da2 = DynamicArray([2, 3])
    print(da)
    print(da2)
    da.merge(da2)
    print(da)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 3")
    values = ["nozgogve", "sdhirt", "bmaafje", "ml", "vsahv", "ea", "h", "jqqvw", "ldnxc", "nuavuy"]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x + y)))
