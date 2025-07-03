import string
import random
import secrets
import requests
import re
import os
import bcrypt
import africastalking
import streamlit as st 
import google.generativeai as genai
import base64


from io import BytesIO
from dotenv import load_dotenv
from google.genai import types

from geopy.geocoders import Nominatim

import folium
import overpy
# from google.generativeai.types import GenerationConfig


load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

nvidia_api = os.getenv("NVIDIA_API_KEY")

sms = africastalking.SMS
airtime = africastalking.Airtime
voice = africastalking.Voice

def send_otp(phone_number, otp_sms):
    # amount = "10"
    # currency_code = "KES"

    recipients = [f"+254{str(phone_number)}"]

    # airtime_rec = "+254" + str(phone_number)

    print(recipients)
    print(phone_number)

    # Set your message
    message = f"{otp_sms}";

    # Set your shortCode or senderId
    sender = 20880

    try:
        # responses = airtime.send(phone_number=airtime_rec, amount=amount, currency_code=currency_code)
        response = sms.send(message, recipients, sender)

        print(response)

        # print(responses)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    st.toast(f"OTP Sent Successfully")



def send_drug_reminder(phone_number, time, drug_name):

    recipients = [f"+254{str(phone_number)}"]

    # Set your message
    message = f"You have to take your {drug_name} today at {time} as prescribed. Get well soon!";

    # Set your shortCode or senderId
    sender = 20880

    try:
        response = sms.send(message, recipients, sender)

        print(response)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    st.toast(f"Reminder Sent Successfully")




def welcome_message(first_name, phone_number):

    recipients = [f"+254{str(phone_number)}"]

    print(recipients)
    print(phone_number)

    # Set your message
    message = f"Hi {first_name}, Welcome to RxEye! Your digital eye for safe medication use.";

    # Set your shortCode or senderId
    sender = 20880

    try:
        response = sms.send(message, recipients, sender)

        print(response)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    st.toast(f"Account Created Successfully")



def make_call(phone_number):    
  
  # Set your Africa's Talking phone number in international format
    callFrom = "+254730731123"
  
  # Set the numbers you want to call to in a comma-separated list
    callTo   = [f"+254{str(phone_number)}"]
    
    try:
  # Make the call
        result = voice.call(callFrom, callTo)
        # print (result)
        return result
    except Exception as e:
        # print ("Encountered an error while making the call:%s" %str(e))
        return f"Encountered an error while making the call:%s" %str(e)



def generate_otp(length=6):
    characters = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))



def check_and_encrypt_password(password: str, confirm_password: str):
    
    if password != confirm_password:
        return st.error("Error: Passwords do not match!")

    if len(password) < 8:
        return st.error(f"Error: Password must be at least 8 characters long!")
    
    if not re.search(r"[A-Z]", password):
        return st.error(f"Error: Password must contain at least one uppercase letter!")
    
    if not re.search(r"\d", password):
        return st.error(f"Error: Password must contain at least one number!")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return st.error(f"Error: Password must contain at least one special character!")

    # Encrypt password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return st.text_input(label='Encrypted password', value=hashed_password.decode(), type='password')



def autogenerate_weekly_outfit(prompt):

    model = genai.GenerativeModel("gemini-2.0-flash", 

        system_instruction = f"""
        
            You are a smart fashion assistant. Based on the user's gender, body type, race, outfit preference, and occasion, generate a weekly outfit plan as a 7-day table.
            Each day's recommendation should include specific clothing items — such as shirts, pants, dresses, shoes, and accessories — not general styles like sporty or 
            formal. Tailor each outfit to suit the user's inputs. Return only the table, concise and outfit-specific.

            """

            )


    response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=1.5, 
      )
    
    )


    
    return response.text



def autogenerate_daily_outfit(prompt):

    model = genai.GenerativeModel("gemini-2.0-flash", 

        system_instruction = f"""
        
            You are an expert fashion assistant. Your job is to return a complete daily outfit recommendation:

            Your response should:
            - Be short and focused.
            - Only return a specific outfit description — not a general style or explanation.
            - Include actual clothing items and accessories that match the context.
            - Avoid any greetings, reasoning, or extra comments — just the outfit.

            """

            )


    response = model.generate_content(
        f"""

        Based on the user's personal style profile, generate a complete outfit recommendation for today.

        {prompt}

        Your response must:
        - Return only the full outfit suggestion, from top to bottom (e.g., hat, top, bottoms, shoes, accessories).
        - Be concise, fashion-forward, and practical for the specified occasion.
        - Use current urban/streetwear/fashionable descriptions.
        - If possible, include a brief, relevant visual description for image generation (e.g., “Prompt: ...”).

        Respond with the outfit suggestion below:

        """,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=1.5, 
      )
    
    )

    
    return response.text



def get_medical_info(image, base_prompt):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        
        prompt = f"""

            You are a medical assistant AI specialized in pharmaceutical recognition and drug analysis. When a user provides an image of a drug, prescription, or medication packaging, you must:

            Identify the name of the drug from the label or pill design.

                - Describe its primary use or disease it treats.
                - List common side effects, dosage instructions, treatment duration, and usage warnings.
                - Mention if a prescription is required or if it’s over-the-counter (OTC).
                - Optionally provide alternative brands or generic names, if known.

            Use only verified medical knowledge from reputable sources (e.g. WHO, MedlinePlus, FDA).

            🔐 You must not make up drug names or uses. If the image is unclear or confidence is low, politely ask for a clearer image or additional information.

            🎯 Your answers must be:

                - Short and medically precise
                - Clear to a non-expert user
                - Free of medical jargon unless explained
                - Focused on real-life use cases and safety

            ❌ Do not give personal diagnoses or prescriptions. Always recommend consulting a licensed healthcare professional for treatment.
            
            {base_prompt}
            
            """

        
        # Generate content with temperature set to 1.5
        generation_config = genai.types.GenerationConfig(temperature=0.1)
        response = model.generate_content(
            [prompt, image],
            generation_config=generation_config
        )
        return response.text
    
    except Exception as e:
        return f"Error generating roast: {str(e)}"





def generate_outfit_image(prompt):

    invoke_url = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-dev"

    headers = {
        "Authorization": f"Bearer {nvidia_api}",
        "Accept": "application/json",
    }

    payload = {
        "prompt": prompt + " \ngenerate an image of a relevant person wearing that specific outfit, consider the gender",
        "mode": "base",
        "cfg_scale": 3.5,
        "width": 1024,
        "height": 1024,
        "seed": 0,
        "steps": 50
    }

    response = requests.post(invoke_url, headers=headers, json=payload)

    response.raise_for_status()
    response_body = response.json()
    st.write(response_body)
    

    # Example: Check for base64 or URL depending on what the API gives
    # Option 1: If image is base64
    # if "image" in response_body:
    #     img_base64 = response_body["image"]
    #     image_data = BytesIO(base64.b64decode(img_base64))
    #     st.image(image_data, caption="Your AI-generated outfit", use_column_width=True)

    # # Option 2: If image is a URL
    # elif "image_url" in response_body:
    #     st.image(response_body["image_url"], caption="Your AI-generated outfit", use_column_width=True)

    # else:
    #     st.error("Image generation failed. No image data returned.")


def google_image_generator(prompt):
    # Initialize the model
    model = genai.GenerativeModel("gemini-2.0-flash-preview-image-generation")

    # Correct config format
    config = types.GenerateContentConfig( 
        response_modalities=["IMAGE"],  
    )

    # Call generate_content using the config object
    response = model.models.generate_content(
        contents=[{"role": "user", "parts": [prompt]}],
        generation_config={"temperature": 0.8},
        config=config
    )

    # Render the image in Streamlit
    for part in response.candidates[0].content.parts:
        if hasattr(part, 'inline_data') and part.inline_data:
            image = Image.open(BytesIO(part.inline_data.data))
            st.image(image, caption="Your AI-generated outfit", use_column_width=True)



def plot_health_facilities(location_name: str, area_coverage_m: int):
        # Step 1: Get coordinates
        geolocator = Nominatim(user_agent="rxeye_locator")
        location = geolocator.geocode(location_name)
        if not location:
            raise ValueError(f"Could not find location: {location_name}")

        lat, lon = location.latitude, location.longitude

        # Step 2: Overpass API query
        api = overpy.Overpass()
        radius = area_coverage_m

        query = f"""
        (
        node["amenity"~"clinic|hospital|pharmacy|doctors|dispensary"](around:{radius},{lat},{lon});
        node["healthcare"](around:{radius},{lat},{lon});
        node["shop"="medical_supply"](around:{radius},{lat},{lon});
        );
        out center;
        """

        result = api.query(query)

        # Step 3: Initialize map
        m = folium.Map(location=[lat, lon], zoom_start=14)
        folium.Marker([lat, lon], tooltip="Search Center", icon=folium.Icon(color='blue')).add_to(m)

        # Step 4: Add facility markers
        for node in result.nodes:
            name = node.tags.get("name", "Unnamed Facility")
            amenity = node.tags.get("amenity", node.tags.get("shop", "healthcare"))
            folium.Marker(
                location=[node.lat, node.lon],
                popup=f"<b>{name}</b><br>{amenity.title()}",
                icon=folium.Icon(color='red', icon='plus-sign')
            ).add_to(m)

        return m