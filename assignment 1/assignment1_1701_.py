""""
COMP 1701 Assignment 1, Task 1
Daily Activity Estimation Module
Author: Robel Tadessse
"""
# Function 1/Step 1: Estimate stride length in centimeters.

def estimate_stride_length(height_cm):
    """
    Estimate a person's stride length in meters based on their height.

    Parameter:
    height_cm (float): The user's height in cm (centimeters).

    Returns:
    float: Estimated stride length in meters.
    """
    # Convert height from cm to inches
    height_inches = height_cm / 2.54

    # Estimate stride length. The formula provided by the assignment
    stride_length = 0.415 * height_inches

    return stride_length


# Calculate and define the daily distance with steps and stride length
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

    # Convert meters to km
    distance_km = distance_meters / 1000

    return distance_km



#Step 3 and 3rd function:
# Estimate the amount of calories burned

def estimate_calories_burned(distance_km):
    """
    Estimate calories burned from walking.

    Parameter:
    distance_km(float): Distance walked in kilometers.

    Returns:
    float: Estimated calories burned.
    """
    calories = distance_km * 60
    return calories

#input the functions into the main function now

def main():

#Get inputs from the user
    height_cm = float(input("Enter your height in cm:"))
steps_taken_today = int(input("Enter your number of steps taken today:"))

#Call your functions in sequence
stride_length = estimate_stride_length (height_cm=)
daily_distance = calculate_daily_distance (steps_taken_today), (stride_length)
calories_burned = estimate_calories_burned(daily_distance)

#round the results from inputs and findings, round to the nearest tenth of a kilometre, and for the calories round to the nearest ten calories as well.

rounded_distance = round (daily_distance, 1) 
rounded_calories= round (calories_burned, -1 )

#print results with the units
print ("Estimated walking distance:", rounded_distance, "km")
print ("Estimated calories burnt throughout the day through movement:", rounded_calories, "calories")

#begin running the program
main()
