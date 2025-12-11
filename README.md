# 🏦 Loan Approval Prediction Web App

[![Project Status](https://img.shields.io/badge/Status-Complete-brightgreen)](https://github.com/subhankarmaji12/Loan-Approval-Prediction-Web-App)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/subhankarmaji12/Loan-Approval-Prediction-Web-App/blob/main/LICENSE)
[![Built with Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io/)

A streamlined web application for predicting loan approvals, helping banks and financial institutions make data-driven, instantaneous decisions based on applicant profiles.

---

## 🚀 Demo

Watch the application in action:

[![App Demo GIF](https://github.com/subhankarmaji12/Loan-Approval-Prediction-Web-App/blob/main/assets/app.gif?raw=true)

---

## ✨ Features

This project integrates a robust machine learning backend with an intuitive web interface:

* *Real-Time Prediction:* Predict loan approval status by inputting various customer details through the web interface.
* *Machine Learning Model:* Utilizes *Logistic Regression* for high-accuracy binary classification (Approved/Rejected).
* *Data Preprocessing Pipeline:* Includes a trained scaler.pkl to ensure that new input data is properly normalized before prediction.
* *Interactive UI:* User-friendly interface built with *Streamlit, featuring dynamic visual feedback and **Lottie* animations for approved/rejected outcomes.
* *Web Deployment Ready:* Designed for easy local testing and future cloud deployment.

---

## 🛠️ Technologies Used

The application is built primarily using the Python data science and web development ecosystem.

| Component | Technology | Role |
| :--- | :--- | :--- |
| *Backend* | Python 3.x | Core programming language |
| *Web Framework* | Streamlit | Creating the interactive web application |
| *Machine Learning* | Scikit-learn | Model training, preprocessing, and serialization |
| *Data Handling* | Pandas | Dataset management and analysis |
| *Visual Assets* | Lottie | Eye-catching animations for user feedback |

---

## 🧠 Model Insights

The core of the prediction service is a trained Logistic Regression model.

* *Algorithm Used:* Logistic Regression
* *Accuracy Achieved:* *90.52%* on the test dataset
* *Key Predictive Features:* The model considers a variety of factors to determine loan eligibility, including:
    * Number of Dependents
    * Education Level
    * Employment Status
    * Annual Income
    * Loan Amount
    * Loan Term
    * CIBIL Score
    * Total Assets

---

📂 Project Structure

    ├── dataset/
    │ └── loan_approval_dataset.csv - Dataset for training and testing the model
    ├── assets/
    │ ├── approved.json - Lottie animation for approved loans
    │ └── rejected.json - Lottie animation for rejected loans
    ├── app.py - Streamlit web application
    ├── Loan_Approval_Pred_Model.ipynb - Jupyter notebook for model development
    ├── model.pkl - Trained machine learning model
    ├── scaler.pkl - StandardScaler for data normalization
    ├── requirements.txt - Project dependencies
    └── README.md - Project documentation
  🛠️ How to Run the App

  Clone the Repository:

    git clone https://github.com/subhankarmaji12/Loan-Approval-Prediction-Web-App.git
    cd Loan-Approval-Prediction-Web-App/

Install Dependencies:

    pip install -r requirements.txt

Run the Application:

    streamlit run app.py

Interact with the App:

Open the provided URL (usually http://localhost:8501) in your browser.
Input customer details to predict loan status dynamically.

🧠 Model Insights

    Algorithm Used: Logistic Regression
    Accuracy Achieved: 90.52% on the test dataset
    Key Features:
        Number of Dependents
        Education Level
        Employment Status
        Annual Income
        Loan Amount
        Loan Term
        CIBIL Score
        Total Assets

🎥 Demo

[![image alt](https://github.com/subhankarmaji12/Loan-Approval-Prediction-Web-App/blob/main/assets/app.gif?raw=true)](https://github.com/subhankarmaji12/Loan-Approval-Prediction-Web-App/blob/main/assets/app.gif?raw=true)

📌 Technologies Used

    Python: Data processing and model development
    Streamlit: Frontend web framework
    Scikit-learn: Machine learning model training
    Pandas: Dataset management and analysis
    Lottie: Eye-catching animations

❤️ Developed By

Subhnkar Maji

📬 Get in Touch

Have questions or suggestions? Feel free to reach out!

    📧 Email: subhankarmajiwork@gmail.com
    💼 LinkedIn: https://www.linkedin.com/in/subhankar-maji-7aba49238
    📄 License

This project is licensed under the MIT License. See the LICENSE file for more details.
⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!

If you found this project helpful, please give it a ⭐ on GitHub!
