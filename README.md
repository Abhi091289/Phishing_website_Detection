# YSentry – Phishing Website Detection System

![CI](https://github.com/Abhi091289/Phishing_website_Detection)

A machine learning web application that detects phishing URLs in real time.

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Tech Stack](#tech-stack)
- [Model Details](#model-details)
- [System Workflow](#system-workflow)
- [Features](#features)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

---

## Overview

Phishing attacks are one of the most common cyber threats. YSentry analyzes the structural characteristics of a URL using machine learning to classify it as legitimate or malicious — before any damage is done.

---

## Getting Started

**Step 1 — Clone the repository**

```bash
git clone https://github.com/Abhi091289/Phishing_website_Detection.git
```

**Step 2 — Create and activate a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate


**Step 3 — Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4 — Run the application**

```bash
python app.py
```

Open your browser at `http://127.0.0.1:5000`

---

## Tech Stack

| Layer        | Technology                        |
|-------------|-----------------------------------|
| Language     | Python 3.10+                      |
| Web          | Flask                             |
| ML           | scikit-learn (Logistic Regression) |
| Data         | Pandas, NumPy                     |
| Vectorizer   | CountVectorizer (scikit-learn)    |

---

## Model Details

- **Algorithm:** Logistic Regression
- **Feature extraction:** Lexical analysis via tokenization and stemming of raw URLs, then converted to numerical vectors using `CountVectorizer`
- **Dataset:** 21,000+ labeled URLs
- **Test accuracy:** 96.4%

---

## System Workflow

1. User submits a URL through the web interface
2. The URL is cleaned and tokenized
3. The CountVectorizer converts it to a numerical feature vector
4. The Logistic Regression model classifies it as **Phishing** or **Legitimate**
5. The result is displayed and saved to a scan history (last 21 entries)

---

## Features

- Real-time URL classification
- Scan history (last 21 results)
- Fast, lightweight inference

---

## Future Enhancements

- Chrome / Edge browser extension for inline protection
- LSTM-based deep learning model
- Mobile API integration
- Live threat intelligence feed

---
