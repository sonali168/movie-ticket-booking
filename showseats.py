import math


class Seats:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    global number
    global customer
    number = []
    customer = []

    # column = []

    def show_seats(self, main_rows, main_columns):
        #self.main_rows = main_rows
        #self.main_columns = main_columns
        global tickets_booked
        tickets_booked = 0
        print("Cinema: ")

        for i in range(main_rows + 1):
            for j in range(main_columns + 1):
                if i == 0:
                    if i == 0 and j == 0:
                        print(" ", end=" ")
                        continue
                    else:
                        print(j, end=" ")
                else:
                    if i == 1 and j == 0:
                        print("")
                    else:
                        count = 1
                        print(i, end=" ")

                        while True:
                            if count <= main_columns:
                                seat_no = int(str(i) + str(count))
                                if seat_no in number:
                                    print('B', end=" ")
                                    tickets_booked += 1
                                else:
                                    print('S', end=" ")
                                    count = count + 1
                            else:
                                print('')
                                break
                        break