print("===================================")
print(" AI CAREER GUIDANCE SYSTEM ")
print("===================================")

name = input("Enter your name: ")

print("\nWelcome,", name)

print("\nSelect your interest:")
print("1. Artificial Intelligence")
print("2. Data Science")
print("3. Software Development")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    print("Recommended Career: AI Engineer")
elif choice == "2":
    print("Recommended Career: Data Scientist")
elif choice == "3":
    print("Recommended Career: Software Developer")
else:
    print("Invalid Choice")
