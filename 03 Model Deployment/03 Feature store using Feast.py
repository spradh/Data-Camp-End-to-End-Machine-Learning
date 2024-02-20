#1
heart_disease_df.to_parquet("heart_disease.parquet")

# Point File Source to the saved file
data_source = FileSource(
    path="heart_disease.parquet",
    event_timestamp_column="timestamp",
    created_timestamp_column="created",
)

#2
# Create a Feature View of the features
heart_disease_fv = FeatureView(
    name="heart_disease",
    entities=[patient],
    schema=[cp, thalach, ca, thal],
    source=data_source,
)

#3
# Create a store of the data and apply the features
store = FeatureStore(repo_path=".")
store.apply([patient, heart_disease_fv])
