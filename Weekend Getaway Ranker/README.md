
# 🚗 Weekend Getaway Ranker

### 4. Data Engineering Assignment

## 📖 Project Overview

This project is a Python-based **Travel Recommendation Engine** designed to suggest the best weekend destinations based on a user's current location. Utilizing the **"Top Indian Places to Visit"** dataset, the algorithm calculates and ranks destinations by balancing travel distance, popularity, and user ratings.

The tool solves a key data gap in the original dataset (lack of geospatial data) by integrating a custom coordinate dictionary to perform real-time distance calculations using the **Haversine formula**.

---

## 📂 Files Included

1. **`code.py`**: The main Python script containing the recommendation logic, coordinate database, and user interface.
2. **`Top Indian Places to Visit.csv`**: The dataset containing metadata for over 300 tourist destinations across India (Ratings, Type, Significance, etc.).

---

## 🛠️ Technologies & Logic

* **Python**: Core programming language.
* **Pandas & NumPy**: Used for data manipulation, vectorization, and efficient sorting.
* **Haversine Formula**: Implemented to calculate the "Great Circle" distance between the source city and potential destinations.

### Ranking Algorithm

The engine calculates a **Final Score** for each destination based on three weighted factors:

1. **Distance (50%)**: Penalizes locations that are too far (>500km) to ensure they are viable for a "Weekend" trip.
2. **Rating (30%)**: Normalizes Google Review ratings (0-5 scale).
3. **Popularity (20%)**: Normalizes the volume of reviews to identify trending spots.

---

## ⚙️ Setup & Configuration

**⚠️ CRITICAL STEP: File Path Configuration**

Before running the script, you must ensure the code can find the CSV file. If the file is not in the exact same folder as the script, you need to provide the **Full Absolute Path**.

1. Open `code.py` in a text editor.
2. Locate the variable `csv_path` near the top of the file.
3. Replace the default filename with the full path to the file on your machine.

**Example:**

```python
# Change this:
csv_path = "Top Indian Places to Visit.csv"

# To this (Example for Linux/Mac):
csv_path = "/home/abhra/projects/Aeka-assingment/Aeka-Assignments/Top Indian Places to Visit.csv"

# Or this (Example for Windows):
csv_path = r"C:\Users\Abhra\Downloads\Top Indian Places to Visit.csv"

```

---

## 🚀 How to Run the Project

### 1. Install Prerequisites

Ensure you have Python installed along with the required libraries:

```bash
pip install pandas numpy

```

### 2. Execute the Script

Run the script using your terminal or command prompt:

```bash
python code.py

```

### 3. Enter Input

When prompted, type the name of your current city (e.g., *Delhi*, *Mumbai*, *Bangalore*).

---

## 💻 Sample Output

Below is an actual execution log generated from the script:

```text
abhra@abhrdeeps-laptop:~/projects/Aeka-assingment/Aeka-Assignments$ /bin/python "/home/abhra/projects/Aeka-assingment/Aeka-Assignments/Weekend Getaway Ranker/code.py"
Enter Source City (e.g., Bangalore, Mumbai, Delhi): Delhi

Top Weekend Getaways from Delhi:
                           Name        City           State            Type  Distance_km  Google review rating
                      Taj Mahal        Agra   Uttar Pradesh       Mausoleum   178.060539                   4.6
                      Agra Fort        Agra   Uttar Pradesh            Fort   178.060539                   4.5
               Gateway of India      Mumbai      Maharastra        Monument  1148.094873                   4.6
                     Amber Fort      Jaipur       Rajasthan            Fort   235.290240                   4.6
Golden Temple (Harmandir Sahib)    Amritsar          Punjab  Religious Site   404.050031                   4.9
                     Hawa Mahal      Jaipur       Rajasthan          Palace   235.290240                   4.4
                   Pushkar Lake     Pushkar       Rajasthan          Temple   352.847250                   4.4
             Albert Hall Museum      Jaipur       Rajasthan          Museum   235.290240                   4.5
                   Har Ki Pauri    Haridwar     Uttarakhand            Ghat   174.678386                   4.5
                    Rock Garden  Chandigarh          Punjab       Sculpture   239.292657                   4.5

```

---

## 👤 Author

* **Name:** Abhradeep Biswas
* **Assignment:** Data Engineering - Weekend Getaway Ranker
* **Date:** January 2026