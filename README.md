# Customer Service AI Chatbot
This AI-powered Customer Service Chatbot is designed to provide users with real-time assistance regarding their orders, shipping status, and frequently asked questions. The chatbot can handle various user queries, retrieve live weather updates, analyze sentiment, and respond dynamically in English and Greek. This project is implemented using the Rasa framework, leveraging natural language understanding (NLU) and machine learning techniques to improve customer interactions.


## Introduction
This AI-powered **Customer Service Chatbot** is designed to provide real-time assistance regarding:
- **Order management** (tracking & cancellation)
- **Shipping status & delays**
- **Frequently Asked Questions (FAQs)**
- **Sentiment Analysis**
- **Multilingual Support** (English & Greek)
- **Real-time Weather Updates**

The chatbot is built using **Rasa**, an advanced conversational AI framework, and integrates **machine learning, APIs, and sentiment analysis** to enhance customer interactions.

## **Features**
###  Order Management  
- Users can **check the status** of their orders.  
- Users can **cancel an order** by providing a valid order number (**1-10**).  
- The chatbot validates inputs and provides appropriate responses.

### FAQ Handling  
- Provides quick responses to common questions about:
  - **Payments**
  - **Returns**
  - **Shipping policies**

### Real-time Weather Integration  
- Retrieves **live weather forecasts** for user-specified locations.  
- Checks if bad weather may **affect shipping times**.

###  Sentiment Analysis  
- Detects **user emotions** (happy, sad, angry, neutral).  
- Adjusts responses based on the sentiment.

###  Multilingual Support  
- Automatically **detects the user’s language** (English or Greek).  
- Replies in the same language as the user.

###  Fallback Handling  
- If the chatbot does not recognize a query, it provides **alternative responses**.
- If an API request **fails**, it **returns a predefined message**.

## **Technologies Used**
- **Rasa 3.6.21** – Conversational AI framework  
- **Python 3.8** – Backend development  
- **OpenWeather API** – Real-time weather data retrieval  
- **NLTK (VADER Sentiment Analysis)** – Sentiment detection  
- **Langdetect** – Automatic language detection  

## **Interaction Scenarios**
###  **1. Order Management**
-Users can **check their order status**.  
-Users can **cancel an order** by providing a valid order number (**1-10**).  
-The chatbot ensures **valid inputs** and **error handling**.

###  **2. FAQ & General Assistance**
 Users can ask about:  
  - **Payment methods**
  - **Return policies**
  - **Shipping options**  
 The chatbot responds with **predefined answers** from an FAQ database.

### **3. Real-World API Integration**
- Users can ask for the **current weather** in a city.  -
- Users can check if bad weather may **delay their shipments**.

## **Real-World API Integrations**
###  **1. OpenWeather API (Weather & Shipping Delay Prediction)**
- Retrieves **live weather forecasts** based on user queries.  
- Determines if **bad weather conditions** may **cause shipping delays**.  
- Implements **robust error handling** for API failures.
API key for OpenWeather (free tier available at https://openweathermap.org/)

### **2. Sentiment Analysis (VADER - NLTK)**
- Analyzes **user emotions** in real-time.  
- Adjusts chatbot responses **based on detected sentiment**.

## **Error Handling & Robustness**
- **Invalid Inputs:**  
   - If a user provides an out-of-range order number, the chatbot **asks them to retry**.  
- **Fallback Responses:**  
   - If an **unrecognized query** is detected, the chatbot provides a **helpful fallback response**.  
- **API Failures:**  
   - If the OpenWeather API **fails**, the chatbot returns a **default response** instead.

## **Changes Made**
To optimize the chatbot's dialogue handling, we implemented the following policy modifications:
- MemoizationPolicy: Increased max_history to 5 to improve recall of past conversations.
- TEDPolicy: Adjusted max_history to 5 and increased epochs to 100 for better learning of conversation patterns.
- UnexpecTEDIntentPolicy: Enabled unexpected intent handling with max_history: 5 and epochs: 100 to improve robustness.
- FallbackClassifier: Configured with a threshold of 0.3 and ambiguity_threshold of 0.1 to enhance responses to unknown inputs.
- LanguageDetector: Added an automatic language detection mechanism to ensure responses align with the user’s language (Greek-English).
- 
 ## Why These Modifications Were Chosen
- The MemoizationPolicy helps the bot remember previous interactions within a session, making conversations more natural and context-aware.
- The TEDPolicy provides a more robust learning process, allowing the chatbot to generalize better across different dialogue flows.
- The UnexpecTEDIntentPolicy ensures the bot can handle unpredictable user inputs without breaking the conversation.
- The fallback responses were designed to be more informative based on internal testing.
- The LanguageDetector ensures smooth multilingual support by dynamically detecting the user’s language and responding accordingly.

 ## Observed Results and Insights
- Improved response accuracy: The chatbot now provides more context-aware answers, thanks to the enhanced MemoizationPolicy and TEDPolicy.
- Better handling of unexpected inputs: The UnexpecTEDIntentPolicy significantly reduced chatbot failures in handling uncommon queries.
- Preliminary tests suggest that fallback responses are more informative compared to a generic error message.

## **Future Improvements**
- Imrove the multilingual chatbot with nlp models such as fasstext
- Replace VADER with a Bert model
-Expand support for more languages beyond English & Greek.
-Implement more APIs for tracking orders in real-time.
-Add voice integration for a more interactive experience.

# Authors
# Antigoni Klimi – M.Sc. Student in Language Technology
# GitHub: AntigoniKlimi
