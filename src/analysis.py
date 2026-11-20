"""
Student Academic Performance Analytics
Run from the project root:
    python src/analysis.py
"""
from pathlib import Path
import numpy as np
import pandas as pd

DATA_PATH = Path("data/02_student_performance_original.csv")
OUTPUT_PATH = Path("data/02_student_performance_cleaned.csv")

df = pd.read_csv(DATA_PATH)
print("Shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate Student_ID:", df["Student_ID"].duplicated().sum())

clean_df = df.copy()
attendance_median = clean_df["Attendance_Percent"].median()
clean_df["Attendance_Percent"] = clean_df["Attendance_Percent"].fillna(attendance_median)

score_columns = ["Python_Marks", "Maths_Marks", "Physics_Marks"]
print("\nScore validation:\n", pd.DataFrame({
    "Below_0": (clean_df[score_columns] < 0).sum(),
    "Above_100": (clean_df[score_columns] > 100).sum()
}))

clean_df["Total_Marks"] = clean_df[score_columns].sum(axis=1)
clean_df["Average_Marks"] = clean_df[score_columns].mean(axis=1)
grade_bins = [-np.inf, 50, 60, 70, 80, 90, np.inf]
grade_labels = ["F", "D", "C", "B", "A", "A+"]
clean_df["Grade"] = pd.cut(clean_df["Average_Marks"], grade_bins, labels=grade_labels, right=False)

clean_df["Attendance_Band"] = pd.cut(
    clean_df["Attendance_Percent"], [-np.inf, 60, 75, 90, np.inf],
    labels=["Low (<60%)", "Moderate (60–74.9%)", "Good (75–89.9%)", "Excellent (90%+)"],
    right=False
)
clean_df["Study_Hours_Band"] = pd.cut(
    clean_df["Study_Hours_Per_Day"], [-np.inf, 2, 4, np.inf],
    labels=["Low (<2 hrs)", "Moderate (2–4 hrs)", "High (>4 hrs)"],
    right=False
)

print("\nGrade distribution:\n", clean_df["Grade"].value_counts().reindex(grade_labels, fill_value=0))
print("\nDepartment summary:\n", clean_df.groupby("Department")["Average_Marks"].agg(["count", "mean"]).sort_values("mean", ascending=False))
print("\nTop 10 students:\n", clean_df.nlargest(10, "Average_Marks")[["Student_ID", "Department", "Average_Marks", "Grade"]])
at_risk = clean_df[clean_df["Average_Marks"] < 40]
print("\nStudents below 40% average:\n", at_risk[["Student_ID", "Department", "Average_Marks"]])
print("\nAttendance band summary:\n", clean_df.groupby("Attendance_Band", observed=False)["Average_Marks"].agg(["count", "mean"]))
print("\nStudy hours band summary:\n", clean_df.groupby("Study_Hours_Band", observed=False)["Average_Marks"].agg(["count", "mean"]))
print("\nStudy hours correlation:", clean_df["Study_Hours_Per_Day"].corr(clean_df["Average_Marks"]))
print("\nInternet summary:\n", clean_df.groupby("Internet_Access")["Average_Marks"].agg(["count", "mean", "median"]))

python_scores = clean_df["Python_Marks"].to_numpy()
q1, median, q3 = np.percentile(python_scores, [25, 50, 75])
print("\nPython_Marks median:", median)
print("Python_Marks sample standard deviation:", np.std(python_scores, ddof=1))
print("Python_Marks quartiles:", q1, median, q3)

iqr = q3 - q1
lower_fence, upper_fence = q1 - 1.5 * iqr, q3 + 1.5 * iqr
outliers = clean_df[(clean_df["Python_Marks"] < lower_fence) | (clean_df["Python_Marks"] > upper_fence)]
print("\nPython score IQR fences:", lower_fence, upper_fence)
print("Potential outliers:\n", outliers[["Student_ID", "Python_Marks"]])

clean_df.to_csv(OUTPUT_PATH, index=False)
print(f"\nSaved cleaned dataset to {OUTPUT_PATH}")
