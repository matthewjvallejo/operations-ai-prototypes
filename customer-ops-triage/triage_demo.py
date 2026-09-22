import csv
from collections import Counter

KEYWORDS = {
    "Billing": ["charge", "refund", "invoice", "charged", "payment", "billing"],
    "Product": ["feature", "workflow", "button", "screen", "product"],
    "Technical": ["error", "bug", "crash", "broken", "loading"],
    "Account Access": ["login", "password", "access", "locked"],
    "Subscription / Plan Change": ["plan", "upgrade", "downgrade", "subscription", "cancel"],
}

def classify(text):
    lower = text.lower()
    for category, words in KEYWORDS.items():
        if any(word in lower for word in words):
            return category
    return "General Support"

def priority(text, category):
    lower = text.lower()

    if category == "Account Access" or any(word in lower for word in ["cannot access", "locked out", "down"]):
        return "P1"

    if category in {"Billing", "Technical", "Subscription / Plan Change"}:
        return "P2"

    return "P3"

def main():
    rows = []

    with open("sample_tickets.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            category = classify(row["issue"])
            p = priority(row["issue"], category)
            row["category"] = category
            row["priority"] = p
            rows.append(row)

    counts = Counter(row["category"] for row in rows)

    print("TRIAGED TICKETS")
    print("-" * 60)
    for row in rows:
        print(f'{row["ticket_id"]}: {row["priority"]} | {row["category"]} | {row["issue"]}')

    print("\nRECURRING THEMES")
    print("-" * 60)
    for category, count in counts.most_common():
        print(f"{category}: {count}")

if __name__ == "__main__":
    main()
