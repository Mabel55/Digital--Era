"""
Phase 6: Add 41 new lessons to Data Science and 44 new lessons to AI Engineering.
"""
import json

NEW_DS_LESSONS = {
    "Intro to Data Science": [
        {
            "title": "What is Data Science?",
            "theory": "## Data Science Lifecycle\nData science involves extracting insights from data using scientific methods, algorithms, and systems. The lifecycle includes collection, cleaning, exploration, modeling, and deployment.",
            "instructions": "## Task: Define the Steps\n1. Create a Python list containing the main steps of the data science lifecycle in order: 'Collect', 'Clean', 'Explore', 'Model', 'Deploy'.",
            "starterCode": "lifecycle = [___, ___, ___, ___, ___]\nprint(\"Data Science Lifecycle:\", lifecycle)",
            "solution": "lifecycle = ['Collect', 'Clean', 'Explore', 'Model', 'Deploy']\nprint(\"Data Science Lifecycle:\", lifecycle)",
            "hint": "Create a list of strings.",
            "rubric": "List correctly defines the 5 main steps."
        },
        {
            "title": "Types of Data",
            "theory": "## Structured vs Unstructured\nStructured data fits neatly into tables (SQL). Unstructured data doesn't (text, images, audio).",
            "instructions": "## Task: Categorize Data\n1. Write a function that returns 'Structured' if the input is 'SQL', and 'Unstructured' if the input is 'Text' or 'Image'.",
            "starterCode": "def dataType(input_type):\n    if input_type == '___':\n        return '___'\n    elif input_type in ['___', '___']:\n        return 'Unstructured'",
            "solution": "def dataType(input_type):\n    if input_type == 'SQL':\n        return 'Structured'\n    elif input_type in ['Text', 'Image']:\n        return 'Unstructured'",
            "hint": "SQL is Structured. Text and Image are Unstructured.",
            "rubric": "Function categorizes data correctly."
        },
        {
            "title": "Roles in Data",
            "theory": "## Analyst vs Scientist vs Engineer\nData Analysts visualize and describe past data. Data Scientists build predictive models. Data Engineers build pipelines.",
            "instructions": "## Task: Identify the Role\n1. Return 'Scientist' if the task is 'Predict', 'Analyst' if 'Visualize', and 'Engineer' if 'Pipeline'.",
            "starterCode": "def getRole(task):\n    if task == 'Predict': return '___'\n    if task == 'Visualize': return '___'\n    if task == 'Pipeline': return '___'",
            "solution": "def getRole(task):\n    if task == 'Predict': return 'Scientist'\n    if task == 'Visualize': return 'Analyst'\n    if task == 'Pipeline': return 'Engineer'",
            "hint": "Map Predict->Scientist, Visualize->Analyst, Pipeline->Engineer.",
            "rubric": "Function maps tasks to roles successfully."
        }
    ],
    "Pandas & NumPy Basics": [
        {
            "title": "NumPy Arrays",
            "theory": "## NumPy\nNumPy is the core library for scientific computing in Python. It provides high-performance multidimensional array objects.",
            "instructions": "## Task: Create an Array\n1. Import numpy as np.\n2. Create a 1D array of numbers 1 to 5.",
            "starterCode": "import ___ as ___\narr = np.___([1, 2, 3, 4, 5])\nprint(arr)",
            "solution": "import numpy as np\narr = np.array([1, 2, 3, 4, 5])\nprint(arr)",
            "hint": "Use import numpy as np and np.array().",
            "rubric": "NumPy array instantiated correctly."
        },
        {
            "title": "Pandas DataFrames",
            "theory": "## DataFrames\nPandas DataFrames are 2-dimensional labeled data structures. They are like spreadsheets or SQL tables.",
            "instructions": "## Task: Create a DataFrame\n1. Import pandas as pd.\n2. Create a DataFrame from a dictionary with 'Name' and 'Age' keys.",
            "starterCode": "import ___ as ___\ndata = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}\ndf = pd.___(data)\nprint(df)",
            "solution": "import pandas as pd\ndata = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}\ndf = pd.DataFrame(data)\nprint(df)",
            "hint": "Use import pandas as pd and pd.DataFrame().",
            "rubric": "DataFrame created properly from a dictionary."
        },
        {
            "title": "Selecting Data in Pandas",
            "theory": "## Loc and Iloc\n`.loc[]` accesses a group of rows and columns by label. `.iloc[]` accesses by integer position.",
            "instructions": "## Task: Select First Row\n1. Use `.iloc` to select the very first row of the DataFrame.",
            "starterCode": "# Assume df exists\nfirst_row = df.___(___)",
            "solution": "# Assume df exists\nfirst_row = df.iloc[0]",
            "hint": "Use df.iloc[0].",
            "rubric": "Correctly selected the first row using iloc."
        }
    ],
    "Data Cleaning": [
        {
            "title": "Handling Missing Data",
            "theory": "## NaN Values\nMissing data is common. You can drop missing rows using `dropna()` or fill them using `fillna()`.",
            "instructions": "## Task: Fill NaN Values\n1. Fill all `NaN` values in the DataFrame `df` with the number 0.",
            "starterCode": "clean_df = df.___(___)",
            "solution": "clean_df = df.fillna(0)",
            "hint": "Use fillna(0).",
            "rubric": "NaN values filled successfully."
        },
        {
            "title": "Removing Duplicates",
            "theory": "## Duplicates\nDuplicate rows can skew analysis. Use `drop_duplicates()` to remove them.",
            "instructions": "## Task: Drop Duplicates\n1. Remove all duplicate rows from `df`.",
            "starterCode": "unique_df = df.___()",
            "solution": "unique_df = df.drop_duplicates()",
            "hint": "Use drop_duplicates().",
            "rubric": "Duplicates dropped correctly."
        },
        {
            "title": "Data Type Conversion",
            "theory": "## astype()\nSometimes numeric data is read as strings. Use `astype()` to cast it to the correct type.",
            "instructions": "## Task: Convert to Float\n1. Convert the 'Price' column of `df` to `float`.",
            "starterCode": "df['Price'] = df['Price'].___('___')",
            "solution": "df['Price'] = df['Price'].astype('float')",
            "hint": "Use astype('float').",
            "rubric": "Column cast to float successfully."
        }
    ],
    "Exploratory Data Analysis": [
        {
            "title": "Summary Statistics",
            "theory": "## describe()\nThe `describe()` method generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's distribution.",
            "instructions": "## Task: Generate Summary\n1. Call the `describe()` method on `df`.",
            "starterCode": "summary = df.___()",
            "solution": "summary = df.describe()",
            "hint": "Use describe().",
            "rubric": "Summary statistics generated correctly."
        },
        {
            "title": "Correlation Matrix",
            "theory": "## corr()\nThe `corr()` method computes pairwise correlation of columns. Values near 1 or -1 indicate strong correlation.",
            "instructions": "## Task: Calculate Correlation\n1. Calculate the correlation matrix of `df`.",
            "starterCode": "correlation = df.___()",
            "solution": "correlation = df.corr()",
            "hint": "Use corr().",
            "rubric": "Correlation matrix computed successfully."
        },
        {
            "title": "Value Counts",
            "theory": "## value_counts()\nUse `value_counts()` on a column (Series) to get a count of unique values.",
            "instructions": "## Task: Count Categories\n1. Get the value counts for the 'Category' column in `df`.",
            "starterCode": "counts = df['___'].___()",
            "solution": "counts = df['Category'].value_counts()",
            "hint": "Use df['Category'].value_counts().",
            "rubric": "Value counts extracted correctly."
        }
    ],
    "Data Visualization": [
        {
            "title": "Matplotlib Basics",
            "theory": "## Pyplot\nMatplotlib's pyplot module provides a MATLAB-like plotting framework.",
            "instructions": "## Task: Line Plot\n1. Import matplotlib.pyplot as plt.\n2. Plot x versus y using `plt.plot()`.",
            "starterCode": "import ___ as ___\nx = [1, 2, 3]\ny = [2, 4, 6]\nplt.___(x, y)\nplt.show()",
            "solution": "import matplotlib.pyplot as plt\nx = [1, 2, 3]\ny = [2, 4, 6]\nplt.plot(x, y)\nplt.show()",
            "hint": "Import matplotlib.pyplot as plt and use plt.plot().",
            "rubric": "Line plot created correctly."
        },
        {
            "title": "Seaborn Styling",
            "theory": "## Seaborn\nSeaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive statistical graphics.",
            "instructions": "## Task: Scatter Plot\n1. Import seaborn as sns.\n2. Create a scatterplot of x vs y.",
            "starterCode": "import ___ as ___\n# Assume df exists\nsns.___(\nx=___, y=___, data=df\n)",
            "solution": "import seaborn as sns\n# Assume df exists\nsns.scatterplot(\nx='Age', y='Income', data=df\n)",
            "hint": "Use sns.scatterplot.",
            "rubric": "Seaborn scatterplot implemented successfully."
        },
        {
            "title": "Histograms",
            "theory": "## Distributions\nHistograms are used to visualize the distribution of a single numerical variable.",
            "instructions": "## Task: Plot Distribution\n1. Use seaborn to create a histogram (histplot) of the 'Age' column.",
            "starterCode": "sns.___(___=df['___'])",
            "solution": "sns.histplot(data=df['Age'])",
            "hint": "Use sns.histplot(data=...).",
            "rubric": "Histogram plotted properly."
        }
    ],
    "Statistical Analysis": [
        {
            "title": "Mean, Median, Mode",
            "theory": "## Central Tendency\nMean is the average. Median is the middle value. Mode is the most frequent value.",
            "instructions": "## Task: Calculate Median\n1. Calculate the median of the 'Income' column in `df`.",
            "starterCode": "median_inc = df['Income'].___()",
            "solution": "median_inc = df['Income'].median()",
            "hint": "Use .median().",
            "rubric": "Median calculated accurately."
        },
        {
            "title": "Standard Deviation",
            "theory": "## Dispersion\nStandard deviation measures the amount of variation or dispersion of a set of values.",
            "instructions": "## Task: Calculate Std Dev\n1. Calculate the standard deviation of the 'Age' column.",
            "starterCode": "std_age = df['Age'].___()",
            "solution": "std_age = df['Age'].std()",
            "hint": "Use .std().",
            "rubric": "Standard deviation calculated accurately."
        },
        {
            "title": "Hypothesis Testing",
            "theory": "## T-Tests\nA t-test determines if there is a significant difference between the means of two groups. Use `scipy.stats.ttest_ind`.",
            "instructions": "## Task: Run a T-Test\n1. Run an independent t-test between array `group1` and `group2`.",
            "starterCode": "from scipy import stats\nt_stat, p_val = stats.___(___, ___)",
            "solution": "from scipy import stats\nt_stat, p_val = stats.ttest_ind(group1, group2)",
            "hint": "Use stats.ttest_ind().",
            "rubric": "T-test executed correctly using scipy."
        }
    ],
    "Intro to Machine Learning": [
        {
            "title": "Supervised vs Unsupervised",
            "theory": "## ML Paradigms\nSupervised learning uses labeled data (has targets). Unsupervised learning uses unlabeled data (finds patterns).",
            "instructions": "## Task: Classify the Paradigm\n1. If a dataset has a 'Target' column, return 'Supervised', else return 'Unsupervised'.",
            "starterCode": "def getParadigm(has_target):\n    if ___:\n        return '___'\n    return '___'",
            "solution": "def getParadigm(has_target):\n    if has_target:\n        return 'Supervised'\n    return 'Unsupervised'",
            "hint": "Check if has_target is true.",
            "rubric": "Paradigm classified accurately."
        },
        {
            "title": "Train/Test Split",
            "theory": "## Model Validation\nSplit your data into a training set (to learn) and a test set (to evaluate) to avoid overfitting.",
            "instructions": "## Task: Split Data\n1. Use `train_test_split` from sklearn.\n2. Set `test_size` to 0.2.",
            "starterCode": "from sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = ___(X, y, test_size=___)",
            "solution": "from sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)",
            "hint": "Use train_test_split with 0.2.",
            "rubric": "Data successfully split into training and testing sets."
        },
        {
            "title": "Fit and Predict",
            "theory": "## Estimator API\nScikit-learn models use `.fit(X_train, y_train)` to train and `.predict(X_test)` to generate predictions.",
            "instructions": "## Task: Train a Model\n1. Fit the `model` object to `X_train` and `y_train`.\n2. Predict on `X_test`.",
            "starterCode": "model.___(___, ___)\npreds = model.___(___)",
            "solution": "model.fit(X_train, y_train)\npreds = model.predict(X_test)",
            "hint": "Use fit() and predict().",
            "rubric": "Model fit and predict methods used correctly."
        }
    ],
    "Scikit-Learn Pipelines": [
        {
            "title": "Data Scaling",
            "theory": "## Standardizing Data\nMany ML algorithms require features to be on the same scale. `StandardScaler` removes the mean and scales to unit variance.",
            "instructions": "## Task: Scale Features\n1. Instantiate `StandardScaler`.\n2. Use `fit_transform` on `X_train`.",
            "starterCode": "from sklearn.preprocessing import StandardScaler\nscaler = ___()\nX_scaled = scaler.___(___)",
            "solution": "from sklearn.preprocessing import StandardScaler\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X_train)",
            "hint": "Use StandardScaler() and fit_transform().",
            "rubric": "Features standardized correctly."
        },
        {
            "title": "Creating a Pipeline",
            "theory": "## Pipelines\nA `Pipeline` chains multiple steps together (e.g., scaling then modeling) to prevent data leakage.",
            "instructions": "## Task: Build Pipeline\n1. Create a `make_pipeline` with a `StandardScaler` and a `LinearRegression` model.",
            "starterCode": "from sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LinearRegression\n\npipe = ___(StandardScaler(), ___())",
            "solution": "from sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LinearRegression\n\npipe = make_pipeline(StandardScaler(), LinearRegression())",
            "hint": "Use make_pipeline() with the components.",
            "rubric": "Pipeline properly instantiated."
        },
        {
            "title": "Fitting a Pipeline",
            "theory": "## Using Pipelines\nYou treat a Pipeline exactly like a single model using `.fit()` and `.predict()`.",
            "instructions": "## Task: Train Pipeline\n1. Fit the pipeline `pipe` on `X_train` and `y_train`.",
            "starterCode": "pipe.___(___, ___)",
            "solution": "pipe.fit(X_train, y_train)",
            "hint": "Use .fit().",
            "rubric": "Pipeline fit successfully."
        }
    ],
    "Regression Models": [
        {
            "title": "Linear Regression",
            "theory": "## Linear Models\nLinear regression fits a straight line to minimize the residual sum of squares between observed and predicted targets.",
            "instructions": "## Task: Instantiate Linear Regression\n1. Create a `LinearRegression` model instance.",
            "starterCode": "from sklearn.linear_model import LinearRegression\nmodel = ___()",
            "solution": "from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()",
            "hint": "Just call LinearRegression().",
            "rubric": "Linear Regression model created."
        },
        {
            "title": "MSE Metric",
            "theory": "## Mean Squared Error\nMSE measures the average squared difference between estimated and actual values. Lower is better.",
            "instructions": "## Task: Calculate MSE\n1. Use `mean_squared_error` on true labels `y_test` and `preds`.",
            "starterCode": "from sklearn.metrics import mean_squared_error\nmse = ___(___, ___)",
            "solution": "from sklearn.metrics import mean_squared_error\nmse = mean_squared_error(y_test, preds)",
            "hint": "Use mean_squared_error().",
            "rubric": "MSE calculated correctly."
        },
        {
            "title": "R-squared Metric",
            "theory": "## R2 Score\nR-squared represents the proportion of variance in the dependent variable explained by the model. 1.0 is a perfect fit.",
            "instructions": "## Task: Calculate R2\n1. Use `r2_score` on true labels `y_test` and `preds`.",
            "starterCode": "from sklearn.metrics import r2_score\nr2 = ___(___, ___)",
            "solution": "from sklearn.metrics import r2_score\nr2 = r2_score(y_test, preds)",
            "hint": "Use r2_score().",
            "rubric": "R2 calculated correctly."
        }
    ],
    "Classification Models": [
        {
            "title": "Logistic Regression",
            "theory": "## Logistic Models\nDespite the name, Logistic Regression is a classification algorithm that outputs probabilities between 0 and 1 using the sigmoid function.",
            "instructions": "## Task: Instantiate Logistic Regression\n1. Create a `LogisticRegression` model.",
            "starterCode": "from sklearn.linear_model import LogisticRegression\nmodel = ___()",
            "solution": "from sklearn.linear_model import LogisticRegression\nmodel = LogisticRegression()",
            "hint": "Call LogisticRegression().",
            "rubric": "Logistic Regression created."
        },
        {
            "title": "Accuracy Score",
            "theory": "## Accuracy\nAccuracy is the fraction of predictions our model got right. Use `accuracy_score`.",
            "instructions": "## Task: Calculate Accuracy\n1. Use `accuracy_score` on `y_test` and `preds`.",
            "starterCode": "from sklearn.metrics import accuracy_score\nacc = ___(___, ___)",
            "solution": "from sklearn.metrics import accuracy_score\nacc = accuracy_score(y_test, preds)",
            "hint": "Use accuracy_score().",
            "rubric": "Accuracy calculated properly."
        },
        {
            "title": "Confusion Matrix",
            "theory": "## Confusion Matrix\nA table used to describe the performance of a classification model, showing True Positives, False Positives, etc.",
            "instructions": "## Task: Generate Matrix\n1. Use `confusion_matrix` on `y_test` and `preds`.",
            "starterCode": "from sklearn.metrics import confusion_matrix\ncm = ___(___, ___)",
            "solution": "from sklearn.metrics import confusion_matrix\ncm = confusion_matrix(y_test, preds)",
            "hint": "Use confusion_matrix().",
            "rubric": "Confusion matrix generated."
        }
    ],
    "Feature Engineering": [
        {
            "title": "One-Hot Encoding",
            "theory": "## Categorical Variables\nML models need numbers. One-Hot Encoding converts categories into binary columns (1 or 0).",
            "instructions": "## Task: Use get_dummies\n1. Use Pandas `pd.get_dummies()` to encode the 'Color' column of `df`.",
            "starterCode": "df_encoded = pd.___(___, columns=['___'])",
            "solution": "df_encoded = pd.get_dummies(df, columns=['Color'])",
            "hint": "Use pd.get_dummies().",
            "rubric": "One-Hot encoding applied via pandas."
        },
        {
            "title": "Binning",
            "theory": "## Discretization\nBinning groups continuous data into discrete bins (e.g., Ages 1-18 -> 'Child').",
            "instructions": "## Task: Use pd.cut\n1. Bin 'Age' into 3 bins using `pd.cut()`.",
            "starterCode": "df['AgeGroup'] = pd.___(___, bins=___)",
            "solution": "df['AgeGroup'] = pd.cut(df['Age'], bins=3)",
            "hint": "Use pd.cut().",
            "rubric": "Binning applied successfully."
        },
        {
            "title": "Polynomial Features",
            "theory": "## Non-linear Relationships\nGenerating polynomial features (like x^2) helps linear models capture non-linear patterns.",
            "instructions": "## Task: Create Polynomial Features\n1. Instantiate `PolynomialFeatures` with degree 2.\n2. Transform `X`.",
            "starterCode": "from sklearn.preprocessing import PolynomialFeatures\npoly = ___(degree=___)\nX_poly = poly.fit_transform(___)",
            "solution": "from sklearn.preprocessing import PolynomialFeatures\npoly = PolynomialFeatures(degree=2)\nX_poly = poly.fit_transform(X)",
            "hint": "Use PolynomialFeatures(degree=2).",
            "rubric": "Polynomial features created."
        }
    ],
    "Ensemble Methods": [
        {
            "title": "Random Forests",
            "theory": "## Bagging Ensembles\nRandom Forests train many decision trees on random subsets of data and features, then average their predictions to reduce overfitting.",
            "instructions": "## Task: Instantiate Random Forest Classifier\n1. Create a `RandomForestClassifier` with 100 estimators.",
            "starterCode": "from sklearn.ensemble import RandomForestClassifier\nmodel = ___(n_estimators=___)",
            "solution": "from sklearn.ensemble import RandomForestClassifier\nmodel = RandomForestClassifier(n_estimators=100)",
            "hint": "Use RandomForestClassifier.",
            "rubric": "Random Forest instantiated correctly."
        },
        {
            "title": "Gradient Boosting",
            "theory": "## Boosting Ensembles\nBoosting trains trees sequentially, where each new tree tries to correct the errors of the previous ones.",
            "instructions": "## Task: Instantiate Gradient Boosting Regressor\n1. Create a `GradientBoostingRegressor`.",
            "starterCode": "from sklearn.ensemble import GradientBoostingRegressor\nmodel = ___()",
            "solution": "from sklearn.ensemble import GradientBoostingRegressor\nmodel = GradientBoostingRegressor()",
            "hint": "Call GradientBoostingRegressor().",
            "rubric": "Gradient Boosting Regressor instantiated."
        }
    ],
    "Model Evaluation & Tuning": [
        {
            "title": "Cross-Validation",
            "theory": "## K-Fold CV\nCross-validation splits the data into K folds, training on K-1 folds and testing on the remaining fold, rotating until all folds are tested.",
            "instructions": "## Task: Run Cross-Validation\n1. Use `cross_val_score` on `model`, `X`, and `y` with 5 folds (`cv=5`).",
            "starterCode": "from sklearn.model_selection import cross_val_score\nscores = ___(___, ___, ___, cv=___)",
            "solution": "from sklearn.model_selection import cross_val_score\nscores = cross_val_score(model, X, y, cv=5)",
            "hint": "Use cross_val_score(model, X, y, cv=5).",
            "rubric": "Cross-validation executed accurately."
        },
        {
            "title": "Grid Search",
            "theory": "## Hyperparameter Tuning\nGrid search tests all possible combinations of a predefined grid of hyperparameters to find the best configuration.",
            "instructions": "## Task: Setup GridSearchCV\n1. Instantiate `GridSearchCV` with `model`, `param_grid`, and `cv=3`.",
            "starterCode": "from sklearn.model_selection import GridSearchCV\nparam_grid = {'max_depth': [3, 5]}\ngrid = ___(___, param_grid, cv=___)",
            "solution": "from sklearn.model_selection import GridSearchCV\nparam_grid = {'max_depth': [3, 5]}\ngrid = GridSearchCV(model, param_grid, cv=3)",
            "hint": "Use GridSearchCV().",
            "rubric": "Grid Search object initialized correctly."
        }
    ],
    "Time Series Analysis": [
        {
            "title": "Datetime Index",
            "theory": "## Time Series in Pandas\nTime series data should have a `DatetimeIndex` to utilize Pandas' time-based functions.",
            "instructions": "## Task: Convert to Datetime\n1. Convert the 'Date' column in `df` to datetime using `pd.to_datetime`.\n2. Set it as the DataFrame index.",
            "starterCode": "df['Date'] = pd.___(___)\ndf.___('Date', inplace=True)",
            "solution": "df['Date'] = pd.to_datetime(df['Date'])\ndf.set_index('Date', inplace=True)",
            "hint": "Use pd.to_datetime() and .set_index().",
            "rubric": "Datetime conversion and indexing performed."
        },
        {
            "title": "Resampling",
            "theory": "## Aggregating by Time\n`resample()` is like `groupby()`, but specifically for time periods (e.g., 'M' for month, 'W' for week).",
            "instructions": "## Task: Monthly Average\n1. Resample the dataframe `df` to Monthly ('M') and calculate the `mean()`.",
            "starterCode": "monthly_avg = df.___('___').___()",
            "solution": "monthly_avg = df.resample('M').mean()",
            "hint": "Use .resample('M').mean().",
            "rubric": "Time series data successfully resampled."
        }
    ],
    "Deep Learning Basics": [
        {
            "title": "Neural Networks",
            "theory": "## Multilayer Perceptron\nNeural networks consist of an input layer, hidden layers, and an output layer of neurons. They learn complex non-linear mappings.",
            "instructions": "## Task: Simple Keras Model\n1. Use TensorFlow/Keras to build a Sequential model with one Dense layer of 10 units.",
            "starterCode": "from tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import Dense\n\nmodel = ___([\n    ___(10, activation='relu')\n])",
            "solution": "from tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import Dense\n\nmodel = Sequential([\n    Dense(10, activation='relu')\n])",
            "hint": "Use Sequential and Dense.",
            "rubric": "Keras Sequential model with Dense layer built."
        },
        {
            "title": "Model Compilation",
            "theory": "## Compiling\nBefore training a neural network, you must configure the learning process with an optimizer and a loss function.",
            "instructions": "## Task: Compile Model\n1. Compile the `model` using the 'adam' optimizer and 'mse' loss function.",
            "starterCode": "model.___(\n    optimizer='___',\n    loss='___'\n)",
            "solution": "model.compile(\n    optimizer='adam',\n    loss='mse'\n)",
            "hint": "Use .compile(optimizer='adam', loss='mse').",
            "rubric": "Deep learning model compiled properly."
        }
    ]
}

NEW_AI_LESSONS = {
    "AI & ML Concepts": [
        {
            "title": "What is AI?",
            "theory": "## Artificial Intelligence\nAI is the broader field of creating systems capable of human-like reasoning. Machine Learning is a subset focusing on learning from data.",
            "instructions": "## Task: Conceptual Categorization\n1. Create a dictionary defining AI, ML, and DL hierarchically.",
            "starterCode": "hierarchy = {\n    \"AI\": \"Broad concept\",\n    \"ML\": \"___ of AI\",\n    \"DL\": \"Subset of ___\"\n}",
            "solution": "hierarchy = {\n    \"AI\": \"Broad concept\",\n    \"ML\": \"Subset of AI\",\n    \"DL\": \"Subset of ML\"\n}",
            "hint": "ML is a Subset of AI, DL is a Subset of ML.",
            "rubric": "Hierarchy logic defined properly."
        },
        {
            "title": "Generative AI",
            "theory": "## GenAI\nGenerative AI models create new content (text, images, code) rather than just predicting labels. LLMs are a type of GenAI.",
            "instructions": "## Task: Identify GenAI\n1. Return True if the task is 'Create Image', False if 'Classify Spam'.",
            "starterCode": "def is_generative(task):\n    return task == \"___\"",
            "solution": "def is_generative(task):\n    return task == \"Create Image\"",
            "hint": "Generative tasks create new things.",
            "rubric": "Generative task classification is correct."
        },
        {
            "title": "Foundation Models",
            "theory": "## Large Pre-trained Models\nFoundation models are huge neural networks trained on massive general datasets, which can be adapted for various tasks.",
            "instructions": "## Task: List Foundation Models\n1. Create a list of 3 famous foundation models: GPT-4, Claude 3, Llama 3.",
            "starterCode": "models = [\"___\", \"___\", \"___\"]",
            "solution": "models = [\"GPT-4\", \"Claude 3\", \"Llama 3\"]",
            "hint": "Add the model names as strings.",
            "rubric": "Foundation models listed."
        }
    ],
    "Python for AI": [
        {
            "title": "Using Requests for APIs",
            "theory": "## API Calling\nPython's `requests` library is heavily used to interact with cloud AI APIs.",
            "instructions": "## Task: Mock API Call\n1. Import requests.\n2. POST to `/v1/chat/completions` with a JSON payload.",
            "starterCode": "import requests\npayload = {\"prompt\": \"Hello\"}\nres = requests.___(\"/v1/chat/completions\", ___=payload)",
            "solution": "import requests\npayload = {\"prompt\": \"Hello\"}\nres = requests.post(\"/v1/chat/completions\", json=payload)",
            "hint": "Use .post() and json=payload.",
            "rubric": "API call configured correctly."
        },
        {
            "title": "Environment Secrets",
            "theory": "## API Keys\nNever hardcode API keys. Use `os.getenv()`.",
            "instructions": "## Task: Get API Key\n1. Use `os.getenv` to get `OPENAI_API_KEY`.",
            "starterCode": "import os\napi_key = os.___(\"___\")",
            "solution": "import os\napi_key = os.getenv(\"OPENAI_API_KEY\")",
            "hint": "Use os.getenv().",
            "rubric": "Environment variable accessed safely."
        },
        {
            "title": "Async API Calls",
            "theory": "## asyncio and aiohttp\nWhen making many API calls, async IO speeds up processing significantly.",
            "instructions": "## Task: Async Fetch\n1. Define an async function `fetch()` that awaits `session.post()`.",
            "starterCode": "___ def fetch(session):\n    res = ___ session.___(\"/api\")\n    return res",
            "solution": "async def fetch(session):\n    res = await session.post(\"/api\")\n    return res",
            "hint": "Use async def and await.",
            "rubric": "Async fetch structured correctly."
        }
    ],
    "Working with APIs": [
        {
            "title": "OpenAI API Basics",
            "theory": "## OpenAI Client\nThe `openai` Python package provides a standard client for interacting with GPT models.",
            "instructions": "## Task: Initialize Client\n1. Import OpenAI and instantiate the client.",
            "starterCode": "from ___ import ___\nclient = ___()",
            "solution": "from openai import OpenAI\nclient = OpenAI()",
            "hint": "from openai import OpenAI.",
            "rubric": "OpenAI client instantiated."
        },
        {
            "title": "Chat Completions",
            "theory": "## Roles\nMessages require roles: 'system' (instructions), 'user' (prompts), 'assistant' (replies).",
            "instructions": "## Task: Create Messages\n1. Create a list of messages. One system message setting behavior, one user message.",
            "starterCode": "messages = [\n    {\"role\": \"___\", \"content\": \"You are helpful.\"},\n    {\"role\": \"___\", \"content\": \"Hi!\"}\n]",
            "solution": "messages = [\n    {\"role\": \"system\", \"content\": \"You are helpful.\"},\n    {\"role\": \"user\", \"content\": \"Hi!\"}\n]",
            "hint": "Use 'system' and 'user'.",
            "rubric": "Message payload roles defined accurately."
        },
        {
            "title": "Parsing the Response",
            "theory": "## API Response Object\nOpenAI returns a nested object. The text response is located at `choices[0].message.content`.",
            "instructions": "## Task: Extract Content\n1. Access the content string from the `response` object.",
            "starterCode": "content = response.___(___).___.___",
            "solution": "content = response.choices[0].message.content",
            "hint": "Follow the path: choices[0].message.content.",
            "rubric": "Response string extracted perfectly."
        }
    ],
    "Prompt Engineering": [
        {
            "title": "Zero-Shot vs Few-Shot",
            "theory": "## Providing Examples\nZero-shot asks a model to perform a task directly. Few-shot provides a few examples first to guide the output format.",
            "instructions": "## Task: Few-Shot Prompt\n1. Write a prompt that provides one example of English to French translation before asking for \"Apple\".",
            "starterCode": "prompt = \"English: Dog \\nFrench: ___ \\nEnglish: Apple \\nFrench:\"",
            "solution": "prompt = \"English: Dog \\nFrench: Chien \\nEnglish: Apple \\nFrench:\"",
            "hint": "Translate Dog to French (Chien).",
            "rubric": "Few-shot pattern utilized."
        },
        {
            "title": "Chain of Thought",
            "theory": "## Let's Think Step by Step\nAsking an LLM to explain its reasoning before outputting an answer improves logic and math performance.",
            "instructions": "## Task: CoT Trigger\n1. Append the classic Chain of Thought trigger to the prompt.",
            "starterCode": "prompt = \"Solve 123 * 45. Let's think ___ by ___.\"",
            "solution": "prompt = \"Solve 123 * 45. Let's think step by step.\"",
            "hint": "step by step.",
            "rubric": "Chain of thought trigger applied."
        },
        {
            "title": "System Prompts",
            "theory": "## Persona and Constraints\nSystem prompts define the 'rules of the game' (persona, tone, formatting constraints).",
            "instructions": "## Task: Define Persona\n1. Write a system prompt that tells the AI to act as a Pirate and output only JSON.",
            "starterCode": "system = \"Act as a ___. Output only in ___ format.\"",
            "solution": "system = \"Act as a Pirate. Output only in JSON format.\"",
            "hint": "Pirate and JSON.",
            "rubric": "System persona defined."
        }
    ],
    "AI Use Cases": [
        {
            "title": "Text Summarization",
            "theory": "## Summarization\nLLMs excel at extracting key information from long documents.",
            "instructions": "## Task: Summarize Prompt\n1. Create a prompt requesting a 2-sentence summary of a variable `article`.",
            "starterCode": "prompt = f\"Provide a ___ sentence summary of the following:\\n{___}\"",
            "solution": "prompt = f\"Provide a 2 sentence summary of the following:\\n{article}\"",
            "hint": "2 sentence summary of {article}.",
            "rubric": "Summarization prompt structured correctly."
        },
        {
            "title": "Sentiment Analysis",
            "theory": "## Sentiment\nClassifying text as positive, negative, or neutral.",
            "instructions": "## Task: Sentiment Prompt\n1. Ask the model to return exactly one word: POSITIVE, NEGATIVE, or NEUTRAL.",
            "starterCode": "prompt = \"Classify sentiment as POSITIVE, ___, or ___. Text: I love this!\"",
            "solution": "prompt = \"Classify sentiment as POSITIVE, NEGATIVE, or NEUTRAL. Text: I love this!\"",
            "hint": "NEGATIVE, NEUTRAL.",
            "rubric": "Sentiment classification prompt created."
        },
        {
            "title": "Data Extraction",
            "theory": "## Extracting Entities\nLLMs can pull structured data (like Names, Dates, Amounts) from unstructured text.",
            "instructions": "## Task: Extraction Prompt\n1. Ask the model to extract the Name and Age from the text and format as JSON.",
            "starterCode": "prompt = \"Extract ___ and ___ from the text and output as ___.\"",
            "solution": "prompt = \"Extract Name and Age from the text and output as JSON.\"",
            "hint": "Name, Age, JSON.",
            "rubric": "Data extraction prompt defined."
        }
    ],
    "LLM Fundamentals": [
        {
            "title": "Tokens",
            "theory": "## Tokenization\nLLMs process text in chunks called 'tokens' (roughly parts of words). 1 token ≈ 4 characters in English.",
            "instructions": "## Task: Estimate Tokens\n1. Write a function that estimates token count by dividing string length by 4.",
            "starterCode": "def estimateTokens(text):\n    return len(___) // ___",
            "solution": "def estimateTokens(text):\n    return len(text) // 4",
            "hint": "Divide length of text by 4.",
            "rubric": "Token estimation logic is correct."
        },
        {
            "title": "Temperature",
            "theory": "## Creativity vs Determinism\nTemperature controls randomness. 0.0 is deterministic and repetitive. 1.0 is highly creative and random.",
            "instructions": "## Task: Set Temperature\n1. Set temperature to 0.0 for a coding task, and 0.8 for a poetry task.",
            "starterCode": "code_temp = ___\npoetry_temp = ___",
            "solution": "code_temp = 0.0\npoetry_temp = 0.8",
            "hint": "0.0 for code, 0.8 for poetry.",
            "rubric": "Temperature settings appropriately chosen."
        },
        {
            "title": "Context Window",
            "theory": "## Max Tokens\nEvery model has a maximum context window (input + output tokens combined). Exceeding it causes errors.",
            "instructions": "## Task: Check Limit\n1. If input tokens + output tokens > 8192, return False (exceeds limit).",
            "starterCode": "def isValid(inp, out):\n    return (inp + out) ___ 8192",
            "solution": "def isValid(inp, out):\n    return (inp + out) <= 8192",
            "hint": "Must be less than or equal to 8192.",
            "rubric": "Context limit validation logic works."
        }
    ],
    "RAG Pipelines": [
        {
            "title": "What is RAG?",
            "theory": "## Retrieval-Augmented Generation\nRAG solves LLM hallucinations by retrieving factual documents from a database and adding them to the prompt before generating an answer.",
            "instructions": "## Task: RAG Steps\n1. The 3 steps of RAG are: 'Retrieve', 'Augment', 'Generate'. Create a list.",
            "starterCode": "rag_steps = [\"___\", \"___\", \"___\"]",
            "solution": "rag_steps = [\"Retrieve\", \"Augment\", \"Generate\"]",
            "hint": "Retrieve, Augment, Generate.",
            "rubric": "RAG steps identified correctly."
        },
        {
            "title": "Chunking Text",
            "theory": "## Text Chunking\nLarge documents must be split into smaller 'chunks' to fit into context windows and produce specific embeddings.",
            "instructions": "## Task: Split by Character\n1. Write a function to split a string into chunks of size 100.",
            "starterCode": "def chunkText(text):\n    return [text[i:___] for i in range(0, len(text), 100)]",
            "solution": "def chunkText(text):\n    return [text[i:i+100] for i in range(0, len(text), 100)]",
            "hint": "Use i:i+100.",
            "rubric": "Chunking algorithm is correct."
        },
        {
            "title": "Augmenting Prompts",
            "theory": "## Context Injection\nOnce documents are retrieved, they must be injected into the prompt.",
            "instructions": "## Task: Create Context Prompt\n1. Inject `retrieved_text` and `user_question` into the prompt template.",
            "starterCode": "prompt = f\"Context: {___}\\nAnswer the question: {___}\"",
            "solution": "prompt = f\"Context: {retrieved_text}\\nAnswer the question: {user_question}\"",
            "hint": "Inject the variables.",
            "rubric": "Context augmentation prompt built properly."
        }
    ],
    "LangChain Basics": [
        {
            "title": "LLM Wrappers",
            "theory": "## LangChain LLMs\nLangChain provides a unified interface for different LLM providers (OpenAI, Anthropic, etc.).",
            "instructions": "## Task: Init ChatOpenAI\n1. Import and instantiate `ChatOpenAI` with `temperature=0`.",
            "starterCode": "from langchain_openai import ___\nllm = ___(temperature=___)",
            "solution": "from langchain_openai import ChatOpenAI\nllm = ChatOpenAI(temperature=0)",
            "hint": "Use ChatOpenAI.",
            "rubric": "LangChain LLM wrapper instantiated."
        },
        {
            "title": "Prompt Templates",
            "theory": "## PromptTemplate\nLangChain templates allow easy dynamic prompt generation.",
            "instructions": "## Task: Create a Template\n1. Create a `PromptTemplate` with input variable `topic`.",
            "starterCode": "from langchain_core.prompts import PromptTemplate\ntemplate = PromptTemplate.from_template(\"Tell me a joke about {___}\")",
            "solution": "from langchain_core.prompts import PromptTemplate\ntemplate = PromptTemplate.from_template(\"Tell me a joke about {topic}\")",
            "hint": "Use {topic}.",
            "rubric": "PromptTemplate created successfully."
        },
        {
            "title": "LCEL Chains",
            "theory": "## LangChain Expression Language\nLCEL allows chaining components using the `|` pipe operator.",
            "instructions": "## Task: Build a Chain\n1. Chain the `template`, `llm`, and a `StrOutputParser` together.",
            "starterCode": "chain = ___ | ___ | StrOutputParser()",
            "solution": "chain = template | llm | StrOutputParser()",
            "hint": "template | llm.",
            "rubric": "LCEL chain built properly."
        }
    ],
    "Vector Databases": [
        {
            "title": "Embeddings",
            "theory": "## Vector Embeddings\nEmbeddings convert text into high-dimensional numerical vectors where similar meanings are close together in vector space.",
            "instructions": "## Task: Mock Embedding\n1. Return a list of 3 floats representing a vector.",
            "starterCode": "def getEmbedding(text):\n    return [0.1, ___, ___]",
            "solution": "def getEmbedding(text):\n    return [0.1, 0.5, 0.9]",
            "hint": "Just add floats.",
            "rubric": "Vector embedding mock generated."
        },
        {
            "title": "Cosine Similarity",
            "theory": "## Similarity Search\nCosine similarity measures the angle between two vectors to determine how similar their meanings are.",
            "instructions": "## Task: Calculate Similarity\n1. Assume a function `dotProduct` and `magnitude` exist. Calculate `dotProduct(A,B) / (magnitude(A)*magnitude(B))`.",
            "starterCode": "sim = ___(A,B) / (___(A) * ___(B))",
            "solution": "sim = dotProduct(A,B) / (magnitude(A) * magnitude(B))",
            "hint": "Use the assumed functions.",
            "rubric": "Cosine similarity formula implemented."
        },
        {
            "title": "Storing Vectors",
            "theory": "## Vector DBs\nDatabases like Chroma, Pinecone, or pgvector store vectors and perform rapid similarity searches.",
            "instructions": "## Task: Name Vector DBs\n1. List two popular vector databases: 'Chroma' and 'Pinecone'.",
            "starterCode": "vector_dbs = [\"___\", \"___\"]",
            "solution": "vector_dbs = [\"Chroma\", \"Pinecone\"]",
            "hint": "Chroma, Pinecone.",
            "rubric": "Vector databases accurately listed."
        }
    ],
    "Fine-tuning Concepts": [
        {
            "title": "When to Fine-tune",
            "theory": "## Fine-tuning vs RAG\nRAG provides external knowledge. Fine-tuning adjusts the model's tone, style, and inherent format responses.",
            "instructions": "## Task: Decide Approach\n1. Return 'RAG' if updating facts. Return 'Fine-tune' if learning a new language style.",
            "starterCode": "def chooseApproach(goal):\n    if goal == 'Facts': return '___'\n    if goal == 'Style': return '___'",
            "solution": "def chooseApproach(goal):\n    if goal == 'Facts': return 'RAG'\n    if goal == 'Style': return 'Fine-tune'",
            "hint": "Facts->RAG, Style->Fine-tune.",
            "rubric": "Fine-tuning decisions map accurately."
        },
        {
            "title": "Dataset Format",
            "theory": "## JSONL\nFine-tuning datasets are usually provided in JSONL format (one JSON object per line) containing prompt/completion pairs.",
            "instructions": "## Task: Format JSONL\n1. Format a dictionary as a JSON string for a JSONL file.",
            "starterCode": "import json\nline = json.___({\"prompt\": \"Q\", \"completion\": \"A\"})",
            "solution": "import json\nline = json.dumps({\"prompt\": \"Q\", \"completion\": \"A\"})",
            "hint": "Use json.dumps().",
            "rubric": "JSONL formatting handled correctly."
        },
        {
            "title": "PEFT and LoRA",
            "theory": "## Efficient Tuning\nParameter-Efficient Fine-Tuning (PEFT) using techniques like LoRA freezes the main model and only trains a tiny adapter layer, saving huge costs.",
            "instructions": "## Task: LoRA concept\n1. Does LoRA train the entire model? Set `trains_all_weights` to `False`.",
            "starterCode": "trains_all_weights = ___",
            "solution": "trains_all_weights = False",
            "hint": "Set to False.",
            "rubric": "LoRA theoretical concept grasped."
        }
    ],
    "LangChain & Agents": [
        {
            "title": "What is an Agent?",
            "theory": "## AI Agents\nAgents use an LLM as a reasoning engine to decide which tools to call and what actions to take in a loop until a goal is met.",
            "instructions": "## Task: Agent Loop\n1. Define the agent loop steps: 'Thought', 'Action', 'Observation'.",
            "starterCode": "loop = [\"___\", \"___\", \"___\"]",
            "solution": "loop = [\"Thought\", \"Action\", \"Observation\"]",
            "hint": "ReAct pattern: Thought, Action, Observation.",
            "rubric": "Agent reasoning loop steps identified."
        },
        {
            "title": "Tools",
            "theory": "## Agent Tools\nTools are functions the agent can execute (e.g., Search, Calculator). They need a clear name and description so the LLM knows when to use them.",
            "instructions": "## Task: Define a Tool\n1. Use the `@tool` decorator on a function `add`.",
            "starterCode": "from langchain_core.tools import tool\n\n@___\ndef add(a: int, b: int) -> int:\n    \"\"\"Adds two integers\"\"\"\n    return a + b",
            "solution": "from langchain_core.tools import tool\n\n@tool\ndef add(a: int, b: int) -> int:\n    \"\"\"Adds two integers\"\"\"\n    return a + b",
            "hint": "Use @tool.",
            "rubric": "LangChain tool defined correctly."
        },
        {
            "title": "Initializing Agents",
            "theory": "## AgentExecutor\nIn LangChain, an `AgentExecutor` runs the agent and handles tool execution loops.",
            "instructions": "## Task: Create Executor\n1. Instantiate an `AgentExecutor` with `agent` and `tools`.",
            "starterCode": "from langchain.agents import AgentExecutor\nexecutor = ___(agent=___, tools=___)",
            "solution": "from langchain.agents import AgentExecutor\nexecutor = AgentExecutor(agent=agent, tools=tools)",
            "hint": "Call AgentExecutor().",
            "rubric": "Agent executor initialized."
        }
    ],
    "Multi-Agent Systems": [
        {
            "title": "LangGraph Basics",
            "theory": "## State Machines\nLangGraph models multi-agent workflows as graphs (State Machines) where nodes are functions/agents and edges determine control flow.",
            "instructions": "## Task: Create a Graph\n1. Initialize a `StateGraph` passing a `State` type.",
            "starterCode": "from langgraph.graph import ___\nworkflow = ___(State)",
            "solution": "from langgraph.graph import StateGraph\nworkflow = StateGraph(State)",
            "hint": "Use StateGraph.",
            "rubric": "LangGraph initialized."
        },
        {
            "title": "Nodes and Edges",
            "theory": "## Graph Components\nAdd nodes (functions) and connect them with edges.",
            "instructions": "## Task: Build the Flow\n1. Add a node 'agent_1'. Add an edge from 'agent_1' to 'agent_2'.",
            "starterCode": "workflow.___(\"agent_1\", agent_1_func)\nworkflow.___(\"agent_1\", \"agent_2\")",
            "solution": "workflow.add_node(\"agent_1\", agent_1_func)\nworkflow.add_edge(\"agent_1\", \"agent_2\")",
            "hint": "Use add_node and add_edge.",
            "rubric": "Nodes and edges added to graph."
        },
        {
            "title": "Conditional Edges",
            "theory": "## Routing\nConditional edges run a function to decide which node to go to next (e.g., continue vs END).",
            "instructions": "## Task: Conditional Routing\n1. Add a conditional edge from 'agent_1' using a router function.",
            "starterCode": "workflow.___(\"agent_1\", router_func)",
            "solution": "workflow.add_conditional_edges(\"agent_1\", router_func)",
            "hint": "Use add_conditional_edges.",
            "rubric": "Conditional edge implemented."
        }
    ],
    "LLM Evaluation": [
        {
            "title": "Evaluating Outputs",
            "theory": "## LLM as a Judge\nSince LLM outputs are unstructured text, we often use another LLM (Judge) to score the output for relevance, toxicity, or accuracy.",
            "instructions": "## Task: Judge Prompt\n1. Write a prompt asking an LLM to score an answer from 1 to 5.",
            "starterCode": "prompt = \"Score this answer from ___ to ___ based on accuracy.\"",
            "solution": "prompt = \"Score this answer from 1 to 5 based on accuracy.\"",
            "hint": "From 1 to 5.",
            "rubric": "Judge evaluation prompt structured."
        },
        {
            "title": "RAG Metrics",
            "theory": "## RAGAS\nEvaluating RAG systems involves two parts: Retrieval metrics (did we find the right documents?) and Generation metrics (did we answer based on the docs?).",
            "instructions": "## Task: Identify Metrics\n1. Assign 'Retrieval' to finding docs, and 'Generation' to answering.",
            "starterCode": "finding = \"___\"\nanswering = \"___\"",
            "solution": "finding = \"Retrieval\"\nanswering = \"Generation\"",
            "hint": "Retrieval, Generation.",
            "rubric": "RAG metrics conceptualized."
        },
        {
            "title": "Ground Truth",
            "theory": "## Test Sets\nEvaluation requires a 'golden' dataset of inputs and known good expected outputs (ground truth) to measure against.",
            "instructions": "## Task: Create Test Case\n1. Create a dict with `question`, `output`, and `ground_truth`.",
            "starterCode": "test_case = {\"___\": \"Hi\", \"___\": \"Hello\", \"___\": \"Hello\"}",
            "solution": "test_case = {\"question\": \"Hi\", \"output\": \"Hello\", \"ground_truth\": \"Hello\"}",
            "hint": "Use the keys mentioned.",
            "rubric": "Test case schema matches evaluation standards."
        }
    ],
    "Production AI Systems": [
        {
            "title": "Streaming Responses",
            "theory": "## UX Optimization\nLLMs are slow. Streaming sends tokens to the UI as they are generated to improve perceived performance.",
            "instructions": "## Task: Async Streaming\n1. Iterate over an async stream using `async for chunk in stream:`.",
            "starterCode": "___ ___ chunk ___ stream:\n    print(chunk, end=\"\")",
            "solution": "async for chunk in stream:\n    print(chunk, end=\"\")",
            "hint": "async for ... in ...",
            "rubric": "Async streaming generator consumed correctly."
        },
        {
            "title": "Caching",
            "theory": "## Semantic Caching\nCaching identical requests saves money. Semantic caching checks if a prompt has the same *meaning* as a cached prompt using vector similarity.",
            "instructions": "## Task: Cache Hit\n1. Return True if similarity score > 0.95.",
            "starterCode": "def isCacheHit(similarity):\n    return similarity > ___",
            "solution": "def isCacheHit(similarity):\n    return similarity > 0.95",
            "hint": "0.95",
            "rubric": "Semantic caching threshold configured."
        },
        {
            "title": "Monitoring LLMs",
            "theory": "## Observability\nIn production, track token usage, costs, latency, and user feedback to ensure the AI system performs well and stays within budget.",
            "instructions": "## Task: Track Usage\n1. Create a log dictionary storing `tokens` and `latency`.",
            "starterCode": "log = {\"___\": 150, \"___\": 1.2}",
            "solution": "log = {\"tokens\": 150, \"latency\": 1.2}",
            "hint": "tokens, latency.",
            "rubric": "Monitoring metrics structured properly."
        }
    ],
    "AI Safety & Ethics": [
        {
            "title": "Prompt Injection",
            "theory": "## Security Vulnerability\nPrompt injection occurs when a user maliciously crafts input that overrides the system prompt's instructions.",
            "instructions": "## Task: Identify Injection\n1. Return True if input contains \"Ignore previous instructions\".",
            "starterCode": "def is_injection(user_input):\n    return \"___ ___ ___\" in user_input",
            "solution": "def is_injection(user_input):\n    return \"Ignore previous instructions\" in user_input",
            "hint": "Ignore previous instructions",
            "rubric": "Basic prompt injection detection algorithm applied."
        },
        {
            "title": "Bias and Hallucination",
            "theory": "## AI Limitations\nHallucinations are confident but factually incorrect outputs. Bias reflects unfair prejudices learned from training data.",
            "instructions": "## Task: Define Issues\n1. Assign 'Hallucination' to making things up, and 'Bias' to unfair treatment.",
            "starterCode": "fake_facts = \"___\"\nunfair_treatment = \"___\"",
            "solution": "fake_facts = \"Hallucination\"\nunfair_treatment = \"Bias\"",
            "hint": "Hallucination, Bias",
            "rubric": "AI safety concepts defined."
        }
    ]
}


def add_lessons(track_file, new_lessons_dict):
    with open(track_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    added = 0
    for course_name, new_lessons in new_lessons_dict.items():
        if course_name in data:
            data[course_name]["lessons"].extend(new_lessons)
            added += len(new_lessons)
            print(f"[OK] {course_name}: +{len(new_lessons)} lessons")
        else:
            print(f"[WARN] Course not found: {course_name}")
    
    with open(track_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\\nDone! Added {added} new lessons to {track_file}")

if __name__ == "__main__":
    print("--- Updating Data Science ---")
    add_lessons("curriculum/tracks/data_science.json", NEW_DS_LESSONS)
    print("\\n--- Updating AI Engineering ---")
    add_lessons("curriculum/tracks/ai_engineering.json", NEW_AI_LESSONS)
