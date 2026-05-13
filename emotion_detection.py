import requests
import json
def emotion_detector(text_to_analyze):
    url="https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj={ "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response=json.loads(response.text)
    emotion1=formatted_response["emotionPredictions"]
    emotion2=emotion1[0]["emotion"]
    return {
        "anger":emotion2["anger"],
        "disgust":emotion2["disgust"],
        "fear":emotion2["fear"],
        "joy":emotion2["joy"],
        "sadness":emotion2["sadness"],
        "domninant_emotion":max(emotion2, key=emotion2.get)
    }