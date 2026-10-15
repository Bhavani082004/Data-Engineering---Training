class Event:
    def __init__(self, event_id, event_name, capacity, ticket_price):
        self.event_id = event_id
        self.event_name = event_name
        self.capacity = capacity
        self.ticket_price = ticket_price

    def display_event(self):
        print("Event ID:", self.event_id)
        print("Event Name:", self.event_name)
        print("Capacity:", self.capacity)
        print("Ticket Price:", self.ticket_price)

    def calculate_revenue(self, tickets_sold):
        return tickets_sold * self.ticket_price


class OnlineEvent(Event):
    def __init__(self, event_id, event_name, capacity, ticket_price, platform):
        super().__init__(event_id, event_name, capacity, ticket_price)
        self.platform = platform

    def display_event(self):
        super().display_event()
        print("Platform:", self.platform)


class PhysicalEvent(Event):
    def __init__(self, event_id, event_name, capacity, ticket_price, venue):
        super().__init__(event_id, event_name, capacity, ticket_price)
        self.venue = venue

    def display_event(self):
        super().display_event()
        print("Venue:", self.venue)


event1 = Event("E101", "AI Innovation Summit", 500, 2500)
event2 = Event("E102", "Leadership Forum", 350, 1500)

online_event = OnlineEvent("E103", "Python Workshop", 200, 1000, "Zoom")
physical_event = PhysicalEvent("E104", "Startup Connect", 300, 2000, "Chennai Trade Centre")

print("Event 1")
event1.display_event()
print("Revenue:", event1.calculate_revenue(100))

print("\nEvent 2")
event2.display_event()
print("Revenue:", event2.calculate_revenue(50))

events = [online_event, physical_event]

for event in events:
    print("\nEvent Details")
    event.display_event()

