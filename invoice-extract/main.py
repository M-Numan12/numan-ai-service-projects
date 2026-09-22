import re
from decimal import Decimal

def extract(text):
    number = re.search(r'Invoice\s*#?\s*([A-Z0-9-]+)', text, re.I)
    total = re.search(r'Total\s*:?\s*\$?([\d,.]+)', text, re.I)
    if not number or not total: return {'status':'manual review required'}
    return {'invoice':number.group(1), 'total':str(Decimal(total.group(1).replace(',',''))),
            'status':'extracted; verify before payment'}

def run(): return extract('Invoice #INV-204\nCustomer: Demo Co\nTotal: $1,250.00')

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
