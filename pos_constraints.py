import numpy as np

def Ab_i1(i, n, d, dt_i, w_i, w_ip1):
  '''
  Ab_i1(i, n, d, dt_i, w_i, w_ip1) computes the linear equality constraint
  constants that require the ith polynomial to meet waypoints w_i and w_{i+1}
  at it's endpoints.
  Parameters:
     i - index of the polynomial.
     n - total number of polynomials.
     d - the number of terms in each polynomial.
     dt_i - Delta t_i, duration of the ith polynomial.
     w_i - waypoint at the start of the ith polynomial.
     w_ip1 - w_{i+1}, waypoint at the end of the ith polynomial.
  Outputs
     A_i1 - A matrix from linear equality constraint A_i1 v = b_i1
     b_i1 - b vector from linear equality constraint A_i1 v = b_i1
  '''

  A_i1 = np.zeros((4, 2*d*n))
  b_i1 = np.zeros((4, 1))
  print("i is", i)

  for m in range(0, 2*d*n, 2):
      for j in range(d-1):
          if m == 2*d*i:
            A_i1[0, m] = 1
            A_i1[1, m+1] = 1
          if m >= 2*d*i and m < 2*d*(i+1):
            A_i1[2, m] = dt_i ** j
            A_i1[3, m+1] = dt_i ** j

  # Set the corresponding values in b_i to ensure continuity
  b_i1[0] = w_i[0]  # x-coordinate of the waypoint at the start
  b_i1[1] = w_i[1]  # y-coordinate of the waypoint at the start
  b_i1[2] = w_ip1[0]  # x-coordinate of the waypoint at the end
  b_i1[3] = w_ip1[1]  # y-coordinate of the waypoint at the end

  print(A_i1,b_i1)
  return A_i1, b_i1



