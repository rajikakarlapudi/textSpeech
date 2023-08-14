import os
import azure.cognitiveservices.speech as speechsdk

# Set your Azure subscription key and endpoint
subscription_key = "Cfff3e7399a2471aa8d4f441a7e61339"
region = "centralindia"
endpoint = "https://centralindia.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

def text_to_speech(text, output_file):
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    result = speech_synthesizer.speak_text_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        audio_data = result.audio_data
        with open(output_file, "wb") as audio_file:
            audio_file.write(audio_data)

if __name__ == "__main__":
    input_text = input("Enter the text: ")
    output_audio_file = "output.wav"
    text_to_speech(input_text, output_audio_file)