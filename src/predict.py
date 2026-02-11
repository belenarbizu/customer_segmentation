import argparse
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


CLUSTER_NAMES = {
    0: "Occasional customers",
    1: "Lost Customers",
    2: "Champions",
    3: "Potential Loyalists",
    4: "Top Customers"
}


def predict(rfm_values):
    rfm_scaled = scaler.transform([rfm_values])
    cluster = model.predict(rfm_scaled)[0]
    name = CLUSTER_NAMES[cluster]

    return cluster, name


def main():
    parser = argparse.ArgumentParser(description="Predict RFM values")
    parser.add_argument("--rfm_values", '-v', type=str, required=True, help="RFM values in the format 'R,F,M' (e.g., '5,10,3')")
    args = parser.parse_args()

    rfm_values = list(map(float, args.rfm_values.split(",")))
    cluster, name = predict(rfm_values)
    print(f"Predicted cluster: {cluster} - {name}")


if __name__ == "__main__":
    main()