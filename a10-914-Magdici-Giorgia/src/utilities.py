
from copy import deepcopy
from unittest import TestCase

def sort(my_list, key = None, function = None, reverse = False):
    def default_key(object):
        return object

    def default_compare(object1, object2):
        return object1 <= object2

    new_list = deepcopy(my_list)

    if key is None:
        key = default_key

    if function is None:
        function = default_compare

    #shell sort

    gap = len(new_list)

    while gap > 0:
        i = 0
        j = gap

        while j < len(new_list):
            if not function(key(new_list[i]), key(new_list[j])):
                new_list[i], new_list[j] = new_list[j], new_list[i]

            i += 1
            j += 1

            k = i
            while k - gap > -1:
                if not function(key(new_list[k - gap]), key(new_list[k])):
                    new_list[k - gap], new_list[k] = new_list[k], new_list[k - gap]
                k -= 1

        gap //= 2

    if reverse:
        i = 0
        j = len(new_list) - 1
        while i < j:
            new_list[i], new_list[j] = new_list[j], new_list[i]
            i += 1
            j -= 1

    return new_list


def my_filter(my_list, validity):
    new_list = []
    for item in my_list:
        if validity(item):
            new_list.append(item)
    return new_list


class Data:
    def __init__(self, new_dict=None):
        if new_dict is None:
            new_dict = {}
        self._dict = new_dict

    def __setitem__(self, id, info):
        self._dict[id] = info

    def __getitem__(self, item):
        return self._dict[item]

    def __delitem__(self, id):
        del self._dict[id]

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def ids(self):
        return self._dict.keys()

    def info(self):
        return self._dict.values()


class TestUtilities(TestCase):
    def setUp(self) -> None:
        self._data = Data()

    def tearDown(self) -> None:
        pass


    def test_sort(self):
        my_list = [3, 1, 2, 10]
        new_list = sort(my_list)
        self.assertEqual(new_list, [1, 2, 3, 10])

        my_list = [3, 1, 2, 10]
        new_list = sort(my_list, reverse=True)
        self.assertEqual(new_list, [10, 3, 2, 1])

        my_list = [3, 1, 2, 10]
        new_list = sort(my_list, function = lambda x,y:x>=y)
        self.assertEqual(new_list, [10, 3, 2, 1])

        my_list = [3, 1, 2, 10]
        new_list = sort(my_list, function=lambda x, y: x >= y,reverse=True)
        self.assertEqual(new_list, [1, 2, 3, 10])

        my_list = [12, 34, 54, 2, 3]
        new_list = sort(my_list)
        self.assertEqual(new_list, [2, 3, 12, 34, 54])


    def test_filter__list_is_not_filtered__list_is_filter(self):
        my_list = [[1, 2], [3, 2], [1, 3], [4, 2]]
        new_list = my_filter(my_list, lambda x: x[1] == 2)
        self.assertEqual(new_list, [[1, 2], [3, 2], [4, 2]])

    def test_get_item(self):
        self._data['0'] = 1
        self.assertEqual(self._data['0'], 1)

    def test_set_item(self):
        self._data['0']=1
        self.assertEqual(self._data['0'], 1)
        self._data['0']=2
        self.assertEqual(self._data['0'], 2)


    def test_del_item(self):
        self._data['0']=1
        self.assertEqual(len(self._data), 1)
        del self._data['0']
        self.assertEqual(len(self._data), 0)

    def test_next(self):
        self._data['banana']= 'yellow'
        self._data['strawberry'] = 'red'
        self._data['orange']= 'orange'
        self._data['cherry']= 'red'
        for fruit in self._data:
            if fruit == 'cherry' or fruit == 'strawberry':
                self.assertEqual(self._data[fruit], 'red')

    def test_ids(self):
        self._data[1] = 'yellow'
        self._data[2] = 'red'
        self._data[3] = 'orange'
        self._data[4] = 'black'
        self.assertEqual(list(self._data.ids()), [1, 2, 3, 4])

    def test_info(self):
        self._data[1] = 'yellow'
        self._data[2] = 'red'
        self.assertEqual(list(self._data.info()), ['yellow', 'red'])




