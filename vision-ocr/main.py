import shutil, subprocess

def extract(image_path):
    if not shutil.which('tesseract'):
        return {'error':'Tesseract OCR is not installed; install it to process local images.'}
    result = subprocess.run(['tesseract',str(image_path),'stdout'],
                            capture_output=True,text=True,check=True,timeout=30)
    return {'text':result.stdout.strip(), 'review_required':True}

def run(): return {'ocr_available':bool(shutil.which('tesseract')),
                    'usage':'python main.py path/to/image.png'}

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
