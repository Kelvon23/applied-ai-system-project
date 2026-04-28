"""
Command line runner for the Music Recommender Simulation.
Now with RAG-powered Gemini explanations and input guardrails.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from recommender import load_songs, recommend_songs
from gemini_explainer import explain_recommendations

VALID_GENRES = ["pop", "rock", "lofi", "jazz", "hip-hop", "classical", "folk", "metal", "r&b", "electronic", "ambient", "synthwave", "indie pop", "reggaeton", "funk", "world", "country"]
VALID_MOODS = ["happy", "sad", "chill", "intense", "energetic", "romantic", "melancholic", "angry", "relaxed", "focused", "moody", "peaceful", "calm", "upbeat", "confident"]

def validate_input(user_prefs: dict) -> list:
    """Guardrail: check for missing or invalid user preferences."""
    errors = []

    genre = user_prefs.get("genre", "").strip().lower()
    mood = user_prefs.get("mood", "").strip().lower()

    if not genre:
        errors.append("Genre cannot be empty.")
    elif genre not in VALID_GENRES:
        errors.append(f"Genre '{genre}' not recognized. Valid options: {', '.join(VALID_GENRES)}")

    if not mood:
        errors.append("Mood cannot be empty.")
    elif mood not in VALID_MOODS:
        errors.append(f"Mood '{mood}' not recognized. Valid options: {', '.join(VALID_MOODS)}")

    for field in ["target_energy", "target_danceability", "target_acousticness"]:
        val = user_prefs.get(field)
        if val is None or not (0.0 <= val <= 1.0):
            errors.append(f"{field} must be a number between 0.0 and 1.0.")

    return errors

def get_float_input(prompt: str) -> float:
    """Keep asking until the user gives a valid float between 0.0 and 1.0."""
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if 0.0 <= val <= 1.0:
                return val
            else:
                print("   ⚠️  Please enter a number between 0.0 and 1.0.")
        except ValueError:
            print("   ⚠️  That doesn't look like a number. Try something like 0.7")

def get_user_input() -> dict:
    """Prompt the user to enter their music preferences with guardrails."""
    print("\n" + "=" * 50)
    print("  🎵 Music Recommender - Tell us your vibe!")
    print("=" * 50)

    # Genre input with validation loop
    while True:
        genre = input(f"\nWhat genre do you like?\n  Options: {', '.join(VALID_GENRES)}\n  > ").strip().lower()
        if genre in VALID_GENRES:
            break
        print(f"   ⚠️  '{genre}' not recognized. Please pick from the list above.")

    # Mood input with validation loop
    while True:
        mood = input(f"\nWhat mood are you in?\n  Options: {', '.join(VALID_MOODS)}\n  > ").strip().lower()
        if mood in VALID_MOODS:
            break
        print(f"   ⚠️  '{mood}' not recognized. Please pick from the list above.")

    energy = get_float_input("\nTarget energy level? (0.0 = very calm, 1.0 = very intense)\n  > ")
    danceability = get_float_input("\nTarget danceability? (0.0 = not danceable, 1.0 = very danceable)\n  > ")
    acousticness = get_float_input("\nTarget acousticness? (0.0 = electronic, 1.0 = fully acoustic)\n  > ")

    return {
        "genre": genre,
        "mood": mood,
        "target_energy": energy,
        "target_danceability": danceability,
        "target_acousticness": acousticness,
    }

def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = get_user_input()

    # Final guardrail check before proceeding
    errors = validate_input(user_prefs)
    if errors:
        print("\n⚠️  Something slipped through validation:")
        for error in errors:
            print(f"   - {error}")
        print("Please restart and try again.")
        return

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
    print("  🤖 Gemini AI Explanation")
    print("=" * 50)
    print("\n⏳ Asking Gemini to explain your recommendations...")
    gemini_explanation = explain_recommendations(user_prefs, recommendations)
    print(f"\n{gemini_explanation}")
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()