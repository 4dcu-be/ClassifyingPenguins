import pymc3 as pm
import numpy as np

def run_model(data, n_clusters, samples=4000):
    print(f"Building model with {n_clusters} cluster and {samples} samples.")

    n_observations, n_features = data.shape
    with pm.Model() as model:
        chol, corr, stds = pm.LKJCholeskyCov(
            "chol",
            n=n_features,
            eta=2.0,
            sd_dist=pm.Exponential.dist(1.0),
            compute_corr=True,
        )
        cov = pm.Deterministic("cov", chol.dot(chol.T))
        μ = pm.Normal(
            "μ", 0.0, 1.5, shape=(n_clusters, n_features), testval=data.mean(axis=0)
        )

        p = pm.Dirichlet("p", a=np.ones(n_clusters))
        category = pm.Categorical("category", p=p, shape=n_observations)

        obs = pm.MvNormal("obs", μ[category], chol=chol, observed=data)

        trace = pm.sample(samples)
    return model, trace