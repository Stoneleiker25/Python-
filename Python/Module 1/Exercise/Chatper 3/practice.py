print("How many you eat apples?")
print()

more_test = "Y"


while more_test.lower() == "y":
    print("Enter applles")
    print("Enter 'end' to end input")

    counter = 0
    apple_total = 0
    eat_apple = 0

    while (eat_apple := input("How many you eat apples?").lower()) != "end":
        eat_apple = int(eat_apple)
        if eat_apple >=0 and eat_apple <= 10:
                apple_total += eat_apple
                counter += 1
        else:
                print(f"Apple must be from 0 thorugh 10. "
                      f"Apple disbcarded, Try again.")
    average_apple = round(apple_total / counter)
    print(f"Total Apple: {apple_total}"
        f"\nAverage Score: {average_apple}")
    more_apples = input("Enter another set of apple (y/n? ")

print("Bye!")
          
                
