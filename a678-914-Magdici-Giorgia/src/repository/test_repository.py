import unittest

from src.domain.book import Book
from src.domain.validators import BookValidator
from src.repository.repository import Repository, RepositoryException


class RepositoryTest(unittest.TestCase):
    """
    class RepositoryTest "is a" unittest.TestCase
    RepositoryTest has all the methods that TestCase has
    """

    def setUp(self) -> None:
        """
        Runs before every test method
        """
        self.validator=BookValidator
        self._repo = Repository(self.validator)

    def tearDown(self) -> None:
        """
        Runs after every test method
        """
        pass

    def test_empty_repo(self):
        #self.assertEqual(len(self._repo), 0)
        assert len(self._repo) == 0

    def test_repo_add_one(self):
        self._repo.add(Book(100, "Dan Brown", "Inferno"))
        self.assertEqual(len(self._repo), 1)

    def test_repo_exception(self):
        self._repo.add(Book(100, "Dan Brown", "Inferno"))

        with self.assertRaises(RepositoryException):
            self._repo.add(Book(100, "Dan Brown", "Inferno"))

    def test_repository(self):
        novel = Book(101, "Dan Brown", "Origin")
        self._repo.add(novel)
        self._repo.add(Book(102, "Virginia Woolf", "The Waves"))
        self.assertEqual(len(self._repo), 2)
        self.assertEqual(self._repo[101], novel)


        self._repo.remove_by_id(102)
        self.assertEqual(len(self._repo), 1)


