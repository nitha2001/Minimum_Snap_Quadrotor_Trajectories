# Minimum_Snap_Quadrotor_Trajectories
This project focuses on formulating a minimum snap trajectory optimization problem for a planar quadrotor system. The goal is to generate efficient trajectories between given waypoints while minimizing snap, ensuring smooth transitions and compliance with dynamic constraints.

## Code Implementation

**Constraints**
- Positional Constraints: Implemented functions in pos_constraints.py to derive linear constraints from waypoint conditions.
- Continuity Constraints: Extended the continuity conditions using AddLinearEqualityConstraint in minsnap.py to ensure smooth transitions between polynomial segments.
**Cost Function**
- Derived the cost associated with minimizing snap and implemented it in add_minsnap_cost() within minsnap.py, utilizing AddQuadraticCost().
**Quadratic Program Structure**
- Formulated the overall minimum snap optimization problem

## Files Included
- `pos_constraints.py`: Contains functions for deriving positional and continuity constraints.
- `minsnap.py`: Implements the minimum snap trajectory optimization, including cost and constraint definitions.
Additional scripts and documentation for running the project and visualizing results.
 
## Results
Executed the complete optimization procedure and visualized the resulting trajectory, confirming smooth transitions between waypoints while adhering to constraints.

![download](https://github.com/user-attachments/assets/fb2d2090-c451-475b-9099-63ed1905ce73)
![download](https://github.com/user-attachments/assets/2e8b848e-81c9-401a-9b64-507da0530995)
![download](https://github.com/user-attachments/assets/73f76714-8efe-4e22-a854-0c2e647fa94d)
![download](https://github.com/user-attachments/assets/7af28ce4-a04d-4007-ab93-f8541ae32b31)
![download](https://github.com/user-attachments/assets/08cc43b3-cbb1-4593-999b-ba83c8edcb27)
