import hashlib, hmac, json, os

def verify_signature(body, signature, secret):
    expected = 'sha256=' + hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)

def handle(body, signature, secret):
    if not verify_signature(body, signature, secret): return {'error':'invalid signature'}
    payload = json.loads(body)
    incoming = payload.get('message','').strip().lower()
    if incoming in ('hello','hi'): return {'reply':'Hello! Tell us what you need help with.'}
    return {'reply':'A member of our team will respond shortly.'}

def run():
    body = b'{"message":"hello"}'; secret = 'demo-only-secret'
    sig = 'sha256=' + hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    return handle(body, sig, secret)

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
