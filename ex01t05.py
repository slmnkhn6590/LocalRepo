print("Welcome to our bank")
print("--"*5 + "Person 1" + "--"*5)
User_name = input("what is your name? ")
Civic_Number = input("Please enter your Civic Number: ")
Amount_of_money = int(input("How much money do you have? "))
Rate_of_interest = int(input("please enter the rate in percent per year "))
Duration_of_holding = int(input("for how long you want to keep it in years "))




# formula to calculate the interest 
Formula = Amount_of_money * (Rate_of_interest  / 100) * Duration_of_holding
Total_amount = Formula + Amount_of_money


#print all the the stored information

print("Your Information:\n"
      f"Name: {User_name}\n"
      f"Civic Number: {Civic_Number}\n"
      f"Balance: {Amount_of_money}\n"
      f"Interest rate: {Rate_of_interest}%\n"
      f"Balance after {Duration_of_holding} year will be {Total_amount} in your bank account\n"
    )
      
new_deposit = int(input("How much you want to deposit more: ")) + Total_amount
print(f"your new balance is {new_deposit}")

print("Welcome to our bank")
print("--"*5 + "Person 2" + "--"*5)
User_name = input("what is your name? ")
Civic_Number = input("Please enter your Civic Number: ")
Amount_of_money = int(input("How much money do you have? "))
Rate_of_interest = int(input("please enter the rate in percent per year "))
Duration_of_holding = int(input("for how long you want to keep it in years "))




# formula to calculate the interest 
Formula = Amount_of_money * (Rate_of_interest  / 100) * Duration_of_holding
Total_amount = Formula + Amount_of_money


#print all the the stored information

print("Your Information:\n"
      f"Name: {User_name}\n"
      f"Civic Number: {Civic_Number}\n"
      f"Balance: {Amount_of_money}\n"
      f"Interest rate: {Rate_of_interest}%\n"
      f"Balance after {Duration_of_holding} year will be {Total_amount} in your bank account\n"
    )
      
new_deposit = int(input("How much you want to deposit more: ")) + Total_amount
print(f"your new balance is {new_deposit}")