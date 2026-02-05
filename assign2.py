raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
print("Is ID05 in unique_users?", "ID05" in unique_users)
print("Length of raw_logs:", len(raw_logs))
print("Length of unique_users:", len(unique_users))
print("Unique users:", unique_users)