# Automatic Speech Recognition
<div>
  <p align="center">
    <img src="https://github.com/PrathuashaKB/ASR-Using-Deep-Learning/blob/main/images/ASD%20Logo.png" width="800"> 
  </p>
</div>


🎙️ *Transforming Voice into Text: Harnessing Deep Learning for Seamless Communication*

**Automatic Speech Recognition** (ASR) is a technique that processes human speech into readable text—commonly known as speech-to-text or transcription systems. This project is designed to develop a simple and functional speech recognition system using advanced **deep learning** methods. ASR is a core technology that improves human-human and human-computer interaction. It enables users to interact with systems using natural speech rather than typing. From customer support chatbots to transcription tools and virtual assistants, ASR has penetrated multiple sectors including healthcare, finance, and education.
Given its growing demand, this project presents an attempt to create a basic speech recognition model using **Wav2Vec2.0**, a state-of-the-art approach developed by Facebook AI and deployed via **Hugging Face** Transformers. It is developed as part of `Mini Project I` during the `V semester-BE` at Sri Siddhartha Institute of Technology, Tumakuru, as a practical exploration of deep learning-based speech recognition systems.

![Python](https://img.shields.io/badge/Python-3.8-blue?style=flat&logo=python&logoColor=white)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-%F0%9F%A7%A0-red?style=flat)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?style=flat&logo=huggingface)
![Wav2Vec2.0](https://img.shields.io/badge/Wav2Vec2.0-ASR-blueviolet?style=flat)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter&logoColor=white)

> ✅ **Mini-Project I** at SSIT | Project Cycle Closed | [Official Guideline](https://github.com/PrathuashaKB/ASR-Using-Deep-Learning/blob/main/MINI%20PROJECT%20I%20Criteria.pdf)

[PROJECT DOCUMENTATION](https://github.com/PrathuashaKB/ASR-Using-Deep-Learning/blob/main/ASR%20report.pdf), you can find the complete project documentation here.

[PROJECT PRESENTATION](https://github.com/PrathuashaKB/ASR-Using-Deep-Learning/blob/main/Project%20Presentation.pptx), you can find the complete project presentation here.


#### *This project is designed to create a simple speech recognition system via Deep learning approach!*

### Features : 
1. Converts speech to text using deep learning.

2. Built with Wav2Vec2.0 model from Hugging Face.

3. Enables human-computer interaction via voice.

4. Suitable for domains like healthcare, finance, and education.

5. Implemented in Python with real-time output.

### Methodology :
1. **Data Acquisition** - Used pre-trained Wav2Vec2.0 model (fine-tuned on English speech datasets) via Hugging Face Transformers.

2. **Audio Input Handling** - Captured or loaded .wav audio files as model input.

3. **Preprocessing**
   - Converted audio into the required format (sampling rate, mono-channel).
   - Tokenized and processed using Wav2Vec2.0 tokenizer.

4. **Model Inference** - Used the Wav2Vec2ForCTC model to generate raw predictions from audio features.

5. **Decoding** - Applied CTC (Connectionist Temporal Classification) decoding to convert logits into final transcribed text.

6. **Output Generation** - Displayed the predicted text in terminal or GUI (optional).

### Technologies required :

 1. Deep-Learning 

 2. Hugging Face

 3. Wav2Vec2.0 Model
 
 4. Python

### System Design :

<img src="https://github.com/PrathuashaKB/ASR-Using-Deep-Learning/blob/main/images/ASR%20simplified%20architecture.png" width="100%"> 

#### Suggestions and project improvement are invited!

#### Prathuasha K B

