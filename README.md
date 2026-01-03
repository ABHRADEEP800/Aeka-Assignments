# 🚀 Aeka Technical Assignments

### Solutions by Abhradeep Biswas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Google Looker](https://img.shields.io/badge/Looker-4285F4?style=for-the-badge&logo=google-looker-studio&logoColor=white)

## 📖 Overview

This repository hosts the complete suite of technical solutions for the **Aeka** assessment. The projects demonstrate competencies in **Data Engineering**, **Machine Learning**, and **Business Intelligence**.

Each assignment is organized into its own dedicated directory containing the source code, relevant datasets, and specific documentation instructions.

---

## 📂 Project Structure

```text
Aeka-Assignments/
│
├── 1. Weekend Getaway Ranker/      # Data Engineering Assignment
│   ├── code.py                     # Recommendation Engine Logic
│   ├── Top Indian Places to Visit.csv
│   └── README.md                   # Execution steps for this specific tool
│
├── 2. Spotify Lyric Search/        # Machine Learning Assignment
│   ├── code.py                     # PyTorch Search Algorithm
│   ├── Spotify Million Song Dataset_exported.csv
│   └── README.md                   # Execution steps for this specific tool
│
└── 3. Cricket World Cup Dashboard/ # BI & Visualization Assignment
    ├── match_results.csv           # Cleaned Data
    ├── batting_stats.csv           # Batting Metrics
    ├── bowling_stats.csv           # Bowling Metrics
    └── README.md                   # Dashboard Link & Analysis

```

---

## 🛠️ Assignment Summaries

### [1. Weekend Getaway Ranker](https://github.com/ABHRADEEP800/Aeka-Assignments/tree/main/Weekend%20Getaway%20Ranker)

**Domain:** Data Engineering

* **🎯 Goal:** Build a location-based recommendation engine for travel destinations in India.
* **✨ Key Features:**
* **Enriched Geospatial Data:** Added missing coordinates for major Indian cities to enable spatial calculations.
* **Real-time Distance Logic:** Implemented the **Haversine Formula** to calculate accurate travel distances from the user's input city.
* **Smart Ranking:** A weighted algorithm that balances *Distance (50%)*, *Rating (30%)*, and *Popularity (20%)*.


* **🛠 Tech Stack:**
> `Python` `Pandas` `NumPy`



### [2. Spotify Lyric Search](https://github.com/ABHRADEEP800/Aeka-Assignments/tree/main/Spotify%20Lyric%20Search)

**Domain:** Machine Learning (NLP)

* **🎯 Goal:** Develop an algorithm to identify songs from short lyric snippets.
* **✨ Key Features:**
* **Content-Based Retrieval:** Implemented a search engine rather than a classifier to handle 50,000+ potential classes.
* **TF-IDF Vectorization:** Preprocessing pipeline including tokenization, stop-word removal, and n-grams.
* **Scalable Search:** Utilized **PyTorch Sparse Tensors** to perform instant similarity matching across the entire ~57,000 song dataset.


* **🛠 Tech Stack:**
> `Python` `PyTorch` `Scikit-Learn`



### [3. Cricket World Cup Dashboard](https://github.com/ABHRADEEP800/Aeka-Assignments/tree/main/Cricket%20World%20Cup%20Dashboard)

**Domain:** Business Intelligence & Visualization

* **🎯 Goal:** Analyze match results and player performance for the 2024 T20 World Cup.
* **✨ Key Features:**
* **Interactive Filters:** Dynamic drilling by Country, Player, and Venue.
* **Geospatial Intelligence:** Bubble maps visualizing winning margins by venue location.
* **Advanced Metrics:** Comparative analytics for batting aggression (Strike Rate/Boundaries) and bowling efficiency.


* **🛠 Tech Stack:**
> `Google Looker Studio` `Google Sheets`



---

## ⚙️ Global Prerequisites

To run the Python-based assignments (Projects 1 & 2), ensure you have the following libraries installed globally:

```bash
# Core Dependencies
pip install pandas numpy

# For ML Assignment (Project 2)
pip install torch scikit-learn

```

> **Note:** Please navigate to the specific folders and read the individual `README.md` files for detailed "How to Run" instructions and file path configurations.

---

## 👤 Author

* **Name:** Abhradeep Biswas
* **Date:** January 2026
