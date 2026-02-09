# Customer Segmentation with RFM and K-Means

## 📌 Project Overview

This project focuses on customer segmentation using RFM analysis (Recency, Frequency, Monetary) combined with K-Means clustering.
The goal is to group customers based on their purchasing behavior in order to identify valuable segments such as loyal customers, champions, or inactive users.

The project covers the full machine learning lifecycle, from data preprocessing and feature engineering to model training and deployment as a REST API.

The project includes:

- Data cleaning and preprocessing

- Feature engineering using RFM metrics

- Unsupervised learning with K-Means

- Model persistence (scaler and clustering model)

- Real-time inference via FastAPI

- Health check endpoint for production readiness

## 📊 Data Preprocessing

The preprocessing stage ensures data quality and consistency before feature engineering and modeling.

Key preprocessing steps:

- Removal of duplicated records

- Handling of missing values:

  - Missing CustomerID values were removed

  - Missing product descriptions were filled using StockCode mappings when possible

- Cancellation invoices (InvoiceNo starting with "C") were excluded

- Rows with non-positive Quantity or UnitPrice were removed

- InvoiceDate was converted to datetime format

- A new feature TotalPrice was created as Quantity × UnitPrice

These steps were designed to avoid noise and incorrect customer behavior signals.

## 🧮 Feature Engineering (RFM)

Customer behavior was summarized using RFM analysis, a widely used technique in customer analytics:

- Recency: Number of days since the customer’s last purchase

- Frequency: Number of unique invoices per customer

- Monetary: Total amount spent by the customer

RFM features were aggregated at the customer level and used as input for clustering.

## 🤖 Model

K-Means was selected as the clustering algorithm due to its simplicity, interpretability, and suitability for numerical features such as RFM metrics.

Key modeling steps:

- Feature scaling using StandardScaler

- Selection of the optimal number of clusters using the Elbow Method

- Training the final K-Means model with the selected number of clusters

- Interpretation and labeling of clusters based on RFM characteristics

Each cluster represents a distinct customer segment (e.g. Champions, Loyal Customers, Lost Customers).

## 📈 Model Interpretation

Clusters were analyzed by computing the average RFM values per cluster, enabling meaningful business interpretation and manual labeling of customer segments.

This step ensures that the clustering results are not only mathematically correct but also actionable from a business perspective.

## 🚀 API Deployment

The trained model was deployed as a REST API using FastAPI, allowing real-time customer segmentation.

Available endpoints:

- POST /predict
  Accepts RFM values and returns the predicted customer segment.

- GET /health
  Health check endpoint used to verify that the service is running correctly.

### Input validation

Request data is validated using Pydantic, ensuring:

- Correct data types

- Non-negative values for RFM features

- Protection against invalid inputs at inference time

## 🛠️ Tech Stack

- Python

- Pandas, NumPy

- Scikit-learn

- FastAPI

- Pydantic

- Joblib

## ✅ Conclusion

RFM analysis provides a compact and interpretable representation of customer behavior. K-Means clustering effectively identifies meaningful customer segments without labeled data. Deploying the model as an API enables real-time inference and integration with other systems. Input validation and health checks improve robustness and production readiness. This project demonstrates how an unsupervised machine learning model can be designed, trained, interpreted, and deployed as a scalable service.
