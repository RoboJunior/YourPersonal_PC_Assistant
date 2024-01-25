
# Voice Assistant for Intel Services

## Overview

This project implements a voice-based virtual assistant designed to assist users with inquiries related to Intel products. The voice assistant is capable of providing information, answering questions, and analyzing system specifications. It utilizes speech recognition, text generation, and system information retrieval to offer a comprehensive user experience.

## Features
Greeting Functionality: The voice assistant greets the user based on the time of day, creating a personalized interaction.

**Speech Recognition:** The assistant utilizes the SpeechRecognition library to transcribe user input from spoken language to text.

**Text Generation Model:** Powered by the Hugging Face Transformers library, the assistant leverages a text generation model to formulate responses to user queries and prompts.

**System Analysis:** The assistant can analyze and benchmark the user's system, providing insights on architecture, processor type, operating system, processor name, total RAM, and graphics card.

**Issue Resolution Assistance:** Users can seek help for performance issues, and the assistant will prompt for additional details to diagnose and provide relevant information.

**Persistent User Interaction:** The voice assistant continuously listens for user input until the user says "bye," allowing for an ongoing conversation.

## Technologies Used
**Python:** The primary programming language for implementing the voice assistant.

**SpeechRecognition:** Library for recognizing speech input.

**pyttsx3:** Text-to-speech library for generating voice responses.

**Hugging Face Transformers:** Used for the text generation model.

**Faker:** Generates fake data for a more personalized interaction.

**psutil**, **wmi**, **cpuinfo:** Libraries for retrieving system information.
## Usage
Users can interact with the voice assistant by speaking into the microphone. The assistant responds to greetings, system analysis requests, and performance issue prompts.

## Setup Instructions
Install the required Python libraries: **speech_recognition**, **pyttsx3**, **faker**, **torch**, **transformers**.
Ensure the necessary models are available for the Hugging Face Transformers library.
Run the **VoiceAssistant** class to start the voice assistant.

Feel free to explore, contribute, and enhance the capabilities of this voice assistant for a more intuitive and informative user experience.


## Related

If you want a clear understanding of this project refer to the below project 
👇


[Voice Assistant Ai](https://github.com/RoboJunior/Voice_Assistant_Ai)

## Documentation
This model was taken from hugging face click the below link for downloading the weights of the model from hugging face

[Model](https://linktodocumentation) 📌


## Authors

- [@RoboJunior](https://github.com/RoboJunior) 👨‍💻



