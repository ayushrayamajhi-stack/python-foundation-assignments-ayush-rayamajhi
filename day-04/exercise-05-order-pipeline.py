"""
Exercise: Order Processing Pipeline
Student: Ayush Rayamajhi
Day: 4
"""

import csv
import json
import logging


def process_orders(csv_path, json_path, log_path):
    logger = logging.getLogger("orders")
    logger.setLevel(logging.INFO)

    # Clear existing handlers to avoid duplicate logs
    logger.handlers.clear()

    handler = logging.FileHandler(log_path, mode="w")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    valid_rows = []
    num_valid = 0
    num_invalid = 0

    try:
        with open(csv_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row_number, row in enumerate(reader, start=1):

                try:
                    qty = int(row["qty"])
                    price = float(row["price"])

                except ValueError:
                    logger.error(
                        f"Row {row_number}: "
                        f"could not convert qty/price "
                        f"({row['qty']!r}, {row['price']!r}) - SKIPPED"
                    )

                    num_invalid += 1
                    continue

                if qty < 0 or price < 0:
                    logger.error(
                        f"Row {row_number}: "
                        f"negative qty or price - SKIPPED"
                    )

                    num_invalid += 1
                    continue

                row["qty"] = qty
                row["price"] = price
                row["total"] = round(qty * price, 2)

                valid_rows.append(row)
                num_valid += 1

                logger.info(
                    f"Row {row_number}: "
                    f"order {row['order_id']} processed successfully"
                )

    except FileNotFoundError:
        logger.critical(
            f"Input file not found: {csv_path}"
        )

        return 0, 0

    finally:
        logger.info("Finished reading input CSV")

    with open(json_path, "w") as file:
        json.dump(valid_rows, file, indent=2)

    return num_valid, num_invalid


# Test
result = process_orders(
    "orders.csv",
    "orders_clean.json",
    "orders_pipeline.log"
)

print(f"Valid orders: {result[0]}")
print(f"Invalid orders: {result[1]}")