
# 🌟 Smart Recommendation System with Sentiment Analysis

This project is a personalized recommendation system that suggests experiences (e.g., restaurants, activities, outings) based on user preferences and mood. The system uses content-based filtering and integrates sentiment analysis to refine recommendations based on the user's emotional tone.

---

## 🔍 Features

- ✅ Personalized recommendations based on cuisine and activity preferences
- 😊 Sentiment analysis using TextBlob to detect user mood
- 🧠 Content-based filtering using TF-IDF and cosine similarity
- 🎯 Adjustable suggestions depending on positive, neutral, or negative sentiment
- 🌐 Streamlit web interface for interactive use

---

## 📂 Project Structure



smart-recommendation-system/
│
├── app.py                # Streamlit app
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation



---

## 🚀 How to Run

### 🔧 Prerequisites

Install the required libraries:

```bash
pip install -r requirements.txt
````

### ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📊 Sample Usage

1. Enter your **user ID** (based on predefined preferences).
2. Type how you're feeling (e.g., "I'm feeling tired and stressed").
3. The system will:

   * Detect the **mood** from your input
   * Filter and rank relevant experiences
   * Show the best matching suggestions

---

## 🧠 Tech Stack

* **Python 3**
* **Streamlit** – Web interface
* **TextBlob** – Sentiment analysis
* **Scikit-learn** – TF-IDF & similarity
* **Pandas/Numpy** – Data processing

---

## 📈 Example Output

```
Detected Mood: negative

Recommended Experiences:
- Spa Retreat      | relaxing wellness spa
- La Pasta         | italian dining relaxing
```

---

## 🙋‍♂️ Author

Kabir Kohli
B.Tech Automation & Robotics
Guru Gobind Singh Indraprastha University

---

## 📄 License

This project is open-source and free to use for educational purposes.

