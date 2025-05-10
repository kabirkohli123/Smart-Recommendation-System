import streamlit as st
import pandas as pd
from textblob import TextBlob
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

users = pd.DataFrame({
    'user_id': [1, 2],
    'preferred_cuisine': ['italian', 'chinese'],
    'preferred_activity': ['dining', 'exploring']
})

experiences = pd.DataFrame({
    'experience_id': list(range(101, 121)),
    'name': [
        'La Pasta', 'Great Wall', 'City Walk', 'Spa Retreat', 'Adventure Park',
        'Sushi World', 'Heritage Museum', 'Mountain Trek', 'Jazz Lounge', 'Vegan Delight',
        'Burger Hub', 'Desert Safari', 'Botanical Garden', 'Tech Expo', 'Art Gallery',
        'Sky Lounge', 'Yoga Retreat', 'Cycling Trail', 'Korean Kitchen', 'Book Café'
    ],
    'tags': [
        'italian dining relaxing',
        'chinese dining spicy',
        'outdoor exploring walking',
        'relaxing wellness spa',
        'thrill rides adventure outdoor',
        'japanese sushi dining calm',
        'history learning cultural quiet',
        'trekking mountain nature fitness',
        'music relaxing indoor drinks',
        'vegan healthy organic dining',
        'american fastfood casual',
        'desert adventure sunset camel',
        'nature relaxing flowers outdoor',
        'technology innovation gadgets indoor',
        'painting art culture creative',
        'rooftop music drinks luxury',
        'meditation wellness yoga peace',
        'cycling outdoor fitness sporty',
        'korean dining spicy bbq',
        'books coffee calm quiet reading'
    ],
    'cuisine': [
        'italian', 'chinese', None, None, None,
        'japanese', None, None, None, 'vegan',
        'american', None, None, None, None,
        None, None, None, 'korean', None
    ],
    'activity_type': [
        'dining', 'dining', 'exploring', 'relaxing', 'adventure',
        'dining', 'learning', 'fitness', 'entertainment', 'dining',
        'dining', 'adventure', 'relaxing', 'learning', 'learning',
        'entertainment', 'relaxing', 'fitness', 'dining', 'relaxing'
    ]
})


def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return 'positive'
    elif polarity < -0.2:
        return 'negative'
    else:
        return 'neutral'

def recommend_experiences(user_id, mood):
    user = users[users['user_id'] == user_id].iloc[0]
    
    filtered_exps = experiences[
        (experiences['cuisine'] == user['preferred_cuisine']) |
        (experiences['activity_type'] == user['preferred_activity'])
    ].copy()
    
    tfidf_matrix = tfidf.transform(filtered_exps['tags'])
    user_vector = tfidf.transform([user['preferred_cuisine'] + " " + user['preferred_activity']])
    
    scores = cosine_similarity(user_vector, tfidf_matrix).flatten()
    filtered_exps['similarity'] = scores
    
    if mood == 'negative':
        filtered_exps = filtered_exps[filtered_exps['tags'].str.contains('relaxing|spa', case=False, na=False)]
    elif mood == 'positive':
        filtered_exps = filtered_exps[filtered_exps['tags'].str.contains('adventurous|exploring', case=False, na=False)]
    
    recommendations = filtered_exps.sort_values(by='similarity', ascending=False)
    return recommendations[['name', 'tags', 'similarity']]

tfidf = TfidfVectorizer()
tfidf.fit(experiences['tags'])

st.title(" Smart Recommendation System")
user_input = st.text_area("How are you feeling today?", placeholder="e.g. I'm feeling tired and want to relax.")

if user_input:
    mood = get_sentiment(user_input)
    st.write(f"🧠 Detected Mood: **{mood}**")
    
    recommendations = recommend_experiences(user_id=1, mood=mood)
    
    if not recommendations.empty:
        st.write("### 🎯 Recommended Experiences:")
        st.dataframe(recommendations)
    else:
        st.warning("No matching experiences found for your mood.")
