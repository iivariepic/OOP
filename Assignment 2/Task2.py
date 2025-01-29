class Seat:
    def __init__(self, row, column):
        self.row:int = row
        self.column:int = column
        self.is_reserved:bool = False

    def reserve(self):
        self.is_reserved = True

    def cancel_reservation(self):
        self.is_reserved = False

    def get_coordinates(self):
        return self.row, self.column

class Carriage:
    def __init__(self, unique_id):
        self.seats:list[Seat] = []
        self.unique_id = unique_id

    def get_seat_info(self):
        unreserved_seats = []
        reserved_seats = []
        for seat in self.seats:
            if seat.is_reserved:
                reserved_seats.append(seat)
                continue
            unreserved_seats.append(seat)

        return unreserved_seats, reserved_seats

    def check_fullness(self):
        unreserved, reserved = self.get_seat_info()
        if len(reserved) == len(self.seats):
            return True
        return False