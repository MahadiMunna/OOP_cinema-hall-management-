class Star_Cinema:
    __hall_list=[]
    
    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)
    @property
    def hall_list(self):
        return self.__hall_list
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        super().__init__()
        self.__seats={}
        self.__show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        self.entry_hall()
    @property
    def rows(self):
        return self.__rows    
    @property
    def cols(self):
        return self.__cols    
    @property
    def hall_no(self):
        return self.__hall_no
        
    def entry_show(self, id, movie_name, time):
        show=(id, movie_name, time)
        self.__show_list.append(show)

        self.__seats[id] = [[0 for i in range(self.__cols)] for j in range(self.__rows)]

         
    def book_seats(self, id):
        if id in self.__seats:
            total_seats_need=int(input("HOW MANY SEAT DO YOU NEED?: "))
            booked_seats=[]
            for i in range(1,total_seats_need+1):
                r=int(input(f"ENTER ROW FOR {i} NO SEAT: "))
                if r>self.__rows:
                    print(f"ENTER A VALID ROW (1 TO {self.__rows})")
                    break
                c=int(input(f"ENTER COL FOR {i} NO SEAT: "))
                if c>self.__cols:
                    print(f"ENTER A VALID COL (1 TO {self.__cols})")
                    break
                if self.__seats[id][r-1][c-1]==0:
                    self.__seats[id][r-1][c-1]=1
                    booked=(r,c)
                    booked_seats.append(booked)
                elif self.__seats[id][r-1][c-1]==1:
                    print("\n\t---->SEAT ALREADY BOOKED! TRY ANOTHER SEAT.\n")
                    break
            if len(booked_seats)!=0:
                print(f"\n\t---->SEAT {booked_seats} BOOKED FOR SHOW {id}")
        else:
            print("\n\t---->INVALID MOVIE ID!")
        

    def view_show_list(self):
        print("\n\t---->SHOW TODAY \n( ID, SHOW NAME, TIME )")
        for i in self.__show_list:
            print(i)
    
    def view_available_seats(self,id):
        if id in self.__seats:
            print("\n\t---->AVAILABLE SEATS")
            for row in self.__seats[id]:
                print(row)
        else:
            print("\n\t---->INVALID MOVIE ID!")

row=5
col=7
hall_no=11    
keya=Hall(row,col,hall_no)
keya.entry_show(111,"BATMAN","2.00 PM")
keya.entry_show(112,"IRONMAN","4.00 PM")
keya.entry_show(113,"SPIDERMAN","6.00 PM")



while True:
    op=int(input("\n\t---->MENU\n1. VIEW ALL SHOW TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. EXIT\nENTER OPTION: "))
    if op==1:
        keya.view_show_list()
    elif op==2:
        id=int(input("ENTER MOVIE ID: "))
        keya.view_available_seats(id)
    elif op==3:
        id=int(input("ENTER MOVIE ID: "))
        keya.book_seats(id)
    elif op==4:
        break
    else:
        print("\n\t---->Choose a valid option!--\n") 

    