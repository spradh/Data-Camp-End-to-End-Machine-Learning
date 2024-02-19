#1
# Drop empty columns
heart_disease_column_dropped = heart_disease_df.drop('oldpeak', axis='columns')

#2
# Drop duplicate rows
heart_disease_duplicates_dropped = heart_disease_column_dropped.drop_duplicates()

#3
# Calculate the mean value of the restecg column
mean_value = heart_disease_duplicates_dropped["restecg"].mean()

#4
# Impute missing values with the mean
heart_disease_duplicates_dropped['restecg'].fillna(mean_value, inplace=True)
print(heart_disease_duplicates_dropped['restecg'].isna().any())
