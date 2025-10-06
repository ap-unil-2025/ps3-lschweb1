"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        # TODO: Get input from user
        # TODO: Check if user typed 'done'
        # TODO: Try to convert to float and add to list
        # TODO: Handle invalid input gracefully
        raw = input("Enter a number ('done' to finish):").strip()
        if raw.lower() == "done":
            break
        try:
            n = float(raw)
            if n.is_integer():
                n = int(n)
            numbers.append(n)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}
    analysis["count"] = len(numbers)
    analysis["sum"] = sum(numbers)
    analysis["average"] = analysis["sum"] / analysis["count"]
    analysis["minimum"] = min(numbers)
    analysis["maximum"] = max(numbers)

    # Count even and odd numbers (only for integers)
    analysis["even_count"] = sum(1 for x in numbers if isinstance(x, int) and x % 2 == 0)
    analysis["odd_count"] = sum(1 for x in numbers if isinstance(x, int) and x % 2 != 0)

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {round(analysis['average'], 2)}")
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even count: {analysis['even_count']}")
    print(f"Odd count: {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()