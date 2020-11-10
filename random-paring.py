import random
import csv


class RandomPairingPeople:
    def __init__(self):
        self.people_from_file = self._get_people()
        self._reset()

    def _get_people(self):
        people = {}
        with open('people.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='\n')
            for row in spamreader:
                person, team = row
                people[person] = team
        print(f"{len(people)} persons to parings")
        return people

    def _reset(self):
        self.pairing = []
        self.people = self.people_from_file.copy()
        self.excludes = []
        self._make_people_list_even()

    def _make_people_list_even(self):
        if len(self.people) % 2 != 0:
            person_to_exclude = random.sample(list(self.people), k=1)
            self.excludes.append(person_to_exclude[0])
            del self.people[person_to_exclude[0]]

    def random_paring(self):
        while(len(self.people) > 0):
            pair = random.sample(list(self.people), k=2)
            person1, person2 = pair
            if self.people[person1] != self.people[person2]:
                self.pairing.append(pair)
                del self.people[person1]
                del self.people[person2]
            if len(self.people) == 2:
                person1, person2 = tuple(self.people.items())
                if person1[1] == person2[1]:
                    print("Paring failled, Restarting and recalculating...")
                    self._reset()

    def show_pairing(self):
        self.random_paring()
        print(f"{'-'*20} Here we go the pairs {'-'*20}")
        print(*self.pairing, sep='\n')
        if self.excludes:
            print(f"{'-'*20} People excluded to make list even {'-'*20}")
            print(self.excludes)


def main():
    random_paring_people = RandomPairingPeople()
    random_paring_people.show_pairing()


if __name__ == '__main__':
    main()
