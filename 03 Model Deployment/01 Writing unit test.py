#1
import unittest
import numpy as np

# Create a class called TestModelInference
class TestModelInference(unittest.TestCase()):
	def setUp(self):
		self.model = model
#2
		# set X_test as a class attribute
		self.X_test = X_test

#3
	# define a test for prediction output values
	def test_prediction_output_values(self):
		print("Running test_prediction_output_values test case")

#4
		# Get model predictions
		y_pred = self.model.predict(self.X_test)
		unique_values = np.unique(y_pred)
		for value in unique_values:
			self.assertIn(value, [0, 1])
