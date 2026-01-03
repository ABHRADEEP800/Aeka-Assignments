import pandas as pd
import numpy as np

# Load the dataset
# provide the full path of the CSV file
csv_path = "/home/abhra/projects/Aeka-assingment/Aeka-Assignments/Weekend Getaway Ranker/Top Indian Places to Visit.csv"

# Enriched Coordinate Dictionary
city_coords = {
    'Delhi': (28.6139, 77.2090), 'New Delhi': (28.6139, 77.2090),
    'Mumbai': (19.0760, 72.8777), 'Bangalore': (12.9716, 77.5946),
    'Bengaluru': (12.9716, 77.5946), 'Hyderabad': (17.3850, 78.4867),
    'Chennai': (13.0827, 80.2707), 'Kolkata': (22.5726, 88.3639),
    'Pune': (18.5204, 73.8567), 'Ahmedabad': (23.0225, 72.5714),
    'Jaipur': (26.9124, 75.7873), 'Lucknow': (26.8467, 80.9462),
    'Chandigarh': (30.7333, 76.7794), 'Surat': (21.1702, 72.8311),
    'Indore': (22.7196, 75.8577), 'Bhopal': (23.2599, 77.4126),
    'Patna': (25.5941, 85.1376), 'Visakhapatnam': (17.6868, 83.2185),
    'Vadodara': (22.3072, 73.1812), 'Ludhiana': (30.9010, 75.8573),
    'Agra': (27.1767, 78.0081), 'Nashik': (19.9975, 73.7898),
    'Nagpur': (21.1458, 79.0882), 'Coimbatore': (11.0168, 76.9558),
    'Thiruvananthapuram': (8.5241, 76.9366), 'Kozhikode': (11.2588, 75.7804),
    'Madurai': (9.9252, 78.1198), 'Vijayawada': (16.5062, 80.6480),
    'Bhubaneswar': (20.2961, 85.8245), 'Guwahati': (26.1445, 91.7362),
    'Lonavala': (18.7515, 73.4056), 'Mahabaleshwar': (17.9237, 73.6586),
    'Alibaug': (18.6414, 72.8722), 'Matheran': (18.9868, 73.2679),
    'Coorg': (12.3375, 75.8069), 'Ooty': (11.4102, 76.6950),
    'Mysore': (12.2958, 76.6394), 'Chikmagalur': (13.3153, 75.7754),
    'Wayanad': (11.6854, 76.1320), 'Munnar': (10.0889, 77.0595),
    'Kodaikanal': (10.2381, 77.4892), 'Puducherry': (11.9416, 79.8083),
    'Mahabalipuram': (12.6208, 80.1973), 'Rishikesh': (30.0869, 78.2676),
    'Haridwar': (29.9457, 78.1642), 'Mussoorie': (30.4598, 78.0664),
    'Nainital': (29.3803, 79.4637), 'Shimla': (31.1048, 77.1734),
    'Manali': (32.2432, 77.1892), 'Dehradun': (30.6288, 78.0435),
    'Dharamshala': (32.2190, 76.3239), 'Dalhousie': (32.5354, 75.9719),
    'Amritsar': (31.6340, 74.8723), 'Varanasi': (25.3176, 82.9739),
    'Udaipur': (24.5854, 73.7125), 'Jodhpur': (26.2389, 73.0243),
    'Jaisalmer': (26.9157, 70.9083), 'Pushkar': (26.4886, 74.5509),
    'Goa': (15.2993, 74.1240), 'Gokarna': (14.5479, 74.3188),
    'Hampi': (15.3350, 76.4600), 'Puri': (19.8135, 85.8312),
    'Konark': (19.8876, 86.0945), 'Darjeeling': (27.0410, 88.2663),
    'Gangtok': (27.3314, 88.6138), 'Shillong': (25.5788, 91.8933),
    'Srinagar': (34.0837, 74.7973), 'Leh': (34.1526, 77.5771),
    'Kochi': (9.9312, 76.2673), 'Alappuzha': (9.4981, 76.3388),
    'Varkala': (8.7379, 76.7163), 'Kanyakumari': (8.0883, 77.5385),
    'Tirupati': (13.6288, 79.4192)
}

def haversine(lat1, lon1, lat2, lon2):
    """Calculates great-circle distance (km) between two points."""
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    return c * 6371

class WeekendGetawayRanker:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.city_coords = city_coords

    def recommend(self, source_city):
        # Normalize Input (Title Case)
        source_city = source_city.strip().title()
        
        # Check Coordinates & Handle Aliases
        source_coords = self.city_coords.get(source_city)
        if not source_coords:
            if source_city == 'Bengaluru': source_coords = self.city_coords.get('Bangalore')
            elif source_city == 'Bangalore': source_coords = self.city_coords.get('Bengaluru')
            
        if not source_coords:
            return f"Error: Coordinates for '{source_city}' not found in database."

        # Filter out the source city itself
        destinations = self.df[self.df['City'] != source_city].copy()

        # Calculate Distances
        def get_dist(row):
            dest_c = self.city_coords.get(row['City'])
            if dest_c:
                return haversine(source_coords[0], source_coords[1], dest_c[0], dest_c[1])
            return None

        destinations['Distance_km'] = destinations.apply(get_dist, axis=1)
        
        # Drop places where distance couldn't be calculated
        destinations = destinations.dropna(subset=['Distance_km'])

        # Filter: Exclude local spots (< 20km)
        destinations = destinations[destinations['Distance_km'] > 20]

        # Scoring Logic
        # Distance (50%): Closer is better. Decay function: 1 / (1 + Dist/100)
        destinations['Distance_Score'] = 1 / (1 + destinations['Distance_km']/100)

        # Rating (30%): Normalized 0-1
        destinations['Rating_Score'] = destinations['Google review rating'] / 5.0

        # Popularity (20%): Normalized by max reviews
        max_rev = destinations['Number of google review in lakhs'].max()
        destinations['Popularity_Score'] = destinations['Number of google review in lakhs'] / (max_rev if max_rev else 1)

        # Final Weighted Score
        destinations['Final_Score'] = (0.5 * destinations['Distance_Score'] + 
                                       0.3 * destinations['Rating_Score'] + 
                                       0.2 * destinations['Popularity_Score'])

        # Return Top 10
        return destinations.sort_values(by='Final_Score', ascending=False).head(10)

# --- Main Execution ---
if __name__ == "__main__":
    ranker = WeekendGetawayRanker(csv_path)
    
    # Take source city from user input
    user_city = input("Enter Source City (e.g., Bangalore, Mumbai, Delhi): ")
    
    recommendations = ranker.recommend(user_city)
    
    if isinstance(recommendations, str):
        print(recommendations)
    else:
        print(f"\nTop Weekend Getaways from {user_city}:")
        print(recommendations[['Name', 'City', 'State', 'Type', 'Distance_km', 'Google review rating']].to_string(index=False))