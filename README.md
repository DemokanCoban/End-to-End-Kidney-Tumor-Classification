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
1. Set up IAM : Create a user, Attach policies: 
    -AmazonEC2ContainerRegistryFullAccess
    -AmazonEC2FullAccess

2. For the created user, go to Security credentials-> Access Keys-> create access key -> Select Command Line Interface and create & copy secret access key (optionally download your secret access key in .csv)

3. Set up ICR: 
    1. Create a repository, under general settings set a repository name. 
    2. Copy URI

4. Create EC2 instance:
    -Lauch instance-> Set name tag-> Select ubuntu VM-> Chose Instance type-> Create new key value pair->Under the network settings allow HTTP and HTTPS-> Set storage volume-> Launch the instance

    -Connect to the instance
    -In instance's CLI:
        ```bash
            curl -fsSL https://get.docker.com -o get-docker.sh
            sudo sh get-docker.sh
            sudo usermod -aG docker ubuntu
            newgrp docker
        ```
5. Configure EC2 as a self-hosted runner:
    -On your github repo, go to:
        Actions-> Runners-> New self-hosted runner-> select runner image as Linux-> copy and paste the commands under Download, Configure on the CLI->Enter the name of runner: self-hosted-> then run "./run.sh"
    
6. Setup Github Secrets:
    On Github, go to Settings-> Secrets and Variables-> Actions-> New repository secret-> and add the name and secret pairs as:
        -AWS_ACCESS_KEY_ID = aws_key_id (obtained in step 2 when setting security credentials)
        -AWS_SECRET_ACCESS_KEY = secret_access_key(obtained in step 2)
        -AWS_REGION = eu-central-1 (can be checked from the aws profile)
        -AWS_ECR_LOGIN_URI = uri(from step 3)
        -ECR_REPOSITORY_NAME = repo_name(from step 3)