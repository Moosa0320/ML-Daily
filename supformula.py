def my_linear_model(x, w, b):
    
    y_hat = (w * x) + b
    return y_hat


house_size_x = 1300


w = 0.1  
b = 40   


predicted_price_y_hat = my_linear_model(house_size_x, w, b)

print(f"House size (x): {house_size_x} sq ft")
print(f"Model's Prediction (y-hat): ${predicted_price_y_hat}k")