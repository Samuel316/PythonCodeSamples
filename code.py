# Convert all strings in a DataFrame to UpperCase

df[df_bbti_orders.select_dtypes(include="object").columns] = (
    df.select_dtypes(include="object").apply(lambda x: x.str.upper())
)

