# 👻 Ghost Code AI
# memory.py
# Version: 0.1

import json
import os
from datetime import datetime


MEMORY_FOLDER = "projects"


class ProjectMemory:

    def __init__(self, project_name="default"):

        self.project_name = project_name

        self.project_folder = os.path.join(
            MEMORY_FOLDER,
            project_name
        )

        self.project_file = os.path.join(
            self.project_folder,
            "project.json"
        )

        self.load()


    def create_project(self, name):

        self.project_name = name

        self.project_folder = os.path.join(
            MEMORY_FOLDER,
            name
        )

        self.project_file = os.path.join(
            self.project_folder,
            "project.json"
        )

        self.data = {
            "name": name,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "files": {},
            "history": []
        }

        os.makedirs(
            self.project_folder,
            exist_ok=True
        )

        self.save()


    def load(self):

        if os.path.exists(self.project_file):

            with open(
                self.project_file,
                "r",
                encoding="utf-8"
            ) as file:

                self.data = json.load(file)

        else:

            self.data = {
                "name": self.project_name,
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
                "files": {},
                "history": []
            }


    def save(self):

        os.makedirs(
            self.project_folder,
            exist_ok=True
        )

        self.data["updated_at"] = (
            datetime.now().isoformat()
        )

        with open(
            self.project_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.data,
                file,
                ensure_ascii=False,
                indent=2
            )


    def add_file(self, filename, code):

        self.data["files"][filename] = code

        self.save()


    def get_file(self, filename):

        return self.data["files"].get(
            filename,
            None
        )


    def get_all_files(self):

        return self.data["files"]


    def delete_file(self, filename):

        if filename in self.data["files"]:

            del self.data["files"][filename]

            self.save()

            return True

        return False


    def add_history(self, request, response):

        self.data["history"].append({

            "time": datetime.now().isoformat(),

            "request": request,

            "response": response

        })

        self.save()


    def get_history(self):

        return self.data["history"]


    def get_context(self):

        return {

            "project_name": self.data["name"],

            "files": self.data["files"],

            "history": self.data["history"]

        }


    def clear_history(self):

        self.data["history"] = []

        self.save()


# تست اولیه
if __name__ == "__main__":

    print("👻 Ghost Code AI")
    print("Project Memory v0.1")
    print("=" * 40)

    memory = ProjectMemory()

    memory.create_project(
        "TestProject"
    )

    memory.add_file(
        "index.html",
        "<h1>Hello Ghost</h1>"
    )

    memory.add_history(
        "یک سایت بساز",
        "پروژه ساخته شد"
    )

    print()
    print("📁 پروژه:")
    print(memory.data["name"])

    print()
    print("📄 فایل‌ها:")

    for filename in memory.get_all_files():

        print(
            "-",
            filename
        )

    print()
    print("💬 تعداد درخواست‌ها:")

    print(
        len(
            memory.get_history()
        )
    )

    print()
    print("✅ حافظه پروژه فعال است.")
