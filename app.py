from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
</head>
<body>
    <h2>Simple Calculator</h2>
    <form method="post">
        <input type="text" name="num1" placeholder="Enter first number" required>
        <input type="text" name="num2" placeholder="Enter second number" required><br><br>

        <button type="submit" name="operation" value="add">Add</button>
        <button type="submit" name="operation" value="subtract">Subtract</button>
        <button type="submit" name="operation" value="multiply">Multiply</button>
        <button type="submit" name="operation" value="divide">Divide</button>
    </form>

    {% if result != "" %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            else:
                result = "Invalid Operation"
        except ValueError:
            result = "Please enter valid numbers"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
