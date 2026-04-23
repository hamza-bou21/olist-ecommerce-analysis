# Olist E-Commerce Analysis

## Overview
Exploratory data analysis of the Olist Brazilian E-Commerce dataset, covering 99,000+ orders placed between September 2016 and October 2018.

The goal of this project is to uncover actionable insights around customer satisfaction, delivery performance, and product category trends.

## Dataset
- Source: [Olist E-Commerce Dataset — Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- 9 tables, 100,000+ orders, 2 years of data
- Covers customers, orders, payments, reviews, products and sellers

## Key Findings

### 1. Late deliveries are the #1 driver of poor reviews
Orders arriving even slightly late (0–10 days) drop from an average score of 4.16 to 2.50. Orders 10+ days late average just 1.71 — effectively a 1–2 star experience.

### 2. Bed, bath & table is the most ordered category
Followed by health & beauty and sports & leisure. Olist's strength is in everyday home and lifestyle products.

### 3. Olist was in strong growth through 2016–2018
Monthly orders grew consistently, with a clear Black Friday peak in November 2017 exceeding 8,000 orders in a single month.

### 4. Furniture categories have the worst satisfaction despite high volume
Office furniture averages just 3.55 stars. Bulky items are harder to deliver intact and on time — directly connecting to Finding 1.

## Project Structure
olist-ecommerce-analysis/
├── data/
│   └── raw/          ← original Kaggle CSVs (not tracked by git)
├── notebooks/
│   ├── 01_data_overview.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_exploratory_analysis.ipynb
├── outputs/          ← charts and exports (not tracked by git)
└── README.md

## Tools Used
- Python (pandas, matplotlib, seaborn)
- Jupyter Notebooks via VS Code
- Git & GitHub