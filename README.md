This is for the manuscript with Abraham Atsiwo titled 'Capital Asset Pricing Model with Size Factor and Normalizing by Volatility Index'. It is available on arXiv:2411.19444.

The file gaussian-simulation.py contains Python code to simulate whether the mean of the logarithm of normal random variable is negative. Namely, find the set of all m, s > 0 such that the normal random variable X with mean m and stdev s has negative expected value of the logarithm of |X|. This corresponds to Section 4. 

The file capital-distribution-simulation.py contains Python code to simulate the capital distribution curve for this market model. We simulate the volatility and the benchmark, and then we make four simulations of the capital distribution curve with two parameters each taking two values, total 2x2 = 4 simulations. We plot all 4 simulations in one graph. In Section 5, we included two such graphs: Run the code twice. 

The file standard-curve-simulation.py contains Python code to simulate the standard normal market curve, based on ranked standard normal sample. This was also done in Section 5. 



