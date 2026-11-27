CREATE TABLE helpdesk_tickets (
    ticket_id INT PRIMARY KEY,
    employee VARCHAR(50),
    department VARCHAR(30),
    category VARCHAR(30),
    priority VARCHAR(20),
    status VARCHAR(20),
    resolution_hours DECIMAL(8,2),
    sla_hours DECIMAL(8,2)
);

INSERT INTO helpdesk_tickets
(ticket_id, employee, department, category, priority, status, resolution_hours, sla_hours)
VALUES
(101, 'Rahul', 'HR', 'Hardware', 'High', 'Closed', 6, 8),
(102, 'Priya', 'Finance', 'Software', 'Medium', 'Closed', 30, 24),
(103, 'Amit', 'IT', 'Access', 'High', 'Open', NULL, 4),
(104, 'Neha', 'Sales', 'Network', 'Critical', 'Closed', 5, 4),
(105, 'Rohan', 'HR', 'Software', 'Low', 'Closed', 20, 48),
(106, 'Anjali', 'Finance', 'Hardware', 'Medium', 'Closed', 12, 24),
(107, 'Arjun', 'Sales', 'Access', 'High', 'Closed', 3, 4),
(108, 'Meera', 'IT', 'Network', 'Medium', 'Open', NULL, 8),
(109, 'Kabir', 'Finance', 'Access', 'Critical', 'Closed', 10, 8),
(110, 'Isha', 'HR', 'Network', 'Low', 'Closed', 40, 48),
(111, 'Dev', 'IT', 'Hardware', 'High', 'Closed', 9, 8),
(112, 'Sara', 'Sales', 'Software', 'Medium', 'Closed', 18, 24),
(113, 'Nikhil', 'Finance', 'Network', 'High', 'Open', NULL, 12),
(114, 'Pooja', 'HR', 'Access', 'Medium', 'Closed', 7, 8),
(115, 'Vikram', 'IT', 'Software', 'Critical', 'Closed', 2, 4),
(116, 'Tara', 'Sales', 'Hardware', 'Low', 'Open', NULL, 24);

SELECT *
FROM helpdesk_tickets
ORDER BY ticket_id;

SELECT COUNT(*) AS total_tickets
FROM helpdesk_tickets;

SELECT status,
       COUNT(*) AS ticket_count
FROM helpdesk_tickets
GROUP BY status;

SELECT priority,
       COUNT(*) AS ticket_count
FROM helpdesk_tickets
GROUP BY priority;

SELECT department,
       COUNT(*) AS ticket_count
FROM helpdesk_tickets
GROUP BY department;

SELECT category,
       COUNT(*) AS ticket_count
FROM helpdesk_tickets
GROUP BY category
ORDER BY category;

SELECT ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours
FROM helpdesk_tickets
WHERE status = 'Closed';

SELECT ticket_id,
       employee,
       resolution_hours,
       sla_hours
FROM helpdesk_tickets
WHERE status = 'Closed'
  AND resolution_hours > sla_hours;
  
SELECT COUNT(*) AS sla_breach_count
FROM helpdesk_tickets
WHERE status = 'Closed'
  AND resolution_hours > sla_hours;

SELECT *
FROM helpdesk_tickets
WHERE priority = 'Critical'
ORDER BY department;

SELECT department,
       COUNT(*) AS ticket_count
FROM helpdesk_tickets
GROUP BY department
HAVING COUNT(*) >= 4;

SELECT
    ticket_id,
    employee,
    status,
    resolution_hours,
    sla_hours,
    CASE
        WHEN status = 'Open' THEN 'Pending'
        WHEN resolution_hours > sla_hours THEN 'Breached'
        ELSE 'Within SLA'
    END AS SLA_Result
FROM helpdesk_tickets;

SELECT ticket_id,
       employee,
       resolution_hours
FROM helpdesk_tickets
WHERE status = 'Closed'
  AND resolution_hours >
      (
          SELECT AVG(resolution_hours)
          FROM helpdesk_tickets
          WHERE status = 'Closed'
      );
      
SELECT
    department,
    COUNT(*) AS total_tickets,
    SUM(CASE
            WHEN status = 'Closed' THEN 1
            ELSE 0
        END) AS closed_tickets
FROM helpdesk_tickets
GROUP BY department;

SELECT
    department,
    COUNT(*) AS total_tickets,
    SUM(CASE
            WHEN status = 'Closed' THEN 1
            ELSE 0
        END) AS closed_tickets
FROM helpdesk_tickets
GROUP BY department;
