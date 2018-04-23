# Command line-driven calendar program.  Allows you to do the following:
# View the calendar
# Add an event to the calendar
# Update or Delete an existing event

from time import sleep, strftime

NAME = "Roy"
calendar = {}

def welcome():
  print("Welcome %s" % NAME)
  print("Opening your calendar...")
  sleep(1)
  print("Current day: " + strftime("%A %B %d, %Y"))
  print("Current time: " + strftime("%H:%M:%S"))
  sleep(1)
  print("What would you like to do?")

def start_calendar():
  welcome()
  start = True
  while start is True:
    def invalid(thing):
      print("Invalid %s." % thing)
      try_again = ""
      while try_again != "Y" and try_again != "N":
        try_again = (raw_input("Try Again? Y for Yes, N for No: ")).upper()
      else:
        if try_again == "Y":
          start_calendar()
        elif try_again == "N":
          start = False

    user_choice = (raw_input("A to Add, U to Update, V to View, D to Delete, X to eXit: ")).upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print("Your calendar is empty.")
      else:
        print(calendar)
    elif user_choice == "U":
      date = raw_input("Which date would you like to update? (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:10]) < int(strftime("%Y")):
        invalid("date")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print("Update successful.")
      print(calendar)
    elif user_choice == "A":
      event = raw_input("Enter the event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) != 10 or int(date[6:10]) < int(strftime("%Y")):
        print int(date[6:10])
        invalid("date")
      else:
        calendar[date] = event
        print("Event successfully added.")
        print calendar
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print("Your calendar is empty.")
      else:
        event = raw_input("Which event would you like to delete? ")
        for date in calendar.keys():
          if event == calendar[date]:
            sure = ""
            while sure != "Y" or sure != "N":
              sure = (raw_input("Are you sure you would like to delete %s? Y for Yes or N for No:" % event)).upper()
              if sure == "Y":
                del(calendar[date])
                print("%s successfully deleted." % event)
              elif sure == "N":
                continue
          else:
            invalid("entry")
    elif user_choice == "X":
      start = False
    else:
      invalid("entry")

start_calendar()