#Question 1: Ticket Pricing System
#You are developing a ticket pricing system for a cinema. Write a Python program that:
#Asks the user for their age.
user_age = int(input("Enter your age:"))
print(user_age)
#Calculates the ticket price based on the following rules:
#Under 5 years: Free
if user_age <=5:
  print("The ticket is free")
#5 to 17 years: $10
elif user_age >=5 and user_age <=17:
  print("The ticket price is $10")
#18 to 60 years: $20
elif user_age >=18 and user_age <=60:
  print("The ticket price is $20")
#Above 60 years: $15
elif user_age >=60:
  print("The ticket price is $15")
  
#Question 2: Meal Recommendation
#Write a Python program that:
#Asks the user what time it is in 24-hour format (e.g., 13 for 1 PM, 18 for 6 PM).
time = int(input("Enter the time:"))
print(time)
#Recommends a meal based on the time:
#5 AM to 11 AM: Breakfast
if time >=5 and time <=11:
  print("Breakfast")
#12 PM to 4 PM: Lunch
elif time >=12 and time <=16:
  print("Lunch")
#5 PM to 9 PM: Dinner
elif time >=17 and time <=21:
  print("Dinner")
#10 PM to 4 AM: Late-night Snack
elif time >=22 and time <=4:
  print("Late-night Snack")
  
#Question 3: Grocery Bill Calculator
#Write a Python program that:
#Takes the price of 5 grocery items as input from the user.
item_1 = int(input("Enter the price of item1:"))
item_2 = int(input("Enter the price of item2:"))
item_3 = int(input("Enter the price of item3:"))
item_4 = int(input("Enter the price of item4:"))
item_5 = int(input("Enter the price of item5:"))
#Calculates and prints the total bill.
total_bill = item_1 + item_2 + item_3 + item_4 + item_5
print(total_bill)
#If the total bill is more than $100, it applies a 10% discount and prints the discounted total.
if total_bill >= 100:
  discount = total_bill * 10
  discounted_price = total_bill - discount
  print(f"The discounted price is {discounted_price}")
else:
  print("Try again")

#Question 4: Username Validator
#Write a Python program that:
#Asks the user to input a username.
username = input("Enter a username:")
print(username)
#Checks if the username is valid using the following rules:
#The username must be between 5 and 15 characters long.
if len(username) >=5 and len(username) <=15:
  #The username must start with a letter (A-Z or a-z).
  if username[0].isalpha:
    print("This username is valid")
else:
#Prints whether the username is valid or not.
 print("This username is not valid")
 
#Question 5: Travel Destination Suggestion
#Write a Python program that:
#Asks the user for their preferred weather (Sunny, Rainy, or Snowy).
weather = input("Enter your preferred weather:")
print(weather)
#Suggests a travel destination based on the weather:
#Sunny: "Go to the beach!"
if weather == "Sunny":
  print("Go to the beach")
#Rainy: "Visit a cozy mountain lodge!"
elif weather == "Rainy":
 print("Visit a cozy mountain lodge")
#Snowy: "Time for a ski trip!"
elif weather == "Snowy":
 print("Time for a ski trip!")
else:
  print("TRY AGAIN")
  
#Question 6: Discount Eligibility Checker
#A store is running a promotion where customers get a 15% discount if:
#They spend more than $200 or
#They are a member of the store’s loyalty program.
#Write a Python program that:
#Asks the user for the total amount spent.
total_amount_spent = float(input("Enter total amount spent:"))
print(total_amount_spent)
#Asks whether the user is a loyalty program member (Yes/No).
loyalty_program = input("Are you a loyalty program member? (Yes/No)")
print(loyalty_program)
if total_amount_spent >= 200 or loyalty_program == "No":
  print("The user is eligible for the discount")
else:
  print("the user is not eligible for the discount")
  
#You are planning an event and want to create a simple guest invitation checker.
#Write a Python program that:
#Takes a list of 5 guests who are invited to the event.
guests = ["Irum", "Kiran", "Asra", "Ami", "Abu"]
#Asks the user to enter their name.
guest_1 = input("Enter your name:")
print(guest_1)
#Prints whether the user is invited or not.
if guest_1 in guests:
  print("You are invited")
else:
  print("you are not invited!")
  
#Question 8: Movie Streaming Eligibility
#A streaming platform allows users to watch certain movies based on the following criteria:
#"Action Movies" can be watched by users aged 18 and above.
#"Animated Movies" can be watched by users of any age.
#"Documentaries" can be watched by users aged 12 and above.
#Write a Python program that:
#Asks the user for their age and
your_age = int(input("Enter your age:"))
print(your_age)
#the type of movie they want to watch.
type_of_movie = input("Type of movie:")
print(type_of_movie)
#Prints whether they are eligible to watch that type of movie.
if your_age >= 18:
  print("You are allowed to watch Action movies")
elif your_age >= 12:
  print("You can watch documentaries")
else:
  print("You can watch animated movie")
  
# Input phone number
phone_number = input("Enter a 10-digit phone number: ")

# Format and print if the input is valid
if len(phone_number) == 10 and phone_number.isdigit():
    print(f"Formatted Phone Number: ({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}")
else:
    print("Invalid input! Please enter a 10-digit number.")
    
#Question 10: Package Shipping Cost
#A shipping company charges different rates based on the weight of the package:
#Write a Python program that:
#Prints the shipping cost.
#Takes the weight of the package as input from the user.
weight = float(input("Enter the weight:"))
print(weight)
#For packages up to 1 kg, the cost is $5.
if weight == 1:
  print("The cost of the package is $5")
#For packages between 1 and 5 kg, the cost is $10.
elif weight >= 1 and weight <=5:
  print("The cost of the package is $10")
#For packages between 5 and 20 kg, the cost is $20.
elif weight <= 5 and weight >=20:
  print("The cost of the package is $20")
#For packages above 20 kg, the cost is $50.
elif weight >= 20:
  print("The cost is $50")
else:
  print("Sorry! Try again!")
  
#Question 11: Student Grading System
#You are building a simple grading system for a school. Write a Python program that:
#Asks the user to input the marks of a student in five subjects. (Each subject has a maximum of 100 marks.)
marks = 500
subject1 = int(input("Enter subject 1 marks:"))
subject2 = int(input("Enter subject 2 marks:"))
subject3 = int(input("Enter subject 3 marks:"))
subject4 = int(input("Enter subject 4 marks:"))
subject5 = int(input("Enter subject 5 marks:"))

total_marks= subject1 + subject2 + subject3 + subject4 + subject5
print(f"Total marks {total_marks}")
#Calculates the total marks and the percentage.
final_percentage = (total_marks / marks) * 100
print(f"Final Percentage is {final_percentage}")
#Prints the grade based on the following criteria:
#90% and above: Grade A
if final_percentage >= 90:
  print("Your Grade is A")
#80% to 89%: Grade B
elif final_percentage >=80 and final_percentage <=89:
  print("Your Grade is B")
#70% to 79%: Grade C
elif final_percentage >=70 and final_percentage <=79:
  print("Your Grade is C")
#60% to 69%: Grade D
elif final_percentage >=60 and final_percentage <=69:
  print("Your Grade is D")
#Below 60%: Grade F
elif final_percentage < 60:
  print("Your Grade is F")
#Prints whether the student passed or failed.
#A student is considered passed if they score 60% or more in all subjects.
if all(subject >= 60 for subject in [subject1, subject2, subject3, subject4, subject5]):
  print("You have passed the exam")
else: 
  print("You have failed the exam")