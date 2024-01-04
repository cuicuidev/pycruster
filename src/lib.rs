use pyo3::prelude::*;

#[pyclass]
struct Elbow {
    estimator: PyObject,
    X: Vec<Vec<f64>>,

    elbow: u8
}

#[pymethods]
impl Elbow {
    fn new(estimator: PyObject, X: Vec<Vec<f64>>) -> Self {
        Elbow { estimator, X, elbow: 0 }
    }

    fn _run_kmeans(&self, n_clusters: usize) -> PyResult<f64> {
        let estimator = self.estimator.call_method1("_run_kmeans", (n_clusters,))?;
        let inertia = estimator.getattr("inertia_")?.extract::<f64>()?;
        Ok(inertia)
    }

    fn _fit(&self, min_k: usize, max_k: usize) -> PyResult<Vec<f64>> {
        let mut inertias = Vec::new();
        for k in min_k..=max_k {
            let inertia = self._run_kmeans(k)?;
            inertias.push(inertia);
        }
        Ok(inertias)
    }

    fn _compute_elbow(&self, min_k: usize, max_k: usize) -> PyResult<u8> {
        let inertias = self._fit(min_k, max_k)?;
        let mut elbow = 0;
        let mut min_diff = 0.0;
        for (i, inertia) in inertias.iter().enumerate() {
            if i == 0 {
                continue;
            }
            let diff = inertias[i - 1] - inertia;
            if diff > min_diff {
                elbow = i as u8;
                min_diff = diff;
            }
        }
        Ok(elbow)
    }

    fn fit(&mut self, min_k: usize, max_k: usize) -> PyResult<()> {
        self.elbow = self._compute_elbow(min_k, max_k)?;
        Ok(())
    }
}

#[pymodule]
fn pycruster(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Elbow>()?;
    Ok(())
}
