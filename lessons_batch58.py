"""
Batch 58: Deep Dive into Data Science (Pandas Data Manipulation Masterclass)
"""
import json, os

NEW_COURSES_BATCH58 = {
    "Pandas Data Manipulation Masterclass": {
        "tier": "Intermediate",
        "aiRubric": "Assess deep understanding of Pandas operations",
        "lessons": [
            {"title": "loc vs iloc", "theory": "## Selecting Data\\n`.loc` is label-based, meaning you specify the exact name of the row/column. `.iloc` is integer-based, meaning you specify the numeric index (0, 1, 2) regardless of the label.", "instructions": "## Task: Integer Selection\\nSelect the first 5 rows and first 2 columns of a DataFrame `df` using integer-based indexing.", "starterCode": "subset = df.___[:5, :2]", "solution": "subset = df.iloc[:5, :2]", "hint": "Use iloc", "rubric": "Uses iloc."},
            {"title": "GroupBy & Aggregations", "theory": "## Split-Apply-Combine\\nThe `.groupby()` method splits your data into groups, applies a function to each group independently (like `sum` or `mean`), and combines the results back into a new DataFrame.", "instructions": "## Task: Group and Mean\\nGroup the DataFrame `df` by the 'Category' column and calculate the mean of the remaining columns.", "starterCode": "avg_by_cat = df.___('Category').___()", "solution": "avg_by_cat = df.groupby('Category').mean()", "hint": "Use groupby and mean", "rubric": "Uses groupby and mean()."},
            {"title": "Window Functions", "theory": "## Rolling Calculations\\nWindow functions perform calculations across a set of rows related to the current row. For example, a 7-day rolling average smooths out daily volatility in a time series.", "instructions": "## Task: Rolling Mean\\nCalculate a 7-period rolling average on the 'Sales' column.", "starterCode": "smoothed = df['Sales'].___(___).mean()", "solution": "smoothed = df['Sales'].rolling(7).mean()", "hint": "Use rolling(7)", "rubric": "Uses rolling(7)."},
            {"title": "Merging and Joining", "theory": "## Combining Datasets\\n`pd.merge()` works similarly to SQL joins. A 'left' join keeps all rows from the left DataFrame, filling in missing matches from the right DataFrame with NaNs.", "instructions": "## Task: Perform a Left Join\\nMerge `df1` and `df2` on the 'user_id' column using a left join.", "starterCode": "merged_df = pd.___(df1, df2, on='user_id', how='___')", "solution": "merged_df = pd.merge(df1, df2, on='user_id', how='left')", "hint": "Use merge and 'left'", "rubric": "Uses merge and left."},
            {"title": "Pivot Tables", "theory": "## Reshaping Data\\n`pd.pivot_table()` creates spreadsheet-style pivot tables as a DataFrame. It is a powerful alternative to `groupby` when you need to specify rows, columns, and aggregate functions simultaneously.", "instructions": "## Task: Create a Pivot Table\\nCreate a pivot table using 'City' as the index and computing the sum of 'Sales'.", "starterCode": "pivot = pd.___(df, values='Sales', index='City', aggfunc='___')", "solution": "pivot = pd.pivot_table(df, values='Sales', index='City', aggfunc='sum')", "hint": "Use pivot_table and 'sum'", "rubric": "Uses pivot_table and sum."},
            {"title": "MultiIndex", "theory": "## Hierarchical Indexing\\nA MultiIndex allows you to have multiple levels of indexes on a single axis. This is useful for working with higher-dimensional data in a 2D DataFrame (like Year -> Month -> Sales).", "instructions": "## Task: Set Multiple Indexes\\nSet both the 'Year' and 'Month' columns as the index of the DataFrame.", "starterCode": "df_multi = df.___( [ 'Year', 'Month' ] )", "solution": "df_multi = df.set_index( [ 'Year', 'Month' ] )", "hint": "Use set_index", "rubric": "Uses set_index."},
            {"title": "Vectorized String Methods", "theory": "## Fast Text Processing\\nPandas allows you to apply string methods to an entire column at once using the `.str` accessor, bypassing slow Python loops.", "instructions": "## Task: String Contains\\nFilter the DataFrame to keep only rows where the 'Email' column contains the string '@gmail.com'.", "starterCode": "gmail_users = df[ df['Email'].___.___('@gmail.com') ]", "solution": "gmail_users = df[ df['Email'].str.contains('@gmail.com') ]", "hint": "Use .str.contains", "rubric": "Uses .str.contains."},
            {"title": "Handling DateTimes", "theory": "## Time Series Foundations\\nBy converting strings to true datetime objects, you unlock powerful methods for extracting years, months, days, or resampling data into different frequencies (like daily to monthly).", "instructions": "## Task: Convert to DateTime\\nConvert the 'Date' column from raw strings into actual pandas datetime objects.", "starterCode": "df['Date'] = pd.___( df['Date'] )", "solution": "df['Date'] = pd.to_datetime( df['Date'] )", "hint": "Use to_datetime", "rubric": "Uses pd.to_datetime."}
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
        
        for new_course_name, course_info in NEW_COURSES_BATCH58.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH58.items():
            tier = course_info["tier"]
            if "Data Science" in index_data and tier in index_data["Data Science"]:
                if new_course_name not in index_data["Data Science"][tier]:
                    index_data["Data Science"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 58: Added {total} lessons to Data Science track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
