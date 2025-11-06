import cv2
import pytesseract
import requests
print(cv2.__version__)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Load image
img = cv2.imread("kanji_sample.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# OCR
text = pytesseract.image_to_string(gray, lang="jpn")
print("Detected text:", text)

# Extract Kanji (basic)
import re
kanji_chars = re.findall(r'[\u4E00-\u9FAF]', text)

# Look up each Kanji meaning
for k in kanji_chars:
    response = requests.get(f"https://jisho.org/api/v1/search/words?keyword={k}")
    data = response.json()
    if data['data']:
        meaning = data['data'][0]['senses'][0]['english_definitions']
        print(f"{k}: {meaning}")
