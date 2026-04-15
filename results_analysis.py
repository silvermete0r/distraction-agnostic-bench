import pandas as pd

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

tasks_max_scores = (
    df
    .groupby("Task_Name")
    .agg(
        Max_Score=("Numerical_Result", "max"),
        Models=("Model", lambda m: list(m))
    )
    .reset_index()
)
# keep only models that achieved the max
tasks_max_scores["Models_Solved"] = tasks_max_scores.apply(
    lambda row: df[
        (df["Task_Name"] == row["Task_Name"]) &
        (df["Numerical_Result"] == row["Max_Score"])
    ]["Model"].tolist(),
    axis=1
)
tasks_max_scores["Num_Models_Solved"] = tasks_max_scores["Models_Solved"].apply(len)
tasks_max_scores = tasks_max_scores.sort_values(
    by=["Max_Score", "Num_Models_Solved"],
    ascending=[True, True]
).reset_index(drop=True)
tasks_max_scores["Task_Name"] = tasks_max_scores["Task_Name"].str.replace("Distraction agnostic main task ", "")
print(tasks_max_scores.to_markdown())