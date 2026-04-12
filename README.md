# 🎵 Music Recommender Simulation

Screenshots:

### CLI Verification
![CLI Verification](assets/CLI_Verifection.png)

### Edge Case 1
![Edge Case 1](assets/Edge_Case1.png)

### Edge Case 2
![Edge Case 2](assets/Edge_case2.png)

### Edge Case 3
![Edge Case 3](assets/Edge_Case3.png)


## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

From my understanding real world system use context-based filtering and collaborative filtering to be able 
to score a song and use that towards knowing how to recommend a song to a user. For example in content-based filtering we see that they use the song itself to help match them to an individual user taste profile like lyrcis,mood and genre. 

Song Features: Genre,Mood,Energy, Dancebility
UserProfile Info: Unique ID, paylist of songs, link to songs, 
Recommender: Song Score, List of ranking songs,

My recommender will compute a score for a song based on the attrubites of a song like mood,genre,energy and danciblity and add them all up for one song. The closer a song is to what the user likes, the more the points it gets. The song with most points will get recommend. 

Algo Recipe:

The recommender takes in a user taste profile with five preferences: genre, mood, target energy, target danceability, and target acousticness

It also takes in the full list of songs loaded from songs.csv and a number k for how many recommendations to return

It then loops through every song in the list and scores each one out of 100 points

Mood is checked first as an exact string match, worth 30 points — it is the strongest signal for how a song feels

Energy is worth up to 25 points, calculated by how close the song's energy value is to the user's target

Genre is checked as an exact string match, worth 20 points

Danceability is worth up to 15 points using the same closeness calculation as energy

Acousticness is worth up to 10 points and mostly acts as a tiebreaker between songs that score similarly on everything else

As each feature is scored, a short reason string is collected to explain why the song ranked the way it did

Once every song is scored, the full list is sorted from highest to lowest score

The top k results are sliced off and returned as a combination of the song, its final score, and its explanation

Even if no song matches genre or mood exactly, the three numeric features can still award up to 50 points so the recommender always returns meaningful results

Poteinal Baises:
DataSet Size Bias - as the dataset isn't that big so some genres and moods may only appeare once or twice
Mood Weight Dominance - mood carries the most points so if dataset has several songs with the same mood then it will always cluster at the top. 


Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

