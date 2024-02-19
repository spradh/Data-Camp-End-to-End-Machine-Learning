#1
# Import required modules
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

#2
# Split the data into training and testing sets (80:20)
X_train, X_test, y_train, y_test = train_test_split(heart_disease_X, heart_disease_y, test_size=.2, random_state=42)

#3
# Define the SVM / SVC model
svc_model = SVC(kernel='linear')
svc_model.fit(X_train, y_train)

#4
# Get predictions from the model
y_pred = svc_model.predict(X_test)
print(y_pred)
