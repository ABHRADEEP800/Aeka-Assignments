import pandas as pd
import numpy as np
import torch
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# ==========================================
# CONFIGURATION
# ==========================================
# Ensure this matches your actual file location
csv_path = "/home/abhra/projects/Aeka-assingment/Aeka-Assignments/Spotify Lyric Search/Spotify Million Song Dataset_exported.csv"

class LyricSearchEngine:
    def __init__(self, dataset_path):
        print("⏳ Loading dataset... (This may take a moment)")
        if not os.path.exists(dataset_path):
            raise FileNotFoundError(f"File not found: {dataset_path}")
            
        self.df = pd.read_csv(dataset_path)
        
        # Basic cleaning: drop rows with missing lyrics
        self.df = self.df.dropna(subset=['text'])
        self.lyrics_data = self.df['text'].tolist()
        
        print(f"✅ Loaded {len(self.df)} songs.")
        
        # Initialize the Model
        self._build_model()

    def _build_model(self):
        print("⚙️  Building PyTorch Vectorization Model...")
        
        # 1. Preprocessing & Vectorization (Using Scikit-Learn for TF-IDF)
        #    - stop_words='english': Removes common words like "the", "and"
        #    - max_features=20000: Keeps top 20k vocabulary
        #    - ngram_range=(1,2): Captures single words and pairs (e.g., "love you")
        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            max_features=20000, 
            ngram_range=(1, 2)
        )
        
        print("   Tokenizing and creating vectors...")
        # This creates a Sparse Matrix (efficient memory usage)
        tfidf_matrix = self.vectorizer.fit_transform(self.lyrics_data)
        
        # 2. Convert to PyTorch Tensor
        #    We convert the Scikit-Learn sparse matrix to a PyTorch Sparse Tensor
        print("   Converting to PyTorch Tensors...")
        coo = tfidf_matrix.tocoo()
        values = coo.data
        indices = np.vstack((coo.row, coo.col))
        
        i = torch.LongTensor(indices)
        v = torch.FloatTensor(values)
        shape = coo.shape
        
        # Create the sparse tensor and move to GPU if available
        self.database_vectors = torch.sparse_coo_tensor(i, v, torch.Size(shape))
        
        # Normalize for Cosine Similarity
        # (For sparse tensors, we normalize 'on the fly' or rely on TF-IDF normalization)
        # Scikit-learn's TfidfVectorizer returns normalized vectors (L2) by default!
        # So we don't need to re-normalize manually in PyTorch.
        
        print("✅ Model Ready!")

    def search(self, query_text, top_k=3):
        """
        Finds the song matching the query_text snippet.
        """
        # 1. Vectorize Query
        query_vector_sparse = self.vectorizer.transform([query_text])
        
        # Convert query to Dense Tensor for matrix multiplication
        # (Query is small, so dense is fine and faster for multiplication)
        query_tensor = torch.FloatTensor(query_vector_sparse.todense())
        
        # 2. Calculate Cosine Similarity
        #    Similarity = (A . B) / (|A| * |B|)
        #    Since vectors are already L2 normalized by TfidfVectorizer:
        #    Similarity = A . B
        
        # Perform Sparse Matrix Multiplication: (N_songs x Vocab) * (Vocab x 1)
        # We transpose query to shape (Vocab, 1)
        scores = torch.sparse.mm(self.database_vectors, query_tensor.t()).flatten()
        
        # 3. Find Top K matches
        top_scores, top_indices = torch.topk(scores, k=top_k)
        
        results = []
        for i in range(top_k):
            score = top_scores[i].item()
            index = top_indices[i].item()
            
            # Filter weak matches (Threshold can be adjusted)
            if score < 0.1: continue
                
            song_info = self.df.iloc[index]
            snippet = song_info['text'].replace('\n', ' ')[:100] + "..."
            
            results.append({
                'rank': i+1,
                'score': f"{score:.4f}",
                'song': song_info['song'],
                'artist': song_info['artist'],
                'snippet': snippet
            })
            
        return results

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    try:
        # Initialize Engine
        engine = LyricSearchEngine(csv_path)
        
        while True:
            print("\n" + "="*40)
            user_input = input("🎤 Enter a lyric snippet (or 'q' to quit): ")
            
            if user_input.lower() == 'q':
                break
                
            if len(user_input.strip()) < 5:
                print("⚠️  Please enter a longer snippet for better accuracy.")
                continue
            
            # Add a simple loading indicator
            print("   🔍 Searching...")
            matches = engine.search(user_input)
            
            if not matches:
                print("❌ No confident matches found.")
            else:
                print(f"\n🎵 Top Match for '{user_input}':")
                for m in matches:
                    print(f"   {m['rank']}. {m['song']} - {m['artist']}")
                    print(f"      Confidence: {m['score']}")
                    print(f"      Snippet: \"{m['snippet']}\"")
                    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Tip: Check if the CSV file path is correct.")