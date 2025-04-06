from flask import Flask, render_template
import logging
import os

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    logging.info("Accessing home route")
    try:
        return render_template('index.html')
    except Exception as e:
        logging.error(f"Error rendering home page: {e}")
        return "Error rendering home page", 500

@app.route('/DES')
def des():
    logging.info("Accessing DES route")
    try:
        return render_template('DES.html')
    except Exception as e:
        logging.error(f"Error rendering DES page: {e}")
        return "Error rendering DES page", 500

@app.route('/AES')
def aes():
    logging.info("Accessing AES route")
    try:
        return render_template('AES.html')
    except Exception as e:
        logging.error(f"Error rendering AES page: {e}")
        return "Error rendering AES page", 500

@app.route('/RSA')
def rsa():
    logging.info("Accessing RSA route")
    try:
        return render_template('RSA.html')
    except Exception as e:
        logging.error(f"Error rendering RSA page: {e}")
        return "Error rendering RSA page", 500

@app.route('/simulation/DES')
def simulation_des():
    try:
        return render_template('Simulation/DES_Simulation.html')

    except Exception as e:
        logging.error(f"Error rendering DES simulation: {e}")
        return "Error rendering DES simulation", 500

@app.route('/simulation/AES')
def simulation_aes():
    try:
        return render_template('Simulation/AES_Simulation.html')

    except Exception as e:
        logging.error(f"Error rendering AES simulation: {e}")
        return "Error rendering AES simulation", 500

@app.route('/simulation/RSA')
def simulation_rsa():
    try:
        return render_template('Simulation/RSA_Simulation.html')

    except Exception as e:
        logging.error(f"Error rendering RSA simulation: {e}")
        return "Error rendering RSA simulation", 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to True for development
