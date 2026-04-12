from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read a CSV file of songs and return a list of dicts with typed numeric fields."""
    import csv

    songs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness']),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song out of 100 based on mood, energy, genre, danceability, and acousticness."""
    score = 0.0
    reasons = []

    # Mood match — 30 points
    if song['mood'].lower() == user_prefs.get('mood', '').lower():
        score += 30.0
        reasons.append("mood match (+30)")

    # Energy proximity — 25 points max
    energy_diff = abs(song['energy'] - user_prefs.get('target_energy', 0.5))
    energy_points = round((1.0 - energy_diff) * 25, 2)
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points})")

    # Genre match — 20 points
    if song['genre'].lower() == user_prefs.get('genre', '').lower():
        score += 20.0
        reasons.append("genre match (+20)")

    # Danceability proximity — 15 points max
    dance_diff = abs(song['danceability'] - user_prefs.get('target_danceability', 0.5))
    dance_points = round((1.0 - dance_diff) * 15, 2)
    score += dance_points
    reasons.append(f"danceability closeness (+{dance_points})")

    # Acousticness proximity — 10 points max
    acoustic_diff = abs(song['acousticness'] - user_prefs.get('target_acousticness', 0.5))
    acoustic_points = round((1.0 - acoustic_diff) * 10, 2)
    score += acoustic_points
    reasons.append(f"acousticness closeness (+{acoustic_points})")

    return round(score, 2), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return the top k ranked highest to lowest with explanations."""
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [(song, score, ", ".join(reasons)) for song, score, reasons in scored[:k]]
