# 🎓 CampusAI – AI-Powered College Assistant

An AI-powered College Assistant built using **LangChain Tool Calling Agent** that intelligently understands user requests and automatically invokes the appropriate tools to provide accurate academic and administrative information.

## ✨ Features

- 📊 Attendance Calculator
- 📝 Result & Grade Calculator
- 💰 Fee Balance Calculator
- 📚 Library Fine Calculator
- 🏠 Hostel Fee Calculator
- 👨‍🎓 Student Information Lookup
- 🤖 Automatic Tool Selection using LangChain Tool Calling Agent
- ⚡ Multi-Tool Query Handling
- 🔍 Verbose Agent Execution for Better Debugging

---

## 🚀 Tech Stack

- Python
- LangChain
- Ollama / OpenAI
- Tool Calling Agent
- AgentExecutor
- ChatPromptTemplate

---

## 🛠️ Tools

### 📊 Attendance Calculator
Calculates attendance percentage and determines exam eligibility.

**Rule**
- Attendance ≥ 75% → Eligible
- Attendance < 75% → Not Eligible

---

### 📝 Result Calculator

Calculates:

- Average Marks
- Grade
- Pass/Fail Status

| Average | Grade |
|---------|-------|
| ≥ 90 | A |
| 75–89 | B |
| 60–74 | C |
| < 60 | D |

Pass if Average ≥ 50.

---

### 💰 Fee Balance Calculator

Calculates pending course fee.

**Formula**

Pending Fee = Total Fee − Paid Fee

---

### 📚 Library Fine Calculator

Calculates fine for delayed book returns.

**Formula**

Fine = ₹5 × Delayed Days

---

### 🏠 Hostel Fee Calculator

Calculates total hostel fee.

**Formula**

Hostel Fee = Monthly Fee × Months Stayed

---

### 👨‍🎓 Student Information Tool

Retrieves student details using Student ID from a Python dictionary.

---

## 📂 Project Structure

```
college-ai-assistant/
│
├── app.py
├── tools.py
├── student_data.py
├── requirements.txt
├── README.md
└── screenshots/
```


---

## ▶️ Example Queries

### Attendance

```
I attended 72 classes out of 90. Am I eligible for exams?
```

---

### Result

```
My marks are 95, 90, 88, 91 and 87. What is my grade?
```

---

### Fee

```
My course fee is 50000 and I have paid 35000.
```

---

### Library

```
I returned a library book 8 days late.
```

---

### Hostel

```
Hostel fee is 6000 per month and I stayed for 5 months.
```

---

### Multi-Tool Query

```
I attended 80 classes out of 100.
My marks are 90, 85, 88, 92 and 95.
My course fee is 60000 and I paid 45000.

Provide:
1. Attendance Status
2. Grade
3. Pending Fee
```

The agent automatically invokes multiple tools and returns a consolidated response.

---

## 🎯 Highlights

- Intelligent Tool Calling
- Modular Tool Design
- Natural Language Query Handling
- Multi-Tool Execution
- Easy to Extend with New Tools
- Clean and Maintainable Code

---

## 🔮 Future Enhancements

- Student Database Integration
- GPA Calculator
- Timetable Management
- Exam Schedule Assistant
- PDF Report Generation
- Streamlit Web Interface
- Voice-Based Interaction
- Cloud Deployment

---

## 📸 Screenshots

Add screenshots of:

- Agent Execution (`verbose=True`)
- Attendance Calculator
- Result Calculator
- Fee Calculator
- Library Fine Calculator
- Hostel Fee Calculator
- Multi-Tool Execution

---

## 👩‍💻 Author

**Diksha Mitra**

B.Tech in Computer Science & Engineering

---

⭐ If you found this project useful, consider giving it a star.
