# Import the ks_2samp function
from scipy.stats import ks_2samp

# Calculate the test statistic and p value
test_statistic, p_value = ks_2samp(january_data, february_data)

# Check the p-value and print the detection result
if p_value<.05:
	print("Data drift detected.")
else:
	print("No data drift detected.")
