class Star_Cinema:
    __hall_list=[]
    
    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)



class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.__seats={}
        self.__show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        
        self.entry_hall()
        
    def entry_show(self,show_id,movie_name,time):
        show_info=(show_id,movie_name,time)
        self.__show_list.append(show_info)
        
        
        seat_arrangment=[['0' for x in range(self.__cols)] for x in range (self.__rows)]
        self.__seats[show_id]=seat_arrangment
        
    def book_seats(self,show_id,seat_list):
        if show_id not in [show[0] for show in self.__show_list]:
            print("Invalid show ID")
            return
        
        
        for seat in seat_list:
            row,col= seat
            
            if row < 0 or row >= self.__rows or col < 0  or col >= self.__cols:
                print("Invalid seat selection")
                return
            
            if self.__seats[show_id][row][col]=='1':
                print(" Seat Already Booked")
                return
            
            self.__seats[show_id][row][col]='1'
            print('Your seat is booked Now')
                
        
    def view_show_list(self):
        for show in self.__show_list:
            print(f"Show_ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")
            
    
    
    def view_available_seat(self,show_id):
        if show_id not in [show [0] for show in self.__show_list]:
            print("Invalid show ID")
            return
        
        print("Available seats: ")
        
        for row in range(self.__rows):
            for col in range(self.__cols):
                print(f'{self.__seats[show_id][row][col]}', end=' ')
            print(' ')
        


# Hall Management team Can be changes
halll=Hall(5,5,1)
halll.entry_show(1,'Prohelica','Date:25/10/2023 12:00AM')
halll.entry_show(2,'Jibon','Date:25/10/2023 1:00PM')



#Client can be used
print('1. View All Show Today')
print('2. View Available Seats')
print('3. Book Ticet')
print('4. Exit')

print('Enter Option: ')
while True:
    n=int(input())
    if n==1:
        halll.view_show_list()
    
    elif n==2:
        
        halll.view_available_seat(int(input('Show ID: ')))
    
    elif n==3:
        halll.book_seats(int(input("Show ID: ")),[(int(input('Row: ')),int(input('Col: ')))])
    else:
        break
