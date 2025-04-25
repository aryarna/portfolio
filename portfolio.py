import os
import json
from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)

# Firebase initialization from environment variable
firebase_creds = os.getenv('FIREBASE_CREDENTIALS')  # Get the JSON credentials from environment variable
cred_dict = json.loads(firebase_creds)  # Convert the JSON string into a dictionary
cred = credentials.Certificate(cred_dict)  # Create a credential object
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Routes (same as before)
@app.route('/')
def home():
    projects_ref = db.collection('projects')
    docs = projects_ref.stream()
    projects = []
    for doc in docs:
        project = doc.to_dict()
        projects.append(project)
    return render_template('index.html', projects=projects)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
