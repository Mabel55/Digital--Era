import json

with open("curriculum/tracks/data_science.json", "r", encoding="utf-8") as f:
    data = json.load(f)

theories = {
    ("Pandas Intro", "Creating DataFrames"): """## The Foundation of Data Science

In data science, your primary tool is the **DataFrame**—a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, but supercharged with Python's programmatic power.

The industry standard library for this is **Pandas**. 

### Why Pandas?

Python's built-in lists and dictionaries are great for general programming, but they are incredibly slow and cumbersome for analyzing millions of rows of data. Pandas is built on top of NumPy (which is written in C), making it incredibly fast.

### Creating DataFrames

While you will usually load data from a file, you must know how to create DataFrames manually to understand their structure.

**1. From a Dictionary (Column-oriented)**
When creating a DataFrame from a dictionary, the keys become the column headers, and the lists become the column values.

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)
```

**2. From a List of Lists (Row-oriented)**
You can also create a DataFrame row by row. In this case, you must pass the column names separately.

```python
rows = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 35, "Paris"]
]

df = pd.DataFrame(rows, columns=["Name", "Age", "City"])
```

### The Index

Every DataFrame has an **Index** (the bold numbers on the far left when printed). By default, Pandas assigns a numeric index starting at 0. The Index is crucial for fast lookups, alignments, and joining tables together.

You can set a specific column to be the index if it contains unique identifiers (like an Employee ID or a Date).

```python
# Make 'Name' the index instead of 0, 1, 2
df.set_index('Name', inplace=True)
```""",

    ("Pandas Intro", "Selecting Data"): """## Indexing and Slicing DataFrames

Extracting specific rows and columns is the most common operation in Pandas. Unlike standard Python lists where you use `my_list[0]`, Pandas has specialized accessors designed for 2D data: **`.loc`** and **`.iloc`**.

### 1. Selecting Columns (Dictionary Style)

You can select a single column using bracket notation. This returns a **Series** (a 1D array).
```python
ages = df["Age"]
```
To select multiple columns, you must pass a *list* of column names inside the brackets. This returns a new **DataFrame**.
```python
subset = df[["Name", "City"]] # Notice the double brackets!
```

### 2. Selecting Rows by Position (`.iloc`)

`iloc` stands for **Integer Location**. It is purely zero-indexed, exactly like standard Python lists.
- `df.iloc[0]` -> The very first row.
- `df.iloc[:5]` -> The first 5 rows (0 through 4).
- `df.iloc[0, 1]` -> The value at row 0, column 1.

### 3. Selecting Rows by Label (`.loc`)

`loc` accesses rows and columns based on their **Labels** (the Index name or Column name). 

```python
# Assuming 'Name' is the index
df.loc["Alice"] 

# Select multiple rows by label
df.loc[["Alice", "Charlie"]]

# Select specific rows AND specific columns!
df.loc["Alice", "City"] # Returns "New York"
```

### 4. Boolean Indexing (Filtering)

The most powerful way to select data is by condition. 
When you evaluate a column (e.g., `df["Age"] > 30`), Pandas returns a Series of True/False values. If you pass that Boolean Series back into the DataFrame brackets, it filters the rows!

```python
# 1. Create the condition
is_old = df["Age"] > 30

# 2. Apply the filter
older_people = df[is_old]

# Doing it in one clean line:
older_people = df[df["Age"] > 30]
```
Mastering boolean indexing is the key to cleaning and exploring messy datasets.""",

    ("Pandas Intro", "Basic Statistics"): """## Statistical Analysis in Pandas

Before you can build complex machine learning models, you must understand the basic statistical properties of your dataset. Pandas provides built-in methods to summarize massive datasets instantly.

### The `describe()` Method

The fastest way to understand a dataset is the `.describe()` method. By default, it generates descriptive statistics for every numeric column in the DataFrame.

```python
df.describe()
```
Output includes:
- **count**: Number of non-null values. (Instantly reveals missing data!)
- **mean**: The average value.
- **std**: Standard Deviation (how spread out the data is).
- **min / max**: The lowest and highest values.
- **25%, 50%, 75%**: The quartiles (50% is the median).

### Individual Statistical Functions

You can also call specific functions on individual columns (Series):

- `df["Salary"].mean()`
- `df["Salary"].median()` (Often more useful than mean, as it ignores extreme outliers like billionaires).
- `df["Salary"].sum()`

### Value Counts (For Categorical Data)

`describe()` doesn't work well for text data (like "City" or "Department"). For categorical columns, the most useful function is `.value_counts()`.

It returns the frequency of each unique value, automatically sorted from most frequent to least frequent.

```python
df["Department"].value_counts()
# Output:
# Sales        150
# Engineering  120
# HR            30
```

To see the percentages instead of raw counts, use `normalize=True`:
```python
df["Department"].value_counts(normalize=True)
# Output:
# Sales        0.50 (50%)
# Engineering  0.40 (40%)
# HR           0.10 (10%)
```""",

    ("Pandas Intro", "Adding & Modifying Columns"): """## Feature Engineering Basics

Data is rarely perfectly formatted when you receive it. You will constantly need to create new columns based on existing data, or modify existing columns to clean them up. This process is the foundation of Feature Engineering.

### Creating a New Column

To create a new column, simply assign data to a column name that doesn't exist yet, just like adding a new key to a Python dictionary.

**1. Creating from a scalar (single value):**
```python
# Sets the value to 'Active' for every single row
df["Status"] = "Active"
```

**2. Creating from a calculation (Vectorization):**
Because Pandas is built on NumPy, you don't need to write `for` loops to do math on columns. You can multiply entire columns together instantly (this is called vectorization).

```python
# Calculate Total Price instantly for millions of rows
df["Total"] = df["Quantity"] * df["Price"]
```

### Modifying Existing Columns

You can overwrite existing columns using the same syntax.

```python
# Convert a discount percentage to a decimal
df["Discount"] = df["Discount"] / 100
```

### The `apply()` Function

When simple math isn't enough, you can use the `.apply()` method to run a custom Python function on every single row (or element) in a column.

```python
# Define a custom logic function
def categorize_age(age):
    if age < 18: return "Minor"
    elif age < 65: return "Adult"
    else: return "Senior"

# Apply it to the column to create a new one
df["Age_Group"] = df["Age"].apply(categorize_age)
```

*Note: While `.apply()` is incredibly flexible, it relies on standard Python loops under the hood, making it significantly slower than vectorized math (like `df["A"] + df["B"]`). Always prefer vectorization when possible for large datasets.*""",

    ("Pandas Intro", "GroupBy & Aggregation"): """## The Split-Apply-Combine Strategy

`groupby` is arguably the most powerful tool in Pandas for data analysis. It allows you to group rows that share a common value, and then calculate statistics for each group independently.

This follows the **Split-Apply-Combine** pattern:
1. **Split** the data into groups based on some criteria.
2. **Apply** a function (like sum, mean, count) to each group independently.
3. **Combine** the results into a new data structure.

### Basic Grouping

Imagine a DataFrame of sales data with columns `['Region', 'Salesperson', 'Revenue']`. To find the total revenue per region:

```python
# 1. Split by Region
groups = df.groupby("Region")

# 2. Select the column to calculate on, and Apply the 'sum' function
total_sales = groups["Revenue"].sum()
```

The result is a new Series where the Index is the unique Regions ("North", "South") and the values are the sums.

### Multiple Aggregations (`.agg`)

Sometimes you want multiple statistics at once. You can use the `.agg()` method to pass a list of functions.

```python
# Get the total revenue AND the average revenue per region
df.groupby("Region")["Revenue"].agg(["sum", "mean", "max"])
```

### Grouping by Multiple Columns

You can group by more than one category by passing a list to `groupby`. This creates a MultiIndex (a hierarchical index).

```python
# Find total revenue for each Salesperson WITHIN each Region
df.groupby(["Region", "Salesperson"])["Revenue"].sum()

# Output might look like:
# Region  Salesperson
# North   Alice          50000
#         Bob            45000
# South   Charlie        60000
```

`groupby` answers the fundamental business questions: "Who sold the most?", "Which region is most profitable?", "What is the average salary by department?" """,

    ("Data Cleaning", "Handling Missing Data"): """## The Reality of Messy Data

In the real world, datasets are never perfect. Sensors fail, users skip form fields, and databases get corrupted. These missing values show up in Pandas as `NaN` (Not a Number) or `None`.

Machine learning algorithms (like Linear Regression or Random Forests in scikit-learn) **will crash** if you feed them `NaN` values. Handling them is your first job as a data scientist.

### 1. Detecting Missing Data

To find out where your missing data is, use `.isna()` (or its alias `.isnull()`).

```python
# Returns a boolean mask of the entire DataFrame
df.isna()

# Combine with .sum() to get a count of missing values per column
print(df.isna().sum())
# Output:
# Age      5
# Salary  12
# City     0
```

### 2. Strategy A: Dropping Missing Data

If you have a massive dataset and only a tiny fraction of rows are missing data, the safest statistical choice is often to just delete those rows.

```python
# Drop any row that contains AT LEAST ONE NaN value
clean_df = df.dropna()

# Drop rows ONLY if the 'Salary' column is missing
clean_df = df.dropna(subset=["Salary"])
```

### 3. Strategy B: Imputation (Filling)

If you have a small dataset, dropping rows is destructive. Instead, you "impute" (guess or fill in) the missing values using `.fillna()`.

- **Numeric Data**: Often filled with the Mean or Median of that column.
- **Categorical Data**: Often filled with the Mode (most frequent value) or a string like "Unknown".

```python
# Calculate the median age
median_age = df["Age"].median()

# Fill missing ages with the median
df["Age"].fillna(median_age, inplace=True)

# Fill missing cities with a string
df["City"].fillna("Unknown", inplace=True)
```
*Note: Always calculate the mean/median on your Training data ONLY, and use that value to fill your Test data to prevent Data Leakage.*""",

    ("Data Cleaning", "Removing Duplicates"): """## Data Deduplication

Duplicate records can severely skew your analysis. If a user accidentally submits a form twice, and you calculate the average user age, that duplicated user is given twice the statistical weight they deserve.

In Machine Learning, if duplicated rows end up in both your Training Set and your Test Set, your model will look artificially brilliant because it is essentially "cheating" by being tested on data it has already seen.

### Finding Duplicates

The `.duplicated()` method returns a Boolean Series: `True` if the row is an exact duplicate of a previous row, and `False` if it is unique.

```python
# Show all rows that are duplicates
duplicates = df[df.duplicated()]
print(f"Found {len(duplicates)} duplicate rows.")
```

By default, `.duplicated()` looks at *all* columns. It only flags a row if every single value matches a previous row.

### Removing Duplicates

The `.drop_duplicates()` method removes these rows, keeping only the first occurrence by default.

```python
# Remove exact duplicates
df = df.drop_duplicates()
```

### Subset Deduplication

Sometimes, you only want to look at specific columns to determine if a row is a duplicate. 

For example, you have a dataset of customer purchases. If a customer is only allowed to use a signup discount once, you want to ensure there is only one row per `Email_Address`, regardless of what they purchased.

```python
# Keep only the LAST purchase made by each email address
df = df.drop_duplicates(
    subset=["Email_Address"], 
    keep="last" # Options are 'first', 'last', or False (drop ALL duplicates)
)
```
Deduplication is a critical step in the ETL (Extract, Transform, Load) pipeline before data enters a warehouse.""",

    ("Matplotlib", "Data Visualization"): """## Visualizing Data with Matplotlib

Humans are terrible at reading spreadsheets, but excellent at recognizing visual patterns. Data visualization is essential for both exploring data (finding outliers and trends) and communicating results to stakeholders.

**Matplotlib** is the foundational plotting library in Python. It provides fine-grained control over every element of a chart.

### The PyPlot Interface

We interact with Matplotlib through its `pyplot` module, universally imported as `plt`.

```python
import matplotlib.pyplot as plt

# 1. Create the data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 2. Plot the data
plt.plot(x, y) // A line chart

# 3. Add context (Crucial!)
plt.title("Revenue over Time")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")

# 4. Render the image
plt.show() 
```

### Core Chart Types

1. **Line Chart (`plt.plot`)**: Best for showing trends over time (Time Series).
2. **Scatter Plot (`plt.scatter`)**: Best for showing the relationship or correlation between two numerical variables (e.g., Height vs. Weight).
3. **Bar Chart (`plt.bar`)**: Best for comparing categorical data (e.g., Sales by Region).
4. **Histogram (`plt.hist`)**: Best for viewing the *distribution* of a single numerical variable (e.g., Age brackets of users).

### Integration with Pandas

Because Pandas is so ubiquitous, it has Matplotlib built directly into it. You can call `.plot()` directly on a DataFrame!

```python
# Instantly plots a line chart of the Revenue column
df["Revenue"].plot(kind="line", title="Daily Revenue")
plt.show()

# Instantly plot a histogram of ages
df["Age"].plot(kind="hist", bins=20)
plt.show()
```
While Matplotlib is powerful, its default styles are quite basic. Modern data scientists often use higher-level libraries like Seaborn (built on top of Matplotlib) for more beautiful, statistical visualizations.""",

    ("Statistical Analysis", "Mean, Median, Mode"): """## Measures of Central Tendency

When describing a dataset, the first question is usually: "What is the typical value?" We use Measures of Central Tendency to answer this, but choosing the *wrong* measure can completely misrepresent the truth.

### 1. The Mean (Average)
The sum of all values divided by the number of values.
- **Pros**: Uses all data points; mathematically useful.
- **Cons**: Extremely sensitive to **Outliers**. 
- *Example*: If 9 people in a bar earn $50,000, the mean is $50k. If Elon Musk walks in, the mean income of the room shoots to $20 Billion. The mean no longer represents the "typical" person in the bar.

```python
average_salary = df["Salary"].mean()
```

### 2. The Median (Middle)
If you sort all the data from smallest to largest, the Median is the exact middle value (the 50th percentile).
- **Pros**: Robust against outliers. Elon Musk walking into the bar barely changes the median.
- **Cons**: Ignores the actual magnitude of extreme values.
- *Rule of Thumb*: Always use Median for Income, House Prices, or anything with a "long tail" distribution (where a few massive values skew the data).

```python
typical_salary = df["Salary"].median()
```

### 3. The Mode (Most Frequent)
The value that appears most often in the dataset.
- **Pros**: The ONLY measure of central tendency you can use on Categorical (text) data! You can't calculate the "average" eye color, but you can find the most frequent one.

```python
# Mode returns a Series, because there could be a tie!
most_common_color = df["Eye_Color"].mode()[0]
```

### The Skew

Comparing the Mean and Median tells you the shape of your data:
- **Mean == Median**: Perfect normal distribution (Bell Curve).
- **Mean > Median**: Right-skewed (e.g., wealth distribution. The tail of rich people pulls the average up).
- **Mean < Median**: Left-skewed (e.g., age of retirement).""",

    ("Scikit-Learn", "Intro to Machine Learning"): """## The Machine Learning Pipeline

**Scikit-Learn** (sklearn) is the industry standard Python library for traditional Machine Learning. It provides a clean, uniform API for hundreds of algorithms, from Linear Regression to Random Forests.

### Supervised vs. Unsupervised Learning

- **Supervised Learning**: The data has "labels" (answers). We train the model to predict the label from the features.
  - *Regression*: Predicting a continuous number (e.g., House Price).
  - *Classification*: Predicting a category (e.g., Spam or Not Spam).
- **Unsupervised Learning**: The data has no labels. The model finds hidden structure (e.g., Clustering customers into marketing segments).

### The Sklearn Workflow

Every model in scikit-learn follows the exact same 3-step API pattern: Instantiate, Fit, Predict.

**1. Prepare the Data (X and y)**
Features (`X`) are usually a 2D DataFrame. The Target (`y`) is usually a 1D Series.
```python
X = df[["Age", "Income", "Credit_Score"]] # The inputs
y = df["Defaulted_On_Loan"]               # The answer
```

**2. Instantiate the Model**
Create an object of the algorithm you want to use.
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
```

**3. Fit (Train) the Model**
The algorithm looks at the data and learns the mathematical relationship between X and y.
```python
model.fit(X, y)
```

**4. Predict**
Pass in new, unseen data to get predictions.
```python
new_customer = [[35, 75000, 680]]
prediction = model.predict(new_customer)
```

### Train/Test Split

If you train a model on all your data, and then evaluate it on that same data, it will look like a genius (because it just memorized the answers). 
You must always split your data into a **Training Set** (to learn) and a **Test Set** (to evaluate performance on unseen data) using `train_test_split()`. Usually an 80/20 split.""",

    ("Feature Engineering", "One-Hot Encoding"): """## Making Text Machine-Readable

Machine Learning models (like Linear Regression or Neural Networks) are just massive mathematical equations. They only understand numbers. If you feed the string `"Paris"` into an equation, it will crash.

**Feature Engineering** is the process of converting real-world data (text, dates, categories) into numerical formats that algorithms can understand.

### The Problem with Label Encoding

Imagine a `Color` column: `["Red", "Green", "Blue"]`.
You might think to map them to integers: `Red=1, Green=2, Blue=3`. This is called Label Encoding.

**Why is this dangerous?**
The algorithm assumes numbers have mathematical relationships. It will think that `Red (1) + Green (2) = Blue (3)`, or that `Blue` is three times larger than `Red`. This ruins models like Linear Regression or K-Means. 

*Label Encoding should ONLY be used for Ordinal data (where order matters, like Small=1, Medium=2, Large=3).*

### The Solution: One-Hot Encoding

For nominal data (no inherent order, like Cities or Colors), we use **One-Hot Encoding** (or Dummy Variables).

It takes a single column and splits it into multiple binary (0 or 1) columns—one for every unique category.

**Original Data:**
| ID | Color |
|----|-------|
| 1  | Red   |
| 2  | Blue  |
| 3  | Green |

**One-Hot Encoded:**
| ID | Color_Red | Color_Blue | Color_Green |
|----|-----------|------------|-------------|
| 1  | 1         | 0          | 0           |
| 2  | 0         | 1          | 0           |
| 3  | 0         | 0          | 1           |

### Implementation in Pandas

Pandas has a built-in function to do this instantly: `pd.get_dummies()`.

```python
# Convert all categorical columns into One-Hot Encoded binary columns
df_encoded = pd.get_dummies(df, columns=["Color"])
```
*Note: In professional pipelines, Data Scientists use `OneHotEncoder` from Scikit-Learn instead of Pandas, because it can save the mapping to apply to future prediction data.*""",

    ("Time Series", "Handling Dates"): """## Temporal Data in Pandas

Time Series data (stock prices, weather readings, daily sales) is unique. Unlike cross-sectional data (a snapshot of customers), time series data has a strict chronological order, meaning yesterday's value strongly influences today's value.

### The Datetime Object

When you load a CSV, Pandas usually treats date columns as standard text (Strings). You cannot calculate the difference between two strings. 
You must explicitly convert them to Pandas `datetime` objects.

```python
# Convert string to datetime
df["Date"] = pd.to_datetime(df["Date"])
```

### The Power of `.dt` Accessor

Once a column is a `datetime`, Pandas unlocks the `.dt` accessor, allowing you to instantly extract components of the date for Feature Engineering.

```python
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["DayOfWeek"] = df["Date"].dt.dayofweek # 0=Monday, 6=Sunday
df["Is_Weekend"] = df["Date"].dt.dayofweek >= 5
```
*Why do this?* A machine learning model doesn't know that "2023-12-25" is a holiday, but if you extract the month and day, it can learn that sales spike in December.

### The Datetime Index

For heavy time series analysis, it is standard practice to set the Date column as the DataFrame Index. This unlocks powerful time-based slicing and resampling.

```python
df.set_index("Date", inplace=True)

# Select all data from the year 2023 instantly!
sales_2023 = df.loc["2023"]

# Select a specific month range
q1_sales = df.loc["2023-01":"2023-03"]
```

### Resampling (Time-based GroupBy)

If you have hourly data and want to view daily totals, you use `.resample()`, which is exactly like `.groupby()`, but for time.

```python
# Resample to Daily ('D') and sum the values
daily_totals = df.resample('D').sum()

# Resample to Monthly ('M') and find the mean
monthly_avg = df.resample('M').mean()
```""",

    ("NLP Basics", "Text Preprocessing"): """## Preparing Text for Machines

Natural Language Processing (NLP) allows algorithms to analyze human text. But as always, models only understand numbers. To turn sentences into math (a process called Vectorization), we must first thoroughly clean and standardize the text.

If you don't preprocess, the computer will think "Apple", "apple", and "apple!" are three entirely different words.

### The NLP Preprocessing Pipeline

**1. Lowercasing**
Standardize all text to lowercase to prevent case-sensitivity issues.
```python
text = text.lower()
```

**2. Removing Punctuation and Numbers**
Punctuation rarely adds meaning to basic classification models (like sentiment analysis). Regular Expressions (Regex) are used to strip them.
```python
import re
# Replace anything that is NOT a letter with a space
text = re.sub(r'[^a-z]', ' ', text) 
```

**3. Tokenization**
Splitting a long string (a document) into a list of individual words (tokens).
```python
# "hello world" -> ["hello", "world"]
tokens = text.split() 
```

**4. Stopword Removal**
Stopwords are common words ("the", "is", "in", "and") that carry almost no semantic meaning. They just clutter the data and slow down the model. We remove them using a predefined list (usually from the `NLTK` library).

**5. Stemming / Lemmatization**
Words like "running", "ran", and "runs" all mean the same core concept. 
- **Stemming**: Crudely chops off the ends of words ("running" -> "run"). Fast, but sometimes creates non-words ("happiness" -> "happi").
- **Lemmatization**: Uses a dictionary to find the linguistic root of the word ("better" -> "good"). Slower, but highly accurate.

### Result

**Original:** "The quick foxes are jumping over the lazy dogs!"
**Processed:** `["quick", "fox", "jump", "lazi", "dog"]`

Once the text is preprocessed into a clean list of tokens, it can be passed to a Vectorizer (like TF-IDF or Word2Vec) to be converted into numbers.""",

    ("Advanced ML Models", "Random Forests"): """## The Power of the Crowd

A **Decision Tree** is a simple algorithm that makes predictions by asking a series of True/False questions (e.g., "Is age > 30?", "Is income > 50k?"). 
While highly interpretable, single Decision Trees are terrible in practice because they **overfit**—they memorize the training data so perfectly that they fail completely on new data.

The solution is the **Random Forest**, one of the most powerful and widely used algorithms in Data Science.

### Ensemble Learning

A Random Forest is an "Ensemble" algorithm. It doesn't rely on one model; it builds a "forest" of hundreds of individual Decision Trees and asks them to vote on the final prediction. 
- In Classification: Majority vote wins (e.g., 80 trees say "Spam", 20 say "Not Spam" -> Result: "Spam").
- In Regression: The average of all trees is taken.

### Why is it "Random"?

If you give 100 trees the exact same data, they will all build the exact same tree. The magic of the Random Forest relies on injecting randomness to ensure every tree is slightly different (this is called *decorrelation*).

1. **Bagging (Bootstrap Aggregation)**: Each tree is trained on a random sample of the rows (with replacement).
2. **Feature Randomness**: At every split in the tree, the algorithm is only allowed to look at a random subset of the columns (features). It can't just pick the "best" column every time.

By forcing the trees to look at different parts of the data, some trees become "experts" in Age, while others become experts in Geography. When they vote together, the collective intelligence is vastly superior to any individual tree.

### Why Data Scientists Love Random Forests

1. **No Scaling Required**: Unlike Neural Networks or SVMs, Random Forests do not care if one column is measured in decimals (0.5) and another in millions (1,000,000). You don't need to normalize your data.
2. **Handles Missing Data & Categoricals well.**
3. **Feature Importance**: After training, the model can tell you exactly which columns were mathematically most important in making the predictions!

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100) # 100 trees in the forest
rf.fit(X_train, y_train)
```""",

    ("Seaborn Visualization", "Statistical Plots"): """## Seaborn — Beautiful Statistical Graphics

While Matplotlib is powerful, it is low-level and requires a lot of code to make charts look professional. **Seaborn** is a library built on top of Matplotlib specifically designed for statistical data visualization. It makes beautiful charts with one line of code.

### Univariate (One Variable) Plots

When exploring a dataset, you first look at the distribution of individual variables.

**1. Histoplot (`sns.histplot`)**
Shows the distribution of a continuous numeric variable (e.g., Age). Seaborn can automatically add a KDE (Kernel Density Estimate) curve to smooth the shape.
```python
import seaborn as sns
sns.histplot(df["Age"], kde=True)
```

**2. Countplot (`sns.countplot`)**
The categorical equivalent of a histogram. It acts like Pandas `.value_counts()`, automatically counting the frequency of categories and plotting them as bars.
```python
sns.countplot(x="Department", data=df)
```

### Bivariate (Two Variables) Plots

To find relationships between variables, we plot them against each other.

**1. Scatterplot (`sns.scatterplot`)**
Shows the correlation between two numeric variables (e.g., Height vs Weight).
Seaborn's superpower is the `hue` parameter, which instantly colors the dots based on a third categorical column.
```python
sns.scatterplot(x="Height", y="Weight", hue="Gender", data=df)
```

**2. Boxplot (`sns.boxplot`)**
The standard for visualizing how a continuous variable is distributed across different categories (e.g., Salary distribution per Department).
It shows the Median (center line), the Quartiles (the box), and the Outliers (individual dots outside the whiskers).
```python
sns.boxplot(x="Department", y="Salary", data=df)
```

### The Pairplot

The ultimate exploratory tool. `sns.pairplot(df)` automatically plots a grid showing the scatterplots of every numeric variable against every other numeric variable, with histograms on the diagonal. It provides an instant overview of all correlations in your dataset.""",

    ("Seaborn Visualization", "Heatmaps"): """## Correlation Matrices and Heatmaps

A fundamental part of Exploratory Data Analysis (EDA) is finding **Correlations**—statistical relationships between variables. 

- **Positive Correlation (1.0)**: As X goes up, Y goes up (e.g., Height and Shoe Size).
- **Negative Correlation (-1.0)**: As X goes up, Y goes down (e.g., Altitude and Temperature).
- **No Correlation (0.0)**: Variables are completely unrelated.

In Machine Learning, if a feature is highly correlated with the target variable, it's a great predictor! If two features are highly correlated with *each other* (Multicollinearity), you often want to drop one to simplify the model.

### 1. Generating the Correlation Matrix

Pandas can instantly calculate the Pearson correlation coefficient between all numeric columns.

```python
# Returns a DataFrame where rows and columns are the variable names,
# and values are the correlation coefficients (-1.0 to 1.0)
corr_matrix = df.corr()
```

### 2. Visualizing with a Seaborn Heatmap

Looking at a giant grid of numbers is difficult. We use a **Heatmap** to map those numbers to colors (e.g., Dark Red for strong positive correlation, Dark Blue for strong negative).

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Annot=True prints the actual numbers inside the colored squares
# cmap defines the color palette
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)

plt.title("Feature Correlation Heatmap")
plt.show()
```

### Interpreting the Heatmap

1. **The Diagonal**: Will always be 1.0 (Dark Red), because every variable is perfectly correlated with itself.
2. **Finding Predictors**: Look at the row/column for your Target Variable (e.g., `House_Price`). Look for squares that are dark red or dark blue. Those are the features you want to feed to your ML model.
3. **Finding Redundancy**: Look for dark red squares between two features (e.g., `Square_Footage` and `Number_of_Rooms`). You might not need both in your model.""",

    ("Cross-Validation", "K-Fold Split"): """## The Flaw in Train/Test Split

The standard way to evaluate a Machine Learning model is to split your data into an 80% Training Set and a 20% Test Set. 

**The Problem**: What if, by pure random chance, all the "hard" examples end up in the Test Set? Your model will perform terribly. What if all the "easy" examples end up in the Test Set? Your model will look like a genius, but will fail in production. This is called *Variance in Evaluation*.

### K-Fold Cross Validation

To solve this, we use **K-Fold Cross Validation**. Instead of splitting the data once, we split it into `K` equal-sized chunks (or "Folds"). Usually, K is 5 or 10.

If K=5, the process works like this:
1. Divide the dataset into 5 chunks (Fold 1, Fold 2, Fold 3, Fold 4, Fold 5).
2. **Iteration 1**: Train the model on Folds 2, 3, 4, 5. Evaluate it on Fold 1. Record the score.
3. **Iteration 2**: Train the model on Folds 1, 3, 4, 5. Evaluate it on Fold 2. Record the score.
4. Repeat this 5 times, so that *every single fold* has been used as the Test Set exactly once.

### The True Score

After 5 iterations, you have 5 different accuracy scores. You calculate the **Mean (Average)** of these scores to get the true performance of your model, and the **Standard Deviation** to see how stable the model is.

If the scores are: `[0.85, 0.86, 0.84, 0.85, 0.85]`, your model is incredibly stable.
If the scores are: `[0.95, 0.60, 0.99, 0.70, 0.80]`, your model is highly unstable and deeply dependent on which data it trained on (a red flag!).

K-Fold Cross Validation is the absolute gold standard in Data Science for proving that a model's performance isn't just a lucky fluke.""",

    ("Cross-Validation", "Cross Val Score"): """## Implementing Cross-Validation in Sklearn

While you *could* write a `for` loop to manually split your data into 5 folds, train the model, and evaluate it 5 times, Scikit-Learn provides a single function that does all of this automatically: `cross_val_score`.

### The `cross_val_score` Function

This function handles the splitting, training, predicting, and scoring behind the scenes.

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

# 1. Instantiate the model (Do NOT fit it!)
model = RandomForestClassifier()

# 2. Run Cross Validation
# cv=5 means 5-Fold Cross Validation
# scoring="accuracy" tells it what metric to return
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")

print("All 5 scores:", scores)
# Output: [0.82, 0.85, 0.81, 0.84, 0.83]

# 3. Calculate the Mean to report to stakeholders
print("Average Accuracy:", scores.mean())
```

### Stratified K-Fold

A hidden danger in cross-validation occurs with imbalanced datasets. If 90% of your patients are Healthy and 10% are Sick, a random K-Fold split might accidentally create a fold that contains 100% Healthy patients. A model trained on that fold will completely forget what "Sick" looks like.

Under the hood, if you pass a Classification model to `cross_val_score`, Scikit-Learn automatically uses a **Stratified K-Fold**. 

"Stratified" guarantees that the ratio of classes is perfectly preserved in every single fold. Every fold will contain exactly 90% Healthy and 10% Sick patients, ensuring stable and reliable training iterations.""",

    ("Hyperparameter Tuning", "Grid Search"): """## Finding the Perfect Configuration

When you instantiate a Machine Learning model in Scikit-Learn (e.g., `RandomForestClassifier()`), it comes with default settings. These settings are called **Hyperparameters**.

Unlike *Parameters* (which the model learns on its own during training, like the weights in an equation), *Hyperparameters* are the knobs and dials you must set *before* training begins.
- Example: `max_depth` (how deep a tree can grow).
- Example: `n_estimators` (how many trees in the forest).

The default hyperparameters are rarely optimal for your specific dataset. The process of finding the best combination is called **Hyperparameter Tuning**.

### GridSearchCV (Brute Force)

`GridSearchCV` automates the process of trying different combinations. 
You provide a "Grid" (a dictionary) of values you want to test. Scikit-Learn will train and evaluate the model using **every single possible combination** of those values.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# 1. Define the grid of hyperparameters to test
param_grid = {
    'n_estimators': [50, 100, 200],      # 3 options
    'max_depth': [None, 10, 20],         # 3 options
    'min_samples_split': [2, 5, 10]      # 3 options
}
# Total Combinations: 3 * 3 * 3 = 27 configurations

# 2. Instantiate the Grid Search object
# cv=5 means it uses 5-Fold Cross Validation for EVERY combination!
# Total model trainings: 27 combos * 5 folds = 135 trainings!
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)

# 3. Fit it to the data (This will take time!)
grid_search.fit(X_train, y_train)

# 4. View the results
print("Best parameters found:", grid_search.best_params_)
print("Best accuracy score:", grid_search.best_score_)

# You can now use grid_search just like a normal model to predict!
best_model = grid_search.best_estimator_
```

**The Drawback:** Grid Search guarantees you find the best combination *within your grid*, but it suffers from the Curse of Dimensionality. If you add a 4th hyperparameter with 5 options, the number of trainings jumps from 135 to 675. It scales exponentially and can take days to run on large datasets.""",

    ("Hyperparameter Tuning", "Randomized Search"): """## Faster Tuning with Randomized Search

Because `GridSearchCV` tries every single possible combination, it becomes computationally impossible when you have dozens of hyperparameters with continuous ranges.

**RandomizedSearchCV** is the modern alternative. Instead of providing a rigid list of values, you provide a statistical distribution (or a list), and tell the algorithm: *"Pick X random combinations and try them."*

### Why Random Beats Grid

Research shows that in most algorithms, only a few hyperparameters actually matter. If you use Grid Search, the algorithm spends hours systematically testing variations of a hyperparameter that doesn't impact performance. 

By searching randomly, you explore a much wider variety of the *important* hyperparameters in a fraction of the time.

### Implementation

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

# 1. Define distributions instead of strict lists
param_dist = {
    'n_estimators': randint(50, 500),      # Pick a random int between 50-500
    'max_depth': [None, 10, 20, 30, 50],
    'min_samples_split': randint(2, 20)    # Pick a random int between 2-20
}

# 2. Instantiate Randomized Search
# n_iter=20 means "Only try 20 random combinations"
random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(), 
    param_distributions=param_dist, 
    n_iter=20, 
    cv=5, 
    random_state=42 # Set seed for reproducibility
)

# 3. Fit to data
random_search.fit(X_train, y_train)

print("Best params:", random_search.best_params_)
```

### The Tuning Strategy
A common strategy is a two-step approach:
1. Run a wide **Randomized Search** to quickly find the general neighborhood of good hyperparameters.
2. Build a narrow **Grid Search** around those specific values to pinpoint the absolute optimal configuration.""",

    ("Ensemble Methods", "Random Forests"): """## Bagging (Bootstrap Aggregating)

*Note: This is a deeper dive into the mechanics of Random Forests.*

Ensemble methods combine multiple "weak learners" (usually Decision Trees) to create one "strong learner". There are two main types of Ensembles: **Bagging** and **Boosting**. Random Forest is the most famous Bagging algorithm.

### The Mechanics of Bagging

"Bagging" stands for **B**ootstrap **Agg**regat**ing**.

1. **Bootstrap (The Data Split)**: 
   If you have a dataset of 1,000 rows, a Random Forest creates 100 new datasets, each containing 1,000 rows. How? By picking rows from the original data *randomly, with replacement*. 
   This means in Dataset 1, Row 42 might appear 3 times, and Row 17 might not appear at all (an Out-Of-Bag sample). This ensures every tree trains on a slightly different perspective of the data.

2. **Feature Subsetting (The Split)**:
   When a standard Decision Tree decides how to split data (e.g., separating ages < 30), it looks at *all* columns and picks the best one. 
   A Random Forest tree is restricted. At every node, it is only allowed to look at a random subset of columns (usually the square root of the total columns). This prevents one dominant feature (e.g., "Credit Score") from being the first split in every single tree, ensuring the trees are *decorrelated*.

3. **Aggregating (The Vote)**:
   All 100 trees make an independent prediction. The forest outputs the majority vote.

### Bias vs. Variance

In Machine Learning, **Variance** means the model is too sensitive to the training data (Overfitting). Single Decision Trees have massive variance.
The mathematical beauty of Bagging is that averaging the predictions of hundreds of decorrelated, high-variance trees results in a model with drastically lower variance, without sacrificing accuracy.

Random Forests are the ultimate "plug-and-play" algorithm. They require almost no tuning to get a highly competitive baseline model.""",

    ("Ensemble Methods", "Gradient Boosting"): """## Boosting: Learning from Mistakes

While Random Forests (Bagging) build hundreds of independent trees in parallel and average their votes, **Boosting** is a sequential process. It builds trees one at a time, where each new tree tries to fix the mistakes of the previous trees.

Gradient Boosting (implemented in libraries like **XGBoost**, **LightGBM**, and **CatBoost**) is widely considered the most powerful algorithm for tabular (spreadsheet) data, consistently winning Kaggle data science competitions.

### The Boosting Workflow

1. **Tree 1 (The Baseline)**: A very shallow, weak decision tree makes predictions on the dataset. It gets some right, and some wrong.
2. **Calculate Residuals (The Errors)**: The algorithm looks at the predictions and calculates the *errors* (e.g., The house was actually 300k, Tree 1 predicted 250k. Error = +50k).
3. **Tree 2 (The Fixer)**: The second tree is trained NOT to predict the house price, but to predict the *error* (the 50k). 
4. **Combine**: The final prediction is `Tree 1 + Tree 2`.
5. **Repeat**: Tree 3 is built to predict the remaining errors of Tree 1+2. This repeats for hundreds of trees.

By continuously focusing on the hardest data points (the ones the previous trees got wrong), the model slowly converges on an incredibly accurate final prediction.

### The Learning Rate

Boosting introduces a critical hyperparameter: the **Learning Rate**. 

If Tree 2 predicts an error of +50k, we don't just add 50k to the final prediction. We multiply it by a small learning rate (e.g., 0.1), adding only +5k. 
Why? If the trees make huge corrections, the model will rapidly overfit the training data. By forcing the trees to take tiny, slow steps (low learning rate), the model generalizes much better to unseen data.

*Trade-off*: A low learning rate requires building a higher number of trees, which increases training time.

### XGBoost vs Random Forest

- **Performance**: Properly tuned XGBoost will almost always beat a Random Forest in accuracy.
- **Tuning**: Random Forests work great out-of-the-box. Gradient Boosting models are highly sensitive to hyperparameters (Learning Rate, Max Depth) and require careful tuning.
- **Overfitting**: Random Forests almost never overfit, even with 10,000 trees. Gradient Boosting *will* overfit if you build too many trees, requiring techniques like "Early Stopping".""",

    ("Principal Component Analysis (PCA)", "Dimensionality Reduction"): """## The Curse of Dimensionality

In Machine Learning, a "Dimension" is simply a column (a feature) in your dataset. 

You might think "More data is always better," but algorithmically, adding too many columns leads to the **Curse of Dimensionality**:
1. The mathematical space becomes infinitely vast, and data points become isolated.
2. Models overfit easily (too many variables, not enough rows to find true patterns).
3. Computation time skyrockets.

**Dimensionality Reduction** is the process of compressing hundreds of columns into a smaller set of columns without losing the core information.

### Principal Component Analysis (PCA)

PCA is the most famous dimensionality reduction algorithm. It is an **Unsupervised Learning** technique.

Imagine a dataset of homes with columns: `[Square_Footage, Number_of_Rooms, Number_of_Bathrooms, Lot_Size]`.
These four columns are highly correlated. They all basically measure the same underlying concept: "Size of the Property."

PCA uses Linear Algebra to combine these correlated columns into a single, brand new column (called a **Principal Component**).

- **Principal Component 1 (PC1)**: A mathematical combination of the original columns that captures the *maximum possible variance* (information) in the dataset.
- **Principal Component 2 (PC2)**: Captures the remaining variance, and is mathematically *orthogonal* (uncorrelated) to PC1.

### Use Cases for PCA

1. **Data Compression**: Reduce a 1,000-column image dataset down to 50 Principal Components, retaining 95% of the information while speeding up neural network training by 10x.
2. **Visualization**: Humans can only see in 2D or 3D. If your dataset has 20 columns, you can't plot it. You can run PCA to compress the 20 columns into 2 Principal Components (X and Y), allowing you to plot the entire dataset on a 2D scatterplot to look for clusters!
3. **Noise Reduction**: The later Principal Components usually contain random noise; dropping them acts as a filter.

*Note: The drawback of PCA is loss of interpretability. PC1 is a mathematical formula of inputs, so you can no longer say "Age is the most important factor," because "Age" is now blended into PC1.*""",

    ("Principal Component Analysis (PCA)", "Explained Variance"): """## How Many Components to Keep?

When you run PCA on a dataset with 50 columns, it generates 50 Principal Components. The entire goal of PCA is to drop the useless components. But how do you know how many to keep?

### The Explained Variance Ratio

Every Principal Component captures a certain percentage of the total information (variance) in the original dataset. PC1 always captures the most. PC2 captures the second most, and so on.

Scikit-Learn provides the `explained_variance_ratio_` attribute, which tells you exactly how much information each component holds.

```python
from sklearn.decomposition import PCA

# Run PCA keeping all components
pca = PCA()
pca.fit(X_scaled) # ALWAYS scale data before PCA!

# Look at the variance ratio
print(pca.explained_variance_ratio_)
# Output: [0.60, 0.25, 0.10, 0.04, 0.01]
```

In this example:
- PC1 holds 60% of the information.
- PC2 holds 25%.
- Together, the first two components hold **85%** of the original information.

### The Cumulative Variance Plot

Data Scientists plot the cumulative sum of the variance ratio to visualize the trade-off between dimensionality and information loss.

If you plot it, you will see a curve that starts steep and flattens out (an "elbow"). 

**The Rule of Thumb**: You usually select the number of components required to retain **90% to 95%** of the variance. 

In Scikit-Learn, you don't even have to guess the number. You can instantiate PCA by passing a float between 0 and 1:
```python
# Tell PCA: "Give me the minimum number of components needed to keep 95% of the variance"
pca = PCA(n_components=0.95)
X_compressed = pca.fit_transform(X_scaled)

print(f"Reduced from 50 columns to {pca.n_components_} columns.")
```""",

    ("Unsupervised Learning", "K-Means Clustering"): """## Finding Hidden Groups

In Supervised Learning, you have labels (e.g., "Spam" or "Not Spam"). In **Unsupervised Learning**, you just have raw data, and you ask the algorithm to find hidden structures or patterns on its own.

The most common unsupervised task is **Clustering**: grouping similar data points together. 
- *Business Use Case*: Customer Segmentation. Given 100,000 customers' purchase histories, group them into distinct buyer profiles for targeted marketing.

### How K-Means Works

K-Means is the most famous clustering algorithm. 
**"K"** represents the number of clusters you want the algorithm to find (you must specify this number upfront).

The algorithm runs iteratively:
1. **Initialization**: Randomly drop `K` points (called Centroids) into the data space.
2. **Assignment**: For every data point in the dataset, calculate the distance to all Centroids. Assign the point to the cluster of the closest Centroid.
3. **Update**: Calculate the mean (average) position of all points in a cluster, and move the Centroid to that new center.
4. **Repeat**: Repeat steps 2 and 3 until the Centroids stop moving.

```python
from sklearn.cluster import KMeans

# Ask for 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit the model and get the cluster assignments (0, 1, or 2)
# Notice there is no 'y' passed to fit()! Unsupervised!
df['Cluster'] = kmeans.fit_predict(X_scaled) 
```

### The Elbow Method (Choosing K)

The hardest part of K-Means is knowing what `K` should be. If you pick K=2, it finds 2 groups. If you pick K=10, it finds 10 groups. Which is structurally true?

We use the **Elbow Method**:
1. Run K-Means for K=1, then 2, then 3... up to 10.
2. For each run, record the **Inertia** (the sum of squared distances from data points to their centroids).
3. Plot the Inertia on a line chart.
4. The inertia drops rapidly at first, then flattens out. The "elbow" (the point of inflection) represents the optimal number of clusters, where adding more clusters no longer significantly improves the grouping.""",

    ("Unsupervised Learning", "DBSCAN"): """## Density-Based Clustering

While K-Means is fast and popular, it has two major flaws:
1. You have to guess `K` (the number of clusters) beforehand.
2. It assumes clusters are perfectly spherical. If your data forms complex shapes (like a crescent moon or rings), K-Means will fail spectacularly, cutting the shapes in half.

**DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) solves both of these problems.

### How DBSCAN Works

Instead of placing centroids, DBSCAN looks for continuous areas of high density. It requires two hyperparameters:
- `eps` (Epsilon): The radius of a neighborhood. How close do points need to be to be considered "together"?
- `min_samples`: The minimum number of points required inside an `eps` radius to form a dense "Core".

**The Algorithm:**
1. Pick a random point. Check if there are at least `min_samples` within its `eps` radius.
2. If yes, it forms a cluster. It then checks the neighbors of those neighbors, expanding the cluster like a spilled puddle of water until the density drops off.
3. If a point has no neighbors within its radius, it is flagged as an **Anomaly/Outlier** (labeled as `-1`).

### Why DBSCAN is Powerful

1. **No K needed**: It figures out how many clusters exist organically based on the density.
2. **Arbitrary Shapes**: Because it flows through dense regions, it can identify clusters of any shape (snakes, rings, etc.).
3. **Outlier Detection**: Unlike K-Means (which forces every single point into a cluster, even extreme outliers), DBSCAN actively identifies and isolates noise. It is widely used in fraud detection and anomaly detection pipelines.

```python
from sklearn.cluster import DBSCAN

# eps=0.5 (distance), min_samples=5 (points to form a core)
dbscan = DBSCAN(eps=0.5, min_samples=5)

# Array of cluster labels. Points labeled -1 are outliers!
labels = dbscan.fit_predict(X_scaled) 
```
*Note: Because DBSCAN relies heavily on distance, scaling your data (using StandardScaler) is absolutely mandatory before running the algorithm.*""",

    ("Numpy Basics", "The NDArray"): """## The Engine of Data Science

Python lists are highly flexible, but they are incredibly slow for mathematical operations because they are arrays of pointers to scattered objects in memory.

**NumPy** (Numerical Python) is the foundational library for all scientific computing in Python. Pandas, Scikit-Learn, and TensorFlow are all built directly on top of NumPy. 

The core of NumPy is the **NDArray** (N-Dimensional Array).

### Why NDArrays are Fast

1. **Homogeneous Data**: Unlike Python lists, an NDArray requires all elements to be the exact same data type (usually `float64` or `int32`). This allows NumPy to allocate a single, contiguous block of memory.
2. **C-Level Execution**: NumPy's core math routines are written in highly optimized C code, bypassing Python's slow interpreter loop.

### Creating Arrays

```python
import numpy as np

# Create a 1D array from a list
arr_1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array (Matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Built-in generators (highly useful for dummy data)
zeros = np.zeros((3, 3))    # 3x3 matrix of 0s
ones = np.ones((2, 4))      # 2x4 matrix of 1s
sequence = np.arange(0, 10) # Array from 0 to 9
```

### Shape and Dimensions

Understanding the shape of your arrays is critical, especially when moving into Deep Learning where you must matrix-multiply arrays of specific sizes.

```python
print(arr_2d.shape) # Output: (2, 3) -> 2 rows, 3 columns
print(arr_2d.ndim)  # Output: 2 -> Number of dimensions
print(arr_2d.dtype) # Output: int64 -> Data type of elements
```
Reshaping arrays (e.g., turning a 1D array of 9 elements into a 3x3 2D matrix) is done constantly using `arr.reshape(3, 3)`.""",

    ("Numpy Basics", "Vectorized Operations"): """## Banning the 'For' Loop

The golden rule of numerical computing in Python is: **Never use a `for` loop if you can avoid it.**

If you have two lists of 1 million numbers and want to add them together, a Python `for` loop will iterate 1 million times, interpreting the types and calculating the sum one by one. It takes seconds.

NumPy uses **Vectorization**. Because the data types are strictly defined in contiguous memory, NumPy hands the entire block of data down to a C function (or directly to specialized CPU SIMD instructions) which performs the math in parallel. It takes milliseconds.

### Element-wise Math

If you perform standard math operations on a NumPy array, the operation is automatically broadcast to every element in the array simultaneously.

```python
import numpy as np

arr = np.array([1, 2, 3, 4])

# Multiply every element by 10 instantly
print(arr * 10) 
# Output: [10, 20, 30, 40]

arr2 = np.array([10, 10, 10, 10])

# Add two arrays element-by-element instantly
print(arr + arr2)
# Output: [11, 12, 13, 14]
```

### Broadcasting

What happens if you try to add a 1D array to a 2D array? In strict linear algebra, this is an error. In NumPy, the smaller array is "Broadcast" (stretched) across the larger array to make their shapes compatible.

```python
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]]) # Shape (2, 3)
                   
vector = np.array([10, 20, 30]) # Shape (3,)

# The vector is broadcast to every row of the matrix
print(matrix + vector)
# Output:
# [[11 22 33]
#  [14 25 36]]
```

### Boolean Indexing

Just like Pandas (which inherited this behavior from NumPy), you can filter arrays without loops using boolean conditions.

```python
arr = np.array([15, 25, 35, 45, 55])

# Creates a boolean mask: [False, False, True, True, True]
mask = arr > 30

# Pass the mask back into the brackets to extract the values
filtered = arr[mask] # [35, 45, 55]

# Or in one line:
filtered = arr[arr > 30]
```""",

    ("Handling Imbalanced Data", "Class Weights"): """## The Imbalanced Dataset Trap

In classification problems, your dataset is rarely split perfectly 50/50. 
Imagine building a model to detect a rare disease. 99% of patients are healthy (Class 0), and 1% have the disease (Class 1).

If you train a standard Machine Learning model on this dataset, it will realize a very simple mathematical truth: *"If I just blindly predict 'Healthy' for every single person, I will achieve 99% accuracy!"*

The model achieves high accuracy, but it is completely useless because it failed to identify a single sick patient. This is the danger of imbalanced data.

### Solution 1: Class Weights

Most algorithms in Scikit-Learn (Logistic Regression, Random Forests, SVMs) treat every row equally during training. Making a mistake on a Class 0 row is penalized exactly the same as making a mistake on a Class 1 row.

You can fix this by explicitly telling the algorithm that the minority class is more important using the `class_weight` hyperparameter.

```python
from sklearn.ensemble import RandomForestClassifier

# class_weight="balanced" tells the algorithm to automatically 
# adjust weights inversely proportional to class frequencies.
# If Class 1 is 1% of the data, mistakes on Class 1 will be penalized 
# 99 times heavier than mistakes on Class 0!

model = RandomForestClassifier(class_weight="balanced")
model.fit(X_train, y_train)
```

By imposing heavy financial "fines" on the model for missing the rare class, you force the algorithm to pay attention to it, rather than taking the easy path of predicting the majority class.

### When to use Class Weights

Class weights are the preferred first step for handling imbalance because:
1. They require no manipulation of the underlying data.
2. They are computationally free (no extra processing time).
3. They preserve the true statistical distribution of your dataset.

If class weights fail to improve the model's ability to detect the minority class, Data Scientists turn to resampling techniques.""",

    ("Handling Imbalanced Data", "SMOTE Oversampling"): """## Generating Synthetic Data

If `class_weight="balanced"` doesn't work, the next strategy for imbalanced data is **Resampling**—physically altering the training dataset to artificially create a 50/50 balance.

- **Undersampling**: Throwing away rows from the majority class until it equals the minority class. (Dangerous, you lose valuable data).
- **Oversampling**: Duplicating rows from the minority class until it equals the majority. (Dangerous, leads to massive overfitting as the model just memorizes the duplicates).

### The Solution: SMOTE

**Synthetic Minority Over-sampling Technique (SMOTE)** is a brilliant algorithm that creates a balanced dataset *without* exact duplication.

Instead of copying existing minority rows, SMOTE uses a K-Nearest Neighbors approach to generate **brand new, synthetic data points** that are statistically similar to the minority class.

**How it works:**
1. Pick a point from the minority class (e.g., a Sick patient).
2. Find its nearest minority neighbor.
3. Draw a line between them in the mathematical space.
4. Pick a random spot along that line and create a fake, synthetic patient.

### Implementation with `imbalanced-learn`

SMOTE is not in Scikit-Learn; it is found in the highly popular `imblearn` library.

```python
from imblearn.over_sampling import SMOTE

# Instantiate SMOTE
smote = SMOTE(random_state=42)

# Generate synthetic data to balance the classes
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Train your model on the new, artificially balanced dataset!
model.fit(X_train_resampled, y_train_resampled)
```

### The Golden Rule of Resampling

**NEVER APPLY SMOTE TO YOUR TEST SET OR BEFORE CROSS-VALIDATION!**

If you run SMOTE on your entire dataset before splitting, synthetic data will leak into your Test Set. Your model will be evaluated on fake, synthetic data, resulting in highly inflated, completely invalid performance metrics.

You must `train_test_split` first, and apply SMOTE **only** to `X_train` and `y_train`. The Test Set must remain the untouched, imbalanced, harsh reality of the real world.""",

    ("Model Evaluation Metrics", "Precision and Recall"): """## Beyond Accuracy

As we saw with imbalanced data (the 99% healthy / 1% sick scenario), **Accuracy** is a terrible metric. If you want to know how well your model actually performed on the minority class, you must look at the **Confusion Matrix**, which breaks predictions into four categories:
- **True Positives (TP)**: Predicted Sick, actually Sick. (Good!)
- **True Negatives (TN)**: Predicted Healthy, actually Healthy. (Good!)
- **False Positives (FP)**: Predicted Sick, actually Healthy. (Type I Error)
- **False Negatives (FN)**: Predicted Healthy, actually Sick. (Type II Error - Fatal!)

From this matrix, we derive two critical metrics: Precision and Recall.

### Precision: Quality of Positive Predictions

*Formula: TP / (TP + FP)*

"Out of all the people the model *claimed* were sick, how many were *actually* sick?"

High Precision means the model is very cautious. It doesn't cry wolf. If it says you are sick, you are definitely sick.
- **Optimize for Precision when False Positives are expensive.** 
- *Example*: Spam filters. If you predict a real email is spam (False Positive), the user misses a critical work email. Precision is paramount.

### Recall (Sensitivity): Finding All Positives

*Formula: TP / (TP + FN)*

"Out of all the people who were *actually* sick, how many did the model manage to *find*?"

High Recall means the model casts a wide net. It catches almost all the sick people, even if it accidentally flags a few healthy people along the way.
- **Optimize for Recall when False Negatives are expensive.**
- *Example*: Cancer screening. If you predict a sick patient is healthy (False Negative), they die. It is much better to over-predict sickness and do a biopsy (False Positive) than miss the cancer entirely. Recall is paramount.

### The F1 Score

Precision and Recall are a trade-off. If you increase one, the other usually drops. If you want a balanced metric that considers both (punishing extreme disparities), you use the **F1 Score**, which is the harmonic mean of Precision and Recall.

```python
from sklearn.metrics import classification_report

# Prints Precision, Recall, and F1 for EVERY class
print(classification_report(y_test, predictions))
```""",

    ("Model Evaluation Metrics", "ROC and AUC"): """## Evaluating Probability Thresholds

When a binary classification model (like Logistic Regression) predicts if a transaction is Fraud (1) or Not Fraud (0), it doesn't just output a 1 or a 0. Under the hood, it outputs a **Probability** (e.g., 0.85 chance of Fraud).

By default, Scikit-Learn uses a **Threshold of 0.5**.
- If probability >= 0.5 -> Predict 1
- If probability < 0.5 -> Predict 0

But 0.5 is arbitrary! If Fraud is extremely costly, you might want to lower the threshold to 0.2, catching more fraud (higher Recall) at the expense of investigating more innocent transactions (lower Precision).

How do you know which threshold is best? You use an ROC Curve.

### The ROC Curve (Receiver Operating Characteristic)

An ROC curve is a line chart that visualizes the model's performance across **every possible threshold** (from 0.0 to 1.0).

- **Y-Axis**: True Positive Rate (Recall). We want this to be high (1.0).
- **X-Axis**: False Positive Rate. We want this to be low (0.0).

The curve starts at (0,0) and ends at (1,1). A perfect model shoots straight up the Y-axis to the top left corner (100% recall, 0% false positives). A terrible model (random guessing) follows the diagonal line across the middle.

### AUC (Area Under the Curve)

While the ROC curve is visual, data scientists need a single number to compare models. We calculate the total area underneath the ROC curve, resulting in the **AUC Score**.

- **AUC = 1.0**: Perfect model. It perfectly separates the two classes.
- **AUC = 0.8 - 0.9**: Excellent model.
- **AUC = 0.5**: Completely worthless model (no better than flipping a coin).

```python
from sklearn.metrics import roc_auc_score

# You must pass PROBABILITIES, not hard 0/1 predictions!
y_probs = model.predict_proba(X_test)[:, 1] # Get probabilities for Class 1

auc = roc_auc_score(y_test, y_probs)
print(f"Model AUC: {auc}")
```

AUC is the most popular metric for evaluating classification models on imbalanced data because it summarizes performance across all possible decision thresholds, proving the model is genuinely separating the classes rather than just taking advantage of the imbalance.""",

    ("Deep Learning for Tabular Data", "Entity Embeddings"): """## Neural Networks vs. Spreadsheets

Traditionally, Deep Learning (Neural Networks) dominates unstructured data: Images (CNNs), Text (Transformers), and Audio. 
However, for structured tabular data (SQL tables, spreadsheets), tree-based algorithms like **XGBoost** and **Random Forests** usually outperform Neural Networks.

There is one major exception where Deep Learning excels in tabular data: **High-Cardinality Categorical Variables**.

### The High-Cardinality Problem

Imagine a dataset of retail sales. You have a `Store_ID` column with 5,000 unique stores, and a `Zip_Code` column with 20,000 unique values.

If you try to One-Hot Encode these columns for XGBoost, you will create 25,000 new binary columns. Your dataset will become incredibly sparse (mostly zeros), memory usage will explode, and tree-based models will struggle to find splits.

### The Solution: Entity Embeddings

Instead of creating 20,000 binary columns, a Neural Network can learn an **Embedding** for each Zip Code.

An embedding is a dense vector of floating-point numbers (e.g., an array of 5 numbers). During the training of the neural network, the model learns to assign mathematically similar vectors to Zip Codes that have similar purchasing behaviors.

- Zip Code A (Rich suburb): `[0.8, -0.2, 0.9, 0.1, 0.5]`
- Zip Code B (Similar rich suburb): `[0.7, -0.1, 0.8, 0.2, 0.4]`
- Zip Code C (College town): `[-0.9, 0.8, -0.5, 0.9, -0.8]`

The network compressed 20,000 categories into 5 continuous dimensions!

### Architecture

In PyTorch or TensorFlow, you construct the network by splitting the inputs:
1. Continuous variables (Age, Price) go straight into a standard Dense layer.
2. Categorical variables (Zip Code) are passed through an `Embedding` layer.
3. The outputs of the Embeddings are concatenated with the continuous variables and passed through deep Dense layers to make the final prediction.

*Bonus*: Once trained, you can extract these learned embeddings and feed them into an XGBoost model, getting the best of both worlds!""",

    ("Deep Learning for Tabular Data", "Autoencoders for Anomaly Detection"): """## Unsupervised Deep Learning

Detecting anomalies (credit card fraud, manufacturing defects, server intrusions) is incredibly difficult because anomalies are rare, and their patterns constantly change. Supervised classification struggles because you don't have enough examples of the "Fraud" class to train on.

**Autoencoders** provide a brilliant Unsupervised Deep Learning solution to anomaly detection.

### The Architecture of an Autoencoder

An Autoencoder is a neural network designed to reconstruct its own input. 
`Input (X) -> Neural Network -> Output (X_hat)`

It consists of two parts:
1. **The Encoder**: Compresses the input data (e.g., 50 features) into a tiny bottleneck layer (e.g., 5 neurons). This is called the "Latent Space".
2. **The Decoder**: Takes the 5 neurons and tries to decompress them back into the original 50 features.

Because the data is forced through a bottleneck, the network cannot just copy/paste the data. It is forced to learn the fundamental, underlying patterns of the dataset to successfully reconstruct it.

### Using Autoencoders for Anomalies

The trick to anomaly detection is how you train it: **You only train the Autoencoder on normal, healthy data.**

1. Train the model on thousands of normal credit card transactions. The model becomes an expert at reconstructing normal behavior.
2. In production, a transaction occurs. You pass it through the Autoencoder and compare the Input to the Output.
3. Calculate the **Reconstruction Error** (Mean Squared Error between Input and Output).

**The Logic:**
- If the transaction is normal, the model recognizes the pattern and reconstructs it perfectly. Reconstruction Error is **Low**.
- If a fraudster steals the card and buys 50 TVs in Russia, this data looks entirely different. The network has never seen this pattern, so it fails completely at reconstructing it. The Reconstruction Error is **Massive**.

By setting a threshold on the Reconstruction Error, you have built an incredibly robust anomaly detector without ever needing a dataset of labeled fraud!""",

    ("Recommendation Systems", "Collaborative Filtering"): """## The "People Like You" Algorithm

Recommendation engines drive the modern internet (Netflix, Amazon, TikTok). The most famous algorithm behind them is **Collaborative Filtering**.

Collaborative Filtering doesn't know anything about the actual items. It doesn't know that "The Matrix" is a Sci-Fi movie. It purely relies on the historical interactions (ratings, clicks, purchases) of the "crowd".

**The Core Assumption:** If User A and User B agreed on 10 movies in the past, they will likely agree on the 11th movie.

### The User-Item Matrix

The foundation is a massive grid where rows are Users, columns are Items (Movies), and values are Ratings (1-5).
Because most users have only seen a tiny fraction of all movies, this matrix is incredibly sparse (99% empty).

|        | Matrix | Shrek | Titanic |
|--------|--------|-------|---------|
| Alice  | 5      | 4     | ?       |
| Bob    | 5      | 5     | 2       |
| Charlie| ?      | ?     | 5       |

### Matrix Factorization

To fill in the missing `?` ratings, we use algorithms like **Singular Value Decomposition (SVD)**.

Matrix Factorization mathematically decomposes the giant sparse matrix into two smaller, dense matrices:
1. **User Matrix**: Represents users mathematically based on hidden preferences (Latent Factors).
2. **Item Matrix**: Represents movies mathematically based on hidden traits.

If we multiply User Alice's vector by the *Titanic* movie vector, the math outputs a predicted rating (e.g., 1.5). Because it's low, Netflix will NOT recommend Titanic to Alice.

### The Cold Start Problem

The fatal flaw of Collaborative Filtering is the **Cold Start Problem**.
- **New User**: If a new user signs up, they have no history. The algorithm has no idea who they are similar to, so it cannot recommend anything.
- **New Item**: If a new movie is uploaded, nobody has watched it yet, so the algorithm will never recommend it to anyone.

To solve this, companies use hybrid systems, combining Collaborative Filtering with Content-Based Filtering.""",

    ("Recommendation Systems", "Content-Based Filtering"): """## Recommending by Attributes

To solve the Cold Start Problem inherent in Collaborative Filtering, systems utilize **Content-Based Filtering**. 

This algorithm doesn't care about what the "crowd" is doing. It focuses entirely on the metadata (the attributes) of the items and the specific user's history.

**The Core Assumption:** If you liked an item in the past, you will like similar items in the future.

### How it Works

1. **Item Profiles**: Every item in the database is tagged with detailed metadata. 
   - A movie is tagged with Director, Actors, Genre, Year, and keywords from the plot summary.
2. **User Profiles**: As a user interacts with items, the system builds a profile of their preferences. 
   - "Alice watches 80% Sci-Fi, 20% Action, and frequently watches Keanu Reeves movies."
3. **Distance Calculation**: The system compares the User Profile to all the Item Profiles using mathematical distance metrics (like **Cosine Similarity**).

If Alice logs in, the system finds movies with the highest Cosine Similarity to her profile (e.g., a new Sci-Fi movie starring Keanu Reeves) and recommends it, even if no other human on earth has watched it yet.

### Text Vectorization (TF-IDF)

How does a computer calculate the "similarity" between two plot summaries? It uses NLP.

A common technique is **TF-IDF** (Term Frequency-Inverse Document Frequency).
1. It counts how many times a word appears in a movie's plot (TF).
2. It penalizes words that appear in *every* movie plot (IDF, like "movie", "story").
3. It boosts words that are unique to that specific movie ("cyborg", "matrix").

Each movie plot is turned into a mathematical vector of TF-IDF scores. Calculating the Cosine Similarity between two movie vectors instantly tells you how similar their plots are.

### Pros and Cons

- **Pros**: Solves the Cold Start problem for new items. Can recommend niche items that the general crowd ignores.
- **Cons**: Suffer from the "Echo Chamber" effect (Overspecialization). If you watch one documentary about conspiracy theories, the system will only ever recommend conspiracy theories, never allowing you to discover new genres.""",

    ("Pandas Data Manipulation Masterclass", "loc vs iloc"): """## Precision Indexing

Pandas provides two powerful accessors to slice and extract data from a DataFrame: `.loc` and `.iloc`. Confusing them is a common source of bugs.

### `.iloc` (Integer Location)
`iloc` is strictly based on numerical position (0-indexed), exactly like standard Python lists. It doesn't care what the index is named.

```python
# Returns the 1st row (index 0)
df.iloc[0] 

# Returns a subset: Rows 0-4, Columns 0-2
df.iloc[0:5, 0:3] 
```
*Rule of thumb: Use `iloc` when you want "The first 10 rows" or "The last column".*

### `.loc` (Label Location)
`loc` is based on the actual *labels* of the index and the column names. 

```python
# Assuming the index is set to Employee Names
# Returns the row where the index label is "Alice"
df.loc["Alice"]

# Returns Alice's Salary specifically
df.loc["Alice", "Salary"]

# Returns rows for Alice through Charlie, and columns Age through Salary
df.loc["Alice":"Charlie", "Age":"Salary"] 
```
*Notice: Unlike `iloc` (where 0:5 excludes 5), slice ranges in `loc` are INCLUSIVE of both the start and end labels.*

### Boolean Masking with `.loc`
The true power of `.loc` is applying boolean filters and selecting specific columns simultaneously.

```python
# "Find rows where Age > 30, and only return their Name and Salary"
df.loc[df["Age"] > 30, ["Name", "Salary"]]
```
If you tried this without `.loc` (e.g., `df[df["Age"] > 30]["Name"]`), Pandas will throw a `SettingWithCopyWarning` if you attempt to modify the result. Always use `.loc` for filtering and assignment.""",

    ("Pandas Data Manipulation Masterclass", "GroupBy & Aggregations"): """## Advanced Split-Apply-Combine

The `.groupby()` method is the workhorse of Pandas data analysis, allowing you to aggregate metrics across categories (like SQL's `GROUP BY`).

### Basic Aggregation
```python
# Sum of Sales per Region
df.groupby("Region")["Sales"].sum()
```

### The `.agg()` Method
Usually, you need more than one statistic, or different statistics for different columns. The `.agg()` method accepts dictionaries to perform complex aggregations simultaneously.

```python
summary = df.groupby("Region").agg({
    "Sales": ["sum", "mean"],      # Total and average sales
    "Employees": "count",          # Number of employees
    "Customer_Rating": ["min", "max"] # Lowest and highest rating
})
```

### Resetting the Index
By default, the column you grouped by ("Region") becomes the Index of the new DataFrame. If you want it to remain a standard column (which is often necessary for plotting or exporting to CSV), use `.reset_index()`.

```python
summary = df.groupby("Region")["Sales"].sum().reset_index()
```

### Grouping by Multiple Columns
You can group by multiple hierarchies to create highly granular summaries.

```python
# Average sales per Department, broken down by Region
df.groupby(["Region", "Department"])["Sales"].mean()
```
This returns a Series with a **MultiIndex**. To flatten it back into a standard 2D table, append `.reset_index()`.

### Custom Aggregation Functions
You are not limited to built-in math. You can pass custom lambda functions to `.agg()`.
```python
# Calculate the Range (Max - Min) for Sales in each Region
df.groupby("Region")["Sales"].agg(lambda x: x.max() - x.min())
```""",

    ("Pandas Data Manipulation Masterclass", "Window Functions"): """## Rolling and Expanding Metrics

Window functions allow you to perform calculations across a sliding window of rows. This is absolutely critical for Time Series analysis, stock market data, and signal processing.

*Note: Your DataFrame should be sorted by time before using window functions!*

### The `.rolling()` Window

A rolling window slides down the dataset, keeping a fixed number of rows in its calculation. It is heavily used to smooth out volatile data (Moving Averages).

```python
# Calculate a 7-day moving average of Sales
# window=7 means it looks at the current row + 6 previous rows
df["7_Day_Avg"] = df["Sales"].rolling(window=7).mean()
```
The first 6 rows of `df["7_Day_Avg"]` will be `NaN` because there isn't enough historical data to calculate a full 7-day average.

### The `.expanding()` Window

An expanding window starts at the first row and grows with every step. The window size increases to encompass all historical data up to the current row.

```python
# Calculate the cumulative max (e.g., "All-time high score up to this date")
df["All_Time_High"] = df["Score"].expanding().max()

# Cumulative sum (Running total)
# Note: Pandas has a built-in shortcut for this: df["Sales"].cumsum()
df["Running_Total"] = df["Sales"].expanding().sum()
```

### The `.shift()` Method

`.shift()` moves data up or down, allowing you to calculate the difference between the current row and a previous row.

```python
# Shift the Sales column down by 1 row
df["Previous_Day_Sales"] = df["Sales"].shift(1)

# Calculate Day-over-Day growth percentage
df["Daily_Growth"] = (df["Sales"] - df["Previous_Day_Sales"]) / df["Previous_Day_Sales"]
```
`.shift(-1)` would look into the *future* (shifting data up), which is commonly used in Machine Learning to create the "Target" variable for tomorrow's prediction.""",

    ("Pandas Data Manipulation Masterclass", "Merging and Joining"): """## Combining Datasets

In the real world, data is relational. Customer details are in one table, and their purchase history is in another. Pandas provides robust tools to combine DataFrames, mirroring SQL joins.

### `.merge()` (The SQL Way)

`.merge()` connects DataFrames horizontally based on a common column (a Key). 

```python
# df_users has columns: ['User_ID', 'Name']
# df_orders has columns: ['Order_ID', 'User_ID', 'Amount']

# Merge on the shared 'User_ID' column
merged_df = pd.merge(df_users, df_orders, on="User_ID", how="inner")
```

**The `how` parameter dictates the Join Type:**
- `inner` (Default): Keeps only rows where the `User_ID` exists in BOTH tables.
- `left`: Keeps ALL users from `df_users`. If they have no orders, the `Amount` column will be `NaN`.
- `right`: Keeps ALL orders. If the user doesn't exist in the users table, `Name` is `NaN`.
- `outer`: Keeps everything from both tables, filling `NaN`s where data is missing.

If the columns have different names (e.g., `id` and `user_id`), use `left_on` and `right_on`:
```python
pd.merge(df_users, df_orders, left_on="id", right_on="user_id")
```

### `pd.concat()` (The Stacking Way)

`.concat()` is used to glue DataFrames together, usually vertically. This is common when you have identical schema data from different sources (e.g., January sales data and February sales data).

```python
jan_sales = pd.read_csv("jan.csv")
feb_sales = pd.read_csv("feb.csv")

# Stack them vertically (adds rows)
all_sales = pd.concat([jan_sales, feb_sales], axis=0)
```
If you set `axis=1`, `concat` glues them horizontally by matching their Indexes, not by a specific column key.

### `.join()` (The Index Way)
`.join()` is a convenience method for merging data based purely on their Indexes. It is basically `merge()` but strictly uses the index as the key.""",

    ("Pandas Data Manipulation Masterclass", "Pivot Tables"): """## Reshaping Data

A Pivot Table is a powerful data summarization tool (familiar to Excel users) that reorganizes raw data into a cross-tabulated grid. It transforms rows into columns, allowing you to see relationships across multiple dimensions.

### The `pivot_table()` Function

Imagine a dataset of sales: `['Date', 'Region', 'Product', 'Revenue']`. 
You want a grid where the Rows are Regions, the Columns are Products, and the values are the Total Revenue.

```python
import pandas as pd
import numpy as np

pivot = pd.pivot_table(
    df, 
    values='Revenue',      # The data to calculate
    index='Region',        # The Rows
    columns='Product',     # The Columns
    aggfunc=np.sum,        # The math function (default is mean)
    fill_value=0           # If a region sold 0 of a product, fill NaN with 0
)
```

### Adding Margins

You often want to see the grand totals for the rows and columns. Setting `margins=True` adds an "All" row and an "All" column.

```python
pivot = pd.pivot_table(
    df, 
    values='Revenue', 
    index='Region', 
    columns='Product', 
    aggfunc=np.sum, 
    margins=True
)
```

### `.melt()` (Un-Pivoting)

Sometimes you receive data that is already pivoted (wide format), but Machine Learning algorithms and Seaborn plotting libraries require "Tidy Data" (long format). 

`pd.melt()` does the reverse of a pivot table. It takes columns and smashes them down into rows.

```python
# Wide data: ['Country', 'Year_2020', 'Year_2021']
# We want: ['Country', 'Year', 'Value']

tidy_df = pd.melt(
    wide_df, 
    id_vars=['Country'],          # The column to keep as an identifier
    value_vars=['Year_2020', 'Year_2021'], # The columns to smash down
    var_name='Year',              # Name of the new category column
    value_name='Revenue'          # Name of the new value column
)
```
Mastering `pivot_table` and `melt` allows you to fluently reshape data for any analytical requirement.""",

    ("Pandas Data Manipulation Masterclass", "MultiIndex"): """## Hierarchical Indexing

A **MultiIndex** (or Hierarchical Index) allows you to have multiple levels of indexes on a single axis. This enables you to store high-dimensional data in a 2D DataFrame.

You will encounter a MultiIndex most often after executing a `groupby()` with multiple columns.

```python
# Grouping by two columns creates a MultiIndex Series
sales = df.groupby(['Region', 'Department'])['Revenue'].sum()

# The Index now has two levels:
# North   HR         500
#         Sales      1200
# South   HR         400
#         Sales      1500
```

### Selecting Data with a MultiIndex

Selecting data requires passing tuples to `.loc`.

```python
# Select all data for the North region (Level 0)
north_sales = sales.loc['North']

# Select specifically the HR department in the North region (Level 0, Level 1)
north_hr_sales = sales.loc[('North', 'HR')]
```

### The `.xs()` (Cross-Section) Method

What if you want to select the 'HR' department across *all* regions? Using `.loc` is tricky because 'Region' is the outer level. The `.xs()` method is designed specifically for this.

```python
# Get HR data, specifying that 'HR' is found in level 1 of the index
all_hr_sales = sales.xs('HR', level=1)
```

### Unstacking

A MultiIndex Series can be difficult to read. You can convert the inner level of the index into columns using `.unstack()`. This turns the long Series into a wide, 2D DataFrame (acting very much like a Pivot Table).

```python
wide_df = sales.unstack()
# Output:
#          HR    Sales
# North   500    1200
# South   400    1500

# To reverse this and smash the columns back into an index, use .stack()
long_series = wide_df.stack()
```
If MultiIndexes become too confusing, the universal escape hatch is `reset_index()`, which flattens all index levels into standard DataFrame columns.""",

    ("Pandas Data Manipulation Masterclass", "Vectorized String Methods"): """## Cleaning Text at Scale

Cleaning messy text data in base Python requires writing loops and applying Regex `re` functions to each string. This is incredibly slow for large datasets.

Pandas provides a suite of vectorized string methods via the `.str` accessor. These operations run highly optimized C code over the entire column simultaneously, handling `NaN` values gracefully without crashing.

### Formatting Text
```python
# Convert all emails to lowercase
df['Email'] = df['Email'].str.lower()

# Remove leading and trailing whitespace
df['Name'] = df['Name'].str.strip()

# Capitalize the first letter of each word
df['City'] = df['City'].str.title()
```

### Searching and Filtering
You can filter a DataFrame based on string contents without writing a loop.

```python
# Returns a boolean mask of rows where the Title contains "Engineer"
mask = df['Job_Title'].str.contains('Engineer', case=False)
engineers_df = df[mask]

# Check if a string starts with a specific prefix
is_gmail = df['Email'].str.startswith('@gmail.com')
```

### Splitting and Replacing
Parsing complex strings into separate columns is a daily task in data cleaning.

```python
# Replace specific characters
df['Phone'] = df['Phone'].str.replace('-', '')

# Split a "First Last" column into two columns
# expand=True forces the output into a new DataFrame instead of a list
name_split = df['Full_Name'].str.split(' ', expand=True)
df['First_Name'] = name_split[0]
df['Last_Name'] = name_split[1]
```

### Regex Integration
The `.str` accessor integrates seamlessly with Regular Expressions for complex extractions.

```python
# Extract exactly 5 digits (a US Zip Code) from a messy address string
df['Zip_Code'] = df['Address'].str.extract(r'(\\d{5})')
```
Mastering the `.str` accessor eliminates the need for `.apply()` in 90% of text processing tasks, drastically speeding up your ETL pipelines.""",

    ("Pandas Data Manipulation Masterclass", "Handling DateTimes"): """## Mastering Temporal Data

Dates and times are notoriously difficult to work with due to varying formats, timezones, and leap years. Pandas provides the `.dt` accessor to make manipulating time series data effortless.

### Conversion and Parsing
Before using `.dt`, you must convert strings to Pandas `datetime64` objects.

```python
# Auto-detects the format (fast, but can be inaccurate)
df['Date'] = pd.to_datetime(df['Date_String'])

# Strict formatting (Much faster and safer)
# %Y = 4-digit year, %m = 2-digit month, %d = 2-digit day
df['Date'] = pd.to_datetime(df['Date_String'], format='%Y-%m-%d')
```

### Extracting Features
Once converted, use `.dt` to extract numerical features for machine learning or grouping.

```python
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day_of_Week'] = df['Date'].dt.dayofweek # 0 = Monday, 6 = Sunday
df['Is_Leap_Year'] = df['Date'].dt.is_leap_year
```

### Time Deltas (Differences)
Subtracting two datetime columns results in a `timedelta64` object. You can use `.dt` to extract the difference in specific units.

```python
# Calculate duration
df['Delivery_Time'] = df['Delivered_At'] - df['Ordered_At']

# Extract the exact number of days as an integer
df['Delivery_Days'] = df['Delivery_Time'].dt.days
```

### Date Offsets
You can mathematically manipulate dates using `pd.DateOffset` or `pd.Timedelta`.

```python
# Add exactly 30 days to every date in the column
df['Expiration'] = df['Date'] + pd.Timedelta(days=30)

# Add exactly 1 month (handles varying month lengths automatically!)
df['Next_Billing'] = df['Date'] + pd.DateOffset(months=1)
```

### Floor and Ceil (Rounding Dates)
If you have extremely precise timestamps (down to the millisecond) but want to group by the Hour or Day, you can "round" the dates.

```python
# Round down to the nearest hour
df['Hour_Bucket'] = df['Timestamp'].dt.floor('H')

# Round up to the nearest day
df['Day_Bucket'] = df['Timestamp'].dt.ceil('D')
```""",

    ("A/B Testing & Causal Inference Masterclass", "Hypothesis Testing"): """## The Scientific Method for Business

In data science, we rarely have data for the entire population. We take a **Sample** (e.g., 10,000 users) and try to infer truths about the **Population** (all 5 million users). 

If a new website button increases conversions in our sample from 5% to 5.2%, how do we know if it's a real improvement, or just random noise in the sample? We use **Hypothesis Testing**.

### The Two Hypotheses

Every experiment starts by defining two opposing hypotheses:

1. **The Null Hypothesis ($H_0$)**: The baseline assumption. It states that there is **no effect**, no difference, or no relationship. 
   - *Example*: "The new red button has the exact same conversion rate as the old blue button."
   - *Goal*: We always assume $H_0$ is true until the data proves otherwise.

2. **The Alternative Hypothesis ($H_1$ or $H_A$)**: The claim you are trying to prove.
   - *Example*: "The new red button has a higher conversion rate than the old blue button."

### The Burden of Proof

In a criminal trial, the defendant is presumed innocent (Null Hypothesis) until proven guilty beyond a reasonable doubt (Alternative Hypothesis). 

In statistics, we assume the new feature did nothing ($H_0$). We collect data. If the data shows a massive improvement, we calculate the probability of seeing that improvement purely by random chance. 

If the probability of random chance is extremely low, we say we have enough evidence to **Reject the Null Hypothesis** and accept the Alternative Hypothesis. If the improvement is small, we **Fail to Reject the Null Hypothesis** (we don't prove the old button is better, we just lack evidence to prove the new one is).""",

    ("A/B Testing & Causal Inference Masterclass", "p-values and Alpha"): """## Quantifying Surprise

Once an experiment (A/B test) concludes, statistical software spits out a **p-value**. This is the single most misunderstood concept in data science.

### What is a p-value?

**The p-value is the probability of observing results as extreme as yours, ASSUMING the Null Hypothesis is completely true.**

*Scenario*: You flip a coin 10 times. It lands on Heads 10 times in a row. 
- Null Hypothesis: The coin is fair (50/50).
- If the coin is truly fair, the probability of getting 10 Heads in a row is $0.5^{10} = 0.00097$ (about 0.1%).
- Your **p-value is 0.001**. 

Because 0.1% is incredibly rare, you conclude: "Either a 1-in-a-1000 miracle just happened, or my Null Hypothesis is wrong and the coin is rigged." You reject the Null Hypothesis.

### Alpha ($\alpha$): The Significance Level

How low does the p-value need to be before we reject the Null Hypothesis? We define this threshold *before* the experiment starts. This threshold is called **Alpha ($\alpha$)**.

The industry standard is **$\alpha = 0.05$** (5%).

- If $p \leq 0.05$: The result is **Statistically Significant**. Reject the Null Hypothesis. We are confident the result is real.
- If $p > 0.05$: The result is **Not Statistically Significant**. Fail to reject the Null Hypothesis. The result could easily be random noise.

### Type I and Type II Errors

- **Type I Error (False Positive)**: The p-value was 0.04. We celebrated and launched the new feature. But it was just a fluke in the sample! The feature actually does nothing. The probability of making a Type I error is exactly your Alpha (5%).
- **Type II Error (False Negative)**: The p-value was 0.08. We threw away the new feature because it wasn't significant. But the feature actually *was* better, our sample was just unlucky and didn't show it clearly.

Data scientists must balance the risk of launching useless features (Type I) versus missing out on good features (Type II).""",

    ("A/B Testing & Causal Inference Masterclass", "Statistical Power"): """## Ensuring Your Test Can Actually Win

**Statistical Power** (or Sensitivity) is the probability that your A/B test will successfully detect a real difference, assuming a difference actually exists. 

If a new feature truly increases revenue by 2%, but your test has low Power, the test will likely output a non-significant p-value, causing you to commit a **Type II Error** (False Negative) and throw the feature away.

### The Four Pillars of Power

Statistical Power is influenced by four interconnected variables. If you change one, the others are affected.

1. **Sample Size ($n$)**: The amount of data you collect. Bigger samples = less random noise = Higher Power.
2. **Effect Size (Minimum Detectable Effect, MDE)**: How big of an impact the new feature has. Detecting a 50% increase is easy (High Power). Detecting a 0.5% increase is extremely difficult (Requires massive sample size).
3. **Alpha ($\alpha$)**: The significance threshold (usually 0.05). If you lower Alpha to 0.01 (being more strict against False Positives), your Power drops.
4. **Power ($1 - \beta$)**: The industry standard is **80% Power**. This means if the feature is genuinely better, you have an 80% chance of successfully proving it, and a 20% chance of missing it.

### Power Analysis (Calculating Sample Size)

Before launching an A/B test, data scientists perform a **Power Analysis** to determine exactly how long the test needs to run.

You must define:
1. Alpha (0.05)
2. Target Power (0.80)
3. Baseline Conversion Rate (e.g., currently 10%)
4. Minimum Detectable Effect (e.g., we only care if it jumps to 11%)

Plug these into a statistical calculator (like `statsmodels` in Python), and it will output the exact number of users required in each group (e.g., 14,000 users). 

If your website gets 1,000 users a day, the test MUST run for 28 days (14k for Group A + 14k for Group B). 

**Never peek at the p-value before the required sample size is reached!** "Peeking" completely invalidates the mathematics of the test and vastly increases your False Positive rate.""",

    ("A/B Testing & Causal Inference Masterclass", "T-Tests"): """## Comparing Two Means

When you run an A/B test where the metric is a continuous number (e.g., Average Order Value, Time Spent on Page, Revenue per User), you use a **T-Test** to determine if the difference between the two groups is statistically significant.

### The Student's t-test

The t-test compares the Means (averages) of two groups, taking into account the variance (spread) of the data and the sample size.

Even if Group B's average is $5 higher than Group A, if the data is wildly volatile (high variance) or the sample size is small, the t-test will output a high p-value, indicating the $5 difference is likely just noise.

**Types of T-Tests:**
1. **Independent Two-Sample T-Test**: Compares two completely separate groups (e.g., Group A saw the old checkout, Group B saw the new checkout). This is the standard A/B test.
2. **Paired T-Test**: Compares the exact same subjects at two different times (e.g., Blood pressure of 50 patients *before* taking a drug, and the *same* 50 patients *after*).

### Implementation in Python

We use the `scipy.stats` library to run the test.

```python
from scipy import stats

# Arrays containing the revenue generated by each user
group_a_revenue = [10.5, 12.1, 9.8, 15.0, 11.2, ...] 
group_b_revenue = [13.2, 14.5, 12.0, 16.1, 14.8, ...]

# Run an Independent T-Test
# Note: A/B testing usually assumes unequal variances (Welch's t-test), 
# so we set equal_var=False
t_statistic, p_value = stats.ttest_ind(group_a_revenue, group_b_revenue, equal_var=False)

print(f"P-Value: {p_value}")

if p_value < 0.05:
    print("Statistically Significant: The new checkout generates more revenue!")
else:
    print("Not Significant: Keep the old checkout.")
```

### Assumptions of the T-Test
The t-test relies on the assumption that the sample means are Normally Distributed (a bell curve). Thanks to the Central Limit Theorem, this is almost always true in tech companies because the sample sizes (thousands of users) are massive. For very small samples (N < 30), you must test for normality first.""",

    ("A/B Testing & Causal Inference Masterclass", "Chi-Square Tests"): """## Comparing Categorical Proportions

While a T-Test is used for continuous numbers (Revenue, Time), what if your metric is binary or categorical? 

Examples:
- Did they click the button? (Yes/No)
- Which subscription tier did they buy? (Basic/Pro/Enterprise)
- Did the email bounce? (Yes/No)

When comparing rates or proportions (like Conversion Rate or Click-Through Rate), you use a **Chi-Square Test of Independence** (pronounced "Kai-Square").

### How Chi-Square Works

The test compares the **Observed** frequencies in your data against the **Expected** frequencies if the Null Hypothesis (that Group A and Group B are exactly the same) were true.

If Group A and Group B are truly the same, their conversion rates should be roughly equal to the global average. The Chi-Square test calculates how far your actual data deviates from that expected average.

### Implementation in Python

First, you must format your data into a Contingency Table (a matrix of counts).

|         | Converted (Yes) | Did Not Convert (No) |
|---------|-----------------|----------------------|
| Group A | 300             | 9700                 |
| Group B | 380             | 9620                 |

Group A conversion: 3.0%
Group B conversion: 3.8%

```python
import numpy as np
from scipy.stats import chi2_contingency

# 1. Create the contingency table
# [[Group A Conversions, Group A Failures], 
#  [Group B Conversions, Group B Failures]]
data = np.array([[300, 9700], 
                 [380, 9620]])

# 2. Run the Chi-Square test
chi2_stat, p_value, dof, expected = chi2_contingency(data)

print(f"P-Value: {p_value}")

if p_value < 0.05:
    print("Significant! Group B's higher conversion rate is real.")
else:
    print("Not Significant. The 0.8% difference could be random noise.")
```

For large-scale A/B tests on conversion rates, the Chi-Square test (or a two-proportion Z-test, which yields identical results for 2x2 tables) is the industry standard.""",

    ("A/B Testing & Causal Inference Masterclass", "The Multiple Testing Problem"): """## The Danger of Digging for Gold

Imagine you run an A/B test. The Alpha (significance threshold) is set at 0.05. This means there is a **5% chance of a False Positive**—seeing a "significant" result when the feature actually does nothing.

You test a new landing page and the p-value is 0.12 (Not Significant). Disappointed, you decide to slice the data.
- "Did it work for mobile users?" (p=0.20)
- "Did it work for iOS users?" (p=0.15)
- "Did it work for Android users?" (p=0.40)
- "Did it work for users in Canada?" (p=0.03) -> *Significant!*

You declare victory: "The new landing page increases conversions for Canadian users!" 

This is a catastrophic statistical error known as **The Multiple Testing Problem** (or p-hacking).

### The Math Behind the Error

If you have a 5% chance of a False Positive, and you run 20 different tests (checking 20 different segments or metrics), the probability of getting *at least one* False Positive by pure random chance is:

$1 - (0.95)^{20} \approx 64\%$

By testing 20 different segments, it is more likely than not that you will find a "significant" result purely by accident. The more you test, the more you guarantee a False Positive.

### The Solutions

**1. Bonferroni Correction**
The simplest defense. Divide your Alpha by the number of tests you plan to run.
If you plan to test 5 different countries, your new Alpha is $0.05 / 5 = 0.01$. A result is now only significant if $p < 0.01$. This drastically reduces False Positives, but severely lowers Statistical Power.

**2. Pre-Registration**
Define exactly what metrics and segments you are going to look at *before* the experiment starts, and stick to it. If you stumble across an interesting effect in a random sub-segment during analysis, you cannot declare it a success. You must launch a brand new A/B test specifically targeting that segment to prove it.

Never torture the data until it confesses.""",

    ("A/B Testing & Causal Inference Masterclass", "Difference-in-Differences"): """## Quasi-Experiments: When A/B Testing is Impossible

A true A/B test requires **Randomized Control Trials (RCT)**. You must be able to randomly assign Alice to Group A and Bob to Group B. 

But what if a government passes a new tax law in California, and you want to know if it reduced unemployment? You can't randomly assign citizens to a "tax" group and a "no tax" group. You only have Observational Data.

To establish Cause and Effect (Causal Inference) without random assignment, economists and data scientists use techniques like **Difference-in-Differences (DiD)**.

### The Mechanics of DiD

Imagine a company launches a massive TV advertising campaign, but only in Chicago. They want to know if it increased sales. 

- **Naive Approach 1**: Compare Chicago sales *After* vs *Before*. (Flaw: What if it's December and sales just naturally go up everywhere due to Christmas?)
- **Naive Approach 2**: Compare Chicago sales *After* vs New York sales *After*. (Flaw: Chicago and NY have fundamentally different economies and baselines).

**Difference-in-Differences** solves this by using a Control Group (New York) to isolate the treatment effect.

1. Find a Control Group (NY) that follows the exact same historical trend as the Treatment Group (Chicago). This is the "Parallel Trends Assumption".
2. Calculate the difference in NY *Before* vs *After*. (e.g., NY grew by $10k). This is the natural growth caused by time/seasonality.
3. Calculate the difference in Chicago *Before* vs *After*. (e.g., Chicago grew by $25k).
4. **The Difference-in-Differences**: Subtract the Control's growth from the Treatment's growth. 
   - `$25k (Chicago Growth) - $10k (NY Natural Growth) = $15k.`

We can causally infer that the TV ad generated exactly $15,000 in incremental revenue, completely controlling for natural baseline differences and seasonal effects!

### Implementation via Regression

In Python, DiD is executed using an Ordinary Least Squares (OLS) regression with an interaction term.

`Sales = B0 + B1*(Is_Chicago) + B2*(Is_After_Ad) + B3*(Is_Chicago * Is_After_Ad)`

The coefficient `B3` (the interaction between being in the treatment group AND being in the post-treatment time period) is the causal effect of the TV ad.""",

    ("A/B Testing & Causal Inference Masterclass", "Propensity Score Matching"): """## Creating "Artificial" A/B Tests

Another method for causal inference in observational data is **Propensity Score Matching (PSM)**.

Imagine you want to prove that users who sign up for your "Premium Newsletter" have a higher Customer Lifetime Value (LTV). 

You query the database:
- Newsletter Subscribers: Average LTV $500
- Non-Subscribers: Average LTV $100

*Can you claim the newsletter causes a $400 increase in LTV?*
**Absolutely not.** This is **Selection Bias**. The users who opt into a premium newsletter are likely already your most engaged, wealthy, and loyal customers. They would have spent $500 even without the newsletter. The newsletter is just correlated with loyalty, it doesn't cause it.

### The PSM Solution

To find the true causal effect, we need to create an artificial A/B test by finding "twins". For every Newsletter Subscriber, we want to find a Non-Subscriber who is identical in every way (Age, Income, Past Purchases), except they didn't sign up for the newsletter.

Finding identical twins across 20 variables is impossible. PSM solves this by crushing those 20 variables into a single score: the **Propensity Score**.

### The Workflow

1. **Calculate Propensity**: Train a Logistic Regression model to predict *the probability that a user signs up for the newsletter* based on their covariates (Age, Income, Past Purchases). 
   - This output probability (0.0 to 1.0) is the Propensity Score.
2. **Matching**: For every user who actually subscribed, look at their Propensity Score (e.g., 0.85). Find a user in the Non-Subscriber pool who has an almost identical score (e.g., 0.84). 
3. **Discard**: Throw away all the unmatched users. You now have two perfectly balanced groups: a Treatment group and a Control group that had the exact same statistical likelihood of subscribing, but one did and one didn't.
4. **Evaluate**: Now, compare the Average LTV of the matched Treatment group vs the matched Control group. 

If the matched subscribers spend $200, and the matched non-subscribers spend $180, the true causal effect of the newsletter is only $20, not $400! 

PSM is a powerful tool to eliminate selection bias (Confounding Variables) when ethical or logistical constraints prevent a true randomized A/B test."""
}

patched = 0
for category_name, category_data in data.items():
    for lesson in category_data.get("lessons", []):
        title = lesson["title"]
        key = (category_name, title)
        if key in theories and theories[key] is not None:
            old_len = len(lesson.get("theory", ""))
            lesson["theory"] = theories[key]
            new_len = len(lesson["theory"])
            print(f"  OK [{category_name}] {title}: {old_len} -> {new_len} chars")
            patched += 1

with open("curriculum/tracks/data_science.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nPatched {patched} lessons in data_science.json")
