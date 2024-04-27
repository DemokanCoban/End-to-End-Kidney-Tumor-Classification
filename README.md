# Running the App:

### Step 0: Clone the repo

```bash
https://github.com/DemokanCoban/End-to-End-Kidney-Tumor-Classification
```
### Step 1: Create a conda environment

```bash
conda create -n env_name python=3.8 -y
```

```bash
conda activate env_name
```

### Step 2: Install the requirements
```bash
pip install -r requirements.txt
```

### Step 3: MLFlow, export your own environment variables for DagsHub
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/username/repo-name.mlflow
export MLFLOW_TRACKING_USERNAME=your_username
export MLFLOW_TRACKING_PASSWORD=your_password
```

### Step 4: DVC
tracking the changes in the pipeline
```bash
dvc init
dvc repro
```

### Step 5: AWS & CI/CD WITH GITHUB ACTIONS