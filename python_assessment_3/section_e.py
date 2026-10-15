with open("event_log.txt", "w") as file:
    file.write("Event registration processed\n")
    file.write("Booking amount calculated\n")
    file.write("Event capacity checked\n")

with open("event_log.txt", "a") as file:
    file.write("Registration confirmed\n")
    file.write("Event report generated\n")

with open("event_log.txt", "r") as file:
    print(file.read())

with open("event_log.txt", "r") as file:
    for line in file:
        print(line, end="")

