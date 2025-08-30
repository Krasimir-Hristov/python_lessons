"""
МОДУЛЕН DOCSTRING: Описва целия файл.
Този скрипт демонстрира работа с речници.
"""


user= {
  "name": "Alexander Ivanov",
  "position": "Software Engineer",
  "skills": ["Python", "Docker", "React"],
}


print(user.get("position"))

user["experiance_years"] = 2

user["position"] = "Senior Software Engineer"


for key, value in user.items():
  print(f"{key}: {value}")


print(user.get("company", "No company information"))
