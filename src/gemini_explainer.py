import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def explain_recommendations(user_prefs: dict, recommendations: list) -> str:
    """Send top recommendations to Gemini and get a natural language explanation."""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")

        client = genai.Client(api_key=api_key)

        song_list = "\n".join([
            f"- {song['title']} by {song['artist']} (Score: {score:.1f}/100, {explanation})"
            for song, score, explanation in recommendations
        ])

        prompt = f"""
You are a music recommendation assistant.

A user has the following taste profile:
- Genre: {user_prefs.get('genre')}
- Mood: {user_prefs.get('mood')}
- Target Energy: {user_prefs.get('target_energy')}
- Target Danceability: {user_prefs.get('target_danceability')}
- Target Acousticness: {user_prefs.get('target_acousticness')}

Based on their profile, here are the top song recommendations retrieved from the catalog:
{song_list}

In 3-4 sentences, explain why these songs are a good match for this user in a friendly, conversational tone.
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"[Gemini explanation unavailable: {str(e)}]"