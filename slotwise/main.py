from datetime import datetime, timedelta

def book(request, busy):
    start = datetime.fromisoformat(request['start'])
    end = start + timedelta(minutes=request['duration_minutes'])
    if start.hour < 9 or end.hour > 17 or start.date() != end.date():
        return {'status':'outside business hours'}
    for item in busy:
        a = datetime.fromisoformat(item['start']); b = datetime.fromisoformat(item['end'])
        if start < b and end > a: return {'status':'slot unavailable'}
    return {'status':'available', 'start':start.isoformat(), 'end':end.isoformat()}

def run():
    return book({'start':'2026-10-05T11:00:00','duration_minutes':30},
                [{'start':'2026-10-05T10:00:00','end':'2026-10-05T10:30:00'}])

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
