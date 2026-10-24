-- CALL CENTER DATABASE (simple version)
-- Tables: agents and calls

-- STEP 1: CREATE THE TABLES

CREATE TABLE agents (
    agent_id   INT PRIMARY KEY,
    agent_name VARCHAR(50),
    team       VARCHAR(30),
    city       VARCHAR(30)
);

CREATE TABLE calls (
    call_id       INT PRIMARY KEY,
    agent_id      INT,
    customer_name VARCHAR(50),
    call_type     VARCHAR(30),
    call_date     DATE,
    duration_min  INT,
    status        VARCHAR(20),
    rating        INT,
    FOREIGN KEY (agent_id) REFERENCES agents (agent_id)
);

-- STEP 2: ADD THE DATA

INSERT INTO agents VALUES (1, 'Anita Rao', 'Support', 'Chennai');
INSERT INTO agents VALUES (2, 'Rahul Verma', 'Support', 'Chennai');
INSERT INTO agents VALUES (3, 'Meera Nair', 'Sales', 'Bengaluru');
INSERT INTO agents VALUES (4, 'Karthik S', 'Sales', 'Bengaluru');
INSERT INTO agents VALUES (5, 'Divya Menon', 'Billing', 'Hyderabad');
INSERT INTO agents VALUES (6, 'Arjun Das', 'Billing', 'Hyderabad');

-- (a rating of NULL means the customer has not rated the call yet)
INSERT INTO calls VALUES (1, 1, 'Suresh Kumar', 'Technical', '2026-10-01', 12, 'Resolved', 5);
INSERT INTO calls VALUES (2, 2, 'Lakshmi Pillai', 'Complaint', '2026-10-01', 18, 'Escalated', 2);
INSERT INTO calls VALUES (3, 3, 'Ganesh Rao', 'Enquiry', '2026-10-02', 6, 'Resolved', 4);
INSERT INTO calls VALUES (4, 5, 'Nisha Patel', 'Complaint', '2026-10-02', 15, 'Resolved', 3);
INSERT INTO calls VALUES (5, 1, 'Harish Singh', 'Technical', '2026-10-03', 20, 'Pending', NULL);
INSERT INTO calls VALUES (6, 4, 'Kavya Menon', 'Enquiry', '2026-10-03', 5, 'Resolved', 5);
INSERT INTO calls VALUES (7, 6, 'Vikram Joshi', 'Complaint', '2026-10-04', 22, 'Escalated', 1);
INSERT INTO calls VALUES (8, 2, 'Pooja Reddy', 'Technical', '2026-10-05', 9, 'Resolved', 4);
INSERT INTO calls VALUES (9, 3, 'Arun Gupta', 'Enquiry', '2026-10-06', 7, 'Resolved', 5);
INSERT INTO calls VALUES (10, 5, 'Swati Bose', 'Complaint', '2026-10-07', 14, 'Pending', NULL);
INSERT INTO calls VALUES (11, 1, 'Manoj Nair', 'Technical', '2026-10-08', 11, 'Resolved', 5);
INSERT INTO calls VALUES (12, 4, 'Deepa Iyer', 'Enquiry', '2026-10-08', 4, 'Resolved', 4);
INSERT INTO calls VALUES (13, 6, 'Naveen Das', 'Complaint', '2026-10-09', 19, 'Resolved', 3);
INSERT INTO calls VALUES (14, 2, 'Ritu Sharma', 'Technical', '2026-10-10', 16, 'Pending', NULL);
INSERT INTO calls VALUES (15, 3, 'Sanjay Menon', 'Enquiry', '2026-10-11', 8, 'Resolved', 4);
INSERT INTO calls VALUES (16, 1, 'Divya Patel', 'Complaint', '2026-10-12', 25, 'Escalated', 2);
INSERT INTO calls VALUES (17, 1, 'Rohan Das', 'Enquiry', '2026-10-13', 6, 'Resolved', 5);
INSERT INTO calls VALUES (18, 4, 'Meena Rao', 'Enquiry', '2026-10-14', 5, 'Resolved', 5);
INSERT INTO calls VALUES (19, 2, 'Karthik Pillai', 'Technical', '2026-10-15', 13, 'Resolved', 4);
INSERT INTO calls VALUES (20, 6, 'Anjali Singh', 'Complaint', '2026-10-16', 17, 'Pending', NULL);

-- STEP 3: QUERIES (SELECT)

-- Q1: Show all agents
SELECT * FROM agents;

-- Q2: Show all calls
SELECT * FROM calls;

-- Q3: Show only the pending calls
SELECT call_id, customer_name, call_type, call_date FROM calls WHERE status = 'Pending';

-- Q4: Count the total number of calls
SELECT COUNT(*) AS total_calls FROM calls;

-- Q5: Average call duration in minutes
SELECT ROUND(AVG(duration_min), 1) AS average_duration FROM calls;

-- Q6: Show calls longer than 15 minutes, longest first
SELECT call_id, customer_name, duration_min FROM calls WHERE duration_min > 15 ORDER BY duration_min DESC;

-- Q7: Number of calls for each call type
SELECT call_type, COUNT(*) AS number_of_calls FROM calls GROUP BY call_type;

-- Q8: Number of calls for each status
SELECT status, COUNT(*) AS number_of_calls FROM calls GROUP BY status;

-- Q9: Number of calls handled by each agent (with the agent name)
SELECT agents.agent_name, COUNT(*) AS calls_handled
FROM calls
JOIN agents ON calls.agent_id = agents.agent_id
GROUP BY agents.agent_name
ORDER BY calls_handled DESC;

-- Q10: Average customer rating for each agent
SELECT agents.agent_name, ROUND(AVG(calls.rating), 1) AS average_rating
FROM calls
JOIN agents ON calls.agent_id = agents.agent_id
GROUP BY agents.agent_name
ORDER BY average_rating DESC;

-- Q11: Number of calls for each team
SELECT agents.team, COUNT(*) AS number_of_calls
FROM calls
JOIN agents ON calls.agent_id = agents.agent_id
GROUP BY agents.team;

-- Q12: The agent who handled the most calls
SELECT agents.agent_name, COUNT(*) AS calls_handled
FROM calls
JOIN agents ON calls.agent_id = agents.agent_id
GROUP BY agents.agent_name
ORDER BY calls_handled DESC
LIMIT 1;

-- Q13: Show all complaints with the agent name and status
SELECT calls.call_id, calls.customer_name, agents.agent_name, calls.status
FROM calls
JOIN agents ON calls.agent_id = agents.agent_id
WHERE calls.call_type = 'Complaint';

-- STEP 4: CHANGING DATA (INSERT, UPDATE, DELETE)

-- C1: A new call comes in. Save it
INSERT INTO calls VALUES (21, 3, 'Prakash Kumar', 'Enquiry', '2026-10-18', 6, 'Pending', NULL);

-- C2: The pending call number 5 is now solved. Update its status and rating
UPDATE calls SET status = 'Resolved', rating = 4 WHERE call_id = 5;

-- C3: Delete the call that was saved by mistake (call 21)
DELETE FROM calls WHERE call_id = 21;

-- Q14: Check the pending calls again (call 5 is gone from this list)
SELECT call_id, customer_name, call_type, status FROM calls WHERE status = 'Pending';

-- Q15: Final number of calls for each status
SELECT status, COUNT(*) AS number_of_calls FROM calls GROUP BY status;
