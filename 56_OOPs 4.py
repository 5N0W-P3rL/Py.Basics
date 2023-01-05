# Railway Ticket conservation:

nm =  input("Enter your name:")
jour = input("Enter the name of the station:")

class railway:
    def __init__(self, name, station, ticket):
        self.name = name
        self.stn = station
        self.ticket = ticket
    
    def status(self):
        print(f"No. of seats in the train: 250")
    
    def ticket(self):
        print("Ticket Price details: \n")
        print("|-------------|------------|")
        print("|    Type     |   Price    |")
        print("|     AC      |    350     |")
        print("|   Non-AC    |    250     |")
        print("|-------------|------------|")
    
    def journey(self):
        print(f"You Choose the train for {self.journey}") #& your Coach type is {self.ticket} )
    
    # @staticmethod
    def greet(self):
        print(f"Hello {self.name}")
    
passenger = railway(nm, jour) 

passenger.greet()
passenger.status()
passenger.ticket()

tkt_p = int(input("select the ticket price:"))
if tkt_p == 250:
    tkt = "Non-AC"
else:
    tkt = "AC"
        
passenger.journey()

# --> ticket price input & jouney details showing problem.