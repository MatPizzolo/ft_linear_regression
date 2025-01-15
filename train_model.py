import csv
import pandas as pd
import matplotlib.pyplot as plt
import json


def plot(df):
	"""
	Plots mileage vs. price using matplotlib.
	"""
	plt.figure(figsize=(8, 6))
	plt.scatter(df['km'], df['price'], color='blue', alpha=0.7, label='Data points')
	plt.title("Mileage vs Price", fontsize=16)
	plt.xlabel("Mileage (km)", fontsize=12)
	plt.ylabel("Price ($)", fontsize=12)
	plt.legend()
	plt.grid(True, linestyle='--', alpha=0.6)
	plt.savefig("mileage_vs_price.png")  # Save the plot as an image
	print("Plot saved as 'mileage_vs_price.png'")

def create_df():
	kms = []
	prices = []

	with open("data.csv", ) as csvfile:
		file = csv.reader(csvfile)
		next(file) #Skip header
		for lines in file:
			kms.append(float(lines[0]))
			prices.append(float(lines[1]))

	df = pd.DataFrame({
		'km': kms,
		'price': prices
		})
	
	return df

class LinearRegressionGD:
	def __init__(self):
		self.theta0 = 0 # Intercept
		self.theta1 = 0 # Coefficient
		self.max_x = 0
		
	def predict_price(self, km):
		"""estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)"""
		return self.theta0 + (self.theta1 * km)
	
	def fit(self, x, y, lr, iterations):
		"""Train the model using Gradient Descent."""
		self.max_x = max(x)
		x = x / self.max_x
		y = y / self.max_x
		m = len(x)

		for _ in range(iterations):
			tmp_theta0 = 0
			tmp_theta1 = 0

			for i in range(m):
				prediction = self.theta0 + (self.theta1 * x[i])
				error = prediction - y[i]
				tmp_theta0 += error
				tmp_theta1 += error * x[i]

			self.theta0 = self.theta0 - ((lr / m) * tmp_theta0)
			self.theta1 = self.theta1 - ((lr / m) * tmp_theta1)

		# Multiply by max_x because it directly relates to the y-intercept, which was scaled
		self.theta0 = self.theta0 * self.max_x
		# theta1 unchanged because the ratio of changes in (the slope) remains consistent, even with scaling.
	
	def save_parameters(self):
		params = {
			'theta0': float(self.theta0),
			'theta1': float(self.theta1)
		}
		with open('parameters.json', 'w') as file:
			json.dump(params, file)


def main():
	df = create_df()

	learning_rate = 0.01
	iterations = 50000
	
	model = LinearRegressionGD()
	model.fit(df['km'].values, df['price'].values, learning_rate, iterations)
	
	print(f"Theta0 (intercept): {model.theta0:.4f}")
	print(f"Theta1 (slope): {model.theta1:.4f}")

	model.save_parameters()

if __name__ == "__main__":
	main()
