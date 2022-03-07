# HCP Resource Limits

HCP has resource limits that need to be accounted for during tests. In
particular, we are limited to:

- 3 HVNs
- 3 Vault Clusters

To account for this, we will _not_ run tests in parallel (defined in
[examples_test.go](./examples_test.go)), but _will_ parallelize by
language runtime in Buildkite (see
[pipeline.verify.yml](../.buildkite/pipeline.verify.yml).
