import streamlit as st

# -------------------------------
# 1. Add Two Numbers
# -------------------------------
def add_numbers(a, b):
    # Task:
    # Input: a and b are two numbers
    # Process: Add both numbers
    # Output: Return the addition result
    # Example: 10 + 5 = 15
    pass


# -------------------------------
# 2. Subtract Two Numbers
# -------------------------------
def subtract_numbers(a, b):
    # Task:
    # Input: a and b are two numbers
    # Process: Subtract b from a
    # Output: Return the subtraction result
    # Example: 10 - 5 = 5
    pass


# -------------------------------
# 3. Multiply Two Numbers
# -------------------------------
def multiply_numbers(a, b):
    # Task:
    # Input: a and b are two numbers
    # Process: Multiply both numbers
    # Output: Return the multiplication result
    # Example: 10 * 5 = 50
    pass


# -------------------------------
# 4. Divide Two Numbers
# -------------------------------
def divide_numbers(a, b):
    return a/b

# -------------------------------
# 5. Find Square of
# -----------------------------
def find_square(number):
    # Task:
    # Input: one number
    # Process: Multiply the number by itself
    # Output: Return the square value
    # Example: 4 -> 16
    return number * number


# -------------------------------
# 6. Find Cube of a Number
# -------------------------------
def find_cube(number):
    # Task:
    # Input: one number
    # Process: Multiply the number three times
    # Output: Return the cube value
    # Example: 3 -> 27
    pass


# -------------------------------
# 7. Check Even or Odd
# -------------------------------
def check_even_odd(number):
    # Task:
    # Input: one number
    # Process: Check whether the number is even or odd
    # Output: Return "Even" or "Odd"
    # Example: 6 -> Even
    # Example: 7 -> Odd
    pass


# -------------------------------
# 8. Find Bigger Number
# -------------------------------
def find_bigger_number(a, b):
    # Task:
    # Input: a and b are two numbers
    # Process: Compare both numbers
    # Output: Return the bigger number
    # Example: 10 and 20 -> 20
    pass


# -------------------------------
# 9. Convert Celsius to Fahrenheit
# -------------------------------
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# -------------------------------
# 10. Calculate Simple Interest
# -------------------------------
def calculate_simple_interest(principal, rate, time):
    si=(principal*rate*time)/100
    return si

# -------------------------------
# 11. Calculate Age
# -------------------------------
def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    return age


# -------------------------------
# 12. Create Greeting Message
# -------------------------------
def create_greeting(name):
    # Task:
    # Input: user's name
    # Process: Create a welcome message using the name
    # Output: Return greeting message
    # Example: "Dhanushree" -> "Hello Dhanushree, welcome!"
    out = "Hello" + name + ", Welcome"
    return out
    


# --------------------------------
# Streamlit UI
# --------------------------------

st.title("Beginner Python Function Tasks")
st.write("Choose one task and complete the function logic.")

task = st.selectbox(
    "Select a Task",
    [
        "1. Add Two Numbers",
        "2. Subtract Two Numbers",
        "3. Multiply Two Numbers",
        "4. Divide Two Numbers",
        "5. Find Square",
        "6. Find Cube",
        "7. Check Even or Odd",
        "8. Find Bigger Number",
        "9. Celsius to Fahrenheit",
        "10. Simple Interest",
        "11. Calculate Age",
        "12. Greeting Message"
    ]
)

# -------------------------------
# Task 1 UI
# -------------------------------
if task == "1. Add Two Numbers":
    st.subheader("Task 1: Add Two Numbers")

    a = st.number_input("Enter first number", key="add_a")
    b = st.number_input("Enter second number", key="add_b")

    if st.button("Run Task"):
        result = add_numbers(a, b)
        st.write("Output:", result)


# -------------------------------
# Task 2 UI
# -------------------------------
elif task == "2. Subtract Two Numbers":
    st.subheader("Task 2: Subtract Two Numbers")

    a = st.number_input("Enter first number", key="sub_a")
    b = st.number_input("Enter second number", key="sub_b")

    if st.button("Run Task"):
        result = subtract_numbers(a, b)
        st.write("Output:", result)


# -------------------------------
# Task 3 UI
# -------------------------------
elif task == "3. Multiply Two Numbers":
    st.subheader("Task 3: Multiply Two Numbers")

    a = st.number_input("Enter first number", key="mul_a")
    b = st.number_input("Enter second number", key="mul_b")

    if st.button("Run Task"):
        result = multiply_numbers(a, b)
        st.write("Output:", result)


# -------------------------------
# Task 4 UI
# -------------------------------
elif task == "4. Divide Two Numbers":
    st.subheader("Task 4: Divide Two Numbers")

    a = st.number_input("Enter first number", key="div_a")
    b = st.number_input("Enter second number", key="div_b")

    if st.button("Run Task"):
        result = divide_numbers(a, b)
        st.write("Output:", result)


# -------------------------------
# Task 5 UI
# -------------------------------
elif task == "5. Find Square":
    st.subheader("Task 5: Find Square")

    number = st.number_input("Enter a number", key="square_number")

    if st.button("Run Task"):
        result = find_square(number)
        st.write("Output:", result)


# -------------------------------
# Task 6 UI
# -------------------------------
elif task == "6. Find Cube":
    st.subheader("Task 6: Find Cube")

    number = st.number_input("Enter a number", key="cube_number")

    if st.button("Run Task"):
        result = find_cube(number)
        st.write("Output:", result)


# -------------------------------
# Task 7 UI
# -------------------------------
elif task == "7. Check Even or Odd":
    st.subheader("Task 7: Check Even or Odd")

    number = st.number_input("Enter a number", step=1, key="even_odd_number")

    if st.button("Run Task"):
        result = check_even_odd(number)
        st.write("Output:", result)


# -------------------------------
# Task 8 UI
# -------------------------------
elif task == "8. Find Bigger Number":
    st.subheader("Task 8: Find Bigger Number")

    a = st.number_input("Enter first number", key="big_a")
    b = st.number_input("Enter second number", key="big_b")

    if st.button("Run Task"):
        result = find_bigger_number(a, b)
        st.write("Output:", result)


# -------------------------------
# Task 9 UI
# -------------------------------
elif task == "9. Celsius to Fahrenheit":
    st.subheader("Task 9: Celsius to Fahrenheit")

    celsius = st.number_input("Enter Celsius value", key="celsius")

    if st.button("Run Task"):
        result = celsius_to_fahrenheit(celsius)
        st.write("Output:", result)


# -------------------------------
# Task 10 UI
# -------------------------------
elif task == "10. Simple Interest":
    st.subheader("Task 10: Calculate Simple Interest")

    principal = st.number_input("Enter principal amount", key="principal")
    rate = st.number_input("Enter rate of interest", key="rate")
    time = st.number_input("Enter time in years", key="time")

    if st.button("Run Task"):
        result = calculate_simple_interest(principal, rate, time)
        st.write("Output:", result)


# -------------------------------
# Task 11 UI
# -------------------------------
elif task == "11. Calculate Age":
    st.subheader("Task 11: Calculate Age")

    birth_year = st.number_input("Enter birth year", step=1, key="birth_year")
    current_year = st.number_input("Enter current year", step=1, key="current_year")

    if st.button("Run Task"):
        result = calculate_age(birth_year, current_year)
        st.write("Output:", result)


# -------------------------------
# Task 12 UI
# -------------------------------
elif task == "12. Greeting Message":
    st.subheader("Task 12: Greeting Message")

    name = st.text_input("Enter your name")

    if st.button("Run Task"):
        result = create_greeting(name)
        st.write("Output:", result)