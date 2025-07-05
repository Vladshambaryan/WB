import requests
import json

url = "https://cart-storage-api.wildberries.ru/api/basket/sync?ts=1751662514844&device_id=site_dba65f37f05745cea815c8d3234c3bf5"

payload = json.dumps([
  {
    "chrt_id": 501748116,
    "quantity": 1,
    "cod_1s": 336013037,
    "client_ts": 1751662662,
    "op_type": 1,
    "target_url": "EX|4|MCS|CR|||||||||",
    "meta_json": "{\"analitic\":{\"tailObject\":{\"loc\":\"MCS\",\"loc_way\":\"CR\",\"sort\":\"\",\"terms\":{\"catalog_type\":\"presets\",\"catalog_value\":\"preset=1000189506\",\"preset_type\":\"sim\",\"recid\":\"recid784401762175166261820250704205658\"}},\"logs\":\"\"},\"originalPrice\":{\"price\":\"489\",\"currency\":\"RUB\"}}",
    "price": 48900,
    "subject_id": 2150,
    "currency": "RUB",
    "timezonemin": 240
  }
])
headers = {
  'accept': '*/*',
  'accept-language': 'ru,en-US;q=0.9,en;q=0.8,hy;q=0.7',
  'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NTE2NjI0NDUsInVzZXIiOiIxMDU0MDA1NzkiLCJzaGFyZF9rZXkiOiI0IiwiY2xpZW50X2lkIjoid2IiLCJzZXNzaW9uX2lkIjoiNDMwNjlkMDBjZThiNGJjYTk3N2NiNGM5MzNmNWZiZWQiLCJ2YWxpZGF0aW9uX2tleSI6ImI4MjRmZWMzZWE0NzA0NTFhYzI0NzkzZDJhNTJkYjdkY2ZjNjAxZDIzYzY4ZGIyZDIwNDE2Njg0YjFkOTE4YjciLCJwaG9uZSI6IjJ3cnoweU5LRFhLNm1EVnhacEo3Y1E9PSIsInVzZXJfcmVnaXN0cmF0aW9uX2R0IjoxNjc3NjEwOTU5LCJ2ZXJzaW9uIjoyfQ.KTLyXGd30BCqPEgOiNOXkzxgYIkSjIdIRm34FXJLtzLcKrCw1eTT0g_1yww6k5Q4Ylg90mC7qxzhb81LW1pgXPuzzpW0a-VHcgIwKxSim1rA7wAZUc1-5gMZfPgKtU3YerBl55OiVNzwWPfhSgkkDC_VWJJ87PmTESLY5Ybr-SNRehFHIq96-Y4aQBjYcC5FULa5Uc_lK-jMPQFfMcw9jJW_lTANDZZI_PUIwb9ygzVPo3O-0Bb8U1z9LlP3_iNjIyI0-pnHuGlFNGg2mJMyzxOCalLn9J6vIWa-eJDp6X-AR6A2PWfSWX_wfn92uD6uGqCUjlK-j2LFrvTpgZlFsA',
  'content-type': 'application/json',
  'origin': 'https://www.wildberries.ru',
  'priority': 'u=1, i',
  'referer': 'https://www.wildberries.ru/',
  'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
  'wb-apptype': 'site'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
