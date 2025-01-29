class Seat:
    def __init__(self, row:int, column:int):
        self.row:int = row
        self.column:int = column
        self.is_reserved:bool = False

    def check_reservation(self):
        return self.is_reserved

    def reserve(self):
        if not self.check_reservation():
            self.is_reserved = True
        else:
            raise ValueError("Seat is already reserved")

    def cancel_reservation(self):
        if self.check_reservation():
            self.is_reserved = False
        else:
            raise ValueError("Seat is not reserved")

    def get_coordinates(self):
        return self.row, self.column

class Carriage:
    def __init__(self, unique_id:int):
        self.seats:list[Seat] = []
        self.unique_id:int = unique_id

    def assign_seats(self, seat_array:list[Seat]):
        self.seats.extend(seat_array)

    def unassign_seat(self, seat:Seat):
        self.seats.remove(seat)

    def reset_reservations(self):
        [], reserved_seats = self.get_seat_info()
        for seat in reserved_seats:
            seat.cancel_reservation()

    def get_seat_info(self):
        unreserved_seats = []
        reserved_seats = []
        for seat in self.seats:
            if seat.is_reserved:
                reserved_seats.append(seat)
                continue
            unreserved_seats.append(seat)

        return unreserved_seats, reserved_seats

    def get_readable_seat_info(self):
        unreserved, reserved = self.get_seat_info()
        first_part = f"Amount of unreserved seats: {len(unreserved)}, "
        second_part = f"Amount of reserved seats: {len(reserved)}"
        return first_part + second_part

    def get_total_seat_amount(self):
        return len(self.seats)

    def check_fullness(self):
        unreserved, reserved = self.get_seat_info()
        if len(reserved) == self.get_total_seat_amount():
            return True
        return False

def main():
    seat_a = Seat(1, 1)
    seat_b = Seat(1, 2)
    seat_c = Seat(2, 1)
    seat_d = Seat(2, 2)

    carriage_a = Carriage(1001)
    carriage_a.assign_seats([seat_a, seat_b, seat_c, seat_d])

    seat_a.reserve()
    seat_b.reserve()
    seat_c.reserve()

    print(f"Total seat amount: {carriage_a.get_total_seat_amount()}")
    print(carriage_a.get_readable_seat_info())
    print("Reserving last seat...")
    seat_d.reserve()
    if carriage_a.check_fullness():
        print("Carriage is full")
    else:
        print("Carriage is not full")

    print("Trying to reserve an already reserved seat...")
    try:
        seat_a.reserve()
        print("Succesful!")
    except ValueError:
        print("Cannot reserve, seat already reserved")

    print("Resetting reservations...")
    carriage_a.reset_reservations()
    print(carriage_a.get_readable_seat_info())


if __name__ == "__main__":
    main()