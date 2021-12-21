import unittest
from banditpam import KMedoids
import pandas as pd
import numpy as np

from utils import *

class PythonTests(unittest.TestCase):
    mnist_70k = pd.read_csv("data/MNIST_70k.csv", sep=" ", header=None)
    print("Loaded MNIST")
    # scrna = pd.read_csv("data/scrna_reformat.csv.gz", header=None)
    # print("Loaded scRNA")

    def test_small_on_the_fly_mnist(self):
        """
        Generate 10 random subsets of MNIST of size 1000 
        and verify BanditPAM agrees with PAM
        """
        count = 0
        for i in range(NUM_LARGE_CASES):
            data = self.mnist_70k.sample(n=1000).to_numpy()
            count += on_the_fly(k=SMALL_K_SCHEDULE[i % N_SMALL_K], data=data, loss="L2")
        self.assertTrue(count == NUM_LARGE_CASES)

    # def test_large_on_the_fly_mnist(self):
    #     """
    #     Test 10 on-the-fly generated samples of 1000 datapoints from mnist-70k dataset
    #     Must get correct medoids on roughly 95% of cases
    #     """
    #     count = 0
    #     size_schedule = [1000, 2000, 3000, 4000, 5000]
    #     for i in range(NUM_LARGE_CASES):
    #         data = mnist_70k.sample(n=size_schedule[i % 5])
    #         count += on_the_fly(k=SMALL_K_SCHEDULE[i % N_SMALL_K], data=data, loss="L2")
    #     self.assertTrue(count == NUM_LARGE_CASES)

    # def test_time_cases_mnist(self):
    #     """
    #     Evaluate the n*log(n) scaling of the BanditPAM algorithm on MNIST datasets.
    #     """
    #     MNIST_10k = mnist_70k.head(10000).to_numpy()
    #     kmed1 = KMedoids(n_medoids=5, algorithm="BanditPAM")
    #     kmed1.fit(MNIST_10k, "L2")

    #     MNIST_schedule = [20, 40, 70]
    #     kmed2 = KMedoids(n_medoids=5, algorithm="BanditPAM")
    #     for num in MNIST_schedule:
    #         MNIST_test = mnist_70k.head(num * 1000).to_numpy()
    #         kmed2.fit(MNIST_test, "L2")
    #         self.assertTrue(kmed2.steps < ((num / 10) ** 1.2) * kmed1.steps)

    # def test_small_on_the_fly_scrna(self):
    #     """
    #     Test 10 on-the-fly generated samples of 1000 datapoints from scrna dataset
    #     Must get correct medoids on roughly 95% of cases
    #     """
    #     count = 0
    #     for i in range(NUM_LARGE_CASES):
    #         data = self.scrna.sample(n=1000).to_numpy()
    #         count += on_the_fly(k=SMALL_K_SCHEDULE[i % N_SMALL_K], data=data, loss="L1")
    #     self.assertTrue(count >= PROPORTION_PASSING*NUM_LARGE_CASES)

    # def test_large_on_the_fly_scrna(self):
    #     """
    #     Test 10 on-the-fly generated samples of 1000 datapoints from scrna dataset
    #     Must get correct medoids on roughly 95% of cases
    #     """
    #     count = 0
    #     size_schedule = [1000, 2000, 3000, 4000, 5000]
    #     for i in range(NUM_LARGE_CASES):
    #         data = scrna.sample(n=size_schedule[i % 5])
    #         count += on_the_fly(k=SMALL_K_SCHEDULE[i % N_SMALL_K], data=data, loss="L2")
    #     self.assertTrue(count >= PROPORTION_PASSING*NUM_LARGE_CASES)

    # def test_time_cases_scrna(self):
    #     """
    #     Evaluate the n*log(n) scaling of the BanditPAM algorithm on scRNA datasets.
    #     """
    #     SCRNA_10k = scrna.head(10000).to_numpy()
    #     kmed1 = KMedoids(n_medoids=5, algorithm="BanditPAM")
    #     kmed1.fit(SCRNA_10k, "L1")

    #     scrna_schedule = [20, 30, 40]
    #     kmed2 = KMedoids(n_medoids=5, algorithm="BanditPAM")
    #     for num in scrna_schedule:
    #         scrna_test = scrna.head(num * 1000).to_numpy()
    #         kmed2.fit(scrna_test, "L1")
    #         self.assertTrue(kmed2.steps < ((num / 10) ** 1.2) * kmed1.steps)

if __name__ == "__main__":
    unittest.main()
