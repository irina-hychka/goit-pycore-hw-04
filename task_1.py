def total_salary(path: str) -> tuple:
    '''
    Analyzes employee salary data from a file

    Param:
    path - file URl (string)
        
    Returns: 
    the total and average salary of all developers - a tuple with two vaues 
    OR a tuple (0, 0): 
    - if there are issues with a file; 
    - it contains no data;
    - if any value error.
    '''
    try:
        with open(path, mode="r", encoding='utf-8') as salary_data:
            salaries = []
            lines = salary_data.readlines()

            for line in lines:
                # Removes all empty spaces and line breaks
                line = line.replace(' ', '').replace('\n', '')
                # Gets salary amount of each employee
                _, salary = line.split(',', 1)

                # Check is it possible to covert a string into the integer
                if not salary.isdigit():
                    return (0, 0)
                else:
                    # Adds salary amount to the list
                    salaries.append(int(salary))

            # Check is file empty
            if not salaries:
                return (0, 0)
            
            # Calculate the Total salary value
            total_salary = sum(salaries)
            # Calculate the Average salary value
            average_salary = (total_salary // len(salaries))
            # Result
            return (total_salary, average_salary)

    # Handle Exceptions
    except FileNotFoundError:
        return (0, 0)
    
    except PermissionError:
        return (0, 0)
    
    except UnicodeError:
        return (0, 0)
    
    except IOError:
        return (0, 0)

# Usage:
total, average = total_salary("goit-pycore-hw-04/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")