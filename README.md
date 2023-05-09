# Robotic-Arm-Motion-Planning-with-Gradient-Descent

This code is an implementation of a robotic arm simulation using Pygame library. The code uses Pygame to create a graphical window, where the arm is drawn, and the user can control the position of a target by either clicking on the screen or randomly. The goal of the simulation is to make the end effector of the robotic arm, the last joint of the arm, to reach the target.

The arm consists of three joints, and each joint can rotate around the previous joint. The simulation calculates the angles of the joints that will make the end effector of the arm reach the target using the Gradient Descent algorithm.
Gradient descent is an optimization algorithm that can be used to find the optimal values for the parameters of a function by minimizing its loss or error.
The gradients of the loss with respect to the parameters are calculated using backpropagation, and the weights are updated iteratively based on these gradients.

The basic idea of gradient descent is to take small steps in the direction of the negative gradient of the loss function. This approach is called "descending" the gradient, which leads to the term "gradient descent." The size of the step taken is controlled by a learning rate hyperparameter, which determines the amount of weight adjustment in each iteration.

The code uses the numdifftools library to calculate the gradient of the distance function, which is the Euclidean distance between the target and the end effector of the arm.

The code uses two modes of operation, the manual mode, where the user can set the target position by clicking on the screen, and the random mode, where the target position is randomly set within the screen's boundaries. The code uses an Armijo rule, a backtracking line search method, to update the step size more efficently.

Note that the code has a hard-coded number of iterations, where the simulation stops if the end effector of the arm is within a certain distance from the target or after a maximum number of iterations have been reached.
