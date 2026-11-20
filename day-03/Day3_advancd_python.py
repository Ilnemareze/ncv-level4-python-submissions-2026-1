# Name: [ Mew I]
# ID Number: [740907054081]
# Date: 2026-11-19
# Description: A console-based learner marks management system demonstrating
#             Python collections (lists, tuples, sets, dictionaries) and
#             first-principles algorithms (aggregation, searching, sorting).

# Starter data
learners = {
    "2024001": {"name": "Thandi", "marks": [65, 72, 58]},
    "2024002": {"name": "Sipho", "marks": [48, 90, 55]},
    "2024003": {"name": "Lerato", "marks": [81, 39, 77]},
    "2024004": {"name": "Dumisani", "marks": [72, 72, 48]},
    "2024005": {"name": "Naledi", "marks": [90, 55, 72]}
}

# ==============================================================================
# QUESTION 1: Collections and data structures
# ==============================================================================
def demonstrate_collections():
    print("\n--- QUESTION 1: COLLECTIONS & DATA STRUCTURES ---")
    
    # 1. List of marks for learner 2024001
    thandi_marks = learners["2024001"]["marks"]
    print("All marks for 2024001:", thandi_marks)
    print("First mark:", thandi_marks[0])
    print("Last mark:", thandi_marks[-1])
    print("Slice of first two marks:", thandi_marks[:2])

    # 2. Tuple representing a fixed classroom coordinate (row, seat)
    seat_coordinate = (4, 12)
    row, seat = seat_coordinate  # Tuple unpacking
    print(f"Unpacked coordinate -> Row: {row}, Seat: {seat}")
    # Comment: A tuple is appropriate here because classroom seat coordinates are fixed
    # physical locations that should remain immutable (cannot be accidentally altered).

    # 3. Set of module codes with at least one duplicate
    module_codes = {"CS101", "MATH102", "ENG105", "CS101", "STAT103"}
    print("Unique module codes:", module_codes)
    print("Number of unique codes:", len(module_codes))
    print("Is 'CS101' in modules?", "CS101" in module_codes)
    print("Is 'BIO101' in modules?", "BIO101" in module_codes)

    # 4. Data structure justification comment:
    # A dictionary keyed by student number provides O(1) fast lookup using a unique ID,
    # ensuring no duplicate student numbers exist. Storing marks in a list inside each
    # record preserves the chronological order of assessments and allows new marks to
    # be appended dynamically as the semester progresses.

# ==============================================================================
# QUESTION 2: First-principles list algorithms
# ==============================================================================
def total_of(values):
    """Calculates the sum of a list using a loop."""
    total = 0
    for val in values:
        total += val
    return total

def mean_of(values):
    """Calculates the arithmetic mean using total_of(). Handles empty lists."""
    if len(values) == 0:
        return None
    return total_of(values) / len(values)

def max_of(values):
    """Finds the highest value using comparisons. Handles empty lists."""
    if len(values) == 0:
        return None
    highest = values[0]
    for val in values[1:]:
        if val > highest:
            highest = val
    return highest

def min_of(values):
    """Finds the lowest value using comparisons. Handles empty lists."""
    if len(values) == 0:
        return None
    lowest = values[0]
    for val in values[1:]:
        if val < lowest:
            lowest = val
    return lowest

def range_of(values):
    """Calculates the range (max - min) reusing max_of() and min_of()."""
    if len(values) == 0:
        return None
    return max_of(values) - min_of(values)

def above_mean(values):
    """Returns a list of values strictly greater than the mean."""
    if len(values) == 0:
        return []
    avg = mean_of(values)
    result = []
    for val in values:
        if val > avg:
            result.append(val)
    return result

# ==============================================================================
# QUESTION 3: Search, duplicates and mode
# ==============================================================================
def find_first(values, target):
    """Returns the first matching index of target, or -1 if absent."""
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def find_all(values, target):
    """Returns a list of all matching indices for target."""
    indices = []
    for i in range(len(values)):
        if values[i] == target:
            indices.append(i)
    return indices

def count_of(values, target):
    """Counts occurrences of target without using .count()."""
    count = 0
    for val in values:
        if val == target:
            count += 1
    return count

def mode_of(values):
    """Finds the mode(s) using a frequency dictionary. Returns a list of tied modes."""
    if len(values) == 0:
        return []
    
    freq = {}
    for val in values:
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1

    highest_freq = 0
    for count in freq.values():
        if count > highest_freq:
            highest_freq = count

    modes = []
    for val, count in freq.items():
        if count == highest_freq:
            modes.append(val)
    return modes

# ==============================================================================
# QUESTION 4: Sorting algorithms
# ==============================================================================
def bubble_sort(values):
    """Sorts a copy of values in ascending order using adjacent swaps."""
    arr = values[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(values):
    """Sorts a copy of values in ascending order by selecting the smallest item."""
    arr = values[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# ==============================================================================
# QUESTION 5: Interactive learner records & menu helpers
# ==============================================================================
def get_valid_mark(prompt):
    """Helper to validate integer marks between 0 and 100."""
    while True:
        raw = input(prompt).strip()
        if raw.isdigit():
            mark = int(raw)
            if 0 <= mark <= 100:
                return mark
        print("Invalid input. Please enter a whole number between 0 and 100.")

def add_learner(records):
    student_no = input("Enter new student number: ").strip()
    if not student_no:
        print("Student number cannot be empty.")
        return
    if student_no in records:
        print(f"Error: Student number {student_no} already exists.")
        return

    name = input("Enter learner name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    marks = []
    while True:
        count_str = input("How many marks to enter? ").strip()
        if count_str.isdigit() and int(count_str) > 0:
            count = int(count_str)
            break
        print("Please enter a valid positive number.")

    for i in range(count):
        m = get_valid_mark(f"Enter mark {i + 1} (0-100): ")
        marks.append(m)

    records[student_no] = {"name": name, "marks": marks}
    print(f"Learner {name} ({student_no}) added successfully.")

def search_learner(records):
    student_no = input("Enter student number to search: ").strip()
    if student_no in records:
        info = records[student_no]
        print(f"Found -> Number: {student_no} | Name: {info['name']} | Marks: {info['marks']}")
    else:
        print(f"Not found: No learner exists with student number '{student_no}'.")

def update_learner(records):
    student_no = input("Enter student number to update: ").strip()
    if student_no not in records:
        print(f"Not found: No learner exists with student number '{student_no}'.")
        return

    print("1. Update Name")
    print("2. Add a Mark")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        new_name = input("Enter new name: ").strip()
        if new_name:
            records[student_no]["name"] = new_name
            print("Name updated successfully.")
        else:
            print("Update cancelled: Name cannot be empty.")
    elif choice == "2":
        new_mark = get_valid_mark("Enter new mark to add (0-100): ")
        records[student_no]["marks"].append(new_mark)
        print("Mark added successfully.")
    else:
        print("Invalid update option.")

def delete_learner(records):
    student_no = input("Enter student number to delete: ").strip()
    if student_no not in records:
        print(f"Not found: No learner exists with student number '{student_no}'.")
        return

    confirm = input(f"Are you sure you want to delete {records[student_no]['name']} ({student_no})? (y/n): ").strip().lower()
    if confirm == "y":
        del records[student_no]
        print(f"Learner {student_no} deleted.")
    else:
        print("Deletion cancelled.")

def display_ranking(records):
    if len(records) == 0:
        print("No learner records available to rank.")
        return

    # Create a list of (average, student_number) tuples
    ranking_list = []
    for student_no, info in records.items():
        avg = mean_of(info["marks"])
        if avg is None:
            avg = 0.0
        ranking_list.append((avg, student_no))

    # Bubble sort logic in descending order by average (index 0 of tuple)
    n = len(ranking_list)
    for i in range(n):
        swapped = False
