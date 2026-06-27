"""
Batch 59: Deep Dive into Data Science (A/B Testing & Causal Inference Masterclass)
"""
import json, os

NEW_COURSES_BATCH59 = {
    "A/B Testing & Causal Inference Masterclass": {
        "tier": "Advanced",
        "aiRubric": "Assess deep understanding of experiment design and causal inference",
        "lessons": [
            {"title": "Hypothesis Testing", "theory": "## The Scientific Method\\nIn A/B testing, you start with a Null Hypothesis (H0) which states there is *no difference* between the control and variant. Your goal is to gather enough data to reject H0 in favor of the Alternative Hypothesis (H1).", "instructions": "## Task: The Default Assumption\\nWhen testing a new button color to see if it increases click-through rates, what does the Null Hypothesis assume?", "starterCode": "# Options: The new color is better, The new color is worse, The color has no effect\\nnull_hypothesis = '___'", "solution": "# Options: The new color is better, The new color is worse, The color has no effect\\nnull_hypothesis = 'The color has no effect'", "hint": "It assumes no effect.", "rubric": "Identifies The color has no effect."},
            {"title": "p-values and Alpha", "theory": "## Measuring Surprise\\nThe p-value is the probability of seeing your experimental results *assuming the Null Hypothesis is true*. If the p-value is lower than your significance level (Alpha, typically 0.05), you reject the Null Hypothesis.", "instructions": "## Task: Statistical Significance\\nIf you run an A/B test with an Alpha of 0.05, and your calculated p-value is 0.02, what is the conclusion?", "starterCode": "# Options: Reject Null, Fail to reject Null\\nconclusion = '___'", "solution": "# Options: Reject Null, Fail to reject Null\\nconclusion = 'Reject Null'", "hint": "0.02 is less than 0.05, so Reject Null", "rubric": "Identifies Reject Null."},
            {"title": "Statistical Power", "theory": "## Avoiding False Negatives\\nStatistical Power (1 - Beta) is the probability that your test will correctly detect a true effect when one exists. A common target for power is 80%. If your power is too low, you might abandon a winning feature.", "instructions": "## Task: Increasing Power\\nWhat is the most direct way to increase the Statistical Power of an A/B test before running it?", "starterCode": "# Options: Decrease sample size, Increase sample size, Change the button color again\\nway_to_increase = '___'", "solution": "# Options: Decrease sample size, Increase sample size, Change the button color again\\nway_to_increase = 'Increase sample size'", "hint": "Increase sample size", "rubric": "Identifies Increase sample size."},
            {"title": "T-Tests", "theory": "## Comparing Means\\nAn Independent Two-Sample T-Test is used to determine if there is a statistically significant difference between the *averages* of two independent groups (e.g., Average Revenue Per User in Group A vs Group B).", "instructions": "## Task: Run a T-Test\\nImport the function from scipy to run an independent t-test.", "starterCode": "from scipy.stats import ___\\n\\nstat, pval = ___(group_a, group_b)", "solution": "from scipy.stats import ttest_ind\\n\\nstat, pval = ttest_ind(group_a, group_b)", "hint": "Use ttest_ind", "rubric": "Uses ttest_ind."},
            {"title": "Chi-Square Tests", "theory": "## Categorical Proportions\\nIf your metric is a binary proportion (e.g., Conversion Rate: converted vs not converted), a T-Test isn't appropriate. Instead, you use a Chi-Square test of independence to compare the categorical distributions.", "instructions": "## Task: Test Selection\\nWhich test should you use to compare the Conversion Rate (a percentage) between the Control and Variant groups?", "starterCode": "# Options: T-Test, Chi-Square Test, ANOVA\\ntest_to_use = '___'", "solution": "# Options: T-Test, Chi-Square Test, ANOVA\\ntest_to_use = 'Chi-Square Test'", "hint": "Chi-Square Test", "rubric": "Identifies Chi-Square Test."},
            {"title": "The Multiple Testing Problem", "theory": "## Peeking and Splitting\\nIf you test 20 different button colors at a 0.05 significance level, you are almost guaranteed to get at least one false positive purely by chance. This is the Multiple Testing Problem.", "instructions": "## Task: The Correction\\nWhat is the name of the conservative method that corrects for this by dividing your alpha by the number of tests (e.g., 0.05 / 20)?", "starterCode": "# Options: The Student Correction, The Bonferroni Correction, The Pearson Correction\\ncorrection = 'The ___'", "solution": "# Options: The Student Correction, The Bonferroni Correction, The Pearson Correction\\ncorrection = 'The Bonferroni Correction'", "hint": "Bonferroni Correction", "rubric": "Identifies Bonferroni Correction."},
            {"title": "Difference-in-Differences", "theory": "## Quasi-Experiments\\nSometimes you can't run a randomized A/B test (e.g., a new law is passed in one state). Difference-in-Differences (DiD) compares the change over time in the treated group to the change over time in the control group to estimate the causal effect.", "instructions": "## Task: The Core Assumption\\nDiD relies on the assumption that, in the absence of treatment, the difference between the two groups would have remained constant over time. What is this assumption called?", "starterCode": "# Options: Parallel Trends, Orthogonal Vectors, Linear Regression\\nassumption = '___'", "solution": "# Options: Parallel Trends, Orthogonal Vectors, Linear Regression\\nassumption = 'Parallel Trends'", "hint": "Parallel Trends", "rubric": "Identifies Parallel Trends."},
            {"title": "Propensity Score Matching", "theory": "## Observational Data\\nWhen analyzing observational data where users *self-selected* into a feature, you have selection bias. Propensity Score Matching pairs a treated user with a non-treated user who has very similar characteristics to simulate a randomized control trial.", "instructions": "## Task: The Score\\nWhat does the 'Propensity Score' actually represent mathematically?", "starterCode": "# Options: Probability of converting, Probability of receiving the treatment, The lifetime value of the user\\nrepresents = '___'", "solution": "# Options: Probability of converting, Probability of receiving the treatment, The lifetime value of the user\\nrepresents = 'Probability of receiving the treatment'", "hint": "Probability of receiving the treatment", "rubric": "Identifies Probability of receiving the treatment."}
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
        
        for new_course_name, course_info in NEW_COURSES_BATCH59.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH59.items():
            tier = course_info["tier"]
            if "Data Science" in index_data and tier in index_data["Data Science"]:
                if new_course_name not in index_data["Data Science"][tier]:
                    index_data["Data Science"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 59: Added {total} lessons to Data Science track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
