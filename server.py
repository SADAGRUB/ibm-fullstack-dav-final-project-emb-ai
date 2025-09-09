from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_dic = emotion_detector(text_to_analyze)

    anger_score = emotion_dic["anger"]
    disgust_score = emotion_dic["disgust"]
    fear_score = emotion_dic["fear"]
    joy_score = emotion_dic["joy"]
    sadness_score = emotion_dic["sadness"]
    dominant_emotion = max(emotion_dic, key=emotion_dic.get)

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
