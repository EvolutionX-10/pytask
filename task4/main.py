import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate random x values as timestamps
x = np.sort(np.random.uniform(0, 10, 60))

# Generate y values using a quadratic equation with some random noise
y = 2 * x**2 - 3 * x + np.random.uniform(-10, 10, 60)

# Create a new x sequence for prediction
x_pred = np.arange(10, 15, 1)

# Define the learning rate and number of iterations
learning_rate = 0.00001
num_iterations = 10000

# Initialize the model parameters (coefficients)
theta0, theta1, theta2 = 0, 0, 0


# Create a function for polynomial regression prediction
def predict(x, theta0, theta1, theta2):
    return theta0 + theta1 * x + theta2 * x**2


# Create a function to update the plot for animation
def update(frame):
    global theta0, theta1, theta2

    plt.cla()
    plt.scatter(x, y, color="blue", label="Data Points")

    if frame > 0:
        for _ in range(num_iterations):
            # Compute the gradients
            gradient0 = np.sum(predict(x, theta0, theta1, theta2) - y) / len(x)
            gradient1 = np.sum((predict(x, theta0, theta1, theta2) - y) * x) / len(x)
            gradient2 = np.sum((predict(x, theta0, theta1, theta2) - y) * x**2) / len(
                x
            )

            # Update the model parameters
            theta0 -= learning_rate * gradient0
            theta1 -= learning_rate * gradient1
            theta2 -= learning_rate * gradient2

        x_pred_frame = x_pred[:frame]
        y_pred_frame = predict(x_pred_frame, theta0, theta1, theta2)
        plt.plot(x_pred_frame, y_pred_frame, color="red", label="Predicted Path")

    plt.legend(loc="upper left")
    plt.xlabel("Timestamp (x)")
    plt.ylabel("Position (y)")
    plt.title("Polynomial Regression Prediction with Gradient Descent")


# Create an animation
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=3, repeat=False, blit=False)

plt.show()
