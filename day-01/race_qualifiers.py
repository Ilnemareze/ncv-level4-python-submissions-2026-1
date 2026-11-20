# 5 km Fun Run Program

num_athletes = int(input("How many athletes entered? "))

qualifiers = 0
valid_entries = 0

winner_name = ""
winner_time = ""
winner_total_seconds = -1

for i in range(num_athletes):

    name = input("Enter athlete name: ")
    time_str = input("Enter time (mm:ss): ")

    # Check format contains :
    if ":" not in time_str:
        print("Invalid time ignored.")
        continue

    parts = time_str.split(":")

    # Must have exactly two parts
    if len(parts) != 2:
        print("Invalid time ignored.")
        continue

    minutes = parts[0]
    seconds = parts[1]

    # Minutes and seconds must be numeric
    if not minutes.isdigit() or not seconds.isdigit():
        print("Invalid time ignored.")
        continue

    minutes = int(minutes)
    seconds = int(seconds)

    # Invalid examples: abc, 5, 22:75
    if seconds > 59 or minutes < 10:
        print("Invalid time ignored.")
        continue

    valid_entries += 1

    # Count qualifiers (25:00 or less)
    if minutes < 25:
        qualifiers += 1
    elif minutes == 25 and seconds == 0:
        qualifiers += 1

    # Convert time to seconds for comparison
    total_seconds = minutes * 60 + seconds

    # Find winner
    if winner_total_seconds == -1:
        winner_name = name
        winner_time = time_str
        winner_total_seconds = total_seconds
    else:
        if total_seconds < winner_total_seconds:
            winner_name = name
            winner_time = time_str
            winner_total_seconds = total_seconds

# Output
if valid_entries == 0:
    print("Winner: None; Qualified 0 out of 0")
else:
    print(f"Winner: {winner_name} ({winner_time}); Qualified {qualifiers} out of {valid_entries}")