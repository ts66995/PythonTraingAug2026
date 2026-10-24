while True:   
    age = int(input("Enter your age: "))
    noOfTickets = int(input("Enter the number of tickets: "))
    if age < 0:
        print("Invalid age. Age cannot be negative.")
    elif noOfTickets <= 0:
        print("Invalid number of tickets. Please enter at least 1 ticket.")
    else:
        if age < 5:
            price = 0
        elif age <= 12:
            price = 150
        elif age <= 60:
            price = 250
        else:
            price = 180
        totalAmount = price * noOfTickets

        print("\n----- Movie Ticket Booking Details -----")
        print("Ticket price per person: Rs.", price)
        print("Number of tickets:", noOfTickets)
        print("Total amount: Rs.", totalAmount)

    # Ask whether the user wants to book again
    choice = input("\nDo you want to book again? (yes/no): ").strip().lower()

    if choice == "no":
        print("Thank you for booking!")
        break

    # .strip() is a string method that removes unwanted whitespace from the beginning and end of a string.Whitespace includes spaces, tabs (\t), and newline characters (\n).

    ''' output
    Enter your age: 12
Enter the number of tickets: 4

----- Movie Ticket Booking Details -----
Enter your age: 12
Enter the number of tickets: 4

----- Movie Ticket Booking Details -----
Ticket price per person: Rs. 150
Number of tickets: 4
Total amount: Rs. 600

Do you want to book again? (yes/no): Yes
Enter your age: 2
Enter the number of tickets: 45

----- Movie Ticket Booking Details -----
Ticket price per person: Rs. 0
Number of tickets: 45
Total amount: Rs. 0

Do you want to book again? (yes/no): yes
Enter your age: 93
Enter the number of tickets: 2

----- Movie Ticket Booking Details -----
Ticket price per person: Rs. 180
Number of tickets: 2
Total amount: Rs. 360

Do you want to book again? (yes/no): no
Thank you for booking!
    '''