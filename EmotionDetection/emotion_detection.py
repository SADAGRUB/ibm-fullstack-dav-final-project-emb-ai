"""
This module provides a function for performing emotion detection on text
using IBM Watson's pre-trained EmotionPredict service.
"""

import requests
import json


def emotion_detector(text_to_analyse):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=payload, headers=headers)
    formatted_response = json.loads(response.text)
  
    emotion_dic = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(
        (k for k in emotion_dic if k != "dominant_emotion"),
        key=lambda k: emotion_dic[k]
    )
    emotion_dic["dominant_emotion"] = dominant_emotion
    display_response = {key: value for key, value in emotion_dic.items()}
    
    return display_response
