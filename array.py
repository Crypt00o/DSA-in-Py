class Array:

    @staticmethod
    def __check_arr_type__(arr_type: object, other: object):

        if type(other) != Array:
            raise ValueError('Expect Array Type')

        if arr_type == other.__arr_type__:
            raise TypeError(
                f'Array Should Have The Same Type, Found : Array({other.__arr_type__})')

    @staticmethod
    def __check_value_type__(arr_type, value):

        if type(value) != arr_type:
            raise ValueError(
                f'''
                    Type of Array is {arr_type} , Found Type {type(value)}
                    ''')

    @staticmethod
    def __check_size__(arr_size: int, arr_value):

        if type(arr_size) == int and len(arr_value) >= arr_size:
            raise IndexError('Array Out of bounds')

    @staticmethod
    def __check_index__(index: int, arr_size: int):

        if type(index) != int or index < 0:
            raise IndexError('Index Can Be Unsigned int Only')

        if arr_size is not None and index > arr_size:
            raise IndexError('Index Out of Range')

    def __init__(self, arr_type: object = None, init_list: list[object] = [], arr_size=None):

        if arr_size is not None and type(arr_size) != int:
            raise TypeError('Array Size Can Be Unsigned int Only')

        if type(arr_size) == int:

            if arr_size < 0:
                raise TypeError('Array Size Can,t Be Negative')

            if len(init_list) > arr_size:
                raise IndexError('Array Out of bounds')

        [Array.__check_value_type__(arr_type, element)
         for element in init_list]

        self.__arr_value__ = list(init_list)
        self.__arr_size__ = arr_size
        self.__arr_type__ = arr_type

    def __len__(self):
        return len(self.__arr_value__)

    def __repr__(self):
        return self.__arr_value__.__repr__()

    def __str__(self):
        return self.__arr_value__.__str__()

    def __getitem__(self, index: int):

        Array.__check_index__(index, self.__arr_size__)

        return self.__arr_value__[index]

    def __setitem__(self, index: int, value):

        Array.__check_index__(index, self.__arr_size__)
        Array.__check_value_type__(self.__arr_type__, value)

        self.__arr_value__[index] = value

    def __add__(self, other):

        Array.__check_arr_type__(self.__arr_type__, other)

        arr_copy = self.copy()

        for value in other.__arr_value__:
            if arr_copy.__arr_size__ is not None and len(arr_copy.__arr_value__) >= arr_copy.__arr_size__:
                break
            arr_copy.append(value)

        return arr_copy

    def __lt__(self, other):

        if len(self) < len(other):
            return True
        else:
            return False

    def __le__(self, other):

        if len(self) <= len(other):
            return True
        else:
            return False

    def __gt__(self, other):

        if len(self) > len(other):
            return True
        else:
            return False

    def __ge__(self, other):

        if len(self) >= len(other):
            return True
        else:
            return False

    def append(self, value):

        Array.__check_size__(self.__arr_size__, self.__arr_value__)
        Array.__check_value_type__(self.__arr_type__, value)

        self.__arr_value__.append(value)

    def pop(self, index=None):

        if index is None:
            return self.__arr_value__.pop()
        else:
            Array.__check_index__(index)
            return self.__arr_value__.pop(index)

    def insert(self, index: int, value):

        Array.__check_index__(index, self.__arr_size__)
        Array.__check_size__(self.__arr_size__, self.__arr_value__)
        Array.__check_value_type__(self.__arr_type__, value)

        self.__arr_value__.insert(index, value)

    def extend(self, other):

        Array.__check_arr_type__(self.__arr_type__, other)

        for value in other.__arr_value__:
            if self.__arr_size__ is not None and len(self.__arr_value__) >= self.__arr_size__:
                break
            self.append(value)

    def remove(self, value):

        Array.__check_value_type__(self.__arr_type__, value)

        self.__arr_value__.remove(value)

    def sort(self, *args):
        self.__arr_value__.sort(args)

    def clear(self):
        self.__arr_value__.clear()

    def reverse(self):
        self.__arr_value__.reverse()

    def copy(self):
        return Array(self.__arr_type__, self.__arr_value__.copy(), self.__arr_size__)

    def count(self, value):

        Array.__check_value_type__(self.__arr_value__, value)

        return self.__arr_value__.count(value)
