# 👻 Ghost Code AI
# model.py
# Version: 0.1

class GhostCodeAI:
    """
    هسته اولیه Ghost Code AI

    این نسخه برای ساخت ساختار مدل و آزمایش
    روند درک درخواست‌های برنامه‌نویسی ساخته شده است.
    """

    def __init__(self):
        self.name = "Ghost Code AI"
        self.version = "0.1"
        self.project = None
        self.history = []

    def understand(self, request):
        """
        دریافت درخواست کاربر.
        در نسخه‌های بعدی این بخش توسط مدل آموزش‌دیده
        انجام خواهد شد.
        """

        request = request.strip()

        if not request:
            return {
                "type": "empty",
                "request": ""
            }

        return {
            "type": "coding_request",
            "request": request
        }

    def remember(self, request, response):
        """
        ذخیره سابقه گفتگو برای استفاده در ادامه پروژه.
        """

        self.history.append({
            "request": request,
            "response": response
        })

    def create_project(self, name):
        """
        ایجاد پروژه جدید.
        """

        self.project = {
            "name": name,
            "files": {}
        }

        return self.project

    def add_file(self, filename, code):
        """
        اضافه کردن فایل به پروژه.
        """

        if self.project is None:
            self.create_project("Untitled Project")

        self.project["files"][filename] = code

    def get_project(self):
        """
        دریافت پروژه فعلی.
        """

        return self.project

    def get_history(self):
        """
        دریافت سابقه درخواست‌های کاربر.
        """

        return self.history


# تست اولیه
if __name__ == "__main__":

    ghost = GhostCodeAI()

    result = ghost.understand(
        "یک ماشین حساب HTML بساز"
    )

    print("👻 Ghost Code AI")
    print("Version:", ghost.version)
    print()

    print("درخواست کاربر:")
    print(result["request"])

    ghost.create_project("Calculator")

    ghost.add_file(
        "index.html",
        "<!-- Calculator code -->"
    )

    ghost.remember(
        result["request"],
        "Project created"
    )

    print()
    print("پروژه:")
    print(ghost.get_project())

    print()
    print("تعداد درخواست‌های ذخیره‌شده:")
    print(len(ghost.get_history()))
