from unittest import TestCase, main
import sys
sys.path.insert(0, '../')
from person import Person
from familyTree import FamilyTree
from family import Family
class TestPerson(TestCase):
    person = Person("Vic", "M")
    family = FamilyTree().construct()

    def test_add_spouse(self):
        spouse = Person("Simona","F")
        self.person.add_spouse(spouse)
        self.assertEqual(spouse.name,self.person.spouse.name)

    def test_add_child(self):
        child = Person("Creto", "M")
        self.person.add_child(child)
        self.assertEqual(child.name, self.person.sons[0].name)

    def test_get_brothers(self):
        person_name = "Satvy"
        person_bothers = ["Savya", "Saayan"]
        person = self.family.find_member_by_name(person_name)
        brothers = Person.get_brothers(person)
        brother_name_list = [x.name for x in brothers]
        for brother in brother_name_list:
            self.assertTrue(brother in person_bothers)
        for brother in person_bothers:
            self.assertTrue(brother in brother_name_list)

    def test_get_sisters(self):
        person_name = "Vich"
        person_sister = ["Satya"]
        person = self.family.find_member_by_name(person_name)
        sisters = Person.get_sisters(person)
        sister_name_list = [x.name for x in sisters]
        for sister in sister_name_list:
            self.assertTrue(sister in person_sister)
        for sister in person_sister:
            self.assertTrue(sister in sister_name_list)

    def test_get_paternal_uncles(self):
        person_name = "Satvy"
        paternal_uncle_names = ["Ish", "Chit", "Vich"]
        person = self.family.find_member_by_name(person_name)
        paternal_uncle = Family.get_uncles(person, person.father)
        paternal_uncle_in_tree = [x.name for x in paternal_uncle]
        for name in paternal_uncle_in_tree:
            self.assertTrue(name in paternal_uncle_names)
        for name in paternal_uncle_names:
            self.assertTrue(name in paternal_uncle_in_tree)

    def test_get_maternal_uncles(self):
        person_name = "Driya"
        maternal_uncle_names = ["Vrita"]
        person = self.family.find_member_by_name(person_name)
        maternal_uncle = Family.get_uncles(person, person.mother)
        maternal_uncle_in_tree = [x.name for x in maternal_uncle]
        for name in maternal_uncle_in_tree:
            self.assertTrue(name in maternal_uncle_names)
        for name in maternal_uncle_names:
            self.assertTrue(name in maternal_uncle_in_tree)

    def test_get_paternal_aunt(self):
        person_name = "Vila"
        paternal_aunt_names = ["Satya", "Ambi"]
        person = self.family.find_member_by_name(person_name)
        paternal_aunt = Family.get_aunt(person, person.father)
        paternal_aunt_in_tree = [x.name for x in paternal_aunt]
        for name in paternal_aunt_in_tree:
            self.assertTrue(name in paternal_aunt_names)
        for name in paternal_aunt_names:
            self.assertTrue(name in paternal_aunt_in_tree)

    def test_get_maternal_aunt(self):
        person_name = "Vila"
        maternal_aunt_names = ["Satya"]
        person = self.family.find_member_by_name(person_name)
        maternal_aunt = Family.get_aunt(person, person.mother)
        maternal_aunt_in_tree = [x.name for x in maternal_aunt]
        for name in maternal_aunt_in_tree:
            self.assertTrue(name in maternal_aunt_names)
        for name in maternal_aunt_names:
            self.assertTrue(name in maternal_aunt_in_tree)

    def test_get_children(self):
        person_name = "Satya"
        children_names = ["Satvy", "Savya", "Saayan"]
        person = self.family.find_member_by_name(person_name)
        children = Person.get_children(person)
        children_in_tree = [x.name for x in children]
        for name in children_in_tree:
            self.assertTrue(name in children_names)
        for name in children_names:
            self.assertTrue(name in children_in_tree)


if __name__ == "__main__":
    main()
