"""
Alias class for creating alias table from a discrete distribution
"""
import numpy as np


class Alias:

    def __init__(self, dist):
        """ initiate class instance from discrete distribution

        Parameters
        ----------
        dist : a discrete distribution (list or array)
        """
        assert np.isclose(np.sum(dist), 1.0), "distribution must sum to 1.0"
        self.dist = dist
        if len(dist) > 1:
            self.table = self._create_table()
        else:
            self.table = [[0, 1]]

    def _create_table(self):
        """ creates the alias table """
        n = len(self.dist)
        alias_table = [[i, d*n] for i, d in enumerate(self.dist)]
        under = []
        over = []
        for b in alias_table:
            if b[1] > 1.0:
                over.append(b)
            if b[1] < 1.0:
                under.append(b)
        over = sorted(over, key=lambda x: x[1], reverse=True)
        under = sorted(under, key=lambda x: x[1])
        while under:
            to_fill = 1 - under[0][1]
            over[0][1] -= to_fill
            # change alias
            under[0][0] = over[0][0]
            # filled the bin
            under.pop(0)
            if np.isclose(over[0][1], 1.0):  # over bin is exactly full
                over[0][1] = 1.0  # float precision issues
                over.pop(0)
            elif over[0][1] < 1.0:
                under.append(over.pop(0))
        return alias_table

    def _sample(self):
        """ one random sample from the discrete distribution

        Returns
        -------
        One randomly drawn sample based on the alias table
        """
        ind = np.random.randint(len(self.dist))
        q = np.random.random()
        if q < self.table[ind][1]:
            return ind
        return self.table[ind][0]

    def sample(self, n=1):
        """ n random samples from the discrete distribution

        Parameters
        ----------
        n : number of samples

        Returns
        -------
        n randomly drawn sample based on the alias table """
        assert n > 0, "number of samples must be positive integer"
        samples = []
        for i in range(n):
            samples.append(self._sample())
        return samples


class C14Date(Alias):
    """ special class for randomly sampling from a C14 date distribution """
    def __init__(self, dist, years):
        """ initiate the alias table by calling the super class

        Parameters
        ----------
        dist : a discrete distribution (list or array)
        years : The years represented by the indices of the distribution
        """
        Alias.__init__(self, dist)
        self.years = years

    def sample_years(self, n=1):
        """ returns n randomly sampled years

        Parameters
        ----------
        n : The number of samples to return from the distribution (default n=1)
        Returns
        -------
        An array of randomly drawn samples based on the alias table,
        translated into years - can have repetition
        """
        return [self.years[i] for i in self.sample(n)]
