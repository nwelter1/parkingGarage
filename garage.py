from IPython.display import clear_output


class Garage(): 
    def __init__(self,tickets,parkingSpaces,currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
    
    def takeTicket(self):
        clear_output()
        if self.tickets == []:
            print('Sorry garage is currently full')
        else:
            self.currentTicket[self.tickets[0]] = ''
            print(f'Please take ticket {self.tickets[0]}')
            del self.tickets[0]
            del self.parkingSpaces[0]
            print(self.currentTicket)
            print(f"Available tickets {self.tickets}")
            print(f"Available spaces {self.parkingSpaces}")

    def payForParking(self):
        clear_output()
        response = int(input('Please enter your ticket number:'))
        if response < 1 or response > 10:
            print('Invalid ticket number')
        else:
            if self.currentTicket[response] == '':
                print('Please pay for your ticket...')
                payment = input('Press any key to pay..')
                self.currentTicket[response] = 'paid'
                print(self.currentTicket)
            else:
                print('You have 15 min 2 leave')
                
            
    def leaveGarage(self):
        clear_output()
        response = int(input('Please scan your ticket:'))
        if self.currentTicket[response] == 'paid':
            print('Thank you have a nice day')
            self.tickets.insert(0, response)
            self.parkingSpaces.insert(0, response)
            del self.currentTicket[response]
            print(f"Available tickets {self.tickets}")
            print(f"Available spaces {self.parkingSpaces}")
            
        else: 
            print('Please pay before exiting')
            
            
def runGarage():
    p_garage = Garage([1,2, 3, 4, 5,6,7, 8, 9, 10],[1,2, 3, 4, 5,6,7, 8, 9, 10],{})
    response = input('Welcome to Wabash Parking, would you like to park your car? Yes or No?')
    if response.lower() == 'no':
        print('Okay, have a nice day!')
    elif response.lower() == 'yes':
        p_garage.takeTicket()
    while True:
        response = input('What would you like to do? Park, Pay, Leave?')
        if response.lower() == 'park': 
            p_garage.takeTicket()
        elif response.lower() == 'pay':
            p_garage.payForParking()
        elif response.lower() == 'leave':
            p_garage.leaveGarage()
        # Usually a parking garage would run nonstop... 
        # added quit functionality for the sake of this example
        elif response.lower() == 'quit':
            break
    
runGarage()