# Student Academic Performance Analytics

**Project 2 | Industry: Education / EdTech**

## Business scenario
Analyze student attendance, study habits, assessment scores and internet access to identify performance patterns and students who may need academic support.

## Dataset
The project uses the supplied `02_student_performance.csv` teaching dataset containing 500 records and 11 original columns.

- `data/02_student_performance_original.csv` — original supplied dataset.
- `data/02_student_performance_cleaned.csv` — cleaned dataset with calculated fields.

## Project structure
```text
student-academic-performance-analytics/
├── SRS/
│   └── project_SRS.pdf
├── data/
│   ├── 02_student_performance_original.csv
│   └── 02_student_performance_cleaned.csv
├── src/
│   ├── student_academic_performance_analysis.ipynb
│   └── analysis.py
├── README.md
└── requirements.txt
```

## Tasks covered
1. Load and inspect the dataset.
2. Report missing values and duplicate `Student_ID` values.
3. Impute missing attendance with the median.
4. Validate subject marks against the 0–100 range.
5. Calculate total and average marks.
6. Assign grades using project-defined ranges.
7. Calculate department-wise average marks.
8. List the top 10 students by average marks.
9. Identify students with average marks below 40%.
10. Compare average marks across attendance bands.
11. Analyze study hours and average marks.
12. Compare students with and without internet access.
13. Calculate median, sample standard deviation and quartiles for `Python_Marks` using NumPy.
14. Flag potential `Python_Marks` outliers using IQR.
15. Provide five academic-support recommendations.

## Cleaning decisions and assumptions
- Missing `Attendance_Percent` values are filled with the median of the observed attendance values.
- Duplicate IDs are reported. No rows are silently removed.
- Subject marks are validated; the analysis does not silently clip or alter invalid marks.
- `Total_Marks` is recalculated as the sum of Python, Maths and Physics marks.
- `Average_Marks` is the arithmetic mean of those three subject scores.
- Grades: A+ (90–100), A (80–<90), B (70–<80), C (60–<70), D (50–<60), F (<50).
- Attendance bands: below 60%, 60–<75%, 75–<90%, and 90% or above.
- Study-hour bands: below 2, 2 to under 4, and 4 or more hours per day.
- At-risk identification follows the assignment's specific criterion: average marks below 40%.

## How to run

### 1. Create and activate a virtual environment (optional)
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the notebook
Open `src/student_academic_performance_analysis.ipynb` in Jupyter Notebook or VS Code. Run all cells from top to bottom. Run it from the repository root so the relative dataset paths work.

### 4. Or run the Python script
```bash
python src/analysis.py
```

The script writes `data/02_student_performance_cleaned.csv`.

## Limitations
This is a teaching dataset. The analysis is descriptive, and correlations or group differences do not prove causation. The grade ranges are defined for this project and may not match an institution's official grading policy. The dataset's original `Result` field may use a different rule from the assignment's below-40% average criterion.

## Author
Student: **Mohd Asim Khan**  
Student ID: **2026B01010183**


