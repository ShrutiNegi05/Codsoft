user_preferences = {
    'User1': {'Movie1': 5, 'Movie2': 4, 'Movie3': 2, 'Movie4': 3},
    'User2': {'Movie1': 3, 'Movie2': 5, 'Movie3': 4, 'Movie5': 2},
    'User3': {'Movie2': 3, 'Movie3': 5, 'Movie4': 4, 'Movie5': 1},
    'User4': {'Movie1': 4, 'Movie3': 3, 'Movie4': 5, 'Movie5': 2}
}

def calculate_similarity(user1_prefs, user2_prefs):
    common_items = set(user1_prefs.keys()) & set(user2_prefs.keys())
    
    if not common_items:
        return 0
    
    numerator = sum(user1_prefs[item] * user2_prefs[item] for item in common_items)
    
    sum_squares_user1 = sum(user1_prefs[item] ** 2 for item in user1_prefs)
    sum_squares_user2 = sum(user2_prefs[item] ** 2 for item in user2_prefs)
    
    denominator = (sum_squares_user1 ** 0.5) * (sum_squares_user2 ** 0.5)
    
    if denominator == 0:
        return 0
    
    return numerator / denominator

def recommend_items(users, target_user):
    recommendations = {}
    
    for user, prefs in users.items():
        if user != target_user:
            similarity = calculate_similarity(users[target_user], prefs)
            
            for item, score in prefs.items():
                if item not in users[target_user] or users[target_user][item] == 0:
                    recommendations[item] = recommendations.get(item, 0) + score * similarity
    
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_recommendations

target_user = 'User4'
recommendations = recommend_items(user_preferences, target_user)

print(f"Recommendations for {target_user}: {recommendations}")
