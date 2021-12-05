from unittest import TestCase, main
import sys

sys.path.insert(0, '../')
from person import Person
from utility import Utility


class TestUtility(TestCase):
    person = Person("Vic", "M")

    def test_connect_new_born_to_parent(self):
        spouse = Person("Simona", "F")
        self.person.add_spouse(spouse)
        child = Person("Creto", "M", spouse, self.person)
        Utility.connect_new_born_to_parent(child, [spouse, self.person])
        self.assertEqual(spouse.sons[0], child)
        self.assertEqual(self.person.sons[0], child)


if __name__ == "__main__":
    main()
