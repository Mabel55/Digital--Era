"""
Batch 51: Expanding Data Science Curriculum (Numpy, Imbalanced Data, Metrics, Tabular DL, RecSys)
"""
import json, os

NEW_COURSES_BATCH51 = {
    "Numpy Basics": {
        "tier": "Beginner",
        "aiRubric": "Assess fundamental numpy array operations",
        "lessons": [
            {"title": "The NDArray", "theory": "## Fast Math\\nNumpy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, which is much faster than standard Python lists.", "instructions": "## Task: Create an Array\\nImport numpy and create a 1D array from the list `[1, 2, 3]`.", "starterCode": "import numpy as np\\n\\narr = np.___( [1, 2, 3] )", "solution": "import numpy as np\\n\\narr = np.array( [1, 2, 3] )", "hint": "Use np.array", "rubric": "Correctly uses np.array()."},
            {"title": "Vectorized Operations", "theory": "## Broadcasting\\nYou can perform mathematical operations directly on Numpy arrays without writing loops. If you multiply an array by 2, every element is multiplied by 2 instantly.", "instructions": "## Task: Multiply Array\\nMultiply every element in `arr` by 10.", "starterCode": "import numpy as np\\n\\narr = np.array([1, 2, 3])\\nresult = arr ___ 10", "solution": "import numpy as np\\n\\narr = np.array([1, 2, 3])\\nresult = arr * 10", "hint": "Just use the * operator", "rubric": "Correctly uses arr * 10."}
        ]
    },
    "Handling Imbalanced Data": {
        "tier": "Intermediate",
        "aiRubric": "Assess imbalanced dataset strategies",
        "lessons": [
            {"title": "Class Weights", "theory": "## Penalizing Mistakes\\nWhen 99% of your data is 'Normal' and 1% is 'Fraud', a model can just predict 'Normal' every time and get 99% accuracy. You can fix this by telling the algorithm to penalize mistakes on the minority class more heavily.", "instructions": "## Task: Balanced Weights\\nInitialize a LogisticRegression model and set it to automatically adjust weights inversely proportional to class frequencies.", "starterCode": "from sklearn.linear_model import LogisticRegression\\n\\nmodel = LogisticRegression(class_weight='___')", "solution": "from sklearn.linear_model import LogisticRegression\\n\\nmodel = LogisticRegression(class_weight='balanced')", "hint": "Use the word 'balanced'", "rubric": "Sets class_weight to 'balanced'."},
            {"title": "SMOTE Oversampling", "theory": "## Generating Synthetic Data\\nSMOTE (Synthetic Minority Over-sampling Technique) fixes imbalance not by removing data, but by generating synthetic examples of the minority class so both classes have equal representation.", "instructions": "## Task: Import SMOTE\\nImport the SMOTE class from the `imblearn` (Imbalanced-Learn) library.", "starterCode": "from imblearn.over_sampling import ___", "solution": "from imblearn.over_sampling import SMOTE", "hint": "Import SMOTE", "rubric": "Imports SMOTE."}
        ]
    },
    "Model Evaluation Metrics": {
        "tier": "Intermediate",
        "aiRubric": "Assess classification metrics beyond accuracy",
        "lessons": [
            {"title": "Precision and Recall", "theory": "## Beyond Accuracy\\nPrecision asks: 'Out of all the emails I flagged as spam, how many were actually spam?'. Recall asks: 'Out of all the real spam emails, how many did I successfully flag?'.", "instructions": "## Task: Calculate F1 Score\\nThe F1 Score is the harmonic mean of Precision and Recall. Import the function to calculate it.", "starterCode": "from sklearn.metrics import ___", "solution": "from sklearn.metrics import f1_score", "hint": "Import f1_score", "rubric": "Imports f1_score."},
            {"title": "ROC and AUC", "theory": "## The ROC Curve\\nThe Receiver Operating Characteristic (ROC) curve plots the True Positive Rate vs the False Positive Rate at different classification thresholds. The Area Under the Curve (AUC) summarizes this into a single number between 0 and 1.", "instructions": "## Task: Calculate AUC\\nCalculate the ROC AUC score given the true labels `y_true` and predicted probabilities `y_probs`.", "starterCode": "from sklearn.metrics import roc_auc_score\\n\\nscore = roc_auc_score(___, ___)", "solution": "from sklearn.metrics import roc_auc_score\\n\\nscore = roc_auc_score(y_true, y_probs)", "hint": "Pass y_true, then y_probs", "rubric": "Correctly calls roc_auc_score(y_true, y_probs)."}
        ]
    },
    "Deep Learning for Tabular Data": {
        "tier": "Advanced",
        "aiRubric": "Assess tabular deep learning",
        "lessons": [
            {"title": "Entity Embeddings", "theory": "## Mapping Categories\\nWhile One-Hot Encoding is standard for categorical variables, deep learning can use Entity Embeddings to map categories (like 'City' or 'Store ID') into dense vectors, capturing semantic relationships between them.", "instructions": "## Task: Embedding Layer\\nIn PyTorch, which layer is used to create trainable embeddings for categorical variables?", "starterCode": "import torch.nn as nn\\n\\nlayer = nn.___ (num_categories, embedding_dim)", "solution": "import torch.nn as nn\\n\\nlayer = nn.Embedding (num_categories, embedding_dim)", "hint": "Use nn.Embedding", "rubric": "Identifies nn.Embedding."},
            {"title": "Autoencoders for Anomaly Detection", "theory": "## Reconstruction Error\\nAn Autoencoder is a neural network trained to compress tabular data into a bottleneck and then reconstruct it. If it is fed anomalous data (like fraud), it will struggle to reconstruct it, resulting in a high 'Reconstruction Error'.", "instructions": "## Task: Bottleneck Size\\nIn an autoencoder, the hidden layer representation (the bottleneck) must be ___ than the input dimension to force compression.", "starterCode": "# Options: larger, smaller, equal\\nsize = '___'", "solution": "# Options: larger, smaller, equal\\nsize = 'smaller'", "hint": "It must be smaller.", "rubric": "Identifies smaller."}
        ]
    },
    "Recommendation Systems": {
        "tier": "Advanced",
        "aiRubric": "Assess RecSys concepts",
        "lessons": [
            {"title": "Collaborative Filtering", "theory": "## User-Item Matrices\\nCollaborative filtering assumes that if User A and User B liked similar movies in the past, they will like similar movies in the future. It relies purely on interaction data.", "instructions": "## Task: Matrix Factorization\\nWhat technique decomposes a sparse User-Item interaction matrix into two lower-dimensional matrices (User factors and Item factors)?", "starterCode": "# Options: PCA, Matrix Factorization, K-Means\\ntechnique = '___'", "solution": "# Options: PCA, Matrix Factorization, K-Means\\ntechnique = 'Matrix Factorization'", "hint": "Matrix Factorization", "rubric": "Identifies Matrix Factorization."},
            {"title": "Content-Based Filtering", "theory": "## Using Metadata\\nContent-based filtering ignores other users and focuses on the items themselves. If you watched a Sci-Fi movie starring Keanu Reeves, it will recommend other Sci-Fi movies or movies with Keanu Reeves.", "instructions": "## Task: Similarity Metric\\nIf you represent each movie as a TF-IDF vector of its plot keywords, which metric is commonly used to find similar movies?", "starterCode": "# Options: Euclidean Distance, Cosine Similarity\\nmetric = '___'", "solution": "# Options: Euclidean Distance, Cosine Similarity\\nmetric = 'Cosine Similarity'", "hint": "Cosine Similarity", "rubric": "Identifies Cosine Similarity."}
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
        
        for new_course_name, course_info in NEW_COURSES_BATCH51.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH51.items():
            tier = course_info["tier"]
            if "Data Science" in index_data and tier in index_data["Data Science"]:
                if new_course_name not in index_data["Data Science"][tier]:
                    index_data["Data Science"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 51: Added {total} lessons to Data Science track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
