import datetime

def get_greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 18:
        return "Good Afternoon!"
    elif 18 <= hour < 22:
        return "Good Evening!"
    else:
        return "Hello!"

if __name__ == "__main__":
    greeting = get_greeting()
    print(greeting)
