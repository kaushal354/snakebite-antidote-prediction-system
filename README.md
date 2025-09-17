# snakebite-antidote-prediction-system

This project is a web-based application built with Django that uses a machine learning model to identify snake species from an uploaded image. Based on the identification, it provides users with crucial information, including first-aid procedures, professional medical treatment guidelines, and details about the snake.

## Features

*   **Image-Based Snake Identification:** Upload an image to classify the snake. The model is trained to identify species like the Indian Cobra, Russell's Viper, and Python.
*   **Information Hub:** Access detailed information about each supported snake species.
*   **First-Aid Guidance:** Get immediate, snake-specific first-aid instructions after a successful identification.
*   **Medical Treatment Information:** View guidelines for professional medical treatment corresponding to the identified snakebite.
*   **Hospital Locator:** A feature to find and register hospitals, helping users quickly locate nearby medical facilities.
*   **Interactive Chatbot:** An integrated chatbot to assist users with their queries.

## Technology Stack

*   **Backend:** Python, Django
*   **Machine Learning:** TensorFlow, Keras, Scikit-learn
*   **Frontend:** HTML, CSS, JavaScript
*   **Database:** SQLite
*   **Libraries:** Pandas, NumPy, Pillow, Geopy

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd snakebite
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6.  Open your web browser and navigate to `http://127.0.0.1:8000` to use the application.

## Usage

1.  From the homepage, select the option to upload an image of a snake.
2.  The system will process the image and display the identified snake species.
3.  Based on the result, you can explore sections for:
    *   **About the Snake:** Detailed information about the species.
    *   **First-Aid:** Immediate steps to take after a bite.
    *   **Professional Treatment:** Medical procedures for healthcare professionals.
4.  Use the hospital locator to find registered medical centers in a specific city.

## Project Structure

```
├───manage.py               # Django's command-line utility
├───requirements.txt        # Project dependencies
├───db.sqlite3              # SQLite database
├───model/                    # Contains the trained ML model (.h5 file)
├───snakebite/              # Django project configuration
├───home/                   # Django app for core functionalities
├───static/                 # Static files (CSS, JS, images)
└───templates/              # HTML templates for the web pages
```