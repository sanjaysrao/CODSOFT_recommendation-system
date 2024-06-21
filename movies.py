movies_data = {
    'The Lion King': ['Drama'],
    'Jersey': ['Drama', 'Sport'],
    'The Mummy': ['Action', 'Adventure', 'Thriller'],
    'Titanic': ['Comedy', 'Romance'],
    'The Avatar': ['Action', 'Adventure', 'Fantasy'],
    'Senior Year': ['Drama', 'Romance'],
    'Home Alone': ['Comedy', 'Drama'],
    'RRR': ['Drama', 'Action'],
    'King Kong': ['Adventure'],
    'The Adventures of Robin Hood': ['Adventure', 'Drama', 'Action'],
    'The Treasure of the Sierra Madre': ['Adventure'],
    'Raiders of the Lost Ark': ['Adventure'],
    'Jurassic Park': ['Adventure']
}
def calculate_similarity(movie_genres, user_preferences):
    movie_genres_lower = [genre.lower() for genre in movie_genres]
    user_preferences_lower = [preference.lower() for preference in user_preferences]
    common_genres = set(movie_genres_lower).intersection(set(user_preferences_lower))
    return len(common_genres)
def recommend_movies(user_preferences):
    similarity_scores = {}
    for movie, genres in movies_data.items():
        score = calculate_similarity(genres, user_preferences)
        if score > 0:
            similarity_scores[movie] = score
    sorted_movies = sorted(similarity_scores.items(), key=lambda item: item[1], reverse=True)
    return [movie for movie, score in sorted_movies]
def get_user_preferences():
    print("Enter your preferred genres (comma-separated):")
    user_input = input().strip().split(',')
    return [genre.strip() for genre in user_input]
def main():
    print("Welcome to the Movie Recommendation System!")
    while True:
        user_preferences = get_user_preferences()
        recommended_movies = recommend_movies(user_preferences)
        if recommended_movies:
            print(f"Based on your preferences, we recommend the following movies:")
            for movie in recommended_movies:
                print(movie)
        else:
            print("No movies found for the given preferences.")
        print("Do you want to get more recommendations? (yes/no)")
        if input().strip().lower() != 'yes':
            break
if __name__ == "__main__":
    main()
