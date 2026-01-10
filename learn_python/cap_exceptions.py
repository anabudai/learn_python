age_as_string = input("Please provide your age=\n")
how_many_times_youger_as_string = input("How many times younger=")

try:
    age = int(age_as_string)
    print(f"Age={age}")
    how_many_times_youger = int(how_many_times_youger_as_string)
    new_age = age//how_many_times_youger
    print(f"New age={new_age}")
except ValueError as e:
    print(f"Please provide a valid value for the age. The value {age_as_string} is not valid. Exception={e}")
except ZeroDivisionError as e:
    print("How many times younger value can't be zero")
except Exception as e:
    print(f"Error while processing user inputs. Exception={e}")

