def hello(user_name):
    print(f"Hi, {user_name}. How are you today?")

def pack(arg_0, arg_1, arg_2):
    return [arg_0, arg_1, arg_2]

def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty")
    else:
        for index in range(len(lunch_items)):
            if index == 0:
                print(f"First I eat {lunch_items[index]}")
            else:
                print(f"Then I eat {lunch_items[index]}")

hello("Samantha Marie")
print(pack("apples", "bananas", "peanut butter"))
eat_lunch(pack("apples", "bananas", "peanut butter"))