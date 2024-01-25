import speech_recognition as sr
import pyttsx3
import random
from datetime import datetime
from faker import Faker
import torch
from transformers import pipeline
import platform
import cpuinfo
import psutil
import wmi

pc = wmi.WMI()
my_cpu = cpuinfo.get_cpu_info()


class ModelPrompt:
    PROMPT = """Greetings! We're thrilled to assist you with any inquiries or guidance related to Intel products. 
    To ensure we provide you with the most relevant information, 
    could you please share your specific interests or needs? 
    Whether you're exploring the latest innovations, seeking 
    product recommendations, or have questions about our technology, 
    we're here to help you make the most informed decisions."""
    USER_PROMPT_ANALYZE = """Please analyze and benchmark my system. 
    Provide insights on the architecture, processor type, operating system, processor name, total RAM, and graphics card. 
    Ensure to include performance metrics and any recommendations for optimization. Thank you!"""
    USER_PROMPT_ISSUE = """Certainly, I'm here to help. 
    To better understand and diagnose the performance issues, could you provide more details about the specific problems you're encountering? 
    Any error messages, recent changes, or unusual behavior would be valuable information."""
    ARCHITECTURE = f"Architecture : {platform.architecture()}"
    PROCESSOR_TYPE = f"Architecture : {platform.platform()}"
    OPERATING_SYSTEM = f"Architecture : {platform.processor()}"
    PROCESSOR_NAME = f"Processor name: {my_cpu['brand_raw']}"
    TOTAL_RAM = f"Total ram installed: {psutil.virtual_memory().total/1024/1024/1024:.2f} GB"
    GRAPHICS_CARD = f"Graphics card installed: {pc.Win32_VideoController()[0].name}"

class VoiceAssistant:
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.filename_no = random.randint(1,100)
        self.filename = "input"
        self.faker_ = Faker()
        self.stop = "bye"
        self.analyse = "analyse"
        self.issue = "issue"

    
    def speak_text(self,text,rate=170,volume=1.0):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',voices[1].id)
        self.engine.setProperty('rate',rate)
        self.engine.setProperty('volume',volume)
        self.engine.say(text)
        self.engine.runAndWait()
    
    def voice_data(self,audio):
        with open(f"User_Data/{self.filename}_{self.filename_no}.wav","wb") as f:
            f.write(audio.get_wav_data())
    
    def voice_assistant(self):
        self.greet()
        model_prompt = ModelPrompt()
        recognizer = sr.Recognizer()
        voice_bot = True
        while voice_bot:
            with sr.Microphone() as source:
                print("Listening")
                audio = recognizer.listen(source)
                transcription = ""
                print("Recording")
                self.voice_data(audio)
                try:
                    transcription = recognizer.recognize_google(audio)
                    transcription = transcription.lower()
                    print(transcription)
                    vc_model = Model()
                    model_response = vc_model.model_response(transcription,model_prompt.PROMPT)
                    self.speak_text(model_response)
                    print(model_response)
                    if self.stop in transcription:
                        voice_bot = False
                    if self.analyse in transcription:
                        user_response = f"""{model_prompt.ARCHITECTURE} {model_prompt.PROCESSOR_TYPE} {model_prompt.OPERATING_SYSTEM} 
                        {model_prompt.PROCESSOR_NAME} {model_prompt.TOTAL_RAM} {model_prompt.GRAPHICS_CARD}"""
                        model_analyzed = vc_model.model_response(user_response,model_prompt.USER_PROMPT_ANALYZE)
                        self.speak_text(model_analyzed)
                        print(model_analyzed)
                    if self.issue in transcription:
                        model_response = vc_model.model_response(transcription,model_prompt.USER_PROMPT_ISSUE)
                        self.speak_text(model_response)
                        print(model_response)
                except Exception as e:
                    print(f"Exception"+str(e))
       
    def greet(self):
        current_time = datetime.now()
        hour = current_time.hour
        if hour >= 0 and hour < 12:
            self.speak_text(f'Good morning Sir this is {self.faker_.first_name_female()} from Intel Services How can I Help you Today')
        elif hour >= 12 and hour < 18:
            self.speak_text(f'Good afternoon Sir this is {self.faker_.first_name_female()} from Intel Services How can I Help you Today')
        else:
            self.speak_text(f'Good evening Sir this is {self.faker_.first_name_female()} from Intel Services How can I Help you Today')

class Model:
    def __init__(self) -> None:
        self.pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")
    
    def model_response(self,user_input,user_prompt):
        messages = [
        {
        "role": "system",
        "content": "Welcome to the Intel Services. I'm Dr. Intel, your dedicated PC health assistant. How may I assist you with optimizing and maintaining the health of your gaming PC today?",
        },
        {"role": "user", "content": user_input},
        {"role": "assistant", "content":user_prompt },
        ]
        prompt = self.pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        outputs = self.pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
        assistant_response = outputs[0]['generated_text'].split('</s>')[-1].strip()

        assistant_response_bot = assistant_response.replace("<|assistant|>","")

        return assistant_response_bot





jr = VoiceAssistant()
jr.voice_assistant()
