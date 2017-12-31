from mstranslator import Translator 
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.twiml.voice_response import Play, VoiceResponse
from twilio.rest import Client
from config import twilio_account_sid, twilio_auth_token, ms_api_key
import urllib
 
# Account SID and Auth Token from www.twilio.com/console
client = Client(twilio_account_sid, twilio_auth_token)
app = Flask(__name__)
 
 
# A route to respond to SMS messages and kick off a phone call.
@app.route('/sms', methods=['POST'])
def inbound_sms():
    response = MessagingResponse()
    response.message('Thanks for texting! Translating your text now. '
                     'Wait to receive a phone call :)')
 
    # Grab the text to be translated.
    text = urllib.quote(request.form['Body'])
 
    # Grab the relevant phone numbers.
    from_number = request.form['From']
    to_number = request.form['To']
 
    # Create a phone call that uses our other route to translate the text.
    client.api.account.calls.create(to=from_number, from_=to_number,
                        url='http://fb9b84bb.ngrok.io/call?text={}'
                        .format(text))
 
    return str(response)
 
 
# A route to handle the logic for phone calls.
@app.route('/call', methods=['POST'])
def outbound_call():
    text = request.args.get('text')
    translator = Translator(ms_api_key)
    translated = translator.translate(text, lang_from='en', lang_to='ja')
    translated_audio =  translator.speak(translated,  lang='ja', format='audio/wav')
 
    response = VoiceResponse()
    response.play(translated_audio)
    return str(response)
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)