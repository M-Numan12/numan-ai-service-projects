MESSAGES = {'en':{'greeting':'Hello! How may we help?', 'hours':'We are open 9am to 5pm.'},
            'ur':{'greeting':'Assalam-o-alaikum! Hum kaise madad kar sakte hain?',
                  'hours':'Hum subah 9 se shaam 5 baje tak khule hain.'},
            'es':{'greeting':'¡Hola! ¿Cómo podemos ayudar?',
                  'hours':'Abrimos de 9 a 17 h.'}}

def respond(intent, locale):
    messages = MESSAGES.get(locale, MESSAGES['en'])
    return {'locale':locale if locale in MESSAGES else 'en',
            'message':messages.get(intent, 'Please contact our team.')}

def run(): return respond('hours','ur')

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
