def main():
    time = input("What time is it?: ")
    converted_time = convert(time)

    if 7.0 <= converted_time <= 8.0:
        print("Breakfast Time")
    elif  12.0 <= converted_time <= 13.0:
        print("Lunch Time")
    elif  18.0 <= converted_time <= 19.0:
        print("Dinner Time")

def convert(time):
    hour_minute = time.split(":")
    hour = float(hour_minute[0])+(float(hour_minute[1])/60)
    return hour

if __name__ == "__main__":
    main()
