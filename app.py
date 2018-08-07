import datetime as dt
import pandas as pd
from sqlalchemy import func
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Data/nbaAttendance.db"



db = SQLAlchemy(app)


class NBA(db.Model):
    __tablename__ = 'Attendancev2'

    NBASeason = db.Column(db.Text)
    Team = db.Column(db.Text, primary_key=True)
    PercentSalaryCap = db.Column(db.Text)
    PrevNumAllStars = db.Column(db.Text)
    PrevWL = db.Column(db.Text)
    NumHGames = db.Column(db.Text)
    HAttendanceSeason = db.Column(db.Text)
    HArenaCapacity = db.Column(db.Text)
    HAvgAttendance = db.Column(db.Text)
    HPercentCapacity = db.Column(db.Text)
    NumAGames = db.Column(db.Text)
    AAvgAttendance = db.Column(db.Text)
    APercentCapacity = db.Column(db.Text)
    AGames = db.Column(db.Text)
    HandAAvg = db.Column(db.Text)
    HandAPCT = db.Column(db.Text)



    def __repr__(self):
        return '<Attendancev2 %r>' % (self.name)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("bubble.html")

@app.route("/data")
def attendance_data():



    results = db.session.query(NBA.NBASeason, NBA.Team, NBA.PercentSalaryCap, NBA.PrevNumAllStars, NBA.PrevWL, NBA.NumHGames, NBA.HAttendanceSeason, NBA.HArenaCapacity, NBA.HAvgAttendance, NBA.HPercentCapacity, NBA.NumAGames, NBA.AAvgAttendance, NBA.APercentCapacity, NBA.AGames, NBA.HandAAvg, NBA.HandAPCT).\
        order_by(NBA.Team.desc()).all()


    attendance_data = {}

    for result in results:
        attendance_data["Season"] = result[0]
        attendance_data["Team"] = result[1]
        attendance_data["% Salary Cap"] = result[3]
        attendance_data["Prev # All-Stars"] = result[4]
        attendance_data["Prev Winning %"] = result[5]
        attendance_data["# Home Games"] = result[6]
        attendance_data["Home Attendance Total"] = result[7]
        attendance_data["Home Arena Capacity"] = result[8]
        attendance_data["Home Avg Attendance"] = result[9]
        attendance_data["Home % Capacity"] = result[10]
        attendance_data["# Away Games"] = result[11]
        attendance_data["Away Avg Attendance"] = result[12]
        attendance_data["Away % Capacity"] = result[13]
        attendance_data["Total Games"] = result[14]
        attendance_data["Total Avg Attendance"] = result[14]
        attendance_data["Total % Capacity"] = result[14]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
