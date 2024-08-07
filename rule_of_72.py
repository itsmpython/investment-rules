
def calculate_time_taken_to_double(fixed_interest_rate):
    """ A simple formula calulate the time it takes to double an investment."""
    time_taken = 72/float(fixed_interest_rate)
    return time_taken


def main():
    # Prompt the user for the Annual Fixed interest rate
    while True:
        try:
            fixed_interest_rate = float(input("Please enter the Annual Fixed interest rate (don't use % sign): "))
            break
        except ValueError:
            print("Please enter a valid Number.")
            continue 
    # Generate the time it takes to double the investment
    time_taken_to_double = round(calculate_time_taken_to_double(fixed_interest_rate),2)
    print(f"Your investment will take {time_taken_to_double} year(s) to double!")

if __name__ == "__main__":
    main()