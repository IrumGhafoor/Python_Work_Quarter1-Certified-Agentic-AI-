#Exercise 3-1: Names
#Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.

names = ['Hania', 'Rameen', 'Aisha', 'Hafsa']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#Exercise 3-2: Greetings
#Start with the list you used in Exercise 3-1, 
#but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, 
#but each message should be personalized with the person’s name.

print("Welcome to my home, "+ names[0])
print("Welcome to my home, "+ names[1])
print("Welcome to my home, " + names[2])
print("Welcome to my home, "+ names[3])

#Exercise 3-3: Your Own List
#Think of your favorite mode of transportation, such as a motorcycle or a car, 
# and make a list that stores several examples. 
# Use your list to print a series of statements about these items, 
# such as “I would like to own a Honda motorcycle.”

cars = ["Honda City", "Civic", "Prado"]
print("I would like to own a " + cars[0])
print("I would like to own a " + cars[1])
print("I would like to own a " + cars[2])

#Exercise 3-4: Guest List
#If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

guest_list = ["Taya", "Khala", "Khala 2", "Khala 3"]
print("I invite you for a dinner at our place, "+ guest_list[0])
print("I invite you for a dinner at our place, "+ guest_list[1])
print("I invite you for a dinner at our place, "+ guest_list[2])
print("I invite you for a dinner at our place, "+ guest_list[3])

#Exercise 3-5: Changing Guest List
#You just heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations.
#Start with your program from Exercise 3-4. 
#Add a print() call at the end of your program, 
#stating the name of the guest who can’t make it.
print("Oh," + guest_list[0] + " can't make it to our party tonight")
#Modify your list, replacing the name of the guest who can’t make it 
#with the name of the new person you are inviting.
guest_list[0] = "Noreen baji"
print(guest_list)
#Print a second set of invitation messages, 
# one for each person who is still in your list.
print("I invite you for a dinner at our place sans taya, "+ guest_list[0])
print("I invite you for a dinner at our place sans taya, "+ guest_list[1])
print("I invite you for a dinner at our place sans taya, "+ guest_list[2])
print("I invite you for a dinner at our place sans taya, "+ guest_list[3])

#You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. 
# Add a print() call to the end of your program, informing people 
# that you found a bigger table.
print("Guys, the party is gonna be big now as we found much bigger space" 
      + guest_list[0] + ", " + guest_list[1] + ", " + guest_list[2] + ", " + guest_list[3])
#Use insert() to add one new guest to the beginning of your list.
guest_list.insert(0, "Mehreen")
print(guest_list)
#Use insert() to add one new guest to the middle of your list.
guest_list.insert(2,"Kiran")
print(guest_list)
#Use append() to add one new guest to the end of your list.
guest_list.append("Asra")
print(guest_list)
#Print a new set of invitation messages, one for each person in your list.
print("Hello and welcome to my party "+ guest_list[0])
print("Hello and welcome to my party "+ guest_list[1])
print("Hello and welcome to my party"+ guest_list[2])
print("Hello and welcome to my party "+ guest_list[3])
print("Hello and welcome to my party, "+ guest_list[4])
print("Hello and welcome to my party "+ guest_list[5])
print("Hello and welcome to my party "+ guest_list[6])

#Exercise 3-7: Shrinking Guest List
#You just found out that your new dinner table won’t arrive in time for the dinner, 
#and now you have space for only two guests.
#Start with your program from Exercise 3-6. 
#Add a new line that prints a message saying that you can invite only two people for dinner.
print("Oh no, my dinner table will not be arriving on time. So now we can invite 2 guests only")
#Use pop() to remove guests from your list one at a time 
#until only two names remain in your list. Each time you pop a name from your list, 
#print a message to that person letting them know you’re sorry you can’t invite them to dinner.
print("I am sorry Mehreen but I have to drop you for now, " + guest_list.pop(0))
print(guest_list)
print("I am sorry Noreen baji but I have to drop you for now, " + guest_list.pop(0))
print(guest_list)
print("I am sorry Kiran but I have to drop you for now, " + guest_list.pop(0))
print(guest_list)
print("I am sorry Khala but I have to drop you for now, " + guest_list.pop(0))
print("I am sorry Khala 2 but I have to drop you for now, " + guest_list.pop(1))
print(guest_list)
#Print a message to each of the two people still on your list, letting them know they’re still invited.
print("Khala 3, you are still invited to the party though, " + guest_list[0])
print("Asra, you are still invited to the guest though, " + guest_list[1])
#Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.
del guest_list[0:]
print(guest_list)

#Exercise 3-8: Seeing the World
#Think of at least five places in the world you’d like to visit.
#Store the locations in a list. Make sure the list is not in alphabetical order.
fav_locations = ["Makkah Madinah", "Turkey", "Maldives", "Baku", "Australia"]
#Print your list in its original order. 
#Don’t worry about printing the list neatly; just print it as a raw Python list.
print(fav_locations)
#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(fav_locations))
#Show that your list is still in its original order by printing it.
print(fav_locations)
#Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
print(sorted(fav_locations, reverse=True))
#Show that your list is still in its original order by printing it again.
print(fav_locations)
#Use reverse() to change the order of your list. Print the list to show that its order has changed.
fav_locations.reverse()
print(fav_locations)
#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
fav_locations.reverse()
print(fav_locations)
#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
fav_locations.sort()
print(fav_locations)
#Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.
fav_locations.sort(reverse=True)
print(fav_locations)

#Exercise 3-9: Dinner Guests
#Working with one of the programs from Exercises 3-4 through 3-7, 
#use len() to print a message indicating the number of people you’re inviting to dinner.
print(len(guest_list))

#Exercise 3-10: Every Function
#Think of things you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, cities, languages, 
# or anything else you’d like. Write a program that creates a list containing these items 
# and then uses each function introduced in this chapter at least once.
mountains = ["Rakaposhi", "Nangaparbat", "Kalar Kahar", "K2", "Mount Everest"]
print(mountains[0])
print(mountains[1])
print(mountains[2])
print(mountains[3])
print(mountains[4])

#in reverse order
print(mountains[-1])
print(mountains[-2])
print(mountains[-3])
print(mountains[-4])
print(mountains[-5])

mountains.insert(0, "Himaliyah Mountains")
print(mountains)

mountains.append("Cho Oyu")
print(mountains)

mountains.pop(2)
print(mountains)

