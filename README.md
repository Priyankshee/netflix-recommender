# 🎬 Netflix Movie Recommender System

A content-based movie recommendation system built using the **Netflix Movies and TV Shows** dataset from Kaggle. This web app recommends similar movies or shows based on the title you enter.

---

## 🔍 Features

- 🔎 Search for any movie or show from the dataset
- 🎯 Get top 5 similar recommendations instantly
- 🧠 Content-based filtering using cosine similarity
- 🌐 Clean web interface built with Flask and HTML

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Scikit-learn**
- **Flask**
- **HTML, CSS, JavaScript**

---

## 🧠 How It Works

1. Combines important features like `title`, `cast`, `director`, `genres`, and `description`
2. Applies **TF-IDF Vectorization** to convert text to numbers
3. Calculates **cosine similarity** between all titles
4. Returns the top 5 most similar titles for any input

---

## 📁 Project Structure

netflix-recommender/
├── dataset/
│   └── netflix_titles.csv
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── result.html
├── app.py
├── recommender.py
├── requirements.txt
└── README.md

