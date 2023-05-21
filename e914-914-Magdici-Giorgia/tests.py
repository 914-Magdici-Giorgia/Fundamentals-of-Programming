import unittest


class RepositoryTest(unittest.TestCase):
    def setUp(self)->None:
        self.b=Board()
        self.c=Controller()
        self.c._random_asteroids()
        self._c._random_aliens(2,0)

    def test_
