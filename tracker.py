from datetime import date
import json
from pathlib import Path
from typing import TypedDict


class Expense(TypedDict):
    item: str
    amount: float
    category: str
    date: str


DATA_FILE = Path("expenses.json")


def load_expenses() -> list[Expense]:
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_expenses(expenses: list[Expense]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses: list[Expense]) -> None:
    item = input("What did you buy? ")
    amount = ask_for_amount("How much did it cost? ")
    category = input("Category (e.g. Food, Transport): ")
    new_expense: Expense = {
        "item": item,
        "amount": amount,
        "category": category,
        "date": date.today().isoformat(),
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Added {item} (${amount:.2f}).")


def list_expenses(expenses: list[Expense]) -> None:
    if not expenses:
        print("No expenses yet.")
        return
    print("\nYour expenses:")
    for number, expense in enumerate(expenses, start=1):
        print(
            f"  {number}. {expense['item']:<15} "
            f"${expense['amount']:>7.2f}  [{expense['category']}]  "
            f"{expense.get('date', '—')}"
        )


def choose_index(expenses: list[Expense], action: str) -> int | None:
    raw = input(f"{action} which number? ").strip()
    if not raw.isdigit():
        print("Please enter a whole number.")
        return None
    number = int(raw)
    if number < 1 or number > len(expenses):
        print(f"No expense #{number}. Pick 1–{len(expenses)}.")
        return None
    return number - 1


def delete_expense(expenses: list[Expense]) -> None:
    list_expenses(expenses)
    if not expenses:
        return
    idx = choose_index(expenses, "Delete")
    if idx is None:
        return

    removed = expenses.pop(idx)
    save_expenses(expenses)
    print(f"Deleted {removed['item']}.")


def edit_expense(expenses: list[Expense]) -> None:
    list_expenses(expenses)
    if not expenses:
        return

    idx = choose_index(expenses, "Edit")
    if idx is None:
        return
    expense = expenses[idx]

    item = input(f"Item [{expense['item']}]: ").strip()
    new_amount = ask_for_amount(
        f"Amount [{expense['amount']:.2f}]: ", allow_blank=True)
    if new_amount is not None:
        expense["amount"] = new_amount
    category = input(f"Category [{expense['category']}]: ").strip()

    if item:
        expense["item"] = item
    if category:
        expense["category"] = category

    save_expenses(expenses)
    print(f"Updated {expense['item']}.")


def ask_for_amount(prompt: str, allow_blank: bool = False) -> float | None:
    while True:
        raw = input(prompt).strip()
        if allow_blank and raw == "":
            return None
        try:
            amount = float(raw)
        except ValueError:
            print("That's not a number. Try something like 12.50.")
            continue
        if amount < 0:
            print("Amount can't be negative.")
            continue
        return amount


def show_summary(expenses: list[Expense]) -> None:
    if not expenses:
        print("No expenses to summarize.")
        return
    total = 0
    by_category = {}
    for e in expenses:
        total += e["amount"]
        by_category[e["category"]] = by_category.get(
            e["category"], 0) + e["amount"]
    print(f"\nTotal spent: ${total:.2f}")
    print("By category:")
    for category, subtotal in by_category.items():
        print(f"  {category:<15} ${subtotal:>7.2f}")


def main() -> None:
    expenses = load_expenses()
    while True:
        print("\n=== Expense Tracker ===")
        print("1) Add  2) List  3) Edit  4) Delete  5) Summary  6) Quit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            edit_expense(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            show_summary(expenses)
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Please choose 1–6.")


if __name__ == "__main__":
    main()
