"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Profile 1: High-Energy Pop
    user_prefs = {"genre": "pop", "mood": "happy", "target_energy": 0.9, "target_danceability": 0.85, "target_acousticness": 0.1}

    # Profile 2: Chill Lofi
    # user_prefs = {"genre": "lofi", "mood": "chill", "target_energy": 0.2, "target_danceability": 0.3, "target_acousticness": 0.8}

    # Profile 3: Deep Intense Rock
    # user_prefs = {"genre": "rock", "mood": "intense", "target_energy": 0.95, "target_danceability": 0.4, "target_acousticness": 0.05}

    # --- Adversarial / Edge Case Profiles ---

    # Edge Case 1: Impossible genre+mood combo — no song has both, so mood/genre scores are always 0.
    # Only the three continuous features decide rankings; reveals scorer behavior without categorical matches.
    # user_prefs = {"genre": "metal", "mood": "happy", "target_energy": 0.9, "target_danceability": 0.5, "target_acousticness": 0.1}

    # Edge Case 2: Perfectly average — no genre/mood, all continuous prefs at 0.5.
    # Every song gets a near-identical score; exposes whether tie-breaking is deterministic or arbitrary.
    # user_prefs = {"genre": "", "mood": "", "target_energy": 0.5, "target_danceability": 0.5, "target_acousticness": 0.5}

    # Edge Case 3: Contradictory prefs — max energy AND max acousticness at the same time.
    # Acoustic songs are typically low-energy, so no song can satisfy both; shows how the scorer handles conflicting signals.
    # user_prefs = {"genre": "folk", "mood": "sad", "target_energy": 0.95, "target_danceability": 0.5, "target_acousticness": 0.95}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print("  Top 5 Song Recommendations")
    print("=" * 50)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank} {song['title']} by {song['artist']}")
        print(f"   Genre: {song['genre']} | Mood: {song['mood']}")
        print(f"   Score: {score:.2f} / 100")
        print(f"   Why:   {explanation}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
