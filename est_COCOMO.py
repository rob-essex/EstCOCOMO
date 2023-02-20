"""Derives a work estimate from anticipated lines of code
and constants impacting productivity using the intermediate COCOMO methodology.

Constants taken from https://www.geeksforgeeks.org/software-engineering-cocomo-model/"""

import math

# constants for different types of software projects
a = float(input("Enter the first complexity constant. Common benchmarks are 2.4 for Organic,"
          " 3.0 for semi-detached, 3.6 for embedded: "))
b = float(input("Enter the second complexity constant: 1.05 for Organic, 1.12 for semi-detached, 1.2 for embedded: "))
ksloc = float(input("Enter the number of thousands of lines of code (KSLOC): "))

# factors for the product, platform, project, and personnel skill level
factors = [1,1,1,1]

factors[0] = float(input("Input the percentage rating of product complexity (100 is average): "))/100
factors[1] = float(input("Input the percentage rating of platform complexity (100 is average): "))/100
factors[2] = float(input("Input the percentage rating of project complexity (100 is average): "))/100
factors[3] = float(input("Input the skill level rating of personnel involved (100 is average): "))/100
2
# establish overall constant for factors
factor_coeff = factors[0] * factors[1] * factors[2] * factors[3]

# application of basic COCOMO formula with intermediate factors
def estimate_effort(ksloc, factor_coeff):
    effort = a * math.pow(ksloc, b) * factor_coeff
    return effort

effort = estimate_effort(ksloc, factor_coeff)

print("Estimated effort for ", ksloc, " KSLOC is ", round(effort, 2), " labour-months.")
