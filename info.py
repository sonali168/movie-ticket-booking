class Bookinfo:
    global customer
    customer = []


    def user_info(self,rows,columns):

        buy_ticket_rows = int(input("Enter the numbers of rows:"))
        while seat_rows < 1 or seat_rows > 10:
            print("Kindly enter numbers of rows between 1 to 10")
            seat_rows = int(input("Enter the numbers of rows:"))

        buy_ticket_columns = int(input("Enter the numbers of columns:"))
        while seat_columns < 1 or seat_columns > 10:
            print("Kindly enter numbers of rows between 1 to 10")
            seat_columns = int(input("Enter the numbers of columns:"))

        for i in customer:
            if (key["buy_ticket_rows"] == buy_ticket_rows) and (key['buy_ticket_columns'] == buy_ticket_columns)):
                print("Name: ", customer['Name'])
                print("Gender: ", customer['Gender'])
                print("Age: ", customer['Age'])
                print("Phone_number: ", customer['Phone_number'])
                print("ticket_price: ", cutomer['ticket_price'])
            else:
                print("ticket is not book.")