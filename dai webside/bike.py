from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        dob = request.form.get("dob")

        # Process the data (e.g., store in a database, send an email, etc.)
        # For now, we'll just print it to the console
        print("Name:", name)
        print("Phone:", phone)
        print("Email:", email)
        print("Date of Birth:", dob)

        # You might want to redirect the user to a thank you page or display a message
        return "Data received!"  # Or: return render_template("thankyou.html")

    return render_template("index.html")  # Render the HTML form

if _name_ == "_main_":
    app.run(debug=True)  # debug=True for easier development