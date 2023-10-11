# Lab_4: Get statistics of the site (total visits, unique visits)

users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# Create dictionary with empty values
statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

total_visits = len(users)  # total amount of visits
unique_visits = len(set(users))  # unique visits amount

# Renew values in the dictionary using keys
statistics["Общее количество"] = total_visits
statistics["Уникальные посещения"] = unique_visits

# Output
print(statistics)
