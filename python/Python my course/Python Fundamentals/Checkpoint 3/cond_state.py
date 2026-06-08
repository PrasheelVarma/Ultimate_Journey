#Let's check who is the person
#Concepts-if, if else, elif, nested if and switch case
#-------------------------------------------------------------------

username=input("Hello, Your Name: ").strip().title()
role=input("Who the Hell are you ? (type Developer/ Student/ Hacker/ Unknown/ Stranger): ").strip().title()

#Level 1:using if, else, elif ->Conditional Statements
print("Authenticating through Conditional Statements")
if role=="Developer":
    print(f"Hello Dev, {username}")
elif role=="Student":
    print(f"Hello Learner, {username}")
elif role=="Hacker":
    print(f"Hey Mr.{username}")
elif role=="Hero":
    if username=="Prasheel":
        print(f"Matrix found the one, Welcome {username}!")
    else: print(f"User: {username}, This user is not the one Matrix needs")

else: #for all other user inputs including Unknown and Stranger
    print(f"Impositor found, Name:{username}, Role:{role}")

#Level 2: Using Match Case
print("Authenticating through Match Case")
print(f"Hello {username}")
match role:
    case "Developer": print(f"Hello Developer {username}")
    case "Student": print(f"Hey newbie join the cloub Mr.{username}")
    case "Hacker": print(f"Let's start the mission {username}")
    case "Hero":
        if username=="Prasheel": print(f"Matrix found the One, Welcome {username}!")
        else: print(f"User:{username}, This user is not the one Matrix searching")
    case _: #for all other users
        print(f"Impositor found: User: {username}, Role: {role}")





