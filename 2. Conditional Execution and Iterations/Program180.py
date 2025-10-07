"""

A hotel offers two types of rooms: studio and apartment.
Write a program that calculates the price of the whole
stay for a studio and an apartment.
Prices depend on the month and discounts as described
in the problem statement.

"""

month = int(input('Enter Month of Stay (e.g. 1,2,3...12): '))
nights = int(input('Enter Number of Nights (up to 30):'))

if(nights > 30 or nights < 0):
    print('Invalid number of nights')
else:

            
    # Apartment discount
    if nights > 7:
        apartmentDiscount = 0.10
    else:
        apartmentDiscount = 0.0

    if month in [1, 2, 3, 4]:

        studioPrice = 50
        apartmentPrice = 60

        # Studio discounts
        if nights > 7:
            studioDiscount = 0.30
        elif nights > 3:
            studioDiscount = 0.20
        else:
            studioDiscount = 0.0

    elif month in [5, 6, 7, 8]:

        studioPrice = 70
        apartmentPrice = 80

        # Studio discounts
        if nights > 7:
            studioDiscount = 0.20
        elif nights > 3:
            studioDiscount = 0.10
        else:
            studioDiscount = 0.0

    elif month in [9, 10, 11, 12]:

        studioPrice = 80
        apartmentPrice = 90

        # Studio discounts
        if nights > 7:
            studioDiscount = 0.10
        elif nights > 3:
            studioDiscount = 0.05
        else:
            studioDiscount = 0.0

    else:
        print('Invalid month entered.')
        studioPrice = 0
        apartmentPrice = 0
        studioDiscount = 0.0
        apartmentDiscount = 0.0

    # Calculate final prices
    studioTotal = studioPrice * nights
    studioTotal = studioTotal - (studioTotal * studioDiscount)
    apartmentTotal = apartmentPrice * nights
    apartmentTotal = apartmentTotal - (apartmentTotal * apartmentDiscount)

    print(f'Studio Rent for {nights} Nights is $ {studioTotal}')
    print(f'Apartment Rent for {nights} Nights is $ {apartmentTotal}')
