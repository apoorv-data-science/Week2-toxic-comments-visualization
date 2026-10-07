from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data_loader import load_raw_data
from src.preprocessing import clean_comments, add_features
from src.config import PROCESSED_DATA_PATH


def main():
    df = load_raw_data()
    df = clean_comments(df)
    df = add_features(df)
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Saved processed data to: {PROCESSED_DATA_PATH}")
    print(f"Dataset shape: {df.shape}")


if __name__ == "__main__":
    main()
