from src.recommender import load_songs, score_song, recommend_songs
from src.main import validate_input

# --- Scoring Tests ---

def test_score_song_genre_match_adds_points():
    user_prefs = {"genre": "pop", "mood": "happy", "target_energy": 0.5, "target_danceability": 0.5, "target_acousticness": 0.5}
    song = {"genre": "pop", "mood": "happy", "energy": 0.5, "danceability": 0.5, "acousticness": 0.5}
    score, reasons = score_song(user_prefs, song)
    assert score > 0
    assert any("genre match" in r for r in reasons)

def test_score_song_no_match_still_returns_score():
    user_prefs = {"genre": "metal", "mood": "angry", "target_energy": 0.5, "target_danceability": 0.5, "target_acousticness": 0.5}
    song = {"genre": "lofi", "mood": "chill", "energy": 0.5, "danceability": 0.5, "acousticness": 0.5}
    score, reasons = score_song(user_prefs, song)
    assert score >= 0

def test_recommend_songs_returns_correct_count():
    songs = [
        {"genre": "pop", "mood": "happy", "energy": 0.8, "danceability": 0.8, "acousticness": 0.2},
        {"genre": "lofi", "mood": "chill", "energy": 0.3, "danceability": 0.4, "acousticness": 0.8},
        {"genre": "rock", "mood": "intense", "energy": 0.9, "danceability": 0.6, "acousticness": 0.1},
    ]
    user_prefs = {"genre": "pop", "mood": "happy", "target_energy": 0.8, "target_danceability": 0.8, "target_acousticness": 0.2}
    results = recommend_songs(user_prefs, songs, k=2)
    assert len(results) == 2

def test_recommend_songs_sorted_by_score():
    songs = [
        {"genre": "pop", "mood": "happy", "energy": 0.8, "danceability": 0.8, "acousticness": 0.2},
        {"genre": "lofi", "mood": "chill", "energy": 0.3, "danceability": 0.4, "acousticness": 0.8},
    ]
    user_prefs = {"genre": "pop", "mood": "happy", "target_energy": 0.8, "target_danceability": 0.8, "target_acousticness": 0.2}
    results = recommend_songs(user_prefs, songs, k=2)
    assert results[0][1] >= results[1][1]

# --- Guardrail Tests ---

def test_validate_input_catches_empty_genre():
    user_prefs = {"genre": "", "mood": "happy", "target_energy": 0.5, "target_danceability": 0.5, "target_acousticness": 0.5}
    errors = validate_input(user_prefs)
    assert any("Genre" in e for e in errors)

def test_validate_input_catches_invalid_energy():
    user_prefs = {"genre": "pop", "mood": "happy", "target_energy": 1.5, "target_danceability": 0.5, "target_acousticness": 0.5}
    errors = validate_input(user_prefs)
    assert any("target_energy" in e for e in errors)

def test_validate_input_passes_valid_input():
    user_prefs = {"genre": "pop", "mood": "happy", "target_energy": 0.5, "target_danceability": 0.5, "target_acousticness": 0.5}
    errors = validate_input(user_prefs)
    assert len(errors) == 0