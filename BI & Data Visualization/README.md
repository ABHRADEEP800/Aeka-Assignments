# Cricket World Cup Insights: 2024 T20 World Cup Dashboard

### 📊 BI & Data Visualization Assignment

## 📖 Project Overview
This project involves the extraction, cleaning, and visualization of historical sports data from the **2024 ICC Men's T20 World Cup**. Using **Google Looker Studio**, I have built an interactive dashboard that identifies key patterns in match results, player aggression, and venue statistics.

The dashboard allows users to filter by country, analyze individual player performance (batting and bowling), and visualize geographical trends regarding match outcomes.

**[View Live Dashboard](https://lookerstudio.google.com/reporting/24eca934-9d20-4b90-99f0-76ff0b75e3c9)**

---

## 📂 Data Sources & Files
The data was compiled from public cricket records (ESPNCricInfo/ICC) and structured into three relational datasets:

1.  **`match_results.csv`**: Contains high-level match details, including dates, venues, toss decisions, winners, and margins of victory.
2.  **`batting_stats.csv`**: Detailed batting metrics including Runs Scored, Strike Rates, and Boundary Counts (4s & 6s).
3.  **`bowling_stats.csv`**: Detailed bowling metrics including Wickets, Economy Rates, and Bowling Averages.

---

## 🛠️ Tools Used
* **Google Sheets:** For data cleaning, schema formatting, and date standardization.
* **Google Looker Studio:** For data modeling, blending sources, and creating interactive visualizations.
* **CSV / Data Extraction:** Raw data compilation.

---

## 🌟 Dashboard Features
This project fulfills the specific assignment requirements as follows:

### 1. Country-Based Performance (Filters)
* **Feature:** A dynamic dropdown filter allows users to isolate data for specific winning teams (e.g., India, Australia).
* **Metric:** Filters update all charts to show relevant match outcomes and player contributions for that nation.

### 2. Player Analytics & Impact
* **Feature:** Comprehensive scorecards and tables replacing standard "Totals" with impact metrics.
* **Custom Metrics:**
    * **Batting:** Analyzed via *Boundary Count (4s/6s)* and *Strike Rate* to measure aggression.
    * **Bowling:** Analyzed via *Wickets* and *Economy Rate*.

### 3. Player vs. Player Comparison
* **Feature:** Side-by-side Bar Charts with **Cross-Filtering** enabled.
* **Functionality:** Clicking on a specific player (e.g., Virat Kohli) filters the entire dashboard to highlight their specific match contributions.

### 4. Trend Analysis
* **Feature:** Time Series Chart tracking the "Highest Score in an Innings" across the tournament timeline.
* **Insight:** Visualizes how scoring conditions improved as the tournament moved from New York (drop-in pitches) to the West Indies.

### 5. Geospatial Intelligence
* **Feature:** Bubble Map visualizing `Venue City` vs. `Winning Margin`.
* **Key Insight:** Specifically filters for "India Wins" to identify which venues (e.g., Bridgetown) were statistically most favorable for the Indian team.

---

## ⚙️ Methodology & Data Cleaning
* **Handling Missing Data:** Granular ball-by-ball data (Wides/No Balls) was aggregated into "Economy Rate" to provide a more strategic view of bowling efficiency.
* **Date Normalization:** All match dates were standardized to `YYYY-MM-DD` format to ensure accurate Time Series plotting.
* **Geo-Tagging:** `Venue City` fields were explicitly cast as *Geo > City* types to enable Google Maps integration.
* **Filtering:** "No Result" (Rain Abandoned) matches were filtered out of average calculations to prevent data skewing.

---

## 👤 Author
* **Name:** Abhradeep Biswas
* **Assignment:** BI & Data Visualization - Cricket World Cup Insights
* **Date:** January 2026