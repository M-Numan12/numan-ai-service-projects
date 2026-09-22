def guide(message):
    text = message.lower()
    if 'deadline' in text: return {'answer':'Application deadline: 15 November.', 'source':'demo policy 2026'}
    if 'documents' in text: return {'answer':'Prepare your transcript and proof of identity.', 'source':'demo checklist'}
    return {'answer':'Please contact the admissions office for a confirmed answer.', 'source':None}

def run(): return guide('Which documents do I need?')

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
