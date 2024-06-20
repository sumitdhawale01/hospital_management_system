# app.py

from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from config import Config  # Import your configuration

app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from config.py

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def xyz():
    if request.method == 'POST':
        try:
            Patient_Name = request.form['Patient_Name']
            Age = int(request.form['Age'])  # Convert to int
            Medical_Condition = request.form['Medical_Condition']
            Doctor_name = request.form['Doctor_name']
            DateOfAppointment = request.form['DateOfAppointment']
            TimeOfAppointment = request.form['TimeOfAppointment']

            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO patientrecord(Patient_Name, Age, Medical_Condition, Doctor_name, DateOfAppointment, TimeOfAppointment) VALUES(%s, %s, %s, %s, %s, %s)",
                (Patient_Name, Age, Medical_Condition, Doctor_name, DateOfAppointment, TimeOfAppointment))
            mysql.connection.commit()
            cur.close()
            # return "INSERTED SUCCESSFULLY !!"
        except Exception as e:
            # Handle the error, log it, and return an error message
            error_message = f"Error: {str(e)}"
            return error_message
    return render_template('index.html')


if __name__ == '__main__':
    app.run()