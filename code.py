# Convert all strings in a DataFrame to UpperCase

df[df_bbti_orders.select_dtypes(include="object").columns] = (
    df.select_dtypes(include="object").apply(lambda x: x.str.upper())
)

# Convert whole DataFrame to percent of Total

df.div(df.sum(axis=1), axis=0).multiply(100)

# --- Datetime ---
# Get Week Number
df["Datetime"].dt.isocalendar().week

#Filter with interval
df[df["Datetime"] >= pd.to_datetime("today") - pd.DateOffset(months=1)]

# Get day of year
df["Datetime"].dt.day_of_year

# Groupby/Resample Examples
df.groupby("Group").size()
df.groupby("Group").resample("h", on="Datetime").size()

df.groupby("Group").agg({"index": "count", "Value": "min"})


