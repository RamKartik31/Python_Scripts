import sys
sys.path.insert(0, "../")
from familyTree import FamilyTree
from problem2 import  Problem2


class Problem3:

    @staticmethod
    def get_mothers(family):
        women_list = []
        for member in family.members:
            if member.sex == "F" and member.spouse:
                daughter_count = len(member.daughters)
                if daughter_count > 0:
                    women_list.append((daughter_count, member.name))
        women_list.sort(reverse=True)
        return women_list


if __name__ == "__main__":
    family = FamilyTree().construct()
    # let's get all the woman who has daughters in the reverse sorted order
    most_daughter_women_list = Problem3.get_mothers(family)
    print(", ".join([x[1] for x in most_daughter_women_list]))
    # let's add a girl child using problem2 code
    Problem2.add_child(family)
    most_daughter_women_list = Problem3.get_mothers(family)
    print(most_daughter_women_list[0][1])
