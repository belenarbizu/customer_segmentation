import argparse
import joblib


CLUSTER_NAMES = {
    0: "Occasional customers",
    1: "Lost Customers",
    2: "Champions",
    3: "Potential Loyalists",
    4: "Top Customers"
}


def predict(rfm_values):
    model = joblib.load("..\\models\\model.pkl")
    scaler = joblib.load("..\\models\\scaler.pkl")

    rfm_scaled = scaler.transform([rfm_values])
    cluster = model.predict(rfm_scaled)
    print(f"Predicted cluster: {cluster[0]} - {CLUSTER_NAMES[cluster[0]]}")

    return cluster[0], CLUSTER_NAMES[cluster[0]]


def main():
    parser = argparse.ArgumentParser(description="Predict RFM values")
    parser.add_argument("--rfm_values", '-v', type=str, required=True, help="RFM values in the format 'R,M,F'")
    args = parser.parse_args()

    rfm_values = list(map(int, args.rfm_values.split(",")))
    predict(rfm_values)


if __name__ == "__main__":
    main()