class Trips:
    def __init__(self, trip_cites, start_date) -> None:
        self.trip_cites = trip_cites
        self.start_date = start_date
        self.aircraft = None
        self.trip_route = None
        self.cost = None

    def __repr__(self) -> str:
        return f'Trip: {self.trip_cites} Aircraft: {self.aircraft} Trip:{self.trip_route} Cost:{self.cost}'