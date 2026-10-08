#Section 1
name = "Mario"
birth_year = 1996
height = 6.0
is_student = True
print(name, type(name))
print(birth_year, type(birth_year))
print(height, type(height))
print(is_student, type(is_student))
print("=" * 50)
print("=" * 50)

#Section 2
first_name = input("Enter your name ").capitalize()
birth_year = int(input("Enter birth year "))
age = 2026 - birth_year
print("Hi, " + first_name +"! You are approximately "+ str(age) + " years old.")
print("=" * 50)
print("=" * 50)

#Section 3
first_num = float(input("Please enter your first number "))
second_num = float(input("Enter your second number "))
result = first_num * second_num
print(f"{first_num} * {second_num} = {result}")
print("=" * 50)
print("=" * 50)


#Section 4
item = "Wheel"
price = 149.99
quantity = 4
total = float(price * quantity)
print("=" * 30)
print("            Receipt")
print("=" * 30)
print("Item:     ",item)
print(f"Price:     {price:.2f}")
print("Quantity: ",quantity)
print("-" * 30)
print(f"Total:     {total:.2f}")
print("=" * 30)
print("=" * 50)
print("=" * 50)

#Section 5
name = input("What is your name: ").capitalize()
last_name = input("What is your last name: ").capitalize()
hometown = input("Where is your hometown: ").capitalize()
hobby = input("Enter your hobby: ").capitalize()
fun_fact = input("Tell us a fun fact about yourself: ").capitalize()
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year
print("=" * 30)
print(f"    PROFILE: {name} {last_name}")
print("=" * 30)
print("Hometown: ",hometown)
print("Hobby:    ",hobby)
print("Fun Fact: ",fun_fact)
print("Age:      ",age)
print("=" * 30)
