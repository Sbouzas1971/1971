# Import the necessary libraries
from google.cloud import speech_v1 as speech # Corrected import
import os

# Set the path to your service account JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = """
{
  "type": "service_account",
  "project_id": "glassy-storm-441717-p1",
  "private_key_id": "fba07f642a178f10b81b81610191f43d330e7868",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHFqneeu33yL+X\nFZQ6fsob50HfyEspa8cvRvMv8SiLSWcpJDezmy/WsVr1iMhTfwA2Tb1jlVZGohTA\nsmjUBBRO0Vn2KB5v/9CUrQYc/Xt/opKQY1zlxHliB8Thp6CT9w89rJAxkbYUpa7s\nNZq+3zNZReyXj28RiSn3eZXb8Hs5rnQGtr0bYUqMlvOHiv14RYsYVD0jxM8WQ8Zh\nll0nQ7aJEMqZvN8jm6kCGYE3eGWYzbKYRrsS3z+lYZ4jboP/FN8WSEn2JVtFHOje\nmm8dnObnHwcn5Q1aKjk1ziXQVazQh3X4vIY0nQGFoyUE4w3iyQj5cblYDDeLLrQr\nAbDjkbN7AgMBAAECggEAQUAg0Z25s830WUjFybw3cpjDYtxrIfrEkC6xUsO39ZrL\nuFS5+uBAeB2twa6gdZk40RN+oI5X9hN2OMfgiqiBnWmJEiAJBc0yqB/jUooTuXvn\njHI8hsPzwpjoQsslWomNUbnmkpB+vFqnL5zMCIXv9vDvf6cPkJBDlGwhnTG+uWLr\nMvgTcUjWRXE5u7xlSP5+/vlLELk0lORERHr/6zt/SLndqL71dwPp6XhoiZHDpSHq\nldIe9y8xaaLj9uLUQSSwB5qWHDuviR5KIGWJWUvJ3u9n8cfXbbRrZeIOp/0VLMMf\ntHeEHkLnU5vAqA9h0SPqcpbZS++VVw/ok+2in97+ZQKBgQDwubHkkny+dAvZzQss\n1J9+J2qym0DokG5I769yYC7dybeyDRVOYL2QL8f7vyP9kosImcOdrTC79lgy1kDg\nW7DqNRO0VcIKyFIKf4P80z1/ItlaPeZIM0F0atN+6Zpk+Xdo/C0VWzPG2hMtRFTU\nLojcMyAQr0Ku9oYcG3KsjTxQXwKBgQDTuKBYcawpMbP47HowdUPa/2O9SxQ0QMfo\nPHyeXc1AxKBGClgOQvqwnvJS0sS45EGzt3t70pPjPbauSopznRYamQhSuyQewrIT\nWKNOb6nc+ZXnupSkCUzJRUSNGPhxj+UMvDXnPJ56sgJeaDXdQly5Z7OiiS5lKFwP\nBpBQvuLCZQKBgDYmL0PxR6o3xGqr2vWspmvkRfYDQmiOBKDXeanKxQAS3gVpN/+3\ndyy18tBIQLpLeobmv7/6M1o0ocZdt55AQd2NLu+D0vBF+15tLK10fwLYPfg0sFZR\nYUnktcp4lchc7WVqRGHncBAtAd9O3Z4VEagmv/HA2sksnyI3cmYqJwUVAoGBAIfD\np4avdc+AoMCpm30BZT7EcAfNYipTtB0W1G6VBe5XZ9MiBO84QhsKAafcoetR61O7\n/8IZ+V1JkKBZCkky3R63LSAoAvR6ssg3GZlNf2ZE4byT54b8s7GI6nl0HrRrqlwt\nQH+EXrec+Gnjd07npB/8ALPkNc0GQWodMmOk1DIFAoGAPinssjpAXp4nvyqztQ81\nNJHYuKlv7UiQepr4eXup+hzXOXkGbdYGQfzjHxRAYMhTQ8RgPLEB/ysacUKHT1Ew\nvdOQA9NefroSaXhhRjY8CUeJv1PvYZyluly1ngHZ/huuL3UVR6SJflnSKLa5xUWZ\nuMrqe0/mypbYukmnYnMfcOQ=\n-----END PRIVATE KEY-----\n",
     "client_email": "nexus-954@glassy-storm-441717-p1.iam.gserviceaccount.com",
     "client_id": "104920924837769464757",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/nexus-954%40glassy-storm-441717-p1.iam.gserviceaccount.com",
     "universe_domain": "googleapis.com"
   }
   """

# Create a SpeechClient object
client = speech.SpeechClient()

# The language of the request
language_code = "en-US"  # English (US)

# Sample audio file (replace with your audio file)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.FLAC,  # Set encoding to FLAC
    sample_rate_hertz=44100,
    language_code=language_code,
)

# Replace "gs://your-bucket-name/myaudio.wav" with the actual path to your audio file in your bucket
audio = speech.RecognitionAudio(uri="gs://nexustest/Spring Run Ave.m4a")  # Replace with your audio file in your bucket

# Send the request to the Speech-to-Text API
response = client.recognize(config=config, audio=audio)

# Print the transcription results
for result in response.results:
    # The first alternative is the most likely one for this portion
    alternative = result.alternatives[0]
    print(u"Transcript: {}".format(alternative.transcript))