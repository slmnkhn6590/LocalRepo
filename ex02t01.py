total_credits = 1000
print(f"You have  {total_credits} in your bank account(only 100 SEK bills available)\n")
withdrawl = int(input("How much you want to withdraw "))

if withdrawl > total_credits:
    print("it is locked please work hard to unlock it")
elif total_credits % withdrawl == 0:
    print("Enjoy have a nice day")
else:
    if total_credits % withdrawl != 0:
        print("other then 100 sek bills is not available sorry")