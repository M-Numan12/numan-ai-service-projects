import json, os, urllib.request

def synthesize(text, api_key, model='tts-1', voice='alloy'):
    """Call the speech API. Returns MP3 bytes; caller chooses a file destination."""
    payload = json.dumps({'model':model,'voice':voice,'input':text}).encode()
    request = urllib.request.Request('https://api.openai.com/v1/audio/speech',
              data=payload, headers={'Authorization':'Bearer '+api_key,
                                     'Content-Type':'application/json'})
    with urllib.request.urlopen(request,timeout=30) as response: return response.read()

def run(): return {'speech_api_configured':bool(os.getenv('OPENAI_API_KEY')),
                    'example_text':'Hello, welcome to our service.'}

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
