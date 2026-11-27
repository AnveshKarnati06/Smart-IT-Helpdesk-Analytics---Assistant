import json

tickets = [
    {"ticket_id": 101, "employee": "Rahul", "department": "HR", "category": "Hardware", "priority": "High", "status": "Closed", "resolution_hours": 6, "sla_hours": 8},
    {"ticket_id": 102, "employee": "Priya", "department": "Finance", "category": "Software", "priority": "Medium", "status": "Closed", "resolution_hours": 30, "sla_hours": 24},
    {"ticket_id": 103, "employee": "Amit", "department": "IT", "category": "Access", "priority": "High", "status": "Open", "resolution_hours": None, "sla_hours": 4},
    {"ticket_id": 104, "employee": "Neha", "department": "Sales", "category": "Network", "priority": "Critical", "status": "Closed", "resolution_hours": 5, "sla_hours": 4},
    {"ticket_id": 105, "employee": "Rohan", "department": "HR", "category": "Software", "priority": "Low", "status": "Closed", "resolution_hours": 20, "sla_hours": 48},
    {"ticket_id": 106, "employee": "Anjali", "department": "Finance", "category": "Hardware", "priority": "Medium", "status": "Closed", "resolution_hours": 12, "sla_hours": 24},
    {"ticket_id": 107, "employee": "Arjun", "department": "Sales", "category": "Access", "priority": "High", "status": "Closed", "resolution_hours": 3, "sla_hours": 4},
    {"ticket_id": 108, "employee": "Meera", "department": "IT", "category": "Network", "priority": "Medium", "status": "Open", "resolution_hours": None, "sla_hours": 8},
    {"ticket_id": 109, "employee": "Kabir", "department": "Finance", "category": "Access", "priority": "Critical", "status": "Closed", "resolution_hours": 10, "sla_hours": 8},
    {"ticket_id": 110, "employee": "Isha", "department": "HR", "category": "Network", "priority": "Low", "status": "Closed", "resolution_hours": 40, "sla_hours": 48},
    {"ticket_id": 111, "employee": "Dev", "department": "IT", "category": "Hardware", "priority": "High", "status": "Closed", "resolution_hours": 9, "sla_hours": 8},
    {"ticket_id": 112, "employee": "Sara", "department": "Sales", "category": "Software", "priority": "Medium", "status": "Closed", "resolution_hours": 18, "sla_hours": 24},
    {"ticket_id": 113, "employee": "Nikhil", "department": "Finance", "category": "Network", "priority": "High", "status": "Open", "resolution_hours": None, "sla_hours": 12},
    {"ticket_id": 114, "employee": "Pooja", "department": "HR", "category": "Access", "priority": "Medium", "status": "Closed", "resolution_hours": 7, "sla_hours": 8},
    {"ticket_id": 115, "employee": "Vikram", "department": "IT", "category": "Software", "priority": "Critical", "status": "Closed", "resolution_hours": 2, "sla_hours": 4},
    {"ticket_id": 116, "employee": "Tara", "department": "Sales", "category": "Hardware", "priority": "Low", "status": "Open", "resolution_hours": None, "sla_hours": 24}
]

# 1 Print Ticket IDs
for ticket in tickets:
    print(ticket["ticket_id"])

# 2 Total tickets
total = len(tickets)
print("Total:", total)

# 3 Open and Closed
open_count = sum(1 for t in tickets if t["status"] == "Open")
closed_count = sum(1 for t in tickets if t["status"] == "Closed")
print("Open:", open_count)
print("Closed:", closed_count)

# 4 Priority count
priority_count = {}
for t in tickets:
    priority = t["priority"]
    priority_count[priority] = priority_count.get(priority, 0) + 1
print(priority_count)

# 5 Department count
department_count = {}
for t in tickets:
    dept = t["department"]
    department_count[dept] = department_count.get(dept, 0) + 1
print(department_count)

# 6 Category count
category_count = {}
for t in tickets:
    cat = t["category"]
    category_count[cat] = category_count.get(cat, 0) + 1
print(category_count)

# 7 Average resolution time
closed_hours = [
    t["resolution_hours"]
    for t in tickets
    if t["status"] == "Closed"
]
avg_resolution = sum(closed_hours) / len(closed_hours)
print("Average:", round(avg_resolution, 2))

# 8 SLA breaches
breaches = [
    t["ticket_id"]
    for t in tickets
    if t["status"] == "Closed"
    and t["resolution_hours"] > t["sla_hours"]
]
print("Breached:", breaches)

# 9 Critical tickets
for t in tickets:
    if t["priority"] == "Critical":
        print(t["employee"], t["ticket_id"])

# 10 Function count by status
def count_by_status(tickets, status):
    if status not in ["Open", "Closed"]:
        return "Invalid Status"
    return sum(
        1 for t in tickets
        if t["status"] == status
    )

# 11 SLA Function
def get_sla_breaches(tickets):
    return [
        t["ticket_id"]
        for t in tickets
        if t["status"] == "Closed"
        and t["resolution_hours"] > t["sla_hours"]
    ]

# 12 Department Summary
def department_summary(tickets):
    summary = {}
    for t in tickets:
        dept = t["department"]
        summary[dept] = summary.get(dept, 0) + 1
    return summary

# 13 Invalid status
print(count_by_status(tickets, "Pending"))

# 14 Report Dictionary
report = {
    "total": total,
    "open": open_count,
    "closed": closed_count,
    "sla_breaches": len(breaches),
    "average_resolution_hours": round(avg_resolution, 2)
}
 
# 15 JSON
print(json.dumps(report, indent=4))