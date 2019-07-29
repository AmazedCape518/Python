# Chap8ex9
# Luke De Guelle
# A program that determines the fuel efficiency

def main():
	odometer = eval(input("Enter the starting odometer: "))
	counter = 1
	cont = 1
	while(cont!= '\n')
		print("Leg number ", counter,".")
		odo = eval(input("Enter the odometer value: "))
		gas = eval(input("Enter the amount of gas in gallons used: "))
		totalLeg = (odometer - odo) / gas
		odometer = odo
		print("The miles per gallon for leg",counter,"is",totalLeg)
		counter = counter + 1
		cont = eval(input("Is there another leg?"))
main()