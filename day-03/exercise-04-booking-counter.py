"""
Exercise: Shared Booking Counter
Student: Ayush Rayamajhi
Day: 3
"""

total_seats_booked = 0


def book_seats(n):
    global total_seats_booked

    total_seats_booked += n

    print(
        f"Booked {n} seat(s). "
        f"Total booked so far: {total_seats_booked}"
    )


def reset_bookings():
    global total_seats_booked

    total_seats_booked = 0


# Test cases
book_seats(3)
book_seats(5)

reset_bookings()

book_seats(2)