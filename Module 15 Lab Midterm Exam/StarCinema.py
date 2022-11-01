class Star_Cinema:
    hall_list = []

    def entry_hall(self,hall_details):
        self.hall_list.append(hall_details) #insert from hall class

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(vars(self))

    def seat_list(self):
        my_list = []

        for i in range(self.rows):
            my_list.append([])

        for seat in my_list:
            for i in range(self.cols):
                seat.append(0)
        return my_list

    def entry_show(self, id, movie_name, time):
        # self.id = id
        # self. movie_name = movie_name
        # self.time = time
        # show = (id, movie_name, time)
        # self.show_list.append(show)
        # self.seats = {id: [[0 for i in range(self.cols)] for j in range(self.rows)]}

        show = (id, movie_name, time)
        self.show_list.append(show)
        self.seats[id] = self.seat_list()

    def book_seats(self,customer_name, phone_number, id,list_of_tuples):
        for i, j in self.seats.items():
            if id == i:
                for k, l in enumerate(j):
                    for m, n in enumerate(list_of_tuples):
                        if j[n[0]][n[1]] != False:
                            print('Already seats are booked')
                            break
                        else:
                            j[n[0]][n[1]] = customer_name
                    break
                break

    def view_show_list(self):
        return self.show_list

    def view_available_seats(self, id):
        for show in self.show_list:
            if id in show:
                available_seats = self.seats[]
                print(available_seats)

                for seat in available_seats:
                    for i in seat:
                        if i == False:
                            return i
                        else:
                            print('Already seats are booked')


