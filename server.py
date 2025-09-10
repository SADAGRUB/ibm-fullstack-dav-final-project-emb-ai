"""
Flask web application for emotion detection using IBM Watson's EmotionPredict API.

Routes:
    /emotionDetector - Accepts 'textToAnalyze' query parameter and returns:
                       - Scores for anger, disgust, fear, joy, sadness
                       - Dominant emotion
                       Handles empty or invalid input with an error message.
    /                - Renders the home page (index.html).

Constants:
    HOST, PORT, DEBUG - Flask server configuration
"""

# -----------------------------
# Imports
# -----------------------------
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# -----------------------------
# Configuration constants
# -----------------------------
HOST = "0.0.0.0"
PORT = 5000
DEBUG = True

# -----------------------------
# Flask app
# -----------------------------
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze text and return emotions and dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    result_text = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return result_text

@app.route("/")
def render_index_page():
    """
    Render the home page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
