def main():
    # Get input
    answer = input("What is the time: ")
    float_time = convert(answer)
    if 7 <= float_time <= 8:
        print("breakfast time")
    elif 12 <= float_time <= 13:
        print("lunch time")
    elif 18 <= float_time <= 19:
        print("dinner time")
    else:
        print("no meal time")


# convert time to a float number
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    if minutes.endswith("p.m.") == True:
        actual_minute, format = minutes.split(" ")
        hours = (hours + 12)
        new_minutes = float(actual_minute) / 60
    elif minutes.endswith("a.m.") == True:
        actual_minute, format = minutes.split(" ")
        new_minutes = float(actual_minute) / 60
    else:
        new_minutes = float(minutes) / 60

    return hours + new_minutes


if __name__ == "__main__":
    main()
