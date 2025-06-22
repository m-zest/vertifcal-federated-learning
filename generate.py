import argparse
import csv
import math
import random
from pathlib import Path


def generate_id(existing_ids: set[str] = set()) -> str:
    """Generate a random unique 8-digit string ID."""
    while True:
        new_id = f"{random.randint(0, 99999999):08d}"
        if new_id not in existing_ids:
            existing_ids.add(new_id)
            return new_id


def generate_first_dataset(size: int) -> list[tuple[float, str, *tuple[float, ...]]]:
    """Generate the first dataset with dr and id columns."""
    return [
        (
            random.uniform(0, 100),
            generate_id(),
            *(random.uniform(0, 100) for _ in range(10)),
        )
        for _ in range(size)
    ]


def generate_second_dataset(
    first_dataset: list[tuple[float, str, *tuple[float, ...]]],
) -> list[tuple[float, str, int]]:
    """Generate the second dataset with ar, id, and fr columns."""
    return [
        (
            ar := random.uniform(0, 10),
            id,
            int(math.sqrt(dr) + ar >= 12),
        )
        for dr, id, *_ in first_dataset
    ]


def save_dataset(data: list[tuple], headers: list[str], output_path: Path) -> None:
    """Save dataset to a CSV file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate interconnected datasets for fraud detection"
    )
    parser.add_argument(
        "--size",
        type=int,
        default=1000,
        help="Number of records to generate (default: 1000)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("output"),
        help="Output directory for datasets (default: output/)",
    )
    parser.add_argument(
        "--first-filename",
        type=str,
        default="dataset1.csv",
        help="Filename for first dataset (default: dataset1.csv)",
    )
    parser.add_argument(
        "--second-filename",
        type=str,
        default="dataset2.csv",
        help="Filename for second dataset (default: dataset2.csv)",
    )

    args = parser.parse_args()

    # Generate first dataset
    first_dataset = generate_first_dataset(args.size)
    first_output = args.output_dir / args.first_filename
    save_dataset(
        first_dataset, ["dr", "id", *(f"x{i}" for i in range(10))], first_output
    )
    print(f"Generated first dataset with {args.size} records: {first_output}")

    # Generate second dataset
    second_dataset = generate_second_dataset(first_dataset)
    second_output = args.output_dir / args.second_filename
    save_dataset(second_dataset, ["ar", "id", "fr"], second_output)
    print(f"Generated second dataset with {args.size} records: {second_output}")

    # Print sample statistics
    fraudulent = sum(1 for _, _, fr in second_dataset if fr == 1)
    print("\nDataset statistics:")
    print(f"Total records: {args.size}")
    print(f"Fraudulent records: {fraudulent} ({fraudulent / args.size * 100:.2f}%)")
    print(
        f"Non-fraudulent records: {args.size - fraudulent} ({(args.size - fraudulent) / args.size * 100:.2f}%)"
    )


if __name__ == "__main__":
    main()
