print(f"\n-------TERMINAL NEO---------")
on=True
while on:
    print("\n---- WELCOME ----")
    print("S - Start Scanner")
    print("R - Results")
    print("M - Maintenance")
    print("X - Terminate the TERMINAL")

    choice = input("Select Command: ").strip().upper()
    match choice:
        case "S":
            print("\nInitializing the Scanner...")
            for scan_count in range(1,6):
                print(f"Scanning sector {scan_count}...")
            print("Scan complete.")

        case "R":
            print("\nTo view results, authenticate your identity")
            role=input("Enter your role: ")
            if role=="matrix":
                print("Results Unlocked")
            else:
                print("Sorry Accesss Denied")

        case "X":
            print("Terminal Terminated!")
            break

        case "M":
            pass

        case _:
            print("Error, Access Denied!, Don't Try Again!'")
            continue
print("Everything Ends Here!")
