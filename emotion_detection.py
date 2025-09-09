"""
This module provides a function for performing emotion detection on text
using IBM Watson's pre-trained EmotionPredict service.
"""

import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}

    # Requête API
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    emotion_dic = formatted_response["emotionPredictions"][0]["emotion"]

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
