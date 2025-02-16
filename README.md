# ResumeMatchAI

An AI-powered tool to analyze the compatibility between resumes and job descriptions using natural language processing and machine learning

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The **ResumeMatchAI** is a tool that takes a job description and a resume as input and outputs a compatibility score. It uses pre-trained language models to compute text similarity and provides a simple web interface for users to upload PDFs and view results. This tool is designed to help job seekers to address their compatibility with a role, and help employers to select better candidates for a role.

## Features
- Converts PDFs (job descriptions and resumes) to text
- Preprocesses the text (removes special characters and stopwords)
- Computes compatibility scores using cosine similarity and pre-trained models.
- Provides a user-friendly interface using Streamlit.

## Installation
1. Clone the repository
```bash
$ git clone https://github.com/beatriz-farias/ResumeMatchAI.git
$ cd ResumeMatchAI
```
2. Install the dependencies
```bash
$ pip install -r requirements.txt
```

## Usage
Run the Streamlit app:

```bash
$ streamlit run app.py
```
2. Upload a job description and a resume in PDF format.
3. View the compatibility score.

## Project Structure
ResumeMatchAI/
├── app.py                     # Streamlit web app
├── requirements.txt           # List of dependencies
├── README.md                  # Project documentation
├── data/                      # Sample data (PDFs)
├── src/                       # Source code
│   ├── __init__.py            # Makes src a Python package
│   ├── pdf_to_text.py         # PDF-to-text conversion
│   ├── preprocess.py          # Text preprocessing
│   ├── similarity.py          # Text similarity computation
│   └── smart_classifier.py    # Main workflow
└── tests/                     # Unit tests
    ├── __init__.py
    ├── test_pdf_to_text.py    # Tests for PDF-to-text
    ├── test_preprocess.py     # Tests for preprocessing
    └── test_similarity.py     # Tests for similarity computation