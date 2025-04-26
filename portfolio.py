import os
import json
from flask import Flask, render_template
from urllib.parse import quote as url_quote

import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)

# Check: Local ya Render
if os.getenv('FIREBASE_CONFIG'):
    firebase_creds = os.getenv('FIREBASE_CONFIG')
    cred_dict = json.loads(firebase_creds)
    cred = credentials.Certificate(cred_dict)
else:
    cred = credentials.Certificate('firebase_service-account.json')  # Local file

firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Routes
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
