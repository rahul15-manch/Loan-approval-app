#  💰LendIQ -Smart Loan Eligibility Predictor

A Machine Learning-based web application that predicts loan approval for applicants based on their financial and personal information. It helps individuals and financial institutions make quick, data-driven decisions.
## 📊 Dataset Used

**Source:** [Loan Approval Prediction Dataset (Kaggle)](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset)

---

| **Feature**                | **Datatype**   | **Description**                                                                 |
|-----------------------------|----------------|---------------------------------------------------------------------------------|
| Loan ID                     | Unique ID      | A unique identifier for each loan application                                   |
| No. of Dependents           | Integer        | Number of dependents of the applicant                                           |
| Education                   | Categorical    | Applicant’s education level (e.g., Graduate, Not Graduate)                      |
| Self Employed               | Categorical    | Whether the applicant is self-employed (Yes/No)                                 |
| Annual Income               | Integer        | Applicant’s total income per year                                               |
| Loan Amount                 | Integer        | Total loan amount requested by the applicant                                    |
| Loan Term (in months)       | Integer        | Duration of the loan in months                                                  |
| CIBIL Score                 | Integer        | Credit score of the applicant                                                   |
| Residential Assets Value    | Integer        | Value of the applicant’s residential property                                   |
| Commercial Assets Value     | Integer        | Value of commercial properties owned by the applicant                           |
| Luxury Assets Value         | Integer        | Value of luxury assets owned by the applicant (cars, jewelry, etc.)             |
| Bank Asset Value            | Integer        | Total value of bank deposits or liquid assets                                   |

---

🧠 *This dataset provides crucial financial and demographic information to predict loan approval outcomes using machine learning models.*



## 🔥 Features

- Predict loan approval using a trained ML model
- Real-time predictions based on user input
- User-friendly interface powered by Streamlit
- Scalable and easy to deploy

## 🛠️ Technologies Used

| Technology | Description |
|-------------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Core programming language for ML model and backend logic |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) | Web interface for real-time predictions |
| ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white) | Machine Learning modeling and evaluation |
| ![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) | Data processing and analysis |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) | Numerical computations and arrays |
| ![pickle](https://img.shields.io/badge/pickle-009688?style=for-the-badge&logo=python&logoColor=white) | Model serialization for deployment |




## 🚀 **Installation & Setup**


# Clone the repository
```
git clone <your-repo-link>
cd <repo-folder>
```
# Install dependencies
```
pip install -r requirements.txt
```
# Run the app
```
streamlit run app.py
```

# 📝Usage

- Fill in the applicant details:
   -  Dependents (Number of family members dependent on the applicant)
    
   -  Education (Graduate / Not Graduate)
    
   -  Self Employed (Yes / No)
    
   -  Annual Income (Applicant’s yearly income)
    
    - Loan Amount (Amount of loan requested)
    
   -  Loan Term (Loan tenure in months)
    
   -  CIBIL Score (Credit score)
    
   -  Residential Asset Value (Value of residential property)
    
    - Commercial Assets Value (Value of commercial property)
    
   -  Luxury Assets Value (Value of luxury assets)
    
    - Bank Asset Value (Savings or other bank assets) 
- Click Predict to see the loan approval result

The app displays: "Loan Approved" or "Rejected"

🔗 **Live Link** : https://loan-approval-app-rsofappgn752jfzdptfhzht.streamlit.app/

## 📬 Author

Rahul Manchanda

- 💼 LinkedIn: https://www.linkedin.com/in/rahul-manchanda-3959b120a/

Tanishka Mukhi 

- 💼 LinkedIn: https://www.linkedin.com/in/tanishka-mukhi09/


