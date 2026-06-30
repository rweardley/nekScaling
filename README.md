# nekScaling

This repo contains cases for NekRS strong and weak scaling runs, as well as utilities for setting up and postprocessing these runs.

## pyscaling

Included in this repo is a python package containing utilities for scaling plots. The recommended installation method for this package is to create a virtual environment

```python -m venv venv```

This environment can be activated with

```source venv/bin/activate```

To install the package in the virtual environment, navigate to `utils` with the environment active, and run

```pip install .```

This can instead be installed in development mode using `pip install -e `, to allow the user to modify this package without needing to reinstall it after each change.

## Workflow

Cases which can be used for scaling runs can be found in `cases`. HPC scaling runs should be set up in `hpc_runs`, with a directory created in there for each HPC architecture.