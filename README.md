# 🚀 Aeka Technical Assignments

### Solutions by Abhradeep Biswas

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

* **Goal:** Build a location-based recommendation engine for travel destinations in India.
* **Key Features:**
* Enriched geospatial data for Indian cities.
* Real-time distance calculation using the **Haversine Formula**.
* Weighted ranking algorithm (Distance vs. Popularity vs. Rating).


* **Tech Stack:** Python, Pandas, NumPy.

### [2. Spotify Lyric Search](https://github.com/ABHRADEEP800/Aeka-Assignments/tree/main/Spotify%20Lyric%20Search)

**Domain:** Machine Learning (NLP)

* **Goal:** Develop an algorithm to identify songs from short lyric snippets.
* **Key Features:**
* **Content-Based Information Retrieval** system.
* **TF-IDF Vectorization** for text preprocessing.
* **PyTorch Sparse Tensors** for scalable, high-speed similarity search across ~57,000 songs.


* **Tech Stack:** Python, PyTorch, Scikit-Learn.

### [3. Cricket World Cup Dashboard](https://github.com/ABHRADEEP800/Aeka-Assignments/tree/main/BI%20%26%20Data%20Visualization)

**Domain:** Business Intelligence & Visualization

* **Goal:** Analyze match results and player performance for the 2024 T20 World Cup.
* **Key Features:**
* Interactive filtering by Country, Player, and Venue.
* Geospatial mapping of match winners.
* Comparative analytics for batting aggression and bowling economy.


* **Tech Stack:** Google Looker Studio, Google Sheets.

---

## ⚙️ Global Prerequisites

To run the Python-based assignments (Projects 1 & 2), ensure you have the following libraries installed globally:

```bash
# Core Dependencies
pip install pandas numpy

# For ML Assignment (Project 2)
pip install torch scikit-learn

```

*Note: Please navigate to the specific folders and read the individual `README.md` files for detailed "How to Run" instructions and file path configurations.*

---

## 👤 Author

* **Name:** Abhradeep Biswas
* **Date:** January 2026