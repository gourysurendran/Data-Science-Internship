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

---

## Task 2: Exploratory Data Analysis (EDA)

### Objective

To analyze the Titanic dataset using visualizations and identify patterns affecting survival.

### Steps Performed

* Plotted survival count
* Analyzed survival based on gender
* Visualized age distribution
* Analyzed fare distribution
* Created correlation heatmap

### Key Insights

* Most passengers did not survive
* Females had higher survival rate than males
* Most passengers were aged between 20–30
* Fare distribution is right-skewed
* Higher class passengers had better survival chances

### Tools Used

* Python
* Pandas
* Matplotlib
* Seaborn

### Output

Visual insights and patterns from the dataset using graphs and analysis

