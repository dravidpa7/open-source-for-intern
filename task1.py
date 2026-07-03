import streamlit as st

# ==================================================
# NEXT LEVEL STREAMLIT FUNCTION TASKS
# Students must complete only the logic inside function
# ==================================================


# -------------------------------
# 1. Calculate Total Marks
# -------------------------------
def calculate_total_marks(mark1, mark2, mark3):
    # Task:
    # Input: 3 subject marks
    # Process: Add all 3 marks
    # Output: Return total marks
    # Example:
    # mark1 = 80, mark2 = 70, mark3 = 90
    # Output: 240
    pass


# -------------------------------
# 2. Calculate Average Marks
# -------------------------------
def calculate_average_marks(mark1, mark2, mark3):
    # Task:
    # Input: 3 subject marks
    # Process: Add all marks and divide by 3
    # Output: Return average mark
    # Example:
    # 80, 70, 90 -> 80
    pass


# -------------------------------
# 3. Check Pass or Fail
# -------------------------------
def check_pass_fail(mark):
    if mark >= 35 :
        return "pass"
    else :
        return "fail"
 
    

# -------------------------------
# 4. Find Grade
# -------------------------------
def find_grade(average):
  
    if average >= 90:
        return "A Grade"
    elif average >= 75:
        return "B Grade"
    elif average >= 50:
        return "C Grade"
    elif average >= 35:
        return "D Grade"
    else:
        return "Fail"


# -------------------------------
# 5. Calculate Electricity Bill
# -------------------------------
def calculate_electricity_bill(units):
    # Task:
    # Input: number of electricity units used
    # Process:
    # If units <= 100, bill = units * 2
    # If units > 100, bill = units * 5
    # Output: Return total bill amount
    # Example:
    # units = 80 -> 160
    # units = 150 -> 750
    pass


# -------------------------------
# 6. Calculate Discount Price
# -------------------------------
def calculate_discount_price(price):
    # Task:
    # Input: product price
    # Process:
    # If price is above 1000, give 10% discount
    # Otherwise no discount
    # Output: Return final price after discount
    # Example:
    # price = 2000 -> 1800
    # price = 500 -> 500
    pass


# -------------------------------
# 7. Check Voting Eligibility
# -------------------------------
def check_voting_eligibility(age):
    # Task:
    # Input: person's age
    # Process:
    # If age is 18 or above, eligible to vote
    # Otherwise not eligible
    # Output: Return message
    # Example:
    # 20 -> "Eligible to vote"
    # 15 -> "Not eligible to vote"
    pass


# -------------------------------
# 8. Create Username
# -------------------------------
def create_username(first_name, birth_year):
    # Task:
    # Input:
    # first_name = user's first name
    # birth_year = user's birth year
    # Process:
    # Join name and birth year together
    # Output: Return username
    # Example:
    # first_name = "dhanush"
    # birth_year = 2005
    # Output: dhanush2005
    pass


# -------------------------------
# 9. Find Length of Name
# -------------------------------
def find_name_length(name):
   a=len(name)
   return a


# -------------------------------
# 10. Convert Minutes to Hours
# -------------------------------
def convert_minutes_to_hours(minutes):
    hours=minutes/60
    return hours


# -------------------------------
# 11. Calculate BMI
# -------------------------------
def calculate_bmi(weight, height):
    return weight/(height*height)


# -------------------------------
# 12. Check Positive, Negative, or Zero
# -------------------------------
def check_number_type(number):
    # Task:
    # Input: one number
    # Process:
    # If number > 0, it is Positive
    # If number < 0, it is Negative
    # If number == 0, it is Zero
    # Output: Return "Positive", "Negative", or "Zero"
    # Example:
    # 10 -> Positive
    # -5 -> Negative
    # 0 -> Zero
    pass


# ==================================================
# Streamlit UI
# ==================================================

st.title("Next Level Python Function Tasks")
st.write("Choose a task and complete the function logic.")


task = st.selectbox(
    "Select a Task",
    [
        "1. Calculate Total Marks",
        "2. Calculate Average Marks",
        "3. Check Pass or Fail",
        "4. Find Grade",
        "5. Electricity Bill",
        "6. Discount Price",
        "7. Voting Eligibility",
        "8. Create Username",
        "9. Find Name Length",
        "10. Minutes to Hours",
        "11. Calculate BMI",
        "12. Positive Negative Zero"
    ]
)


# -------------------------------
# Task 1 UI
# -------------------------------
if task == "1. Calculate Total Marks":
    st.subheader("Task 1: Calculate Total Marks")

    mark1 = st.number_input("Enter mark 1", key="total_mark1")
    mark2 = st.number_input("Enter mark 2", key="total_mark2")
    mark3 = st.number_input("Enter mark 3", key="total_mark3")

    if st.button("Run Task"):
        result = calculate_total_marks(mark1, mark2, mark3)
        st.write("Output:", result)


# -------------------------------
# Task 2 UI
# -------------------------------
elif task == "2. Calculate Average Marks":
    st.subheader("Task 2: Calculate Average Marks")

    mark1 = st.number_input("Enter mark 1", key="avg_mark1")
    mark2 = st.number_input("Enter mark 2", key="avg_mark2")
    mark3 = st.number_input("Enter mark 3", key="avg_mark3")

    if st.button("Run Task"):
        result = calculate_average_marks(mark1, mark2, mark3)
        st.write("Output:", result)


# -------------------------------
# Task 3 UI
# -------------------------------
elif task == "3. Check Pass or Fail":
    st.subheader("Task 3: Check Pass or Fail")

    mark = st.number_input("Enter mark", key="pass_fail_mark")

    if st.button("Run Task"):
        result = check_pass_fail(mark)
        st.write("Output:", result)


# -------------------------------
# Task 4 UI
# -------------------------------
elif task == "4. Find Grade":
    st.subheader("Task 4: Find Grade")

    average = st.number_input("Enter average mark", key="grade_average")

    if st.button("Run Task"):
        result = find_grade(average)
        st.write("Output:", result)


# -------------------------------
# Task 5 UI
# -------------------------------
elif task == "5. Electricity Bill":
    st.subheader("Task 5: Calculate Electricity Bill")

    units = st.number_input("Enter electricity units", key="units")

    if st.button("Run Task"):
        result = calculate_electricity_bill(units)
        st.write("Output:", result)


# -------------------------------
# Task 6 UI
# -------------------------------
elif task == "6. Discount Price":
    st.subheader("Task 6: Calculate Discount Price")

    price = st.number_input("Enter product price", key="price")

    if st.button("Run Task"):
        result = calculate_discount_price(price)
        st.write("Output:", result)


# -------------------------------
# Task 7 UI
# -------------------------------
elif task == "7. Voting Eligibility":
    st.subheader("Task 7: Check Voting Eligibility")

    age = st.number_input("Enter age", step=1, key="age")

    if st.button("Run Task"):
        result = check_voting_eligibility(age)
        st.write("Output:", result)


# -------------------------------
# Task 8 UI
# -------------------------------
elif task == "8. Create Username":
    st.subheader("Task 8: Create Username")

    first_name = st.text_input("Enter first name")
    birth_year = st.number_input("Enter birth year", step=1, key="birth_year_username")

    if st.button("Run Task"):
        result = create_username(first_name, birth_year)
        st.write("Output:", result)


# -------------------------------
# Task 9 UI
# -------------------------------
elif task == "9. Find Name Length":
    st.subheader("Task 9: Find Name Length")

    name = st.text_input("Enter name")

    if st.button("Run Task"):
        result = find_name_length(name)
        st.write("Output:", result)


# -------------------------------
# Task 10 UI
# -------------------------------
elif task == "10. Minutes to Hours":
    st.subheader("Task 10: Convert Minutes to Hours")

    minutes = st.number_input("Enter minutes", key="minutes")

    if st.button("Run Task"):
        result = convert_minutes_to_hours(minutes)
        st.write("Output:", result)


# -------------------------------
# Task 11 UI
# -------------------------------
elif task == "11. Calculate BMI":
    st.subheader("Task 11: Calculate BMI")

    weight = st.number_input("Enter weight in kg", key="weight")
    height = st.number_input("Enter height in meters", key="height")

    if st.button("Run Task"):
        result = calculate_bmi(weight, height)
        st.write("Output:", result)


# -------------------------------
# Task 12 UI
# -------------------------------
elif task == "12. Positive Negative Zero":
    st.subheader("Task 12: Check Number Type")

    number = st.number_input("Enter a number", key="number_type")

    if st.button("Run Task"):
        result = check_number_type(number)
        st.write("Output:", result)