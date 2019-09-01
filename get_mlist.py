import json
import random
import time
import re
import subprocess


text = ''
with open('text', 'r') as lines:
    for line in lines:
        text += line

start            = '<a class="yt-simple-endpoint style-scope ytd-playlist-video-renderer" href="/watch?v='
end              = '&amp;list='

music            = re.findall('{}(.*?){}'.format(re.escape(start), re.escape(end)), text)
url_req          = """curl 'https://www.youtube.com/service_ajax?name=playlistEditEndpoint' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://www.youtube.com/playlist?list={current_playlist}' -H 'X-YouTube-Client-Name: 1' -H 'X-YouTube-Client-Version: 2.20190711' -H 'X-Youtube-Identity-Token: QUFFLUhqbVY2TkNzcEN0TFZvcUpXUjEtZlQtaUtYRVgzd3w=' -H 'X-YouTube-Page-CL: 257652704' -H 'X-YouTube-Page-Label: youtube.ytfe.desktop_20190710_8_RC2' -H 'X-YouTube-Variants-Checksum: 14c85a2b55384b5479272a868615c2a6' -H 'X-YouTube-Utc-Offset: 480' -H 'X-SPF-Referer: https://www.youtube.com/playlist?list={current_playlist}' -H 'X-SPF-Previous: https://www.youtube.com/playlist?list={current_playlist}' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Connection: keep-alive' -H 'Cookie: SID=mAdcHIWsnUuZxpaRE1505TbVfAdgsvqtWiwBf7r8U0RoUqjWR2btv7TgJiHkFWqHE2PLMQ.; HSID=Aa-1h5owbXmqKfOFf; SSID=AU_hbP0IL8ga172Yt; APISID=jTMvU0x5fs_2R3KB/AYF49Wtl47fgM4F9e; SAPISID=YYhV74w_qIoJ9jiG/AmbnxXM0R22BXggKw; LOGIN_INFO=AFmmF2swRgIhAKzFWMgETZipBrIi6KaN2kE3cAkeRmKKcoP7K6tvhKMBAiEA1xpbupOknPYKAga7qLhN_Cm5du3cncZAL2DTOaXT_VQ:QUQ3MjNmeWlOajIxMng2LWFfNmZlV3lvN1hMTTd5elNXQ2tiRDVQZjVkaWpwQ2tqOEhMYzNWVmtpdlBKVmE5Tnc5UjNKaDByTmVKeEJkTkFaOHU3c1pkSWJsWk5CeWJ1Z1VZWllSenJJeEtRUHBNellkMWpxTk9ib0c4S1dkbXJOTmpxSDM0aGt2Z2oyZGp4MDJGRE1XYzVucDFZMHlxU2t4U3VlRDIxUXF3SnUzMW5vZ0M1VjNF; VISITOR_INFO1_LIVE=hyjEsX__4UQ; PREF=al=ru&f1=50000000&f5=30; SIDCC=AN0-TYuE_901MHGHZSQoJjO4uDSY0QcrybDI2WhVZv6pUXaKthhQW7PBBHSPzGyQ0d445yRSgA; YSC=BnscHJc310c; s_gl=c2b7e804c78d5155b602c25657860b1ecwIAAABSVQ==; ST-1w9u2il=itct=IhMIzof79u-x4wIVSy6yCh3BKQGF&csn=B8kpXYzkA8Lg7QT535iwCQ' -H 'TE: Trailers' --data 'sej=%7B%22clickTrackingParams%22%3A%22IhMIzof79u-x4wIVSy6yCh3BKQGF%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fservice_ajax%22%2C%22sendPost%22%3Atrue%7D%7D%2C%22playlistEditEndpoint%22%3A%7B%22playlistId%22%3A%22{new_playlist}%22%2C%22actions%22%3A%5B%7B%22addedVideoId%22%3A%22{video_name}%22%2C%22action%22%3A%22ACTION_ADD_VIDEO%22%7D%5D%7D%7D&csn=B8kpXYzkA8Lg7QT535iwCQ&session_token=QUFFLUhqblJXYTRjT0hwM3dSR0VJbjRfLWRpdktYeVZvd3xBQ3Jtc0trNHQ0RFNyNS1xOHBrWnFqVUNTYVlrc1FlMkd6ZXl0OVkyVHNjMnk1MVlYVGYwanNNNGZZeUV1Z1VGX0pQaWc3RVlwb3NnTURlN2J6eWNEUEttekx0Ukl6dTFCdXo0VXh6QkpWMGlkYnJzZjQ2eS0tSHRFWGtVR1BjeEZGRXlWekdub20ybVV0SkZtMW9QMDVJVUlHWUtLcndRR3c%3D' > log"""
current_playlist = 'LLM9kGVK051O9s5Bkz-s0pSQ'
new_playlist     = 'PLwWKeMd0d_L9OVHSPeepnrlUGiHmhoN28'

index = 1
for item in music:
    video_name = item
    subprocess.call([url_req.format(video_name=video_name, current_playlist=current_playlist, new_playlist=new_playlist), '-q'], shell=True)
    print('Add video №{}'.format(index))
    index += 1
    time.sleep(random.randint(1, 5))

print('grats')
