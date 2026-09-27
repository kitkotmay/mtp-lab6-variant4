from flask import Flask, render_template_string


app = Flask(__name__)


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Таблица студентов</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }

        table {
            border-collapse: collapse;
            width: 700px;
        }

        th, td {
            border: 1px solid black;
            padding: 10px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Таблица студентов</h1>

    <table>
        <tr>
            <th>ФИО</th>
            <th>Группа</th>
            <th>Вариант</th>
        </tr>

        {% for student in students %}
        <tr>
            <td>{{ student.name }}</td>
            <td>{{ student.group }}</td>
            <td>{{ student.variant }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""


@app.route("/")
def index():
    students = [
        {
            "name": "Ковалевич Александра Андреевна",
            "group": "221141р",
            "variant": 4,
        },
        {
            "name": "Иванов Иван Иванович",
            "group": "221141р",
            "variant": 2,
        },
        {
            "name": "Петров Пётр Петрович",
            "group": "221141р",
            "variant": 7,
        },
    ]

    return render_template_string(
        HTML_TEMPLATE,
        students=students,
    )


if __name__ == "__main__":
    app.run(debug=True)
