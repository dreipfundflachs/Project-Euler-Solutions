#################################
#  PROJECT EULER - PROBLEM 088  #
#################################
import time


def generate_products(curr_prod: int, d: int, factors: list[int]) -> list[int]:
    global min_sum_prod
    new_products = []
    for k in factors:
        new_prod = factor * curr_prod
        if new_prod < C:
            new_products.append(curr_prod)
            min_sum_prods[curr_prod] =\
                    min(mini_sum_prods[curr_prod], d + (curr_prod - d))
    return new_products


start = time.time()

N = 15
products = {}
number_of_factors = 0
product = 1
while number_of_factors < 10:
    for i in range(15):





end = time.time()
print(f"Program runtime: {end - start} seconds")
