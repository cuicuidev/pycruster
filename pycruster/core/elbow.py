import numpy as np

class Elbow:

    def __init__(self, estimator, X) -> None:
        
        # Parameters
        self.estimator = estimator
        self.X = X

        assert hasattr(self.estimator, 'n_clusters'), 'estimator must have n_clusters attribute.'
        assert hasattr(self.estimator, 'fit'), 'estimator must have fit method.'

        assert isinstance(self.X, np.ndarray), 'X must be a numpy array.'

        # Attributes
        self.inertia = np.array([])
        self._elbow_point = None
        self._raw_elbow_point = None

        return

    def fit(self, min_clusters = 2, max_clusters = 10) -> None:

        if min_clusters < 2:
            raise ValueError(f'min_clusters must be greater than 1. Got {min_clusters=}.')
        if max_clusters < 2:
            raise ValueError(f'max_clusters must be greater than 1. Got {max_clusters=}.')
        if min_clusters > max_clusters:
            raise ValueError(f'min_clusters must be less than max_clusters. Got {min_clusters=}, {max_clusters=}.')

        # Clear state
        self._clear_state()

        # Fit estimator
        for i in range(min_clusters, max_clusters+1):
            self.estimator.n_clusters = i
            self.estimator.fit(self.X)
            self.inertia = np.append(self.inertia, self.estimator.inertia_)

        return self.get_elbow_point(False, min_clusters)

    def get_elbow_point(self, raw: bool = False, min_clusters: int = 2) -> int:
        if self.elbow_point is None:
            self._find_elbow_point(raw, min_clusters)

        return self._elbow_point

    def _find_elbow_point(self, raw: bool, min_clusters: int) -> None:
        """
        Finds the point (a, b) closest to the origin, where a is the number of clusters and b is the inertia, both normalized.
        Sets the elbow_point attribute as b, which is the optimal number of clusters.
        """

        # Normalize inertia
        inertia = self.inertia if raw else self.inertia / self.inertia.max()

        # Find elbow point
        elbow_point = np.argmin(np.sqrt(inertia**2 + (np.arange(len(inertia))/len(inertia))**2))
        self._elbow_point = elbow_point + min_clusters

        return

    def _clear_state(self) -> None:
        self.inertia = np.array([])
        self.elbow_point = None

        return
