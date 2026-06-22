print("===================================")
print(" AI CAREER GUIDANCE SYSTEM ")
print("===================================")

name = input("Enter your name: ")

print("\nWelcome,", name)

print("\nWhat do you enjoy most?")
print("1. Building AI models")
print("2. Working with data")
print("3. Creating software applications")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    print("\nRecommended Career:")
    print("- AI Engineer")
    print("- Machine Learning Engineer")

elif choice == "2":
    print("\nRecommended Career:")
    print("- Data Scientist")
    print("- Data Analyst")

elif choice == "3":
    print("\nRecommended Career:")
    print("- Software Developer")
    print("- Full Stack Developer")

else:
    print("\nInvalid choice. Please try again.")
