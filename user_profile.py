profiles = {}

print ("Welcome to the user profile manager!")

while True:
    print("\nOptions: ")
    print("1. Add new profile")
    print("2. Veiw all profiles")
    print("3. exit")
    
    choice = input("choose an option (1/2/3): ")
    
    if choice == "1":
        username = input("Enter username: ")
        email = input("Enter email: ")
        age = input("enter age: ")
        
        
        profiles[username] = {
        "email" : email,
        "age" : age
    }
        
        print(f"profile for {username} added succesfully")
        
    elif choice == "2":
        if not profiles:
            print("no profiles yet")
            
        else:
            for user, details in profiles.items():
                print(f"\nUsername: {user}")
                print(f"Email: {details["email"]}")
                print(f"age: {details["age"]}")
                print ("-" * 20)
                
    elif choice == "3":
        print("Goodbye!")
        break
    
    else :
        print("invalid option")
                    
        
       