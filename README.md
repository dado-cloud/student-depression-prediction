# Student Depression Prediction Using Machine Learning

This project is a machine learning web application designed to predict the likelihood of student depression based on behavioral, academic, and demographic factors.

The goal of this project is to explore how data science and machine learning can support early mental health risk awareness among students. The system uses student-related information such as academic pressure, sleep duration, CGPA, dietary habits, financial stress, and family history of mental illness to generate a prediction through a simple and interactive web interface.

> **Disclaimer:** This project is for educational and research purposes only. It is not intended to provide medical diagnosis or replace professional mental health support.

---

## Project Overview

Student mental health is an important issue that can affect academic performance, social life, and overall well-being. This project applies machine learning techniques to analyze student data and predict depression risk.

The project follows the CRISP-DM methodology, including:

* Data understanding
* Data preprocessing
* Exploratory Data Analysis
* Feature encoding and scaling
* Model training
* Model evaluation
* Hyperparameter tuning
* Streamlit deployment

---

## Dataset

The project uses the **Student Depression Dataset** from Kaggle.

The dataset includes student behavioral, academic, and demographic features such as:

* Age
* Gender
* Academic pressure
* Sleep duration
* CGPA
* Dietary habits
* Financial stress
* Family history of mental illness
* Depression status

Dataset size:

* **27,901 rows**
* **15 features**

---

## Machine Learning Models

Several classification models were trained and compared:

* Logistic Regression
* Support Vector Machine
* Random Forest
* MLPClassifier

After applying hyperparameter tuning using **GridSearchCV**, the **Tuned MLPClassifier** achieved the best overall performance.

### Best Model Performance

| Model               | Accuracy |
| ------------------- | -------: |
| Tuned MLPClassifier |   0.8380 |

---

## Tools & Technologies

* Python
* Pandas
* Scikit-learn
* Streamlit
* Logistic Regression
* Support Vector Machine
* Random Forest
* MLPClassifier
* GridSearchCV
* MinMaxScaler
* Label Encoding
* Exploratory Data Analysis

---

## Project Workflow

1. Load and understand the dataset
2. Clean and preprocess the data
3. Handle categorical features using label encoding
4. Scale numerical features using MinMaxScaler
5. Perform exploratory data analysis
6. Train multiple machine learning models
7. Tune model parameters using GridSearchCV
8. Evaluate model performance
9. Deploy the final model using Streamlit

---

## Streamlit Web App

The final model was deployed as an interactive Streamlit application.

Users can enter student-related information through the app interface and receive a prediction result.

Main app features:

* User-friendly input form
* Depression prediction result
* Clean and simple interface
* Fast model inference

---

## Installation

Clone the repository:

```bash
git clone https://github.com/dado-cloud/student-depression-prediction.git
cd student-depression-prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## Repository Structure

```text
student-depression-prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── model.pkl
├── scaler.pkl
├── notebooks/
│   └── student_depression_analysis.ipynb
├── data/
│   └── student_depression_dataset.csv
└── assets/
    └── screenshots/
```

---

## Ethical Considerations

Because this project is related to mental health, ethical use is important.

This project considers:

* Data privacy
* Responsible use of predictions
* Avoiding harmful assumptions
* Reducing bias where possible
* Using the model as a support tool, not a medical diagnosis tool

The prediction result should only be used for awareness and educational purposes.

---

## Future Improvements

Possible improvements include:

* Adding model explainability using SHAP or LIME
* Improving class balance handling
* Testing additional models
* Adding more visualizations to the Streamlit app
* Deploying the app online
* Improving UI design and user experience

---

## Author

**Daad Alhassan**

GitHub: [@dado-cloud](https://github.com/dado-cloud)

---

## Keywords

Machine Learning, Student Depression Prediction, Mental Health Analytics, Streamlit, Python, Scikit-learn, Classification, MLPClassifier, Responsible AI
