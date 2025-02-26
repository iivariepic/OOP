class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.people:list[Person] = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        return len(self.people) == 0

    def combined_height(self):
        result = 0
        for person in self.people:
            result += person.height
        return result

    def print_contents(self):
        print(f"There are {len(self.people)} persons in the room, and their combined height is {self.combined_height()} cm")
        for person in self.people:
            print(person)

    def shortest(self):
        shortest = min(self.people, key=lambda person: person.height)
        return shortest


def main():
    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 175))
    print("Is the room empty?", room.is_empty())
    room.print_contents()
    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())
    print()
    room.print_contents()

if __name__ == '__main__':
    main()