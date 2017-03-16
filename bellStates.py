import numpy as np

def generate_CHSH_pairs(n, theta1 = np.pi, theta2 = 0, printProbDist = False):
    """
    Generates n pairs of eigenstates based off Operator O
    composed of 0_theta1  and 0_theta2
    """
    p11 = pn1n1 = np.cos(theta1/2.0 - theta2/2.0)
    p1n1 = pn11 = np.sin(theta1/2.0 - theta2/2.0)
    prob_dist = np.square(np.array([p11, p1n1, pn11, pn1n1]))/2.0
    choice = np.random.choice(4, n, p=prob_dist)
    poss_states = np.array([(1,1), (1,-1), (-1,1), (-1,-1)])
    if(printProbDist):
        print(prob_dist)
    return poss_states[choice]

def pair_v_to_prod_v(pair_v):
    """
    Converts vector of shape n by m first to a vector of
    m by n (using .transpose()), and then returns the vector
    of length n containing the product.
    """
    return np.prod(pair_v.transpose(), axis=0)



def generate_ensemble_A(n, phi2shift):
    return generate_CHSH_pairs(n, theta1 = 0, theta2 = phi2shift + (np.pi / 4.0))

def generate_ensemble_B(n, phi2shift):
    return generate_CHSH_pairs(n, theta1 = 0, theta2 = phi2shift + (np.pi / -4.0))

def generate_ensemble_C(n, phi2shift):
    return generate_CHSH_pairs(n, theta1 = np.pi / 2.0, theta2 = phi2shift + (np.pi / 4.0))

def generate_ensemble_D(n, phi2shift):
    return generate_CHSH_pairs(n, theta1 = np.pi / 2.0, theta2 = phi2shift + (np.pi / -4.0))


def generate_correlator(n, phi2shift):
    """
    Simulates 4 seperate ensembles A, B, C, D built using angle phi
    n times, and sums the resulting pair products according to CHSH
    Specification.
    """
    ave_A = np.average(pair_v_to_prod_v(generate_ensemble_A(n, phi2shift)))
    ave_B = np.average(pair_v_to_prod_v(generate_ensemble_B(n, phi2shift)))
    ave_C = np.average(pair_v_to_prod_v(generate_ensemble_C(n, phi2shift)))
    ave_D = np.average(pair_v_to_prod_v(generate_ensemble_D(n, phi2shift)))
    return ave_A + ave_B + ave_C - ave_D
