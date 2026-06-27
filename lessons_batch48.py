"""
Batch 48: Adding Unsupervised Learning to Data Science
"""
import json, os

NEW_COURSES_BATCH48 = {
    "Unsupervised Learning": {
        "tier": "Intermediate",
        "aiRubric": "Assess clustering and unsupervised learning concepts",
        "lessons": [
            {"title": "K-Means Clustering", "theory": "## Finding Patterns\\nUnsupervised learning models do not have target labels (y). K-Means algorithm partitions data into K distinct clusters based on feature similarity.", "instructions": "## Task: Initialize K-Means\\nInitialize a KMeans model from scikit-learn with 3 clusters.", "starterCode": "from sklearn.cluster import KMeans\\n\\nkmeans = KMeans(n_clusters=___, random_state=42)", "solution": "from sklearn.cluster import KMeans\\n\\nkmeans = KMeans(n_clusters=3, random_state=42)", "hint": "Use 3 for n_clusters", "rubric": "Sets n_clusters to 3."},
            {"title": "DBSCAN", "theory": "## Density-Based Spatial Clustering\\nUnlike K-Means which forces every point into a cluster (often forming spherical shapes), DBSCAN groups together points that are closely packed together, and marks points in low-density regions as outliers (noise).", "instructions": "## Task: Outlier Label\\nIn scikit-learn's DBSCAN, what label is assigned to noisy/outlier points that don't belong to any cluster?", "starterCode": "outlier_label = ___", "solution": "outlier_label = -1", "hint": "It is -1", "rubric": "Identifies -1 as the outlier label."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'data_science.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        for new_course_name, course_info in NEW_COURSES_BATCH48.items():
            if new_course_name not in track_data:
                track_data[new_course_name] = {
                    "aiRubric": course_info["aiRubric"],
                    "lessons": course_info["lessons"]
                }
                updated = True
                total += len(course_info["lessons"])
                
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(track_data, f, indent=2, ensure_ascii=False)
                
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH48.items():
            tier = course_info["tier"]
            if "Data Science" in index_data and tier in index_data["Data Science"]:
                if new_course_name not in index_data["Data Science"][tier]:
                    index_data["Data Science"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 48: Added {total} lessons to Data Science track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
