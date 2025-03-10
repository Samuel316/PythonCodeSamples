# Convert all strings in a DataFrame to UpperCase

df[df_bbti_orders.select_dtypes(include="object").columns] = (
    df.select_dtypes(include="object").apply(lambda x: x.str.upper())
)

# Reorder Column Levels
df.pivot_table(...).reorder_levels([{New Column List}], axis=1).sort_index(axis=1)

# Convert whole DataFrame to percent of Total

df.div(df.sum(axis=1), axis=0).multiply(100)

# Create multiindex
df.columns = pd.MultiIndex.from_tuples([("A", "1"), ("A", "2"), ("B", "1")])

# --- Datetime ---
# Get Week Number
df["Datetime"].dt.isocalendar().week

#Filter with interval
df[df["Datetime"] >= pd.to_datetime("today") - pd.DateOffset(months=1)]

# Get day of year
df["Datetime"].dt.day_of_year

# String Methods
df["String"].str.contains(regex=True, pat=r"\d+")

# Filter
df.filter(like="String Part")

# Map - Replaces Everything - can be dict or series
df["Value"].map({"A": "a", "B", "b"})

# Replace - Replaces Matches Only - Can also be a regex, string
df["Value"].replace("A", "a)
df["Value"].replace({"A": "a", "B", "b"})

# Groupby/Resample Examples
df.groupby("Group").size()
df.groupby("Group").resample("h", on="Datetime").size()

df.groupby("Group").agg({"index": "count", "Value": "min"})

df.groupby("Group").agg(Count=("Index", "size"), ConcatString=("String", lambda x: ",".join(x)))

# Get row with min/max value in particular column
df.loc[df.groupby("LabelColumn")["ValueColumn"].idxmin()]
df.sort_values(by="ValueColumn").groupby("LabelColumn", as_index=False).first()

# Background Gradient
df..style.background_gradient()
