from preprocessing import (
    open_file,
    basic_cleaning,
    build_rfm
)
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score


def select_kclusters(file_path):
    data = open_file(file_path)
    data = basic_cleaning(data)
    rfm = build_rfm(data)

    X = rfm[['Recency', 'Frequency', 'Monetary']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    inertias = []
    silhouette_scores = []
    for k in range(2, 11):
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(X_scaled)
        inertias.append(model.inertia_)
        labels = model.fit_predict(X_scaled)
        silhouette = silhouette_score(X_scaled, labels)
        silhouette_scores.append(silhouette)

    plt.figure()
    plt.plot(range(2, 11), inertias, marker='o')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for Optimal k')
    plt.savefig('../images/elbow_plot.png')
    plt.close()

    plt.figure()
    plt.plot(range(2, 11), silhouette_scores, marker='o')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Score for Optimal k')
    plt.savefig('../images/silhouette_plot.png')
    plt.close()

    return model


if __name__ == "__main__":
    select_kclusters('..\\data\\online_retail.csv')