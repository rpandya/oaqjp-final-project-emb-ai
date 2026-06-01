"""This is the server.py to create the flask app and call the emotional dtector service"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotional Detector")

@app.route("/emotionDetector")
def em_detector ():
    """Call the emotional detector function"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the Emotional Detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response

    anger = response['anger']
    fear = response['fear']
    disgust = response['disgust']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion  = response['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."
    # Return a formatted string with the sentiment label and score
    return (
        "For the given statement, the system response is "
        "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} "
        "and 'sadness': {}. The dominant emotion is {}."
    ).format(anger, disgust, fear, joy, sadness, dominant_emotion)


@app.route("/")
def render_index_page():
    """Render the main index page of the Sentiment Analyzer application."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
