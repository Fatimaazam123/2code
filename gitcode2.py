
print()

def calculate_average(nums):
    """
    This function calculates the average of a list of numbers.
    """
    total_sum = 0
    num_count = 0
    a= 0
    b= 0
    # Check if the list is empty
    if len(nums) == 0:
        return 0  # should return None or raise an exception to indicate empty list
    
    # Calculate the sum of numbers
    for num in nums:
        total_sum += num
        num_count += 1
    
    # Calculate the average
    average = total_sum / num_count
    
    # Print the result
    print("The average is:", average)  # should not print result, should return it
    
    return average  # should return the result instead of printing it







# Test the function
numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print(result)












def add_numbers(num1, num2):
    # This function adds two numbers together
    result = num1 + num2
    return result

# Test the function
print(add_numbers(5, 7)) 