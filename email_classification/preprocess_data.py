import argparse

import pandas as pd


def preprocess(input_csv, output_txt):
    data = pd.read_csv(input_csv)

    with open(output_txt, "w") as f:
        for _, row in data.iterrows():
            label = row["product"]
            text = row["narrative"]
            f.write(f"__label__{label} {text}\n")


if __name__ == "__main__":
    # TODO: set up it as input parameters
    parser = argparse.ArgumentParser(description="Preprocess data")
    parser.add_argument(
        "--input", type=str, required=True, help="Path to the input CSV file"
    )
    parser.add_argument(
        "--output", type=str, required=True, help="Path to save the processed txt file"
    )

    args = parser.parse_args()
    preprocess(args.input, args.output)
