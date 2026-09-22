import json, os, urllib.request

PROVIDERS = {'openai':('https://api.openai.com/v1/responses','OPENAI_API_KEY'),
             'gemini':('https://generativelanguage.googleapis.com/v1beta/openai/chat/completions','GEMINI_API_KEY'),
             'claude':('https://api.anthropic.com/v1/messages','ANTHROPIC_API_KEY')}

def configuration(provider):
    if provider not in PROVIDERS: raise ValueError('unknown provider')
    endpoint, key_name = PROVIDERS[provider]
    return {'endpoint':endpoint, 'configured':bool(os.environ.get(key_name)),
            'credential_env':key_name}

def run(): return {name:configuration(name) for name in PROVIDERS}

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
