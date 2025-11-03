import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Function to draw a coordinate frame
def draw_frame(ax, origin, R, label, length=20):
    colors = ['r', 'g', 'b']  # X, Y, Z
    axes = ['X', 'Y', 'Z']
    for i in range(3):
        vec = R[:, i] * length
        ax.quiver(*origin, *vec, color=colors[i], linewidth=2)
        ax.text(*(origin + vec), f"{axes[i]}{label}", fontsize=10)

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Base frame (Frame 0)
O0 = np.array([0, 0, 0])
R0 = np.eye(3)  # identity matrix for base frame
draw_frame(ax, O0, R0, '0')

# Frame 1: Rotated -90 deg around X from Frame 0 (alpha1 = -90)
theta1 = 0
alpha1 = -np.pi / 2
Rz1 = np.array([[np.cos(theta1), -np.sin(theta1), 0],
                [np.sin(theta1),  np.cos(theta1), 0],
                [0,              0,             1]])
Rx1 = np.array([[1, 0, 0],
                [0, np.cos(alpha1), -np.sin(alpha1)],
                [0, np.sin(alpha1),  np.cos(alpha1)]])
R1 = R0 @ Rz1 @ Rx1
O1 = O0 + R0 @ np.array([0, 0, 0])  # d1 = 0
draw_frame(ax, O1, R1, '1')

# Frame 2: Translate along X1 by L1, alpha2 = 0
L1 = 50
alpha2 = 0
Rz2 = np.eye(3)
Rx2 = np.array([[1, 0, 0],
                [0, np.cos(alpha2), -np.sin(alpha2)],
                [0, np.sin(alpha2),  np.cos(alpha2)]])
R2 = R1 @ Rz2 @ Rx2
O2 = O1 + R1 @ np.array([L1, 0, 0])
draw_frame(ax, O2, R2, '2')

# Frame 3: Translate along X2 by L2, alpha3 = -90
L2 = 40
alpha3 = -np.pi / 2
Rz3 = np.eye(3)
Rx3 = np.array([[1, 0, 0],
                [0, np.cos(alpha3), -np.sin(alpha3)],
                [0, np.sin(alpha3),  np.cos(alpha3)]])
R3 = R2 @ Rz3 @ Rx3
O3 = O2 + R2 @ np.array([L2, 0, 0])
draw_frame(ax, O3, R3, '3')

# Set plot limits and labels
ax.set_xlim([-10, 120   ])
ax.set_ylim([-60, 60])
ax.set_zlim([-60, 60])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Kinematic Diagram Based on DH Parameters")
plt.tight_layout()
plt.show()
