from statistics import mean

def report(daily):
    if not daily: return {'error':'no data'}
    totals = {'leads':sum(x['leads'] for x in daily),
              'deals':sum(x['deals'] for x in daily)}
    totals['conversion_percent'] = round(100*totals['deals']/totals['leads'],1) if totals['leads'] else 0
    totals['alerts'] = ['Conversion below 10%'] if totals['conversion_percent'] < 10 else []
    return totals

def run(): return report([{'leads':24,'deals':2},{'leads':12,'deals':1}])

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
