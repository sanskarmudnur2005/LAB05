"""Inventory system (cleaned).

Preserves original function names and external behavior while fixing safety
and style problems reported by linters and Bandit.
"""

import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def addItem(item="default", qty=0, logs=None):  # pylint: disable=invalid-name
    """Add qty of item to stock_data and optionally append a log entry."""
    if logs is None:
        logs = []

    if not item:
        return

    if not isinstance(item, str):
        logger.warning(
            "addItem: item must be a string; got %r. Ignoring.",
            item,
        )
        return

    try:
        qty_int = int(qty)
    except (TypeError, ValueError):
        logger.warning(
            "addItem: qty must be int-convertible; got %r. Ignoring.",
            qty,
        )
        return

    stock_data[item] = stock_data.get(item, 0) + qty_int
    logs.append(f"{datetime.now()}: Added {qty_int} of {item}")
    logger.info(
        "Added %d of %s (now %d).",
        qty_int,
        item,
        stock_data[item],
    )


def removeItem(item, qty):  # pylint: disable=invalid-name
    """Remove qty of item from stock_data; warn if item missing"""
    try:
        qty_int = int(qty)
    except (TypeError, ValueError):
        logger.warning(
            "removeItem: qty must be int-convertible; got %r. Ignoring.",
            qty,
        )
        return

    try:
        stock_data[item] -= qty_int
        if stock_data[item] <= 0:
            del stock_data[item]
        # compute current qty into a short variable so the logger call is short
        current_qty = stock_data.get(item, 0)
        logger.info(
            "Removed %d of %s (now %d).",
            qty_int,
            item,
            current_qty,
        )
    except KeyError:
        logger.warning(
            "removeItem: %s not found in inventory.",
            item,
        )


def getQty(item):  # pylint: disable=invalid-name
    """Return current quantity for item (0 if missing)."""
    return stock_data.get(item, 0)


def loadData(file="inventory.json"):  # pylint: disable=invalid-name
    """Load inventory from JSON file into the existing stock_data dict."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            normalized = {}
            for k, v in data.items():
                try:
                    normalized[str(k)] = int(v)
                except (TypeError, ValueError):
                    logger.warning(
                        "loadData: value for %r not int-convertible; "
                        "skipping item.",
                        k,
                    )
            stock_data.clear()
            stock_data.update(normalized)
            logger.info("Loaded inventory from %s", file)
        else:
            logger.warning(
                "loadData: %s does not contain an object/dict. Ignoring.",
                file,
            )
    except FileNotFoundError:
        logger.warning(
            "loadData: %s not found. Starting with empty inventory.",
            file,
        )
    except json.JSONDecodeError:
        logger.warning(
            "loadData: %s contains invalid JSON. Ignoring.",
            file,
        )


def saveData(file="inventory.json"):  # pylint: disable=invalid-name
    """Save current stock_data to a JSON file (UTF-8)."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, ensure_ascii=False, indent=2)
        logger.info("Saved inventory to %s", file)
    except OSError as exc:
        logger.exception(
            "saveData: failed to write %s: %s",
            file,
            exc,
        )


def printData():  # pylint: disable=invalid-name
    """Print items and their quantities."""
    print("Items Report")
    for name, qty in stock_data.items():
        print(name, "->", qty)


def checkLowItems(threshold=5):  # pylint: disable=invalid-name
    """Return list of items whose quantity is below threshold."""
    try:
        threshold_int = int(threshold)
    except (TypeError, ValueError):
        logger.warning(
            "checkLowItems: threshold not int-convertible; using 5.",
        )
        threshold_int = 5

    result = []
    for name, qty in stock_data.items():
        if qty < threshold_int:
            result.append(name)
    return result


def main():  # pylint: disable=invalid-name
    """Example usage preserved from original script."""
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # invalid types; will be ignored with a warning
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    # unsafe eval removed


if __name__ == "__main__":
    main()
