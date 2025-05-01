employees = [
    {"dept_no": 101, "roll_no": 1, "salary": 50000},
    {"dept_no": 101, "roll_no": 2, "salary": 60000},
    {"dept_no": 102, "roll_no": 3, "salary": 70000},
    {"dept_no": 102, "roll_no": 4, "salary": 55000},
    {"dept_no": 103, "roll_no": 5, "salary": 80000},
    {"dept_no": 103, "roll_no": 6, "salary": 45000},
]

salaries = {}

for emp in employees:
    dept_no = emp["dept_no"]
    salary = emp["salary"]
    
    if dept_no not in salaries:
        salaries[dept_no] = []
    
        salaries[dept_no].append(salary)

salary_stats = {}
for dept, salaries in salaries.items():
    salary_stats[dept] = {"min_salary": min(salaries), "max_salary": max(salaries)}

for dept, stats in salary_stats.items():
    print(f"Department {dept}: Min Salary = {stats['min_salary']}, Max Salary = {stats['max_salary']}")
