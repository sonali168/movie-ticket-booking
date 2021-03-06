import math

class Statfunction:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    global number
    global customer
    number = []
    customer = []
    global main_rows
    global main_columns


    def statistics(self,rows,columns):

        global total_income

        total_income = ()
        total_seats = main_rows * main_columns
        total_tickets = total_seats
        print("Total seats=", total_tickets)

        no_of_tickets_booked = len(number)
        print("no_of_purchased_tickets: ",no_of_tickets_booked)


        percentage_of_tickets_book = (no_of_purchased_tickets / total_tickets) * 100
        print("percentage_of_tickets_book is: ", percentage_of_tickets_book ,"%")

        current_income = [key['ticket_price'] for key in cutomer]
        print("current_income = $ ", sum(current_income), "$")

        x = rows * columns
        if x <= 60:
            total_income
            10 * x
        else:
            x = rows // 2

            first_hallf_ticket_price = 10 * x * columns
            left_rows = rows - x

            second_half_ticket_price = 8 * left_rows * columns

            total_income = first_hallf_ticket_price + second_half_ticket_price
        print("total_income = $ ", total_income)




