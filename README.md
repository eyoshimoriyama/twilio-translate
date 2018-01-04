# Twilio Translate

This repository contains a Flask app that hooks up a Twilio phone number to receieve text messages in English and return a phone call with a audio translation in Japanese. 


### Using the App
You can send a text in English to 909-675-0677 and you will shortly after recieve a phone call with your text spoken in Japanese.


### Recreating the App
In order to run your own version of the app and add more functionality, you'll need a Twilio account and Mircsoft Azure account.

You can create a free Twilio account to get your `twilio_account_sid` and `twilio_auth_token` and setup a new phone number. You can sign up here: https://www.twilio.com/try-twilio.

This app also uses the Microsoft Translator API to translate the text message. You can setup a Microsoft Azure account and get your `ms_api_key` by signing up here: https://azure.microsoft.com.
