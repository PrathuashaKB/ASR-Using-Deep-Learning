#importing all the necessary packages
import nltk
import librosa
import torch
import gradio as gr
from transformers import Wav2Vec2Tokenizer,Wav2Vec2ForCTC
nltk.download("punkt")

#loading the pre-trained model and the tokenizer
model_name="facebook/wav2vec2-base-960h"
tokenizer=Wav2Vec2Tokenizer.from_pretrained(model_name)
model=Wav2Vec2ForCTC.from_pretrained(model_name)

#creating a function that makes sure that the speech input has a sampling rate of 16kHz
def load_data(input_file):
    #reading a file
    speech,sample_rate=librosa.load(input_file)
    #make it 1-D
    if len(speech.shape)>1:
        speech=speech[:,0]+speech[:,1]
    #resampling the audio at 16kHz
    if sample_rate!=16000:
        speech=librosa.resample(speech,sample_rate,16000)
    return speech

#creating the function for correcting the letter casing 
def correct_casing(input_sentence):
    sentences=nltk.sent_tokenize(input_sentence)
    return (''.join([s.replace(s[0],s[0].capitalize(),1) for s in sentences]))

#defining a function for getting a transcript of the audio input
def asr_transcript(input_file):
    speech=load_data(input_file)
    #tokenize
    input_values=tokenizer(speech,return_tensors="pt").input_values
    #take logits
    logits=model(input_values).logits
    #take argmax
    predicted_ids=torch.argmax(logits,dim=-1)
    #get the words from predicted word ids
    transcription=tokenizer.decode(predicted_ids[0])
    #correcting the letter casing
    transcription=correct_casing(transcription.lower())
    return transcription

#creating a UI to the model using gr.Interface
gr.Interface(asr_transcript,
            inputs=gr.inputs.Audio(source="microphone",type="filepath",optional=True,label="Speaker"),
            outputs=gr.outputs.Textbox(label="Output Text"),
            title="ASR using Wav2Vec 2.0",
            description="This application displays transcribed text for given audio input(Please accord the audio in ENGLISH only)",
            examples=[["my-audio.wav"],["male.wav"]],theme="grass").launch()
