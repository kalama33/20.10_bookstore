# create func process data


students = [("Alice", 20), ("Bob", 22), ("Charlie", 19)] # list of tuples
grades = {"ID001": 85, "ID002": 92, "ID003": 78} # dic


def process_data(students, grades):
    result = {}                    # create a empty dic. to store the new data
    id_counter = 1                 # variable to keep track of the student id
    for student in students:       # to itirate in the students tuple
        '''
        The :03d part will be replaced by the id_counter value with 3 digits 
        and leading zeros if necessary. This ensures that the ID is a 3 character string, 
        such as "ID001", "ID002", etc.
        '''
        student_id = f"ID{id_counter:03d}" # format str, key of the new dict.
        id_counter += 1                    # to increase the id to ensure that every student has an unique Id
        name, age = student                # unpacking tuple
        grade = grades.get(student_id)     # use of get method to to get the grades 
        result[student_id] = (name, age, grade) # tuple containing info
    return result


result = process_data(students, grades)
print(result)