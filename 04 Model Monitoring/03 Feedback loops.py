#1
# Calculate and print the balanced accuracy of the model
balanced_accuracy_jan = 60.0
balanced_accuracy_feb = balanced_accuracy_score(true_labels_feb, predicted_labels_feb) * 100
print(f"Model Balanced Accuracy In February: {balanced_accuracy_feb:.2f}%")
print(f"Is there a decline in accuracy? {'Yes' if balanced_accuracy_feb < balanced_accuracy_jan else 'No'}")

#2
# Use the Kolmogorov-Smirnov test to check for data drift
ks_statistic, p_value = ks_2samp(jan_data_samples, feb_data_samples)

significant_drift = p_value < .05

print(f"Kolmogorov-Smirnov Statistic: {ks_statistic:.4f}")
print(f"P-value: {p_value:.4f}")
print(f"Is there significant data drift? {'Yes' if significant_drift else 'No'}")
