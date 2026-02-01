import torch
import soundfile as sf
import numpy as np
import datetime
import os
import pygame
from openai import OpenAI
from qwen_tts import Qwen3TTSModel
from dotenv import load_dotenv

# Load API Key dari file .env
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-Base",
    device_map="cuda:0",
    dtype=torch.bfloat16,
    attn_implementation="sdpa"
)

ref_audio = "yae-wav_train.WAV"
ref_text = "I am the Guuji of the Grand Narukami Shrine. The purpose of my visit is to monitor your every move, for such is the order of the shrine... Oh, come on, don't be so nervous"

prompt_items = model.create_voice_clone_prompt(
    ref_audio=ref_audio, 
    ref_text=ref_text
)

pygame.mixer.init()

def chat_with_yae(user_input):
    print("Yae Miko is thinking...")
    response = client.chat.completions.create(
        model="google/gemini-3-flash-preview",
        messages=[
            {
                "role": "system", 
                "content": "You are Yae Miko from Genshin Impact. Speak with her personality: wise, teasing, and elegant. Keep responses concise for TTS."
            },
            {
                "role": "user", "content": user_input
            }
        ]
    )
    return response.choices[0].message.content

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

print("\n--- Chat with Yae Miko (type 'exit' to stop) ---")

while True:
    user_msg = input(f"\nYou: ")
    if user_msg.lower() == "exit":
        break

    ai_response = chat_with_yae(user_msg)
    print(f"Yae Miko: {ai_response}")

    print("\nGenerating voice...")
    wavs, sr = model.generate_voice_clone(
        text=ai_response,
        language="English",  
        voice_clone_prompt=prompt_items 
    )


    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{timestamp}.wav"
    
    audio_data = wavs[0]
    if np.abs(audio_data).max() > 0:
        audio_data = audio_data / np.abs(audio_data).max()
        
    sf.write(filename, audio_data, sr)
    print(f"Audio saved to: {filename}")

    play_audio(filename)