print("\n                HELLO, WELCOME, ADMIN                   ")
print("\n----------------------DASHBOARD-----------------------")
drone_name=input("Drone Name: ")
charge=int(input("Charge the drone: (Enter the percentage): "))
print(f"Charging status unplugged with {charge}%")

deliver=int(input("Enter how many deliveries to be done in this single journey: ")) #Deliveries to be done
if 90<=charge<=100:
    if 0<=deliver<=10:
        print(f"Initializing, {deliver} deliveries are starting with {charge}% Battery")
    else: print("The maximun deliveries in single journey is 10 only")
elif 60<=charge<=89:
    if 0<=deliver<=5:
        print(f"Alright, {deliver} deliveries are starting with {charge}% Battery")
    else: print(f"Sorry less than 5 deliveries are only possible, for more deliveries charge the device")
elif 30<=charge<=59:
    if 0<=deliver<=3:
        print(f"ok, {deliver} deliveries are starting with {charge}% Battery")
    else: print("sorry less that 3 deliveries are only possible, for more deliveries charge the device")
else:
    print(f"Low Battery, Deliveries not possible charge now")

M=charge-20
P=charge-30
F=charge-40

print(f"Delivery Started, Select the item type:(M/P/F) ")
