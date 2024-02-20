fig, ax = plt.subplots(1, 2, figsize=(15, 6))  # 1 row, 2 columns
# January Plot
logs_january['target'].value_counts().plot(kind='bar',  ax=ax[0])
ax[0].set_title('Distribution of Predicted Classes - January')
ax[0].set_xlabel('Class')
ax[0].set_ylabel('Frequency')

# February Plot
logs_february['target'].value_counts().plot(kind='bar',  ax=ax[1])
ax[1].set_title('Distribution of Predicted Classes - February')
ax[1].set_xlabel('Class')
ax[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()
