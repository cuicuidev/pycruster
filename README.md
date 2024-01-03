# PyCruster - Clustering made simple! 
---
The PyCruster project aims to enhance some of the Scikit-Learn functionality by
providing a set of tools to help with clustering problems. The main goal is to 
help developers and data scientists to make better decisions when choosing the 
clustering algorithms and their parameters, thus streamlining their daily workflow.

## Usage
---

### Installation

Install the package using pip:

```sh
pip install pycruster
```

Or, alternatively, you can compile the package from source:

```sh
python setup.py install
```

### Main features

_Elbow_ object:

This object wraps a KMeans estimator instance from SciKit-Learn and enables you to
quickly find the optimal number of clusters for your dataset. You need to pass the 
estimator instance and the X matrix to the object constructor. Then, you will be able 
to call the `fit()` method. Once the `fit()` method is called, the object will store the
inertia values for each number of clusters. This method returns the optimal number of 
clusters, which is the number of clusters that minimizes the inertia value. 

You can also call the `plot()` method to plot the inertia values for each number of 
clusters. This method will return a matplotlib figure object.

_Silhouette_ object:

This object wraps a KMeans estimator instance from SciKit-Learn and enables you to
quickly find the optimal number of clusters for your dataset. You need to pass the
estimator instance and the X matrix to the object constructor. Then, you will be able
to call the `fit()` method. Once the `fit()` method is called, the object will store the
silhouette values for each number of clusters. This method returns the optimal number of
clusters, which is the number of clusters that maximizes the silhouette value.

You can also call the `plot()` method to plot the silhouette values for each number of
clusters. This method will return a matplotlib figure object.

_GapStatistic_ object:

This object wraps a KMeans estimator instance from SciKit-Learn and enables you to
quickly find the optimal number of clusters for your dataset. You need to pass the
estimator instance and the X matrix to the object constructor. Then, you will be able
to call the `fit()` method. Once the `fit()` method is called, the object will store the
gap statistic values for each number of clusters. This method returns the optimal number of
clusters, which is the number of clusters that maximizes the gap statistic value.

You can also call the `plot()` method to plot the gap statistic values for each number of
clusters. This method will return a matplotlib figure object.
