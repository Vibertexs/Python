from flask import Flask, render_template, redirect, url_for, request

from student import Student

students = []

app = Flask(__name__)


@app.route("/",met  hods = ["GET", "POST"])
def students_page():
    if requesst.method == "POST":
        new_student_id = request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")

        new_student = Stuednt(name=new_student_name, student_id=new_student_id)
        students.append(new_student)

        return redirect(url_for("students_page")
        
    return render_template("index.html", students=students))

if __name__ = "__main__":
    app.run(debug=True)
