# Create a function to calculate the total cost of a holiday assuming it will cost 140£ per night at a hotel. 
def hotel_cost(num_nights):
    return num_nights * 140

# Create a function to calculate the cost of a plane flight 
def plane_cost(city_flight):
    if city_flight == "Warsaw":
        return 200
    elif city_flight == "Los Angeles":
        return 600
    elif city_flight == "New York":
        return 500
    elif city_flight == "Tokyo":
        return 800
    elif city_flight == "Dubai":
        return 400
    else:
        return 0

# Create a function to calculate the cost of renting a car for a number of days assuming it will cost 60£ per day
def car_rental(rental_days):
    return rental_days * 60

# Create a function to calculate the total cost of a holiday( hotel + plane + car)
def holiday_cost(city_flight, num_nights, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# Create variables to store user input
city_flight = input("Please enter the city you would like to fly to (Warsaw, Los Angeles, New York, Tokyo, Dubai): ")
num_nights = int(input("Please enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Please enter the number of days you will be renting a car for: "))

# Calculate total holiday cost
total_holiday_cost = holiday_cost(city_flight, num_nights, rental_days)

# Print holiday details
print("Holiday Details:")
print(f"City: {city_flight}")
print(f"Hotel: {num_nights} nights")
print(f"Car rental: {rental_days} days")
print(f"Total Holiday Cost: £{total_holiday_cost}")