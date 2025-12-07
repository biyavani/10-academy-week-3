# 10 Academy AI Mastery Week 3 - ACIS Insurance Analytics

## Project overview
This repository contains my work for the Week 3 challenge for AlphaCare Insurance Solutions (ACIS).  
The goal is to analyse historical car insurance claim data to:
- understand risk and profitability
- identify low risk customer segments
- support data driven premium and marketing decisions

## Tasks
- Task 1 - Git, GitHub, EDA and statistics
- Task 2 - Data Version Control (DVC)
- Task 3 - A/B hypothesis testing
- Task 4 - Statistical and machine learning modeling

## Repo structure

```text
.
├── .github/workflows/    # CI configuration
├── notebooks/            # Jupyter notebooks for analysis
├── scripts/              # Python scripts (EDA, helpers, etc)
├── src/                  # Reusable modules
├── tests/                # Unit tests
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

---
## Data and DVC

Raw data is stored in `data/raw` and is tracked with DVC.

To get the data after cloning:

```bash
pip install -r requirements.txt
dvc pull
