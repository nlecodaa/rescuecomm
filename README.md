RescueComm – AI Powered Emergency Response System

RescueComm is a lightweight prototype that uses artificial intelligence to classify and prioritize emergency alerts. It demonstrates how automation and NLP can make emergency management faster, more reliable, and easier to scale.


1. Introduction

Emergency response systems often depend on human operators to interpret and forward alerts. This causes delays and misclassification when time is critical.  
RescueComm automates this process by using a trained NLP model to identify the type of emergency (Police, Fire, or Ambulance) and a simple rule-based engine to decide how urgent the case is.  
It then logs and displays the simulated dispatch through a clean web interface.


2. Features

- Automatic classification of emergency messages using NLP  
- Priority scoring based on keywords and context  
- Simulated multi-channel dispatch (web interface)  
- SQLite database to log alerts and priorities  
- Simple and responsive UI with ready emergency buttons  


## 3. Project Structure

RescueComm/
├── app.py # Main Flask application
├── risk_engine.py # Rule-based risk scoring logic
├── train_model.py # Script to train the classifier
├── train.csv # Sample dataset
├── rescuecomm_clf.pkl # Trained model 
├── requirements.txt # Required Python libraries
└── README.md 



4. Setup Instructions

Step 1: Clone or Extract the Project
git clone https://github.com/nlecodaa/RescueComm.git
cd RescueComm
Or just unzip the provided file.

Step 2: Create and Activate Virtual Environment
python -m venv venv

venv\Scripts\activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Train the Model
If the model file rescuecomm_clf.pkl is missing:
python train_model.py

Step 5: Run the Web Application
python app.py
Open your browser and go to:
http://127.0.0.1:5000

5. How It Works
The user submits an emergency message through the web form.

The NLP model classifies it into one of three categories – Police, Fire, or Ambulance.

The risk engine analyzes severity keywords and assigns a score (0–100).

Based on the score, the system labels the case as High, Medium, or Low priority.

The result is stored in the database and displayed with a simulated dispatch alert.

6. Example Messages
Input Message	Category	Priority	Risk Score
"A big fire near the city mall!"	Fire	High	88
"My shop was robbed last night"	Police	Medium	63
"A man fainted at the railway station"	Ambulance	High	91

Nikhil

