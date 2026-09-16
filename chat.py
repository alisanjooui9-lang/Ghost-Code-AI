# 👻 Ghost Code AI
# chat.py
# Version: 0.1

from model import GhostCodeAI


def print_header():
    print()
    print("=" * 50)
    print("👻 Ghost Code AI")
    print("Coding Assistant v0.1")
    print("=" * 50)
    print("برای خروج بنویس: exit")
    print()


def show_project(ghost):
    project = ghost.get_project()

    if project is None:
        print("📁 هنوز پروژه‌ای ساخته نشده.")
        return

    print()
    print("📁 پروژه:", project["name"])
    print("📄 فایل‌ها:")

    if not project["files"]:
        print("  هنوز فایلی وجود ندارد.")
        return

    for filename in project["files"]:
        print("  -", filename)


def process_request(ghost, request):
    result = ghost.understand(request)

    if result["type"] == "empty":
        print("⚠️ درخواست خالی است.")
        return

    print()
    print("🧠 درخواست دریافت شد:")
    print(result["request"])

    # فعلاً پاسخ آزمایشی
    response = (
        "درخواست شما دریافت شد. "
        "در نسخه‌های بعدی مدل واقعی Ghost Code AI "
        "کد پروژه را تولید و اصلاح خواهد کرد."
    )

    ghost.remember(
        request,
        response
    )

    print()
    print("👻 Ghost AI:")
    print(response)


def main():

    ghost = GhostCodeAI()

    print_header()

    while True:

        try:
            request = input("🧑 شما: ").strip()

        except KeyboardInterrupt:
            print("\n\n👋 Ghost Code AI بسته شد.")
            break

        except EOFError:
            print("\n\n👋 Ghost Code AI بسته شد.")
            break

        if request.lower() in ["exit", "quit", "خروج"]:
            print()
            print("👋 خداحافظ!")
            break

        if request.lower() in [
            "project",
            "پروژه",
            "پروژه من"
        ]:
            show_project(ghost)
            continue

        process_request(
            ghost,
            request
        )


if __name__ == "__main__":
    main()
