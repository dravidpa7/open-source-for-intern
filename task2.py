import streamlit as st

# ==================================================
# LEVEL 3 STREAMLIT FUNCTION TASKS
# Topic: Lists, Loops, Conditions, Strings
# Students must complete only the logic inside each function
# ==================================================


# -------------------------------
# 1. Find Total from List
# -------------------------------
def find_total(numbers):
    # Task:
    # Input: numbers is a list of numbers
    # Process: Add all numbers in the list using loop
    # Output: Return total value
    # Example:
    # numbers = [10, 20, 30]
    # Output: 60
    pass


# -------------------------------
# 2. Find Average from List
# -------------------------------
def find_average(numbers):
    # Task:
    # Input: numbers is a list of numbers
    # Process:
    # Add all numbers
    # Divide total by number of items
    # Output: Return average value
    # Example:
    # numbers = [10, 20, 30]
    # Output: 20
    pass


# -------------------------------
# 3. Find Biggest Number from List
# -------------------------------
def find_biggest_number(numbers):
    # Task:
    # Input: numbers is a list of numbers
    # Process: Compare each number and find the biggest number
    # Output: Return biggest number
    # Example:
    # numbers = [5, 10, 3, 25]
    # Output: 25
    pass


# -------------------------------
# 4. Find Smallest Number from List
# -------------------------------
def find_smallest_number(numbers):
    # Task:
    # Input: numbers is a list of numbers
    # Process: Compare each number and find the smallest number
    # Output: Return smallest number
    # Example:
    # numbers = [5, 10, 3, 25]
    # Output: 3
    pass


# -------------------------------
# 5. Count Even Numbers
# -------------------------------
def count_even_numbers(numbers):
    # Task:
    # Input: numbers is a list of numbers
    # Process:
    # Check each number
    # Count how many numbers are even
    # Output: Return even number count
    # Example:
    # numbers = [1, 2, 3, 4, 6]
    # Output: 3
    pass


# -------------------------------
# 6. Count Odd Numbers
# -------------------------------
def count_odd_numbers(numbers):
    # Task:
    # Input: numbers is a list of numbers
    # Process:
    # Check each number
    # Count how many numbers are odd
    # Output: Return odd number count
    # Example:
    # numbers = [1, 2, 3, 4, 6]
    # Output: 2
    pass


# -------------------------------
# 7. Search Name in List
# -------------------------------
def search_name(names, search_value):
    # Task:
    # Input:
    # names = list of student names
    # search_value = name to search
    # Process:
    # Check whether search_value is available in names list
    # Output:
    # Return "Found" if name exists
    # Return "Not Found" if name does not exist
    # Example:
    # names = ["Ravi", "Kumar", "Anu"]
    # search_value = "Anu"
    # Output: Found
    pass


# -------------------------------
# 8. Count Passed Students
# -------------------------------
def count_passed_students(marks):
    # Task:
    # Input: marks is a list of student marks
    # Process:
    # Check each mark
    # If mark is 35 or above, count as pass
    # Output: Return pass count
    # Example:
    # marks = [80, 20, 45, 30, 90]
    # Output: 3
    pass


# -------------------------------
# 9. Count Failed Students
# -------------------------------
def count_failed_students(marks):
    fail_count = 0

    for mark in marks:
        if mark < 35:
            fail_count += 1

    return fail_count



# -------------------------------
# 10. Count Vowels in Name
# -------------------------------
def count_vowels(text):
    # Task:
    # Input: text is a word or sentence
    # Process:
    # Check each character
    # Count vowels: a, e, i, o, u
    # Output: Return vowel count
    # Example:
    # text = "apple"
    # Output: 2
    pass


# -------------------------------
# 11. Reverse Text
# -------------------------------
def reverse_text(text):
    # Task:
    # Input: text is a word or sentence
    # Process:
    # Reverse the text
    # Output: Return reversed text
    # Example:
    # text = "python"
    # Output: "nohtyp"
    pass


# -------------------------------
# 12. Check Login
# -------------------------------
def check_login(username, password):
    # Task:
    # Input:
    # username = entered username
    # password = entered password
    # Process:
    # Check username and password
    # Correct username: admin
    # Correct password: 1234
    # Output:
    # Return "Login Success" if both are correct
    # Return "Invalid Login" if username or password is wrong
    # Example:
    # username = "admin"
    # password = "1234"
    # Output: Login Success
    pass


# ==================================================
# Streamlit UI
# ==================================================

st.title("Level 3 Python Function Tasks")
st.write("Topic: Lists, Loops, Conditions, and Strings")

task = st.selectbox(
    "Select a Task",
    [
        "1. Find Total from List",
        "2. Find Average from List",
        "3. Find Biggest Number",
        "4. Find Smallest Number",
        "5. Count Even Numbers",
        "6. Count Odd Numbers",
        "7. Search Name",
        "8. Count Passed Students",
        "9. Count Failed Students",
        "10. Count Vowels",
        "11. Reverse Text",
        "12. Check Login"
    ]
)


# Helper UI idea:
# For list input, students can enter values separated by comma.
# Example: 10,20,30,40


# -------------------------------
# Task 1 UI
# -------------------------------
if task == "1. Find Total from List":
    st.subheader("Task 1: Find Total from List")

    user_input = st.text_input("Enter numbers separated by comma", "10,20,30")

    if st.button("Run Task"):
        numbers = [int(num) for num in user_input.split(",")]
        result = find_total(numbers)
        st.write("Output:", result)


# -------------------------------
# Task 2 UI
# -------------------------------
elif task == "2. Find Average from List":
    st.subheader("Task 2: Find Average from List")

    user_input = st.text_input("Enter numbers separated by comma", "10,20,30")

    if st.button("Run Task"):
        numbers = [int(num) for num in user_input.split(",")]
        result = find_average(numbers)
        st.write("Output:", result)


# -------------------------------
# Task 3 UI
# -------------------------------
elif task == "3. Find Biggest Number":
    st.subheader("Task 3: Find Biggest Number")

    user_input = st.text_input("Enter numbers separated by comma", "5,10,3,25")

    if st.button("Run Task"):
        numbers = [int(num) for num in user_input.split(",")]
        result = find_biggest_number(numbers)
        st.write("Output:", result)


# -------------------------------
# Task 4 UI
# -------------------------------
elif task == "4. Find Smallest Number":
    st.subheader("Task 4: Find Smallest Number")

    user_input = st.text_input("Enter numbers separated by comma", "5,10,3,25")

    if st.button("Run Task"):
        numbers = [int(num) for num in user_input.split(",")]
        result = find_smallest_number(numbers)
        st.write("Output:", result)


# -------------------------------
# Task 5 UI
# -------------------------------
elif task == "5. Count Even Numbers":
    st.subheader("Task 5: Count Even Numbers")

    user_input = st.text_input("Enter numbers separated by comma", "1,2,3,4,6")

    if st.button("Run Task"):
        numbers = [int(num) for num in user_input.split(",")]
        result = count_even_numbers(numbers)
        st.write("Output:", result)


# -------------------------------
# Task 6 UI
# -------------------------------
elif task == "6. Count Odd Numbers":
    st.subheader("Task 6: Count Odd Numbers")

    user_input = st.text_input("Enter numbers separated by comma", "1,2,3,4,6")

    if st.button("Run Task"):
        numbers = [int(num) for num in user_input.split(",")]
        result = count_odd_numbers(numbers)
        st.write("Output:", result)


# -------------------------------
# Task 7 UI
# -------------------------------
elif task == "7. Search Name":
    st.subheader("Task 7: Search Name in List")

    names_input = st.text_input("Enter names separated by comma", "Ravi,Kumar,Anu")
    search_value = st.text_input("Enter name to search", "Anu")

    if st.button("Run Task"):
        names = names_input.split(",")
        result = search_name(names, search_value)
        st.write("Output:", result)


# -------------------------------
# Task 8 UI
# -------------------------------
elif task == "8. Count Passed Students":
    st.subheader("Task 8: Count Passed Students")

    user_input = st.text_input("Enter marks separated by comma", "80,20,45,30,90")

    if st.button("Run Task"):
        marks = [int(mark) for mark in user_input.split(",")]
        result = count_passed_students(marks)
        st.write("Output:", result)


# -------------------------------
# Task 9 UI
# -------------------------------
elif task == "9. Count Failed Students":
    st.subheader("Task 9: Count Failed Students")

    user_input = st.text_input("Enter marks separated by comma", "80,20,45,30,90")

    if st.button("Run Task"):
        marks = [int(mark) for mark in user_input.split(",")]
        result = count_failed_students(marks)
        st.write("Output:", result)


# -------------------------------
# Task 10 UI
# -------------------------------
elif task == "10. Count Vowels":
    st.subheader("Task 10: Count Vowels")

    text = st.text_input("Enter text", "apple")

    if st.button("Run Task"):
        result = count_vowels(text)
        st.write("Output:", result)


# -------------------------------
# Task 11 UI
# -------------------------------
elif task == "11. Reverse Text":
    st.subheader("Task 11: Reverse Text")

    text = st.text_input("Enter text", "python")

    if st.button("Run Task"):
        result = reverse_text(text)
        st.write("Output:", result)


# -------------------------------
# Task 12 UI
# -------------------------------
elif task == "12. Check Login":
    st.subheader("Task 12: Check Login")

    username = st.text_input("Enter username")
    password = st.text_input("Enter password", type="password")

    if st.button("Run Task"):
        result = check_login(username, password)
        st.write("Output:", result)