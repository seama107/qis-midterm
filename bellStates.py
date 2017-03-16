import numpy as np

def generate_CHSH_pairs(n, theta1 = np.pi, theta2 = 0):
    u = np.cos(theta1/2.0 - theta2/2.0)
    v = np.sin(theta1/2.0 - theta2/2.0)
    prob_dist = np.square(np.array([u, v, v, u]))/2.0
    choice = np.random.choice(4, n, p=prob_dist)
    poss_states = np.array([(1,1), (1,-1), (-1,1), (-1,-1)])
    return poss_states[choice]

def pair_v_to_prod_v(pair_v):
    out = np.zeros(len(pair_v))
    for i in range(len(pair_v)):
        out[i] = np.prod(pair_v[i])
    return out

def generate_ensemble_A(n):
    return generate_CHSH_pairs(n, theta1 = 0, theta2 = np.pi / 4.0)

def generate_ensemble_B(n):
    return generate_CHSH_pairs(n, theta1 = 0, theta2 = np.pi / -4.0)

def generate_ensemble_C(n):
    return generate_CHSH_pairs(n, theta1 = np.pi / 2.0, theta2 = np.pi / 4.0)

def generate_ensemble_D(n):
    return generate_CHSH_pairs(n, theta1 = np.pi / 2.0, theta2 = np.pi / -4.0)


n_0 = 100000
print(pair_v_to_prod_v(generate_ensemble_A(n_0)))
ave_A = np.average(pair_v_to_prod_v(generate_ensemble_A(n_0)))
ave_B = np.average(pair_v_to_prod_v(generate_ensemble_B(n_0)))
ave_C = np.average(pair_v_to_prod_v(generate_ensemble_C(n_0)))
ave_D = np.average(pair_v_to_prod_v(generate_ensemble_D(n_0)))
total = ave_A + ave_B + ave_C + ave_D

print("Average A: %f, Average B: %f, Average C: %f, Average D: %f" % (ave_A, ave_B, ave_C, ave_D))
print("Sum: %f" % (total))
