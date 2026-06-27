"""
Batch 46: Expanding Data Science Curriculum (Seaborn, CV, Tuning, Ensembles, PCA)
"""
import json, os

NEW_COURSES_BATCH46 = {
    "Seaborn Visualization": {
        "tier": "Beginner",
        "aiRubric": "Assess Seaborn plotting skills",
        "lessons": [
            {"title": "Statistical Plots", "theory": "## High-Level Interface\\nSeaborn is built on top of Matplotlib and makes it extremely easy to draw attractive statistical graphics like scatter plots with regression lines.", "instructions": "## Task: Scatter Plot\\nUse Seaborn to create a scatter plot of total_bill vs tip from a dataset.", "starterCode": "import seaborn as sns\\n\\ntips = sns.load_dataset('tips')\\nsns.___(x='total_bill', y='tip', data=tips)", "solution": "import seaborn as sns\\n\\ntips = sns.load_dataset('tips')\\nsns.scatterplot(x='total_bill', y='tip', data=tips)", "hint": "Use scatterplot", "rubric": "Correctly uses scatterplot()."},
            {"title": "Heatmaps", "theory": "## Visualizing Matrices\\nHeatmaps are an excellent way to visualize a correlation matrix between features, using colors to indicate strength.", "instructions": "## Task: Draw a Heatmap\\nDraw a heatmap of the provided correlation matrix.", "starterCode": "import seaborn as sns\\n\\ncorr = tips.corr(numeric_only=True)\\nsns.___(corr, annot=True)", "solution": "import seaborn as sns\\n\\ncorr = tips.corr(numeric_only=True)\\nsns.heatmap(corr, annot=True)", "hint": "Use heatmap", "rubric": "Correctly uses heatmap()."}
        ]
    },
    "Cross-Validation": {
        "tier": "Intermediate",
        "aiRubric": "Assess cross-validation techniques",
        "lessons": [
            {"title": "K-Fold Split", "theory": "## Robust Evaluation\\nInstead of a single train/test split, K-Fold Cross-Validation splits the data into K parts, training on K-1 and testing on 1, rotating until all parts have been the test set.", "instructions": "## Task: Set K Folds\\nInstantiate KFold from scikit-learn with 5 splits.", "starterCode": "from sklearn.model_selection import KFold\\n\\nkf = KFold(n_splits=___, shuffle=True)", "solution": "from sklearn.model_selection import KFold\\n\\nkf = KFold(n_splits=5, shuffle=True)", "hint": "Use 5 for n_splits", "rubric": "Sets n_splits to 5."},
            {"title": "Cross Val Score", "theory": "## Automation\\nThe `cross_val_score` function automates the entire process of fitting the model K times and returning the accuracy for each fold.", "instructions": "## Task: Run Cross Val\\nCalculate the cross-validation scores for the model.", "starterCode": "from sklearn.model_selection import cross_val_score\\n\\nscores = ___(model, X, y, cv=5)", "solution": "from sklearn.model_selection import cross_val_score\\n\\nscores = cross_val_score(model, X, y, cv=5)", "hint": "Use cross_val_score", "rubric": "Uses cross_val_score."}
        ]
    },
    "Hyperparameter Tuning": {
        "tier": "Intermediate",
        "aiRubric": "Assess model tuning",
        "lessons": [
            {"title": "Grid Search", "theory": "## Exhaustive Search\\nGrid Search tries every possible combination of hyperparameters provided in a dictionary to find the best performing model.", "instructions": "## Task: Define the Grid\\nDefine a parameter grid for an SVM searching over 'C' values 1 and 10, and 'kernel' values 'linear' and 'rbf'.", "starterCode": "param_grid = {\\n    '___': [1, 10],\\n    '___': ['linear', 'rbf']\\n}", "solution": "param_grid = {\\n    'C': [1, 10],\\n    'kernel': ['linear', 'rbf']\\n}", "hint": "The keys are 'C' and 'kernel'", "rubric": "Sets the correct keys in the grid."},
            {"title": "Randomized Search", "theory": "## Faster Tuning\\nWhen the grid is too large, `RandomizedSearchCV` samples a fixed number of combinations randomly, which is much faster and often finds a near-optimal solution.", "instructions": "## Task: Number of Iterations\\nSet the randomized search to try exactly 20 random combinations.", "starterCode": "from sklearn.model_selection import RandomizedSearchCV\\n\\nrs = RandomizedSearchCV(model, param_grid, n_iter=___)", "solution": "from sklearn.model_selection import RandomizedSearchCV\\n\\nrs = RandomizedSearchCV(model, param_grid, n_iter=20)", "hint": "Set n_iter to 20", "rubric": "Sets n_iter to 20."}
        ]
    },
    "Ensemble Methods": {
        "tier": "Advanced",
        "aiRubric": "Assess ensemble models",
        "lessons": [
            {"title": "Random Forests", "theory": "## Bagging\\nA Random Forest builds multiple decision trees on bootstrap samples of the data and averages their predictions to reduce variance and prevent overfitting.", "instructions": "## Task: Number of Trees\\nInitialize a RandomForestClassifier with 100 trees.", "starterCode": "from sklearn.ensemble import RandomForestClassifier\\n\\nrf = RandomForestClassifier(n_estimators=___)", "solution": "from sklearn.ensemble import RandomForestClassifier\\n\\nrf = RandomForestClassifier(n_estimators=100)", "hint": "Use 100 for n_estimators", "rubric": "Sets n_estimators to 100."},
            {"title": "Gradient Boosting", "theory": "## Boosting\\nInstead of building independent trees, Gradient Boosting builds trees sequentially. Each new tree tries to correct the errors (residuals) made by the previous trees.", "instructions": "## Task: Learning Rate\\nInitialize a GradientBoostingClassifier with a learning rate of 0.01.", "starterCode": "from sklearn.ensemble import GradientBoostingClassifier\\n\\ngbm = GradientBoostingClassifier(learning_rate=___)", "solution": "from sklearn.ensemble import GradientBoostingClassifier\\n\\ngbm = GradientBoostingClassifier(learning_rate=0.01)", "hint": "Use 0.01", "rubric": "Sets learning_rate to 0.01."}
        ]
    },
    "Principal Component Analysis (PCA)": {
        "tier": "Advanced",
        "aiRubric": "Assess PCA and dimensionality reduction",
        "lessons": [
            {"title": "Dimensionality Reduction", "theory": "## Finding Principal Components\\nPCA reduces the number of features in a dataset while retaining as much variance as possible. It is great for visualizing high-dimensional data.", "instructions": "## Task: Reduce to 2D\\nInitialize PCA to reduce the dataset down to 2 principal components.", "starterCode": "from sklearn.decomposition import PCA\\n\\npca = PCA(n_components=___)", "solution": "from sklearn.decomposition import PCA\\n\\npca = PCA(n_components=2)", "hint": "Use 2 for n_components", "rubric": "Sets n_components to 2."},
            {"title": "Explained Variance", "theory": "## Information Retention\\nAfter fitting PCA, you can check `explained_variance_ratio_` to see what percentage of the original data's variance is captured by the new components.", "instructions": "## Task: Total Variance\\nCalculate the total variance explained by the components.", "starterCode": "total_variance = sum(pca.___) * 100", "solution": "total_variance = sum(pca.explained_variance_ratio_) * 100", "hint": "Use explained_variance_ratio_", "rubric": "Uses explained_variance_ratio_."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'data_science.json')
    
    # 1. Update data_science.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH46.items():
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
                
    # 2. Update index.json
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH46.items():
            tier = course_info["tier"]
            if "Data Science" in index_data and tier in index_data["Data Science"]:
                if new_course_name not in index_data["Data Science"][tier]:
                    index_data["Data Science"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 46: Added {total} lessons to Data Science track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
