"""4. Add Functions to Previous Pracs"""
# 1. Calculate salary for worker level
def main_error_checking():
    MIN_WORKER_LEVEL = 1
    MAX_WORKER_LEVEL = 10
    SALARY_PER_LEVEL = 5000

    worker_level = get_worker_level(MIN_WORKER_LEVEL, MAX_WORKER_LEVEL)
    salary = calculate_salary(worker_level, SALARY_PER_LEVEL)

    print(f"Based on your worker level {worker_level}, your salary is ${salary:,.2f}")

def get_worker_level(min_level, max_level):
    """prompts the user to enter a valid worker level within specified range."""
    level = int(input(f"Worker level ({min_level}-{max_level}): "))
    while level < min_level or level > max_level:
        print("Invalid worker level")
        level = int(input(f"Worker level ({min_level}-{max_level}): "))
    return level

def calculate_salary(level, salary_per_level):
    """calculate the salary based on worker level and salary per level."""
    return level * salary_per_level

# run the function and error check
main_error_checking()


# 6. Print grid(rows, columns)
def main_nested_loops():
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
    print_matrix(rows, columns)

def print_matrix(rows, columns):
    """prints a matrix of given rows and columns,
    where each element is the column number."""
    for i in range(rows):
        for j in range(columns):
            print(j, end=" ")
        print()

#run the function for the nested loops
main_nested_loops()



