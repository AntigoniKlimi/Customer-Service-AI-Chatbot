import requests
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect

class ActionDetectLanguage(Action):
    def name(self):
        return "action_detect_language"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get('text')
        current_lang = tracker.get_slot("language")
        
        if current_lang:
            return []  # Αν υπάρχει ήδη γλώσσα, δεν αλλάζουμε κάτι
        
        try:
            lang = detect(user_message)
            if lang not in ["en", "el"]:
                lang = "en"  # Default στα Αγγλικά αν η γλώσσα δεν αναγνωρίζεται
        except:
            lang = "en"  # Default στα Αγγλικά αν υπάρχει σφάλμα
        
        return [SlotSet("language", lang)]


class ActionGetWeather(Action):
    def name(self):
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get('text')
        words = user_message.split()
        city = words[-1] if words else "Athens"

        api_key = "0f2d54bdbb7ac1a95c1c04bb1de3f619"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=el"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                temp = weather_data['main']['temp']
                weather_desc = weather_data['weather'][0]['description']
                
                lang = tracker.get_slot("language")
                if lang == "el":
                    dispatcher.utter_message(text=f"Ο καιρός στην {city} είναι {weather_desc} με θερμοκρασία {temp}°C.")
                else:
                    dispatcher.utter_message(text=f"The weather in {city} is {weather_desc} with a temperature of {temp}°C.")
            else:
                dispatcher.utter_message(text="Sorry, I couldn't retrieve the weather information.")
        
        except requests.exceptions.RequestException:
            dispatcher.utter_message(text="There was a connection issue. Please try again later.")

        return []


class ActionCheckShippingWeather(Action):
    def name(self):
        return "action_check_shipping_weather"

    def run(self, dispatcher, tracker, domain):
        shipping_city = tracker.get_slot("shipping_city") or "Αθήνα"

        api_key = "0f2d54bdbb7ac1a95c1c04bb1de3f619"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={shipping_city}&appid={api_key}&units=metric&lang=el"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                weather_desc = weather_data['weather'][0]['description']
                
                lang = tracker.get_slot("language")
                if lang == "el":
                    if "rain" in weather_desc or "storm" in weather_desc or "snow" in weather_desc:
                        dispatcher.utter_message(text=f"Υπάρχει πιθανότητα καθυστέρησης στην αποστολή λόγω {weather_desc} στην περιοχή {shipping_city}.")
                    else:
                        dispatcher.utter_message(text=f"Ο καιρός στην {shipping_city} είναι {weather_desc}. Η παραγγελία σου δεν θα έχει καθυστερήσεις.")
                else:
                    if "rain" in weather_desc or "storm" in weather_desc or "snow" in weather_desc:
                        dispatcher.utter_message(text=f"There might be a delay in your shipment due to {weather_desc} in {shipping_city}.")
                    else:
                        dispatcher.utter_message(text=f"The weather in {shipping_city} is {weather_desc}. Your order should not be delayed.")

            else:
                dispatcher.utter_message(text="I couldn't check the weather for your shipping location right now.")
        
        except requests.exceptions.RequestException:
            dispatcher.utter_message(text="There was a connection issue. Please try again later.")

        return []


class ActionCancelOrder(Action):
    def name(self):
        return "action_cancel_order"

    def run(self, dispatcher, tracker, domain):
        order_number = tracker.get_slot("order_number")

        # Αν ο χρήστης δεν έχει επιλέξει αριθμό παραγγελίας
        if not order_number:
            dispatcher.utter_message(text="Παρακαλώ επίλεξε έναν αριθμό παραγγελίας από το 1 έως το 10:")
            return []

        # Έλεγχος αν ο αριθμός είναι μεταξύ 1 και 10
        try:
            order_number = int(order_number)
            if 1 <= order_number <= 10:
                dispatcher.utter_message(text=f"Η παραγγελία με αριθμό {order_number} ακυρώθηκε επιτυχώς!")
            else:
                dispatcher.utter_message(text="Ο αριθμός παραγγελίας πρέπει να είναι από 1 έως 10. Δοκίμασε ξανά.")
                return [SlotSet("order_number", None)]  # Διαγράφουμε το λάθος slot για να ζητήσει νέο αριθμό
        except ValueError:
            dispatcher.utter_message(text="Παρακαλώ επίλεξε έναν έγκυρο αριθμό παραγγελίας από το 1 έως το 10.")
            return [SlotSet("order_number", None)]

        return []

sia = SentimentIntensityAnalyzer()

class ActionAnalyzeSentiment(Action):
    def name(self):
        return "action_analyze_sentiment"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get('text')
        sentiment_score = sia.polarity_scores(user_message)
        compound_score = sentiment_score['compound']

        lang = tracker.get_slot("language")

        if compound_score >= 0.05:
            response = "Χαίρομαι που ακούω ότι είσαι ευχαριστημένος!" if lang == "el" else "I'm glad to hear that you're happy!"
        elif compound_score <= -0.05:
            response = "Λυπάμαι που νιώθεις έτσι. Μπορώ να βοηθήσω με κάτι;" if lang == "el" else "I'm sorry you feel that way. Can I help with something?"
        else:
            response = "Εντάξει! Υπάρχει κάτι άλλο που μπορώ να κάνω για εσένα;" if lang == "el" else "Alright! Is there anything else I can do for you?"

        dispatcher.utter_message(text=response)
        return []
    
class ActionTrackOrder(Action):
    def name(self):
        return "action_track_order"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Έλεγξε το status της παραγγελίας σου στο σύστημα!")
        return []
