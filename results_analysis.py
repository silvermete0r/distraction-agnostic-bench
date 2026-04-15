import pandas as pd
import numpy as np

df = pd.read_csv("assets/armanzhalgasbayev_distraction-agnostic-bench_leaderboard.csv")
needed_cols = ["Model", "Task_Name", "Numerical_Result"]
df = df[needed_cols]
print("Unique models list: ", df["Model"].unique().tolist())

res_leaderboard = (
    df.groupby(by="Model")["Numerical_Result"]
    .mean()
    .sort_values(ascending=False)
    .to_frame(name="Mean_score")
)
res_leaderboard["Mean_score"] = res_leaderboard["Mean_score"].round(3)
print(res_leaderboard.to_markdown())


max_scores = df.groupby("Task_Name", as_index=False)["Numerical_Result"].max()
max_scores = max_scores.rename(columns={"Numerical_Result": "Max_Score"})
merged = df.merge(max_scores, on="Task_Name")
best = merged[np.isclose(merged["Numerical_Result"], merged["Max_Score"])]
tasks_max_scores = (
    best.groupby(["Task_Name", "Max_Score"])["Model"]
    .apply(list)
    .reset_index(name="Models_Solved")
)
tasks_max_scores["Num_Models_Solved"] = tasks_max_scores["Models_Solved"].str.len()
tasks_max_scores = tasks_max_scores.sort_values(
    by=["Max_Score", "Num_Models_Solved"],
    ascending=[True, False]
).reset_index(drop=True)
tasks_max_scores["Task_Name"] = tasks_max_scores["Task_Name"].str.replace(
    "Distraction agnostic main task ", "", regex=False
)
print(tasks_max_scores.to_markdown())