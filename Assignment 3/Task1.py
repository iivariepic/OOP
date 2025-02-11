import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Assignment 2')))

from Task2 import Carriage, Seat

class Train:
    def __init__(self, unique_id:int, initial_carriage:Carriage):
        self.__unique_id:int = unique_id
        self.__carriages:list[Carriage] = [initial_carriage]
        self.__location_departure:str = "Default"
        self.__location_arrival:str = "Default"

    def attach_carriage(self, carriage) -> None:
        if carriage not in self.__carriages:
            self.__carriages.append(carriage)
        else:
            raise ValueError(f"Carriage {carriage.get_id()} already attached")

    def detach_carriage(self, carriage) -> None:
        if carriage in self.__carriages:
            self.__carriages.remove(carriage)
        else:
            raise ValueError(f"Carriage {carriage.get_id()} not attached")

    def set_departure_location(self, target_location) -> None:
        self.__location_departure = target_location

    def set_arrival_location(self, target_location) -> None:
        self.__location_arrival = target_location

    def get_end_stops(self) -> tuple[str, str]:
        return self.__location_departure, self.__location_arrival

    def get_train_info(self) -> str:
        info = f"\n## NEW INFO STARTS HERE ##"
        info += f"\nTrain Unique ID: {self.__unique_id}"
        info += f"\nDeparture Location: {self.__location_departure}"
        info += f"\nArrival Location: {self.__location_arrival}"
        info += f"\nAmount of carriages: {len(self.__carriages)}"

        for accumulator, carriage in enumerate(self.__carriages, start=1):
            info += f"\n\nCarriage {accumulator}:"
            info += f"\nCarriage ID: {carriage.get_id()}"
            info += f"\n{carriage.get_readable_seat_info()}"

        return info

    def reserve_first_available_seat(self) -> None:
        for carriage in self.__carriages:
            available_seats, unavailable_seats = carriage.get_seat_info()
            if available_seats:
                available_seats[0].reserve()
                return

        raise ValueError(f"No seats available for reservation in Train {self.__unique_id}")


def main() -> None:
    seat_a = Seat(1, 1)
    seat_b = Seat(1, 2)
    seat_c = Seat(2, 1)
    seat_d = Seat(2, 2)

    carriage_a = Carriage(1001)
    carriage_a.assign_seats([seat_a, seat_b, seat_c, seat_d])

    pendolino = Train(1, carriage_a)

    unreserved_seats, [] = carriage_a.get_seat_info()
    for seat in unreserved_seats:
        seat.reserve()

    seat_e = Seat(1, 1)
    seat_f = Seat(1, 2)
    carriage_b = Carriage(1002)
    carriage_b.assign_seats([seat_e, seat_f])

    pendolino.attach_carriage(carriage_b)

    print(pendolino.get_train_info())

    pendolino.detach_carriage(carriage_a)

    print(pendolino.get_train_info())

    pendolino.reserve_first_available_seat()
    pendolino.reserve_first_available_seat()

    print(pendolino.get_train_info())



if __name__ == '__main__':
    main()