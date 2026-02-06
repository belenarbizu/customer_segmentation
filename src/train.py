from preprocessing import (
    open_file,
    basic_cleaning,
    build_rfm
)
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib
import os


def train(data_path):
    data = open_file(data_path)
    data = basic_cleaning(data)
    rfm = build_rfm(data)

    X = rfm[['Recency', 'Frequency', 'Monetary']]

    # Standardize the RFM features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = KMeans(n_clusters=5, random_state=42)
    model.fit(X_scaled)

    if not os.path.exists('..\\models'):
        os.makedirs('..\\models')

    joblib.dump(model, '..\\models\\model.pkl')
    joblib.dump(scaler, '..\\models\\scaler.pkl')

    return model


if __name__ == "__main__":
    train('..\\data\\online_retail.csv')