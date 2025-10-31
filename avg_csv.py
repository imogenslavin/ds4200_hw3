import pandas as pd # type: ignore

# Read data
df = pd.read_csv("/Users/imogenslavin/Desktop/ds42000/HW3/socialMedia.csv")

avg_df = df.groupby(['Platform', 'PostType'], as_index=False)["Likes"].mean()

avg_df["Likes"] = avg_df["Likes"].round(2)
avg_df = avg_df.rename(columns={"Likes": "AvgLikes"})

avg_df.to_csv("/Users/imogenslavin/Desktop/ds42000/HW3/socialMediaAvg.csv", index = False)

print(avg_df.head())



