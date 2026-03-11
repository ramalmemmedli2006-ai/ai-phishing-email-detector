# AI-Powered Phishing Email Detector

A Python-based phishing email detection tool that analyzes email text and predicts whether it is phishing or legitimate using machine learning and rule-based checks.

## Author
Ramal Memmedli  
IT Student | Network | Cybersecurity | Helpdesk | System Administration

---

## Project Overview

AI-Powered Phishing Email Detector is a practical cybersecurity project designed to analyze email content for phishing indicators.

This project is useful for:
- Cybersecurity portfolio building
- Email threat analysis practice
- Learning machine learning for security
- Demonstrating phishing detection logic

---

## Features

- Detect phishing emails using machine learning
- Analyze suspicious keywords and urgent language
- Identify risky URLs and common scam patterns
- Predict email risk score
- CLI-based testing interface
- Rule-based + AI-based hybrid detection

---

## Tech Stack

- Python
- Scikit-learn
- Pandas
- Joblib
- Regex

---

## Project Structure

```text
ai-phishing-email-detector/
├── README.md
├── requirements.txt
├── main.py
├── train_model.py
├── model/
│   └── phishing_model.pkl
├── data/
│   └── sample_emails.csv
├── detector/
│   ├── preprocess.py
│   ├── features.py
│   ├── predictor.py
│   └── rules.py
└── output/
