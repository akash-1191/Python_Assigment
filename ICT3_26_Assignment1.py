#!/usr/bin/env python
# coding: utf-8

# In[1]:


# (Q1). Given a two integer numbers return their product and  if the product is greater
# than 1000, then return their sum


def Product_of_sum(a,b):
    product=a*b
    if product>1000:
        return a+b
    else:
        return product

a=int(input("Enter Frist No "))
b=int(input("enter Second no "))

result = Product_of_sum(a,b)
print("result: ",result)


# In[6]:


# Q2. Given a range of first 10 numbers, Iterate from start number to the end number
# and print the sum of the current number and previous numbe

def sum_current_previous():
    a=int(input("Input a number"))
    previous = 0
    for current in range (a):
        print(f"Current: {current}, Previous: {previous}, Sum: {current + previous}")
        previous = current

sum_current_previous()


# In[7]:


# 3. Given a string, display only those characters which are present at an even index number.

def even_index_chars(s):
    return s[0::2]

print(even_index_chars("HELLO_WORLD"))


# In[12]:


# 4. Given a list of numbers, return True if first and last number of a list is same

def first_last_same(lst):
    if len(lst) == 0:
        return False
    return lst[0] == lst[-1]


print(first_last_same([10, 20, 30, 10]))  
print(first_last_same([5, 6, 7,8,10,6])) 


# In[16]:


# 5. Given a two list. Create a third list by picking an odd-index element from the first
# list and even index elements from second.


def merge_odd_even(list1, list2):
    result = []
 
    result.extend([list1[i] for i in range(1, len(list1), 2)])
  
    result.extend([list2[i] for i in range(0, len(list2), 2)])
    return result


list1 = [10, 11, 12, 13, 14, 15]
list2 = [20, 21, 22, 23, 24, 25]
print(merge_odd_even(list1, list2))


# In[ ]:


# 6. Given an input list removes the element at index 4 and add it to the 2nd position
# and also, at the end of the list

def modify_list(lst):
    if len(lst) > 4:
        element = lst.pop(4)
        lst.insert(1, element)
        lst.append(element)
    else:
        print("Enter the at list 5 element.")
    return lst

user_input = input("Insert list element sepreter by comm: ")
input_list = [x.strip() for x in user_input.split(",")]

result = modify_list(input_list)
print("Modified list:", result)


# In[20]:



# 7. Given a list slice it into a 3 equal chunks and reverse each list

def slice_and_reverse(lst):
    n = len(lst)
    chunk_size = n // 3
    chunks = [lst[i*chunk_size:(i+1)*chunk_size] for i in range(3)]
    reversed_chunks = [chunk[::-1] for chunk in chunks]
    return reversed_chunks

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(slice_and_reverse(my_list))


# In[25]:


# 8. Given a list iterate it and count the occurrence of each element and create a
# dictionary to show the count of each element

def count_occurrences(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(count_occurrences(my_list))


# In[26]:


# 9. Add a list of elements to a given set: {‘yellow’,’orange’} List:[blue,black]

my_set = {'yellow', 'orange'}
new_elements = ['blue', 'black']

my_set.update(new_elements)

print(my_set)


# In[28]:



# 10. Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


# In[29]:


# 11. calculate the sum of all number between 1 and given number
def sum_between_1_and_n(n):
    return sum(range(1, n + 1))
print(sum_between_1_and_n(10))


# In[32]:


# 12. Given a list iterate it and display numbers which are divisible by 5 and if you find
# number greater than 150 stop the loop iteration

def display_divisible_by_5(lst):
    for num in lst:
        if num > 150:
            break
        if num % 5 == 0:
            print(num)
            
numbers = [10, 25, 33, 50, 120, 155, 5, 200]
display_divisible_by_5(numbers)


# In[3]:


# 13. Reverse the following list using for loop

List1 = [10,20,30,40]

reversed_list = []

for i in range(len(List1) - 1, -1, -1):
    reversed_list.append(List1[i])

print(reversed_list)


# In[4]:


# 14. Write a Python program to display all the prime numbers within a range


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:  # primes are greater than 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)


# In[ ]:


# 15. Write a Python program for a Car Show room that sells cars of different brans of different price.
# Consider all features of a car and develop an OOP program that has following functionalities:


import pandas as pd
import numpy as np


class Car:
    def __init__(self, car_id, brand, model, year, price, color, fuel_type, transmission):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.color = color
        self.fuel_type = fuel_type
        self.transmission = transmission

    def get_details(self):
        return {
            "Car ID": self.car_id,
            "Brand": self.brand,
            "Model": self.model,
            "Year": self.year,
            "Price": self.price,
            "Color": self.color,
            "Fuel Type": self.fuel_type,
            "Transmission": self.transmission
        }


class Showroom:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f"{car.brand} {car.model} added to the showroom.")

    def view_available_cars(self):
        if not self.inventory:
            print("No cars currently available.")
            return

        data = [car.get_details() for car in self.inventory]
        df = pd.DataFrame(data)
        print("\nAvailable Cars:")
        print(df.to_string(index=False))

    def display_car_details(self, car_id):
        found = False
        for car in self.inventory:
            if car.car_id == car_id:
                df = pd.DataFrame([car.get_details()])
                print("\nCar Details:")
                print(df.to_string(index=False))
                found = True
                break
        if not found:
            print(f"No car found with ID: {car_id}")

    def sell_car(self, car_id):
        try:
            car = next(car for car in self.inventory if car.car_id == car_id)
            self.inventory.remove(car)
            print(f"Car {car.brand} {car.model} (ID: {car_id}) sold successfully.")
        except StopIteration:
            print(f"Error: Car with ID {car_id} not found. Cannot sell.")

    def buy_car(self, brand, model, year, price, color, fuel_type, transmission):
        try:
            
            car_id = "CAR" + str(np.random.randint(1000, 9999))
            new_car = Car(car_id, brand, model, year, price, color, fuel_type, transmission)
            self.add_car(new_car)
        except Exception as e:
            print(f"Error while buying car: {str(e)}")



if __name__ == "__main__":
    showroom = Showroom()

    # Adding some cars initially
    showroom.buy_car("Toyota", "Corolla", 2022, 20000, "White", "Petrol", "Automatic")
    showroom.buy_car("Honda", "Civic", 2023, 25000, "Black", "Petrol", "Manual")
    showroom.buy_car("Tesla", "Model 3", 2024, 45000, "Red", "Electric", "Automatic")

    while True:
        print("\n===== Car Showroom Menu =====")
        print("1. View Available Cars")
        print("2. Display Details of a Car")
        print("3. Sell a Car")
        print("4. Buy a Car")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            showroom.view_available_cars()

        elif choice == "2":
            car_id = input("Enter Car ID to view details: ")
            showroom.display_car_details(car_id)

        elif choice == "3":
            car_id = input("Enter Car ID to sell: ")
            showroom.sell_car(car_id)

        elif choice == "4":
            print("Enter car details to add:")
            brand = input("Brand: ")
            model = input("Model: ")
            try:
                year = int(input("Year: "))
                price = float(input("Price: "))
            except ValueError:
                print("Invalid year or price. Please enter numeric values.")
                continue
            color = input("Color: ")
            fuel_type = input("Fuel Type: ")
            transmission = input("Transmission: ")
            showroom.buy_car(brand, model, year, price, color, fuel_type, transmission)

        elif choice == "5":
            print("Exiting showroom system.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


# In[ ]:





# In[ ]:




