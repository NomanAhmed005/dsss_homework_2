import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within a specified range.

    Parameters:
    min_value (int): Minimum value for the range.
    max_value (int): Maximum value for the range.

    Returns:
    int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Select a random mathematical operator.

    Returns:
    str: A random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])

def create_problem(number1, number2, operator):
    """
    Formulate a math problem and calculate its answer.

    Parameters:
    number1 (int): The first number.
    number2 (int): The second number.
    operator (str): The operator ('+', '-', or '*').

    Returns:
    tuple: The math problem as a string and its correct answer as an integer.
    """
    problem = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:  # operator == '*'
        answer = number1 * number2
    return problem, answer

def math_quiz():
    """
    Run the Math Quiz Game, presenting math problems to the user and calculating their score.
    """
    score = 0
    total_questions = 3  # Set the number of questions for the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = create_problem(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        
        # Error handling for invalid input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue  # Skip to the next question if input is invalid

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
