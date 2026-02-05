"""
COMP 1701 Assignment 1 – Task 1
Daily Activity Estimation Module
Author: <Your Name>
"""

# ---------------------------------------------------------
# Function 1: Estimate stride length from height
# ---------------------------------------------------------
def estimate_stride_length(height_cm):
    """
    Estimate a person's stride length in meters based on their height.

    Parameter:
    height_cm (float): The user's height in centimeters.

    Returns:
    float: Estimated stride length in meters.
    """
    # Convert height from centimeters to inches
    height_inches = height_cm / 2.54

    # Estimate stride length (formula given in assignment)
    stride_length = 0.415 * height_inches

    return stride_length


# ---------------------------------------------------------
# Function 2: Calculate daily walking distance
# ---------------------------------------------------------
def calculate_daily_distance(steps, stride_length):
    """
    Calculate total daily walking distance.

    Parameters:
    steps (int): Number of steps taken in a day.
    stride_length (float): Stride length in meters.

    Returns:
    float: Total walking distance in kilometers.
    """
    # Distance in meters
    distance_meters = steps * stride_length

    # Convert meters to kilometers
    distance_km = distance_meters / 1000

    return distance_km


# ---------------------------------------------------------
# Function 3: Estimate calories burned
# ---------------------------------------------------------
def estimate_calories_burned(distance_km):
    """
    Estimate calories burned from walking.

    Parameter:
    distance_km (float): Distance walked in kilometers.

    Returns:
    float: Estimated calories burned.
    """
    calories = distance_km * 60
    return calories


# ---------------------------------------------------------
# Main function
# ---------------------------------------------------------
def main():
    """
    Main program that gathers user input, calls functions,
    and displays estimated distance and calories burned.
    """

    # Get user input
    height_cm = float(input("Enter your height in cm: "))
    steps_today = int(input("Enter your number of steps today: "))

    # Call functions in sequence
    stride_length = estimate_stride_length(height_cm)
    daily_distance = calculate_daily_distance(steps_today, stride_length)
    calories_burned = estimate_calories_burned(daily_distance)

    # Round results
    rounded_distance = round(daily_distance, 1)     # nearest tenth of a km
    rounded_calories = round(calories_burned, -1)   # nearest ten calories

    # Display results with units
    print("Estimated walking distance:", rounded_distance, "km")
    print("Estimated calories burnt throughout the day through movement:",
          rounded_calories, "calories")


# Run the program
main()


"""
Reflection Answers

A. Splitting the problem into separate functions makes the program easier to
understand, test, and maintain. Each function performs one specific task,
such as calculating stride length or distance. This modular design allows
functions to be reused in other parts of a larger system and makes it easier
to find and fix errors without affecting the entire program.

B. The round() function can round numbers to different place values depending
on its second argument. To round to the nearest tenth, we use round(value, 1),
which keeps one digit after the decimal point. To round to the nearest ten,
we use round(value, -1), where -1 tells Python to round to the tens place to
the left of the decimal.

C. This model assumes that stride length is directly proportional to height
and that each step is of equal length. It also assumes a constant walking
intensity and does not account for differences in terrain, speed, age, or
individual walking style.

D. This estimate may be inaccurate if a person is running, walking uphill,
carrying heavy loads, or has an injury that affects stride. It may also be
misleading for children, elderly individuals, or athletes whose stride
patterns differ from the average used in the formula.
"""
