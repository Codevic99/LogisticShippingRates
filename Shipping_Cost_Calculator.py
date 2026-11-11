# Shipping Cost Calculator

## Imput package weight and shipping rate
weight == float(imput("Enter the package weight in kilograms: "))
rate == float(imput("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
Shipping_cost = weight * rate

## Display the result
print(f"Shipping cost: {shipping_cost} USD")
