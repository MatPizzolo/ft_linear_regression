import json

def get_theta_values(file_path):
	try:
		with open(file_path, 'r') as file:
			data = json.load(file)
			theta0 = data.get("theta0")
			theta1 = data.get("theta1")
			
			if theta0 is None or theta1 is None:
				raise ValueError("Missing 'theta0' or 'theta1' in the JSON file.")
			
			return theta0, theta1
	except FileNotFoundError:
		print(f"Error: File '{file_path}' not found.")
	except json.JSONDecodeError:
		print(f"Error: Could not decode JSON from file '{file_path}'.")
	except ValueError as e:
		print(f"Error: {e}")

def ask_input():
	while True:
		nbr = input("KMs? ")
		
		if not nbr:
			print("Please enter a value.")
			continue
		
		try:
			nbr = float(nbr)  # Convert to float
			if nbr <= 0:
				print("The value must be greater than 0.")
			elif nbr >= 410000:
				print("The value must be less than 410,000.")
			else:
				return nbr  # Input is valid, return the value
		except ValueError:
			print("Invalid input. Please enter a numeric value.")



def predict_price(km, theta0, theta1):
	"""estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)"""
	return theta0 + (theta1 * km)


def main():
	theta0, theta1 = get_theta_values("parameters.json")
	print(f"Theta0: {theta0}, Theta1: {theta1}")
	kms = ask_input()
	estimatePrice = predict_price(kms, theta0, theta1)

	print(f"estimatePrice({kms}): {estimatePrice:.2f}")


if __name__ == "__main__":
	main()
