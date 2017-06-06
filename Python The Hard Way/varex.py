cars = 100
seats = 4
drivers = 30
passengers = 90
not_used_cars = cars - drivers
cars_used = drivers
capacity = cars_used*seats
avg_ocupancy  = passengers / cars_used

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", not_used_cars, "empty cars today.")
print ("We can transport", capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", avg_ocupancy, "in each car.")
