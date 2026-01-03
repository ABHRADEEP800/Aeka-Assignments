
# 🎵 Spotify Lyric Search Engine

### 5. Machine Learning Project

## 📖 Project Overview

This project implements a **Content-Based Information Retrieval System** using **PyTorch**. It is designed to identify a song's **Title** and **Artist** when provided with a short snippet of lyrics.

The system processes a dataset of **~57,000 songs**, converting lyrics into mathematical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**. It then utilizes **PyTorch Sparse Tensors** to perform high-speed similarity searches, finding the closest matching songs based on the user's input.

---

## 📂 Files Included

1. **`code.py`**: The main Python script containing the PyTorch model, vectorization logic, and search interface.
2. **`Spotify Million Song Dataset_exported.csv`**: The dataset containing Artist names, Song Titles, and full Lyrics.

---

## 🛠️ Technologies & Logic

* **Python**: Core programming language.
* **PyTorch**: utilized for high-performance matrix operations (`torch.sparse.mm`) to calculate similarity scores instantly across thousands of songs.
* **Scikit-Learn**: Used for the `TfidfVectorizer` to handle text preprocessing (Tokenization, Stop-word removal, and N-gram generation).
* **Pandas**: For efficient data loading and management.

### How It Works

1. **Ingestion**: Loads ~57,000 songs and removes empty rows.
2. **Vectorization**:
* Converts lyrics into a **Sparse Matrix** using TF-IDF, which prioritizes unique/meaningful words over common ones (like "the" or "and").
* Transforms this matrix into a **PyTorch Sparse Tensor** for memory-efficient computation.


3. **Search**:
* The model vectorizes the user's input snippet.
* It calculates the **Cosine Similarity** (Dot Product) between the input and the entire database.
* It returns the top 3 matches with their confidence scores.



---

## ⚙️ Setup & Configuration

**⚠️ CRITICAL STEP: File Path Configuration**

Before running the script, you must tell the code where your CSV file is located.

1. Open `code.py` in a text editor.
2. Locate the variable `csv_path` near the top.
3. Replace the default value with the **Full Absolute Path** to your downloaded CSV file.

**Example:**

```python
# Linux/Mac
csv_path = "/home/abhra/projects/Aeka-Assignments/Spotify Million Song Dataset_exported.csv"

# Windows
csv_path = r"C:\Users\Abhra\Downloads\Spotify Million Song Dataset_exported.csv"

```

---

## 🚀 How to Run

### 1. Install Prerequisites

Run the following command to install the necessary libraries:

```bash
pip install torch pandas scikit-learn numpy

```

### 2. Run the Engine

Execute the script from your terminal:

```bash
python code.py

```

### 3. Usage

When prompted, type a lyric snippet. The engine will display the top ranked matches based on textual similarity.

---

## 💻 Sample Output

Below is an actual execution log showing the model identifying songs based on the lyric snippet *"Is this the real life is this just fantasy"*:

```text
⏳ Loading dataset... (This may take a moment)
✅ Loaded 57650 songs.
⚙️  Building PyTorch Vectorization Model...
   Tokenizing and creating vectors...
   Converting to PyTorch Tensors...
✅ Model Ready!

========================================
🎤 Enter a lyric snippet (or 'q' to quit): Is this the real life is this just fantasy
   🔍 Searching...

🎵 Top Match for 'Is this the real life is this just fantasy':
   1. Sometimes A Fantasy - Billy Joel
      Confidence: 0.5607
      Snippet: "I didn't want to do it but I got too lonely   I had to call you up in the middle of the night   I kn..."
   2. In Real Life - Demi Lovato
      Confidence: 0.4927
      Snippet: "In real life I'm waking up alone   It's one more night you didn't make it home   And one more time y..."
   3. Real Life - The Weeknd
      Confidence: 0.4738
      Snippet: "[Verse 1]   Tell 'em this boy wasn't meant for lovin'   Tell 'em this heart doesn't stay to one   I'..."

```

---

## 👤 Author

* **Name:** Abhradeep Biswas
* **Assignment:** Machine Learning - Spotify Lyric Search
* **Date:** January 2026