#1
# Print the first 5 rows of the DataFrame
print(heart_disease_df.head())

# Print information about the DataFrame
print(heart_disease_df.info())


#2


# Visualize the cholestrol column
heart_disease_df['chol'].plot(kind='hist')

# Set the title and axis labels
plt.title('Cholestrol distribution')
plt.xlabel('Cholestrol')
plt.ylabel('Frequency')
plt.show()
