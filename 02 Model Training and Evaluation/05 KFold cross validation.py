# Create a KFold object
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Get the train and test data from the first split from the shuffled KFold
train_data_split, test_data_split = next(kfold.split(heart_disease_df_X))

# Print out the number of datapoints in the train and test splits
print("Number of training datapoints in heart_disease_df_X:", heart_disease_df_X.shape[0])
print("Number of training datapoints in split:", train_data_split.shape[0])
print("Number of testing datapoints in split:", test_data_split.shape[0])
