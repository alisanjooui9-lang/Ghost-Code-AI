# 👻 Ghost Code AI
# coder.py
# Version: 0.1

import re
from model import GhostCodeAI
from memory import ProjectMemory


class CodeEngine:

    def __init__(self, project_name="GhostProject"):

        self.ai = GhostCodeAI()

        self.memory = ProjectMemory(
            project_name
        )

        if self.memory.data["name"] != project_name:
            self.memory.create_project(
                project_name
            )


    def analyze_request(self, request):

        request = request.strip()

        if not request:
            return {
                "action": "empty",
                "request": ""
            }

        text = request.lower()

        if any(word in text for word in [
            "بساز",
            "ایجاد کن",
            "ساخت",
            "create",
            "build",
            "make"
        ]):

            action = "create"

        elif any(word in text for word in [
            "اضافه کن",
            "افزودن",
            "اضافه",
            "add",
            "دارک",
            "تغییر بده",
            "change",
            "update"
        ]):

            action = "modify"

        elif any(word in text for word in [
            "خطا",
            "ارور",
            "رفع کن",
            "fix",
            "debug"
        ]):

            action = "debug"

        else:

            action = "understand"

        return {
            "action": action,
            "request": request
        }


    def detect_language(self, request):

        text = request.lower()

        if "html" in text:
            return "html"

        if "javascript" in text or "js" in text:
            return "javascript"

        if "python" in text or "پایتون" in text:
            return "python"

        if "css" in text:
            return "css"

        if "java" in text:
            return "java"

        return "unknown"


    def generate_placeholder(self, request):

        language = self.detect_language(
            request
        )

        if language == "html":

            return """<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Ghost Project</title>
</head>

<body>

    <h1>Ghost Code AI</h1>

</body>
</html>
"""

        if language == "python":

            return """def main():
    print("Hello from Ghost Code AI")


if __name__ == "__main__":
    main()
"""

        if language == "javascript":

            return """function main() {
    console.log("Hello from Ghost Code AI");
}

main();
"""

        if language == "css":

            return """body {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}
"""

        return """/*
 Ghost Code AI
 Generated project
*/

"""


    def create_file(self, filename, request):

        code = self.generate_placeholder(
            request
        )

        self.memory.add_file(
            filename,
            code
        )

        return code


    def update_file(
        self,
        filename,
        request
    ):

        old_code = self.memory.get_file(
            filename
        )

        if old_code is None:

            return self.create_file(
                filename,
                request
            )

        # فعلاً نسخه آزمایشی.
        # مدل واقعی بعداً این بخش را انجام می‌دهد.

        updated_code = old_code

        comment = (
            "\n\n"
            "<!-- Ghost Code AI modification request: "
            + request
            + " -->\n"
        )

        if filename.endswith(".html"):

            updated_code += comment

        elif filename.endswith(".py"):

            updated_code += (
                "\n# Ghost Code AI modification: "
                + request
                + "\n"
            )

        elif filename.endswith(".js"):

            updated_code += (
                "\n// Ghost Code AI modification: "
                + request
                + "\n"
            )

        self.memory.add_file(
            filename,
            updated_code
        )

        return updated_code


    def process(self, request):

        analysis = self.analyze_request(
            request
        )

        action = analysis["action"]

        if action == "empty":

            return {
                "success": False,
                "message": "درخواست خالی است."
            }


        # درخواست ساخت پروژه
        if action == "create":

            language = self.detect_language(
                request
            )

            if language == "html":

                filename = "index.html"

            elif language == "python":

                filename = "main.py"

            elif language == "javascript":

                filename = "script.js"

            elif language == "css":

                filename = "style.css"

            else:

                filename = "main.txt"

            code = self.create_file(
                filename,
                request
            )

            return {
                "success": True,
                "action": "create",
                "filename": filename,
                "code": code
            }


        # درخواست تغییر پروژه
        if action == "modify":

            files = self.memory.get_all_files()

            if not files:

                return {
                    "success": False,
                    "message":
                    "هنوز پروژه‌ای برای تغییر وجود ندارد."
                }

            filename = next(
                iter(files)
            )

            code = self.update_file(
                filename,
                request
            )

            return {
                "success": True,
                "action": "modify",
                "filename": filename,
                "code": code
            }


        # درخواست رفع خطا
        if action == "debug":

            files = self.memory.get_all_files()

            if not files:

                return {
                    "success": False,
                    "message":
                    "فایلی برای بررسی وجود ندارد."
                }

            filename = next(
                iter(files)
            )

            code = self.memory.get_file(
                filename
            )

            return {
                "success": True,
                "action": "debug",
                "filename": filename,
                "code": code,
                "message":
                "فایل برای بررسی آماده است."
            }


        return {
            "success": True,
            "action": "understand",
            "message":
            "درخواست دریافت شد و آماده پردازش توسط مدل است."
        }


# تست
if __name__ == "__main__":

    print("👻 Ghost Code AI")
    print("Code Engine v0.1")
    print("=" * 40)

    engine = CodeEngine(
        "DemoProject"
    )

    result = engine.process(
        "یک صفحه HTML بساز"
    )

    print()

    print("نتیجه:")

    print(result)

    print()

    print("📁 فایل‌های پروژه:")

    for filename in engine.memory.get_all_files():

        print(
            "-",
            filename
        )

    print()
    print("✅ Code Engine آماده است.")
