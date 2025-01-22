# Machine Learning Algorithm Cheatsheet

## Introduction
This document is authored by Lani Lewis for educational learning reference.

This document serves as a quick reference for key machine learning algorithms and their use cases. It is designed for users to download and print for convenient offline access.

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [Machine Learning Algorithms Overview](#machine-learning-algorithms-overview)
    - 2.1 [Linear Regression](#linear-regression)
    - 2.2 [Logistic Regression](#logistic-regression)
    - 2.3 [Decision Trees](#decision-trees)
    - 2.4 [Random Forest](#random-forest)
    - 2.5 [Support Vector Machines (SVM)](#support-vector-machines-svm)
    - 2.6 [K-Nearest Neighbors (KNN)](#k-nearest-neighbors-knn)
    - 2.7 [Naïve Bayes](#naive-bayes)
    - 2.8 [Neural Networks](#neural-networks)
    - 2.9 [Gradient Boosting](#gradient-boosting)
    - 2.10 [Clustering Algorithms](#clustering-algorithms)
3. [Key Metrics](#key-metrics)
4. [Error Types](#error-types)
5. [Confusion Matrix and Metrics](#confusion-matrix-and-metrics)

---

## Getting Started
- Download and print this document for easy access while working on machine learning projects.
- Each section contains a concise summary of the algorithm, its use case, key parameters, output, and evaluation metrics.

---

## Machine Learning Algorithms Overview

### 2.1 Linear Regression
**Use Case:** Predicting continuous numerical outputs (e.g., housing prices).
- **Parameters:** Learning rate, regularization strength (L1 or L2).
- **Metrics:** MSE, RMSE, MAE, R-squared.

### 2.2 Logistic Regression
**Use Case:** Binary or multiclass classification (e.g., spam detection).
- **Parameters:** Regularization strength, multi-class options.
- **Metrics:** Accuracy, Precision, Recall, F1 Score, ROC-AUC Score.

### 2.3 Decision Trees
**Use Case:** Classification and regression tasks (e.g., customer segmentation).
- **Parameters:** Maximum depth, minimum samples per split, criterion.
- **Metrics:** Classification - Accuracy, F1 Score, Precision, Recall. Regression - MSE, RMSE, MAE.

### 2.4 Random Forest
**Use Case:** Reduces overfitting and improves decision trees (e.g., feature importance analysis).
- **Parameters:** Number of trees, maximum depth, minimum samples per leaf.
- **Metrics:** Similar to decision trees.

### 2.5 Support Vector Machines (SVM)
**Use Case:** Small datasets for classification and regression (e.g., image recognition).
- **Parameters:** Kernel, regularization parameter (C), gamma.
- **Metrics:** Accuracy, Precision, Recall, F1 Score, ROC-AUC Score.

### 2.6 K-Nearest Neighbors (KNN)
**Use Case:** Classification and regression with non-linear boundaries (e.g., recommendation systems).
- **Parameters:** Number of neighbors (k), distance metric.
- **Metrics:** Classification - Accuracy, F1 Score. Regression - MSE, MAE.

### 2.7 Naïve Bayes
**Use Case:** Text classification, spam detection, sentiment analysis.
- **Parameters:** Smoothing parameter.
- **Metrics:** Accuracy, Precision, Recall, F1 Score, ROC-AUC Score.

### 2.8 Neural Networks
**Use Case:** Complex tasks (e.g., image recognition, NLP).
- **Parameters:** Number of layers and neurons, learning rate, activation functions, regularization.
- **Metrics:** Classification - Accuracy, F1 Score, ROC-AUC. Regression - MSE, RMSE, MAE.

### 2.9 Gradient Boosting (e.g., XGBoost, LightGBM, CatBoost)
**Use Case:** Predictive analytics for classification and regression.
- **Parameters:** Learning rate, number of estimators, maximum depth.
- **Metrics:** Similar to decision trees.

### 2.10 Clustering Algorithms (e.g., K-Means, DBSCAN)
**Use Case:** Unsupervised learning for grouping data points (e.g., customer segmentation).
- **Parameters:** Number of clusters, epsilon and minimum samples (for DBSCAN).
- **Metrics:** Silhouette Score, Davies-Bouldin Index, Inertia (for K-Means).

---

## Key Metrics
- **Classification Metrics:** Confusion Matrix, Precision-Recall Curve, ROC Curve, Log Loss.
- **Regression Metrics:** Explained Variance, Mean Bias Deviation.
- **Unsupervised Learning Metrics:** Silhouette Coefficient, Dunn Index.

---

## Error Types
- **Type 1 Error (Alpha, α):** Rejecting the null hypothesis when it is true (false positive).
- **Type 2 Error (Beta, β):** Failing to reject the null hypothesis when it is false (false negative).

---

## Confusion Matrix and Metrics

| Actual \ Predicted | Positive (P)          | Negative (N)          |
|--------------------|-----------------------|-----------------------|
| **Positive (P)**   | True Positive (TP)    | False Negative (FN)   |
| **Negative (N)**   | False Positive (FP)   | True Negative (TN)    |

### Key Terms
- **True Positive (TP):** Correct positive predictions.
- **False Positive (FP):** Incorrect positive predictions (Type 1 Error).
- **True Negative (TN):** Correct negative predictions.
- **False Negative (FN):** Incorrect negative predictions (Type 2 Error).

### Metrics Formulas
- **Accuracy:**
- **Precision:**
- **Recall (Sensitivity):**
- **F1 Score:** Harmonic mean of precision and recall.
- **Specificity:** Proportion of true negatives out of all actual negatives.
