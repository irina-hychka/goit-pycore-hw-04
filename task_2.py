def get_cats_info(path):
    '''
    Analyzes information about cats from a file

    Param:
    path - file URl (string)
        
    Returns: a list of dict with keys: "id", "name", "age"
    OR empty list:
    - if there are issues with a file; 
    - it contains no data.

    Notes:
    If the row is not valid, it is not processed

    If the age in the row is incorrect, it will be assigned to None
    '''
    cats = []
    keys = ["id", "name", "age"]
    try: 
        with open(path, mode='r', encoding='utf-8') as file:
            # Reads file line by line
            for line in file:
                # Removes all empty spaces and line breaks
                line = line.replace(' ', '').replace('\n', '')
                # Creates a list of values
                cat_list = line.split(',')
                # Checks if the line contains at least 3 values (id, name, age)
                if len(cat_list) < 3:
                    continue
                else: 
                    '''
                    Creates a dictionary by mapping keys ("id", "name", "age") 
                    to the values in the list
                    '''
                    cat_data = dict(zip(keys, cat_list))
                    # Checks if the "age" value is a valid number
                    if not cat_data["age"].isdigit():
                        cat_data["age"] = None
                    # Adds the processed dictionary to the list of cats
                    cats.append(cat_data)
            return cats
        
    # Handle Exceptions
    except FileNotFoundError:
        return cats
    
    except PermissionError:
        return cats
    
    except UnicodeError:
        return cats
    
    except IOError:
        return cats           

# Usage:
cats_info = get_cats_info("cats_file.txt")
print(cats_info)
