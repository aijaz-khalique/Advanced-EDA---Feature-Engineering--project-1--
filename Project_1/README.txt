# E-Commerce Data Cleaning and Preprocessing using Python

## 📌 Project Overview

This project demonstrates the complete data cleaning and preprocessing workflow for an e-commerce sales dataset using **Python** and **Pandas**.

The goal is to prepare raw data for further analysis and machine learning by handling missing values, checking data quality, detecting outliers, creating new features, and exporting a cleaned dataset.

---

## 🚀 Features

- Load and inspect the dataset
- Display dataset information
- Check missing values
- Identify duplicate records
- Analyze categorical columns
- Generate statistical summaries
- Detect outliers using the **Interquartile Range (IQR)** method
- Handle missing coupon codes
- Convert date column to datetime format
- Create new features:
  - Discount Applied
  - Order Month
  - Order Value Category
- Export the cleaned dataset as a new CSV file

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas

---

## 📂 Dataset

The dataset contains e-commerce order information, including:

- Order Date
- Product
- Quantity
- Unit Price
- Total Price
- Payment Method
- Order Status
- Coupon Code
- Referral Source
- Items in Cart

---

## 📋 Data Cleaning Steps

### 1. Data Exploration

The project begins by exploring the dataset using:

- `head()`
- `shape`
- `columns`
- `dtypes`
- `info()`
- `describe()`

---

### 2. Missing Values

The project checks missing values in every column.

Missing values in the **CouponCode** column are replaced with:

```
Not Applied
```

---

### 3. Duplicate Records

Duplicate rows are identified using:

```python
Data.duplicated().sum()
```

---

### 4. Outlier Detection

Outliers are detected for the following numerical columns:

- Quantity
- UnitPrice
- ItemsInCart
- TotalPrice

The **Interquartile Range (IQR)** method is used.

---

### 5. Feature Engineering

Three new features are created.

### Discount Applied

Determines whether a coupon was used.

| Coupon Code | Discount Applied |
|-------------|------------------|
| Not Applied | NO |
| Any Coupon | YES |

---

### Order Month

Extracts the month name from the order date.

Example:

```
January
February
March
```

---

### Order Value Category

Orders are classified into three categories.

| Total Price | Category |
|--------------|----------|
| Less than 1000 | Low |
| 1000–2000 | Medium |
| Greater than 2000 | High |

---

### 6. Export Cleaned Dataset

The processed dataset is saved as:

```
cleaned_dataset.csv
```

---

## 📁 Project Structure

```
E-Commerce-Data-Cleaning/
│
├── DatasetforDataAnalytics.csv
├── cleaned_dataset.csv
├── data_cleaning.py
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/aijaz-khalique/Decode_Lab_Internship/tree/main/Project_1
```

2. Install the required library.

```bash
pip install pandas
```

3. Update the dataset path in the Python script if necessary.

4. Run the script.

```bash
python data_cleaning.py
```

---

## 📈 Output

The script produces:

- Dataset summary
- Missing value report
- Duplicate record count
- Outlier detection results
- Feature engineered dataset
- Cleaned CSV file

---

## 🎯 Learning Outcomes

Through this project, I practiced:

- Data cleaning
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Missing value handling
- Duplicate detection
- Outlier detection using IQR
- Feature engineering
- Working with dates in Pandas
- Exporting processed datasets

---

## 👨‍💻 Author

**Aijaz Khalique**

BS Data Science Student  
Ghulam Ishaq Khan Institute (GIKI)

---

