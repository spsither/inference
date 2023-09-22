# Django Project to handle STT and TTS api inference request

## API login
`curl -X POST http://localhost:8000/login -d "username=spsither&password=password"`

## Run TTS inference
replace `{token}` with the response from API login
```
curl -X GET http://localhost:8000/tts   \
   -H "Accept: application/json"    \
   -H "Authorization: token {token}"   \
   -d "text=test transcript"
```