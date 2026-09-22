from collections import defaultdict

def metrics(events):
    by_channel = defaultdict(lambda:{'leads':0,'wins':0})
    for event in events:
        channel = event['channel']
        by_channel[channel]['leads'] += 1
        by_channel[channel]['wins'] += int(event['won'])
    return {channel:{**values,'conversion_percent':round(100*values['wins']/values['leads'],1)}
            for channel,values in by_channel.items()}

def run(): return metrics([{'channel':'web','won':True},
                           {'channel':'web','won':False},{'channel':'referral','won':True}])

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
