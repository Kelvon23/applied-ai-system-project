# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

SongRecommenderXD 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

My recommender was design to use content-based filtering as a way to find songs that will be good to recommend to users based on a algorithm score I came up with that will then rank and return top 5 songs that I beleive the user will enjoy. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Each song is scored out of 100 by checking five things: mood match (+30), energy closeness (+25 max), genre match (+20), danceability closeness (+15 max), and acousticness closeness (+10 max). Mood and genre are all-or-nothing exact matches, while energy, danceability, and acousticness award partial points based on how close the song is to your target. The top 5 highest-scoring songs are returned as recommendations.

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

20 songs across 15 unique genre/mood combinations. Each song has 9 attributes: title, artist, genre, mood, energy (0–1), tempo (BPM), valence (0–1), danceability (0–1), and acousticness (0–1). Most genres have exactly one song — only lofi has 3 and pop has 2. Energy skews high, with 8 songs above 0.75.

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

It works best when the user's requested genre and mood both exist as a pair in the dataset. For example in — like pop/happy or rock/intense — the top result is clear, high-scoring, and genuinely relevant. The continuous features (energy, danceability, acousticness) then do a good job separating the remaining songs into a sensible ranked order.

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 
I noticed that if a user doesn't set target_energy, the default would be 0.5. This is an issues as low energy users and high engery users both get penalized equally. As for recommendations they get will be mid energy songs will be pushed to them by deafault. Another biases is that High-energy songs cluster at the top of continous only rankings. Meaning that high - energy songs dominate bc there are simply more of them near the top of the distrubition. 


Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 
I created a High Energy Pop, Chill Lofi, and Deep Intense Rock profiles. For these profiles I was looking to see in the  recommendations output songs that would follow similar profile based on mood and energy levels. For example in High-Energy Pop, I expected songs that are upbeat, danceable, and elctric. So that meant looking for happy mood and energy levels that gave a dominant #1 with high confidence score. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

I would probably add in my next model a partial genre credit. In which I would score genres that are similar to each other some credit instead of just a 0. In the example of indie pop it got 0 due to not being same genre like pop but still it near match to it so best to it get some credit next time. 


Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

In this project I learned about how Music Streaming Services recommend songs to users. They use content-based filtering or Collaborative Filtering Alogrithms to help recommend Users the best songs they believe the user will most enjoy. I also notice while doing this project on how skewed my model could get if I suddenly change the scoring alogrithm I came up with and how that affects the output of my result of song recommendations. 

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
