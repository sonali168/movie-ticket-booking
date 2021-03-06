from buy_ticket import Movie
from showseats import Seats
#from statf import Statfunction
#from info import Bookinfo

global main_rows
global main_columns

main_rows = int(input("Enter the numbers of rows:"))
while main_rows < 1 or main_rows > 10:
    print("Kindly enter numbers of rows between 1 to 10")
    main_rows = int(input("Enter the numbers of rows:"))

main_columns = int(input("Enter the numbers of columns:"))
while main_columns < 1 or main_columns > 10:
    print("Kindly enter numbers of rows between 1 to 10")
    main_columns = int(input("Enter the numbers of columns:"))


def opt():
    print("1.Show the seats")
    print("2.Buy a ticket")
    print("3.Statistics")
    print("4.Show booked Tickets User Info")
    print("0.Exit")


opt()
choice = int(input("Kindly enter options between 0,1,2,3,4:"))
while choice < 0 or choice > 4:
    print("Kindly enter options between 1,2,3,4,0")
    choice = int(input("Kindly enter options between 1,2,3,4,0:"))

obj = Movie(main_rows, main_columns)
st = Seats(main_rows, main_columns)
#stats = Statfunction(main_rows, main_columns)
#user = Bookinfo(main_rows, main_columns)

while choice != 0:
    if choice == 2:
        obj.buy_ticket(main_rows, main_columns)
        opt()
        choice = int(input("Kindly enter options between 0,1,2,3,4:"))
        while choice < 0 or choice > 4:
            print("Kindly enter options between 1,2,3,4,0")
            choice = int(input("Kindly enter options between 1,2,3,4,0:"))

    elif choice == 1:
        st.show_seats(main_rows, main_columns)
        opt()
        choice = int(input("Kindly enter options between 0,1,2,3,4:"))
        while choice < 0 or choice > 4:
            print("Kindly enter options between 1,2,3,4,0")
            choice = int(input("Kindly enter options between 1,2,3,4,0:"))

    #elif choice == 3:
     #   stats.statistics(main_rows,main_columns)
      #  opt()
       # choice = int(input("Kindly enter options between 0,1,2,3,4:"))
        #while choice < 0 or choice > 4:
         #   print("Kindly enter options between 1,2,3,4,0")
          #  choice = int(input("Kindly enter options between 1,2,3,4,0:"))

    #elif choice == 4:
     #   user.user_info(main_rows,main_columns)
      #  opt()
       # choice = int(input("Kindly enter options between 0,1,2,3,4:"))
        #while choice < 0 or choice > 4:
         #   print("Kindly enter options between 1,2,3,4,0")
          #  choice = int(input("Kindly enter options between 1,2,3,4,0:"))

    elif choice == 0:
        print("End")









#    except ValueError:
#        print("please don't enter any alphabets")

# obj = Movie()
# if choice == 1:
#    obj.show_seats(main_rows, main_columns)

#if choice == 2:
#    obj.buy_ticket(main_rows, main_columns)
#elif choice == 1:
#    st.show_seats(main_rows, main_columns)
#else:
#    print("End")