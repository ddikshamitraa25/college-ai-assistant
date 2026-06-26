from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import ChatPromptTemplate

# =====================================
# ATTENDANCE TOOL
# =====================================

@tool
def attendance_calculator(total_classes: int, attended_classes: int):
    """
    Calculate attendance percentage and exam eligibility
    """

    percentage = (attended_classes / total_classes) * 100

    if percentage >= 75:
        status = "Eligible for Exam"
    else:
        status = "Not Eligible for Exam"

    return f"Attendance Percentage: {percentage:.2f}%\nStatus: {status}"


# =====================================
# RESULT TOOL
# =====================================

@tool
def result_calculator(m1: int, m2: int, m3: int, m4: int, m5: int):
    """
    Calculate average marks, grade and pass/fail status
    """

    average = (m1 + m2 + m3 + m4 + m5) / 5

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"

    return f"Average Marks: {average:.2f}\nGrade: {grade}\nResult: {result}"


# =====================================
# FEE BALANCE TOOL
# =====================================

@tool
def fee_balance_calculator(total_fee: int, amount_paid: int):
    """
    Calculate pending fee amount
    """

    pending = total_fee - amount_paid

    return f"Pending Fee Amount: ₹{pending}"


# =====================================
# LIBRARY FINE TOOL
# =====================================

@tool
def library_fine_calculator(delayed_days: int):
    """
    Calculate library fine amount
    """

    fine = delayed_days * 5

    return f"Library Fine Amount: ₹{fine}"


# =====================================
# HOSTEL FEE TOOL
# =====================================

@tool
def hostel_fee_calculator(monthly_fee: int, months_stayed: int):
    """
    Calculate hostel fee
    """

    total = monthly_fee * months_stayed

    return f"Total Hostel Fee: ₹{total}"


# =====================================
# BONUS TOOL
# =====================================

student_database = {
    101: {"name": "Rahul", "department": "CSE", "year": 2},
    102: {"name": "Priya", "department": "AIML", "year": 3},
    103: {"name": "Amit", "department": "ECE", "year": 1},
}

@tool
def student_info(student_id: int):
    """
    Retrieve student details using student ID
    """

    if student_id in student_database:
        return student_database[student_id]
    else:
        return "Student not found"


# =====================================
# TOOLS LIST
# =====================================

tools = [
    attendance_calculator,
    result_calculator,
    fee_balance_calculator,
    library_fine_calculator,
    hostel_fee_calculator,
    student_info
]


# =====================================
# LLM MODEL
# =====================================

llm = ChatOllama(
model="qwen2.5:7b"
)



# =====================================
# PROMPT
# =====================================

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI-powered College Assistant."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ]
)


# =====================================
# CREATE AGENT
# =====================================

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)


# =====================================
# AGENT EXECUTOR
# =====================================

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


# =====================================
# TEST CASES
# =====================================

queries = [

    "I attended 72 classes out of 90. Am I eligible for exams?",

    "My marks are 95, 90, 88, 91 and 87. What is my grade?",

    "My course fee is 50000 and I have paid 35000. How much fee is pending?",

    "I returned a library book 8 days late. What is the fine amount?",

    "Hostel fee is 6000 per month and I stayed for 5 months. Calculate my hostel fee.",

    """
    I attended 80 classes out of 100.
    My marks are 90, 85, 88, 92 and 95.
    My course fee is 60000 and I paid 45000.

    Provide:
    1. Attendance Status
    2. Grade
    3. Pending Fee
    """
]


# =====================================
# RUN TEST CASES
# =====================================

for i, query in enumerate(queries, start=1):

    print("\n")
    print("=" * 50)
    print(f"TEST CASE {i}")
    print("=" * 50)

    response = agent_executor.invoke(
        {"input": query}
    )

    print("\nFINAL RESPONSE:")
    print(response["output"])

