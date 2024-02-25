# loan prediction machine learning model

## Project Overview:

This project seamlessly integrates the power of SQL for data manipulation, harnesses the insights derived from Exploratory Data Analysis (EDA), and employs cutting-edge modeling techniques to ensure accuracy and reliability.
Loans are the core business of banks. The main profit comes directly from the loan’s interest. The loan companies grant a loan after an intensive process of verification and validation.

## Table of Contents:
- Understanding the Data
- Data Exploration
- Import data to python
- Data Preprocessing and Feature Engineering
- Modeling and Evaluation
- Modeling and Evaluation
- key highlights 
- Conclusion

### Understanding the Data:

Before coding, understanding the business goal is crucial. In banking, the aim is to predict loan defaults and pinpoint key predictors. This approach ensures focused model development, resource efficiency, and the identification of impactful features for better predictions and strategic decisions.

### Data Exploration:
There are totally eight datasets where each of the dataset contains different information and can be connected together, the realtion is provided below,

<![relations](https://github.com/Stanitaa/loan-prediction-machine-learning-model/assets/152231834/6a6f31e2-5920-4ef8-a529-0e770b273412)>

While it's possible to join all tables for a comprehensive dataset, our primary focus should align with the business goal of predicting loan status. Therefore, the loan table takes precedence.

To enhance predictive capabilities, I conducted case analyses on individual tables and performed feature transformations. Specifically, for the transaction table, I extracted valuable insights such as the number of orders, the latest transaction date, the count of each operation type, and the average transaction amount for each type. This approach ensures a targeted exploration of features, optimizing our efforts towards predicting loan status effectively

### Import data to python: 
 set up the connection between MySQL and python.

### Data Preprocessing and Feature Engineering: 
In this task, our response variable is the 'Status' column, which consists of four characters representing different meanings. To focus on predicting customers more likely to default, I assigned values: A and C to 0, and B and D to 1.

Addressing duplicate values in the 'account_id' column, considering multiple transactions on the same day, I calculated the average balance and removed duplicates, as the exact date-time of these transactions wasn't available.

With a dataset of 682 records, I split it into 80% training data and 20% testing data using train/test split. Checking for missing values revealed two columns with gaps: 'collection_from_another_bank_amount' and 'credit_card_withdrawal_amount.' Recognizing that these missing values might indicate no transactions for that account, I imputed them with zeros.

While the class sizes weren't extremely imbalanced, I employed SMOTE to balance them further. SMOTE (Synthetic Minority Over-sampling Technique) is used to increase the size of the minority class by creating synthetic samples. This step aims to enhance the model's performance by addressing potential class imbalances and evaluating if it leads to any improvement in predictive capabilities

### Modeling and Evaluation:

In our analysis, we focused on a relatively modest dataset, employing two algorithms – Random Forest and Logistic Regression. Utilizing 10-fold cross-validation, we aimed to compare the accuracy of these models and predict customers more likely to default.

Before applying any sampling techniques, the Random Forest model exhibited an accuracy of 0.91. However, after implementing SMOTE to address class imbalances, the accuracy improved to 0.95. Notably, the model identified a customer with 'account_id' equal to 1244 as having a 100% chance of default.

Contrastingly, the Logistic Regression accuracy witnessed a significant drop from 0.90 to 0.78 after resampling the data using SMOTE. This highlights an important nuance – increasing the dataset size through resampling might not always lead to enhanced accuracy. It underscores the necessity to carefully evaluate the impact of resampling techniques on different models and consider their implications on overall predictive performance.

## Key Highlights:

SQL Expertise: Dive into the world of SQL, where data manipulation and extraction are elevated to an art form. Learn to leverage the full potential of SQL to preprocess and transform raw data, setting the foundation for a robust predictive model.

Exploratory Data Analysis (EDA): Uncover hidden patterns and valuable insights as we embark on a data exploration journey. Through visually rich EDA, gain a deep understanding of the dataset, paving the way for informed feature selection and engineering.

Modeling Mastery: Harness the power of advanced modeling techniques to construct a predictive framework for loan default. From traditional algorithms to state-of-the-art machine learning models, delve into the nuances of model selection, fine-tuning, and evaluation.

End-to-End Implementation: Seamlessly integrate each phase of the project to witness the evolution from raw data to a sophisticated classification model. Experience the satisfaction of seeing your insights come to life as a practical and actionable solution.

## Conclusion:

The Determining the threshold for identifying customers more likely to default depends on specific business requirements. While a general threshold like 0.5 is common, it's crucial to tailor it based on the business context. Focusing on customers with a probability exceeding 50% of defaulting might be a reasonable starting point.

Furthermore, the balance of each customer emerges as a key predictor in assessing the likelihood of default. Companies should prioritize monitoring and managing customer balances, recognizing its significance in predicting default risk. This nuanced approach ensures a more accurate and targeted strategy in identifying and addressing potential default scenarios.
