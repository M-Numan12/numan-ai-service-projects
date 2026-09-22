def triage(ticket):
    text = ticket['text'].lower()
    if any(word in text for word in ('refund', 'chargeback', 'security')):
        return {'id':ticket['id'], 'queue':'human review', 'priority':'high', 'reply':None}
    if 'password' in text:
        return {'id':ticket['id'], 'queue':'account help', 'priority':'normal',
                'reply':'Please use the account reset page. Never send a password in email.'}
    return {'id':ticket['id'], 'queue':'general support', 'priority':'normal',
            'reply':'Thanks for contacting us. A team member will review your request.'}

def run():
    return [triage(t) for t in [{'id':1,'text':'I forgot my password'},
                                {'id':2,'text':'I need a refund'},
                                {'id':3,'text':'Can you update my details?'}]]

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
