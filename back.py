class Event:
    def __init__(self, name, date, venue):
        self.name = name
        self.date = date
        self.venue = venue
        self.attendees = []

    def add_attendee(self, attendee):
        self.attendees.append(attendee)

    def get_details(self):
        print("Event: ", self.name)
        print("Date: ", self.date)
        print("Venue: ", self.venue)
        print("Attendees:")
        for attendee in self.attendees:
            print("-", attendee)


def main():
    print('Welcome To Database')
ch=input('Press Y to continue_')
flag=0
while flag==0:
    if ch=='Y' or ch=='y':
        print('Please Login')
        user1=input('enter your username')
        pass2=input('enter your password')
        print('Signing in..')
        print("Connecting to database... ... SUCCESSFULLY CONNECTED!")
    events = []

    while True:
        print("\n--- Dream Events ---")
        print("1. Book Event")
        print("2. Add Attendee to Event")
        print("3. Display Event Details")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            venue = input("Enter event venue: ")

            event = Event(name, date, venue)
            events.append(event)
            print("Event and venue booked sucessfully!")

        elif choice == "2":
            if len(events) == 0:
                print("No events created yet!")
                continue

            print("--- Events ---")
            for i, event in enumerate(events):
                print(i + 1, ". ", event.name)

            event_choice = int(input("Enter event number: ")) - 1
            if event_choice < 0 or event_choice >= len(events):
                print("Invalid event number!")
                continue

            event = events[event_choice]
            attendee = input("Enter attendee name: ")
            event.add_attendee(attendee)
            print("Attendee added successfully!")

        elif choice == "3":
            if len(events) == 0:
                print("No events created yet!")
                continue

            print("--- Events ---")
            for i, event in enumerate(events):
                print(i + 1, ". ", event.name, event.date, event.venue)

            event_choice = int(input("Enter event number: ")) - 1
            if event_choice < 0 or event_choice >= len(events):
                print("Invalid event number!")
                continue

            event = events[event_choice]
            event.get_details()

        elif choice == "4":
            print("Exiting the Event Management System...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
