# 👻 Ghost Code AI
# train.py
# Version: 0.1

import json
import os
from model import GhostCodeAI


DATASET_FILE = "dataset.json"


def load_dataset():
    """بارگذاری دیتاست آموزشی."""

    if not os.path.exists(DATASET_FILE):
        print("❌ فایل dataset.json پیدا نشد.")
        return []

    with open(DATASET_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def show_dataset(data):
    """نمایش نمونه‌های آموزشی."""

    print()
    print("📚 Ghost Code AI Dataset")
    print("=" * 40)

    for index, item in enumerate(data, start=1):

        instruction = item.get("instruction", "")
        output = item.get("output", "")

        print(f"\nنمونه {index}")
        print("درخواست:", instruction)
        print("پاسخ:", output)


def prepare_training_data(data):
    """
    تبدیل دیتاست به ساختاری که بعداً
    برای آموزش مدل استفاده می‌کنیم.
    """

    training_data = []

    for item in data:

        instruction = item.get("instruction", "")
        input_text = item.get("input", "")
        output = item.get("output", "")

        training_data.append({
            "instruction": instruction,
            "input": input_text,
            "output": output
        })

    return training_data


def save_prepared_data(data):
    """ذخیره دیتاست آماده‌شده."""

    output_file = "training_data.json"

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )

    print()
    print("✅ دیتاست آماده شد:")
    print(output_file)


def test_model():
    """تست اولیه هسته Ghost Code AI."""

    ghost = GhostCodeAI()

    result = ghost.understand(
        "یک سایت فروشگاهی بساز"
    )

    print()
    print("🧠 تست Ghost Code AI")
    print("=" * 40)

    print("درخواست:")
    print(result["request"])


def main():

    print("👻 Ghost Code AI")
    print("Training System v0.1")
    print("=" * 40)

    dataset = load_dataset()

    if not dataset:
        print("❌ دیتاست خالی است.")
        return

    print(f"📚 تعداد نمونه‌ها: {len(dataset)}")

    show_dataset(dataset)

    training_data = prepare_training_data(dataset)

    save_prepared_data(training_data)

    test_model()

    print()
    print("🎉 مرحله آماده‌سازی آموزش با موفقیت انجام شد.")


if __name__ == "__main__":
    main()
