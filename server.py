"""Flask web application for emotion detection."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Render the emotion detection page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the submitted text and return its emotion scores."""
    text_to_analyze = request.args["textToAnalyze"]
    emotions = emotion_detector(text_to_analyze)

    return (
        "For the given statement, the system response is\n"
        f"'anger': {emotions['anger']},\n"
        f"'disgust': {emotions['disgust']},\n"
        f"'fear': {emotions['fear']},\n"
        f"'joy': {emotions['joy']},\n"
        f"and 'sadness': {emotions['sadness']}.\n"
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
