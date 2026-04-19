# Data-Science-Internship

CODTECH Data Science Internship Tasks

---

## Task 1: Data Pipeline

### Objective

To clean and preprocess the dataset so it can be used for analysis and modeling.

### Steps Performed

* Loaded dataset using pandas
* Viewed data using `head()` and `info()`
* Checked missing values using `isnull().sum()`
* Filled missing values:

  * `Age` → mean
  * `Embarked` → mode
* Dropped `Cabin` column due to many missing values
* Verified that no missing values remain
* Saved cleaned dataset as `processed_data.csv`

### Files Included

* `data.csv` → Original dataset
* `pipeline.ipynb` → Code implementation
* `processed_data.csv` → Cleaned dataset

### Tools Used

* Python
* Pandas
* Jupyter Notebook

### Output

A cleaned dataset with no missing values, ready for further analysis and modeling.
