import sys
sys.path.insert(0, "../")
from familyTree import FamilyTree
from problem1234Solution.problem1 import Problem1


class Problem2:

    @staticmethod
    def add_child(family):
        parent_name = input("Enter Parent Name: ")
        options = ["Daughter", "Son"]
        for index, name in enumerate(options):
            print("Enter " + str(index) + " If you want to  " + name + ".")
        option_number = int(input("Your option : "))
        child_name = input("Enter "+options[option_number] + " name :")
        sex = "F" if option_number == 0 else "M"
        family.add_new_born(parent_name, child_name, sex)
        print("child Added successfully")


if __name__ == "__main__":
    family = FamilyTree().construct()
    Problem2.add_child(family)
    # using problem1 here to get a person's relatives based on a relationship
    Problem1.print_relatives_of_member(family)

