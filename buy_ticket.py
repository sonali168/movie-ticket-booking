class Movie:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    global number
    global customer
    number = []
    customer = []


    def buy_ticket(self, rows, columns):
        global ticket_price  # make it final
        global seat_status
        global seat_no
        customer = []
        number = []
        main_rows = 9
        main_columns = 9

        buy_ticket_rows = int(input("Enter the numbers of rows:"))
        # while buy_ticket_rows < main_rows: #or buy_ticket_rows > main_rows: # main row>1 and main<
        #   print("Kindly enter numbers of rows between 1 to 10")
        #  seat_rows = int(input("Enter the numbers of rows:"))

        buy_ticket_columns = int(input("Enter the numbers of columns:"))
        # while buy_ticket_columns < main_columns: #or buy_ticket_columns > main_columns:
        #   print("Kindly enter numbers of rows between 1 to 10")
        #  buy_ticket_columns = int(input("Enter the numbers of columns:"))

        total_rows = main_rows
        total_columns = main_columns
        total_seats = total_rows + total_columns

        buy_ticket_seat_no = int(str(buy_ticket_rows) + str(buy_ticket_columns))
        seat_no = int(str(main_rows) + str(main_columns))
        seat_status = "Available"

        if buy_ticket_seat_no in number:
            print("Seat is already booked.")
            seat_status = "Booked"

        if seat_status == "Available":
            if buy_ticket_rows <= main_rows and buy_ticket_columns <= main_columns:
                seat_no = int(str(buy_ticket_rows) + str(buy_ticket_columns))

                ticket_price = 0

        if total_seats <= 60:
            ticket_price = 10
            print("ticket_price =", ticket_price)
        else:
            if buy_ticket_rows < (total_rows / 2):
                ticket_price = 10
                print("ticket_price =", ticket_price)
            else:
                ticket_price = 8
                print("ticket_price =", ticket_price)

        options = input("Do you want to book ticket? (yes/no):")
        answer = options.lower()

        if answer == 'yes':
            data = {}
            Name = input("Name:")
            Age = input("Age:")

            while True:
                Gender = input("Gender(male, female, transgender):")
                if Gender.lower() not in ['male', 'female', 'transgender']:
                    print("invalid Gender")
                    continue
                break

            while True:
                Phone_number = input("Phone_number:")
                if len(Phone_number) > 10 or len(Phone_number) < 10:
                    print("Invalid Number")
                else:
                    break
                # no_of_ticket_book = input("no_of_ticket_book: ")

            data['Name'] = Name
            data['Gender'] = Gender
            data['Age'] = Age
            data['Phone_number'] = Phone_number
            data["buy_ticket_rows"] = buy_ticket_rows
            data['buy_ticket_columns'] = buy_ticket_columns
            data['ticket_price'] = ticket_price
            data['seat_no'] = seat_no
            customer.append(data)

            if data['Name'] in Name:
                number.append(seat_no)
                print("Booked Successfully !!!!")
                print("Thank you for booking.")
                # print(no_of_ticket_book)
            else:
                print("Error")

                # print(customer)


        else:
            print("Thank you for visting")