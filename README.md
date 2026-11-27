# Smart IT Helpdesk Analytics & Assistant

## Project Overview

The Smart IT Helpdesk Analytics & Assistant project is a beginner-friendly capstone project designed to demonstrate the practical application of Python, SQL, Excel, JSON, AI concepts, Git, and GitHub.

The project analyzes IT support tickets raised by employees and generates key business insights such as ticket volume, status distribution, SLA compliance, department trends, category trends, and average resolution time.

The same dataset is analyzed independently using Python, SQL, and Excel to validate consistency across different tools.

---

## Business Scenario

An organization receives IT support tickets related to hardware, software, network, and access issues.

Management requires a performance report that provides:

- Total number of tickets
- Open and Closed ticket counts
- SLA performance tracking
- Average resolution time
- Ticket distribution by department
- Ticket distribution by category
- Basic troubleshooting guidance through an FAQ Assistant

---

## Technologies Used

- Python 3
- SQL
- Microsoft Excel
- JSON
- Git
- GitHub

---

## Project Structure

```text
Smart-IT-Helpdesk/
│
├── README.md
├── helpdesk_python.py
├── helpdesk_sql.sql
├── helpdesk_ai_assistant.py
├── helpdesk_excel.xlsx
├── comparison_results.md
├── .gitignore
│
└── .github/
    └── workflows/
        └── python-ci.yml
```

---

## Dataset Overview

The project uses a fixed dataset containing:

- 16 Helpdesk Tickets
- 4 Departments
  - HR
  - Finance
  - IT
  - Sales
- 4 Categories
  - Hardware
  - Software
  - Access
  - Network

---

## Python Features

The Python implementation performs:

- Ticket ID listing
- Total ticket calculation
- Open and Closed ticket counts
- Priority-wise ticket counts
- Department-wise ticket counts
- Category-wise ticket counts
- Average resolution time calculation
- SLA breach identification
- Critical ticket reporting
- JSON report generation
- FAQ Assistant implementation

Run:

```bash
python helpdesk_python.py
```

---

## SQL Features

The SQL script demonstrates:

- SELECT Statements
- WHERE Clause
- ORDER BY
- COUNT
- AVG
- GROUP BY
- HAVING
- CASE Statements
- Subqueries
- Window Functions (Bonus)

Run the SQL script in:

- MySQL
- SQL Server
- PostgreSQL
- SQLite Online Editor

---

## Excel Features

The Excel workbook includes:

- COUNTIF Functions
- COUNTA Functions
- AVERAGEIFS Functions
- IF Statements
- Conditional Formatting
- Pivot Tables
- Dashboard Creation

Key Metrics:

| Metric | Value |
|----------|----------|
| Total Tickets | 16 |
| Open Tickets | 4 |
| Closed Tickets | 12 |
| SLA Breaches | 4 |
| Average Resolution Hours | 13.50 |

---

## AI Assistant Module

The project includes a simple FAQ-based IT Assistant that:

- Parses JSON requests
- Searches an approved knowledge base
- Returns predefined responses
- Demonstrates Retrieval-Based AI concepts
- Demonstrates Rule-Based Agentic AI concepts

Topics Covered:

- JSON Processing
- Retrieval-Augmented Concepts
- FAQ Search
- Rule-Based Automation
- Basic Agent Workflow

---

## Cross-Tool Verification Results

| Metric | Result |
|----------|---------|
| Total Tickets | 16 |
| Open Tickets | 4 |
| Closed Tickets | 12 |
| SLA Breaches | 4 |
| Average Resolution Hours | 13.50 |
| Hardware Tickets | 4 |
| Software Tickets | 4 |
| Access Tickets | 4 |
| Network Tickets | 4 |
| HR Tickets | 4 |
| Finance Tickets | 4 |
| IT Tickets | 4 |
| Sales Tickets | 4 |

All outputs generated using Python, SQL, and Excel matched successfully.

---

## Learning Outcomes

This project demonstrates:

- Python Programming Fundamentals
- SQL Query Writing
- Data Analysis in Excel
- JSON Data Handling
- AI and RAG Concepts
- Rule-Based Agent Design
- Git Version Control
- GitHub Collaboration
- Continuous Integration Basics

---

## Git Commands Used

```bash
git init -b main

git add .

git commit -m "Initial Smart IT Helpdesk Project"

git switch -c feature/improve-report

git commit -m "Improve project documentation"

git switch main

git merge feature/improve-report

git push -u origin main
```

---

## Future Enhancements

Possible improvements:

- Web-based Dashboard
- Database Integration
- Real-Time Ticket Updates
- Power BI Reporting
- Advanced Analytics
- LLM-Powered Helpdesk Assistant
- Vector Database Integration
- Full RAG Implementation

---

## Author

**Anvesh Karnati**

Intern | Python | SQL | AI | Excel | Git & GitHub

---

## Project Status

✅ Completed Successfully

✅ Python Analysis

✅ SQL Analysis

✅ Excel Dashboard

✅ AI Assistant

✅ Git & GitHub Version Control

✅ Cross-Tool Verification