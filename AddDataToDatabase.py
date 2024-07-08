import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ai-faceid-attendance-system-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "680456": {
        "name": "Lebron James",
        "major": "Comp Sci",
        "starting_year": 2023,
        "total_attendance": 6,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2024-07-07 00:00:00"
    }
}

for key, value in data.items():
    ref.child(key).set(value)