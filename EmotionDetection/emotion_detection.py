import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)
    print(type(formatted_response))

    #print(formatted_response['emotionPredictions'][0]['emotionMentions'][0]['span']['text'])
    #return(formatted_response['emotionPredictions'][0]['emotionMentions'][0]['span']['text'])

    anger = formatted_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']['anger']
    fear = formatted_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']['fear']
    disgust = formatted_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']['disgust']
    joy = formatted_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']['sadness']
    
    emotions_dict = {
    'anger': anger,
    'disgust': disgust,
    'fear': fear,
    'joy': joy,
    'sadness': sadness
    }

    # Find the key with the highest value
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    emotions_dict = {
    'anger': anger,
    'disgust': disgust,
    'fear': fear,
    'joy': joy,
    'sadness': sadness,
    'dominant_emotion':dominant_emotion
    }
    print(emotions_dict)
    return(emotions_dict)