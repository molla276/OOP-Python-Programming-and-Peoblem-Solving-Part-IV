from queue import Empty

#part1
class Star_Cinema:
    hall_list = []

    def entry_hall(self):
        self.hall_list.append()
#part2
class Hall(Star_Cinema):
    def __init__ (self,rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = []
        self.show_list = ()
#part3
    def entry_show(self, id, movie_name, time):
        # self.id = id
        # self.movie_name = movie_name
        # self.time = time
        self.show_list.append([id,movie_name,time])
        seat = [['Empty']*self.rows*self.cols]
        self.seats[id] = seat
#part4
    def book_sets(self,customer_name, phone_number, id, least_of_tuples):
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.least_of_tuples = []

#part5
    def view_show_list(self):
        pass

#part6
    def view_available_sets(self):
        pass
