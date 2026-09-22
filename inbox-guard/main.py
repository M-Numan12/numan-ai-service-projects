from datetime import datetime, timezone
import re

def eligible(thread, now):
    address = thread['recipient'].lower()
    if re.search(r'(no-?reply|do-?not-?reply)', address): return False
    if thread.get('human_reply') or thread.get('followed_up'): return False
    if thread.get('bounce') or thread.get('rejection') or thread.get('unsubscribe'): return False
    sent = datetime.fromisoformat(thread['sent_at'])
    return (now - sent).total_seconds() >= 86400

def run():
    now = datetime(2026, 10, 5, 12, tzinfo=timezone.utc)
    threads = [{'recipient':'hello@example.org','sent_at':'2026-10-03T12:00:00+00:00'},
               {'recipient':'noreply@example.org','sent_at':'2026-10-02T12:00:00+00:00'}]
    return [{'recipient':t['recipient'], 'eligible':eligible(t, now)} for t in threads]

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
