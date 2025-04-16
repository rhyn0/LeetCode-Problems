"""Meta Interview Question Practice List on LeetCode.

185. Department Top Three Salaries on LeetCode.

====================================================
Below is also how I would solve this using PostgreSQL.

```sql
Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int);
Create table If Not Exists Department (id int, name varchar(255));
Truncate table Employee;
insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('2', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId) values ('3', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId) values ('4', 'Max', '90000', '1');
insert into Employee (id, name, salary, departmentId) values ('5', 'Janet', '69000', '1');
insert into Employee (id, name, salary, departmentId) values ('6', 'Randy', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('7', 'Will', '70000', '1');
Truncate table Department;
insert into Department (id, name) values ('1', 'IT');
insert into Department (id, name) values ('2', 'Sales');

WITH empl_dept AS (
    SELECT
        e.name as name,
        e.salary as salary,
        d.id as departmentId,
        d.name as name_dept,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) as rank
    FROM Employee e
    JOIN Department d on e.departmentId = d.id
)
SELECT
    ed.name_dept as "Department",
    ed.name as "Employee",
    ed.salary as "Salary"
FROM empl_dept as ed
WHERE ed.rank <= 3;
```

Setup:
    >>> data = [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [4, 'Max', 90000, 1], [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]]
    >>> employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
    >>> data = [[1, 'IT'], [2, 'Sales']]
    >>> department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})

Example 1:
    >>> top_three_salaries(employee, department)
      Department Employee  Salary
    0         IT      Joe   85000
    1      Sales    Henry   80000
    2      Sales      Sam   60000
    3         IT      Max   90000
    4         IT    Randy   85000
    5         IT     Will   70000
"""  # noqa: E501

# External Party
import pandas as pd


def top_three_salaries(
    employee: pd.DataFrame,
    department: pd.DataFrame,
) -> pd.DataFrame:
    """Return the employees that are high earners per department.

    A high earner is one of the top 3 unique salaries within a department.

    Args:
        employee (pd.DataFrame): Table of employee data: name, department, salary
        department (pd.DataFrame): Table department data: id, name

    Returns:
        pd.DataFrame: Output table of department, employee name, and salary
    """
    merged_df = employee.merge(
        department,
        left_on="departmentId",
        right_on="id",
        suffixes=("", "_dept"),
    )

    # Group by department and get the top 3 unique salaries
    top_salaries = (
        merged_df.groupby("departmentId")["salary"]
        .apply(lambda x: x.drop_duplicates().nlargest(3))
        .reset_index()
    )

    # Merge back to get the employee details
    result = merged_df.merge(top_salaries, on=["departmentId", "salary"])

    # Select relevant columns
    return result[
        [
            "name_dept",
            "name",
            "salary",
        ]
    ].rename(
        columns={
            "name_dept": "Department",
            "name": "Employee",
            "salary": "Salary",
        },
    )
