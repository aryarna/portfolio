from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)

# Firebase initialization
cred = credentials.Certificate('firebase_service-account.json')  # Path to your Firebase service account JSON
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Route for Home page
@app.route('/')
def home():
    # Fetch data from Firestore (your projects collection)
    projects_ref = db.collection('projects')  # Firebase collection to store projects data
    docs = projects_ref.stream()  # Fetch all the documents in the 'projects' collection
    projects = []
    for doc in docs:
        project = doc.to_dict()  # Convert the document to a dictionary
        projects.append(project)  # Add the project to the list

    # Render index.html with the fetched projects data
    return render_template('index.html', projects=projects)

# Route for Services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route for Skills page
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Route for Education page
@app.route('/education')
def education():
    return render_template('education.html')

# Route for Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
