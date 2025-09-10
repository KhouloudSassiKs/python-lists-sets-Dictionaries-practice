def recommend_movies(user_history, popular_movies, unpopular_movies):
    """
    Recommend movies to a user based on their history and popularity lists.

    Args:
        user_history (iterable): Movies the user has already watched.
        popular_movies (iterable): List of popular movies.
        unpopular_movies (iterable): List of unpopular movies to avoid.

    Returns:
        list: Sorted list of recommended movies that are popular, 
              not watched by the user, and not unpopular.
    """
    # Convert inputs to sets for efficient operations
    watched = set(user_history)
    popular = set(popular_movies)
    unpopular = set(unpopular_movies)

    # Compute popular movies the user hasn't watched yet
    unwatched_popular = popular - watched

    # Exclude unpopular movies
    recommended = unwatched_popular - unpopular

    # Return sorted list
    return sorted(recommended)


if __name__ == "__main__":
    # Example usages
    print(recommend_movies(
        ["Movie A", "Movie B"],
        ["Movie B", "Movie C", "Movie D"],
        ["Movie D"]
    ))
    # Output: ['Movie C']

    print(recommend_movies(
        [],
        ["Movie X", "Movie Y"],
        ["Movie Y"]
    ))
    # Output: ['Movie X']

    print(recommend_movies(
        ["Movie A"],
        ["Movie A", "Movie B"],
        ["Movie C"]
    ))
    # Output: ['Movie B']
