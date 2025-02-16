# Customer Service AI Chatbot
# Introduction
This AI-powered Customer Service Chatbot is designed to provide users with real-time assistance regarding their orders, shipping status, and frequently asked questions. The chatbot can handle various user queries, retrieve live weather updates, analyze sentiment, and respond dynamically in English and Greek. This project is implemented using the Rasa framework, leveraging natural language understanding (NLU) and machine learning techniques to improve customer interactions.

# Features
1.Order Management: Users can check their order status or request order cancellation.
2.FAQ Handling: Provides quick responses to common questions about payments, returns, and shipping.
3.Real-time Weather Integration: Retrieves weather forecasts and checks weather conditions that might affect deliveries.
4.Sentiment Analysis: Detects user emotions (happy, sad, angry, etc.) and adapts responses accordingly.
5. Multilingual Support: Detects user language and responds in either English or Greek.
6.Fallback Handling: If an API request fails or an unrecognized intent is received, the chatbot provides alternative responses.

# Technologies Used
Rasa 3.6.21 – Conversational AI framework Python 3.8 – Backend development OpenWeather API – Real-time weather data retrieval NLTK (VADER Sentiment Analysis) – Sentiment detection Langdetect – Automatic language detection

# Interaction Scenarios
1. Order Management Users can check their order status. Users can cancel an order by providing a valid order number (1-10). The chatbot ensures valid inputs and provides appropriate responses.
2.FAQ & General Assistance Users can ask about payment methods, return policies, and shipping options. The chatbot responds with predefined answers based on frequently asked questions.
3. Real-World Data Integration Users can inquire about the weather for a specific city. Users can check if bad weather may cause shipping delays.
   
# Real-World API Integrations 
1.OpenWeather API (Weather & Shipping Delay Prediction) Retrieves live weather forecasts based on user queries. Determines if weather conditions may delay an order. Implements robust error handling for API failures.
2. Sentiment Analysis (VADER - NLTK)
Analyzes user emotions (happy, sad, angry, neutral) and adjusts responses based on the detected sentiment.

# Error Handling & Robustness
Invalid Inputs: If a user provides an out-of-range order number, the chatbot prompts them to retry. Fallback Responses: If the chatbot doesn’t recognize a query, it provides a helpful fallback response. API Failures: If the OpenWeather API is unavailable, the chatbot returns a predefined response.

# Installation & Setup
Prerequisites Python 3.8 installed Rasa installed (pip install rasa) API key for OpenWeather (free tier available at https://openweathermap.org/)
