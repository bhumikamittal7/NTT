def synthetic_division(dividend, divisor):
    #reverse the list of dividend
    dividend.reverse()
    # Ensure both dividend and divisor are lists
    if not isinstance(dividend, list) or not isinstance(divisor, list):
        raise ValueError("Both dividend and divisor must be lists")

    # Ensure both dividend and divisor have numerical elements
    if not all(isinstance(x, (int, float)) for x in dividend) or not all(isinstance(x, (int, float)) for x in divisor):
        raise ValueError("Both dividend and divisor must contain numerical elements")

    # Ensure divisor is not an empty list
    if not divisor:
        raise ValueError("Divisor list cannot be empty")

    # Ensure the degree of the divisor is less than or equal to the degree of the dividend
    if len(divisor) > len(dividend):
        raise ValueError("Degree of divisor must be less than or equal to the degree of dividend")

    # Copy the dividend to avoid modifying the original list
    result = list(dividend)

    # Perform synthetic division
    for i in range(len(dividend) - len(divisor) + 1):
        # Calculate the factor for division
        factor = result[i] // divisor[0]

        # Update the result list
        for j in range(1, len(divisor)):
            result[i + j] -= factor * divisor[j]

    # Return the quotient and remainder
    # quotient = result[:-len(divisor) + 1]
    remainder = result[-len(divisor) + 1:]
    return remainder

# Example usage:
dividend = [1, 4, 7, 11, 10, 3, 4]
# dividend = [4, 3, 10, 11, 7, 4, 1]
divisor = [1, 0, 0, 1]  # Represents x^3 + 1
remainder = synthetic_division(dividend, divisor)
print("Remainder:", remainder)
