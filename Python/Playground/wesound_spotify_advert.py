import requests
from time import sleep

urlPlay = "https://api.spotify.com/v1/me/player/play"
urlPause = "https://api.spotify.com/v1/me/player/pause"


payloadDescarga = "{\n\t\"position_ms\":74400,\n\t\"uris\": [\"spotify:track:161gOWTZqCKPw7S5cRJ1BQ\"]\n}"
payloadWe = "{\n\t\"position_ms\":34200,\n\t\"uris\": [\"spotify:track:1lCRw5FEZ1gPDNPzy1K4zW\"]\n}"
payloadSound = "{\n\t\"position_ms\":83100,\n\t\"uris\": [\"spotify:track:4jVQBszyxsa0GeRSe5ToVC\"]\n}"

payloadDale = "{\n\t\"position_ms\":10000,\n\t\"uris\": [\"spotify:track:3F2qAJPgxhzobZX4kbgjWC\"]\n}"
payloadUna = "{\n\t\"position_ms\":7500,\n\t\"uris\": [\"spotify:track:3zb856RMKFjdvWre0TKcmA\"]\n}"
payloadCerveza = "{\n\t\"position_ms\":19150,\n\t\"uris\": [\"spotify:track:0M4DX7XIdMgeXxXHSwabnr\"]\n}"
payloadA = "{\n\t\"position_ms\":12700,\n\t\"uris\": [\"spotify:track:0M4DX7XIdMgeXxXHSwabnr\"]\n}"
payloadJavi = "{\n\t\"position_ms\":90900,\n\t\"uris\": [\"spotify:track:5uWtVfdJYLoNKpUuetcgAV\"]\n}"


headers = {
  'Authorization': 'Bearer AAA',
  'Content-Type': 'application/json'
}

requests.request("PUT", urlPlay, headers=headers, data = payloadDescarga)
sleep(1)
requests.request("PUT", urlPlay, headers=headers, data = payloadWe)
sleep(0.5)
requests.request("PUT", urlPlay, headers=headers, data = payloadSound)
sleep(0.8)
requests.request("PUT", urlPause, headers=headers, data = {})

sleep(1)

requests.request("PUT", urlPlay, headers=headers, data = payloadDale)
sleep(1)
requests.request("PUT", urlPlay, headers=headers, data = payloadUna)
sleep(0.2)
requests.request("PUT", urlPause, headers=headers, data = {})
sleep(0.1)
requests.request("PUT", urlPlay, headers=headers, data = payloadCerveza)
sleep(0.8)
requests.request("PUT", urlPause, headers=headers, data = {})
sleep(0.05)
requests.request("PUT", urlPlay, headers=headers, data = payloadA)
sleep(0.1)
requests.request("PUT", urlPause, headers=headers, data = {})
sleep(0.1)
requests.request("PUT", urlPlay, headers=headers, data = payloadJavi)
sleep(0.1)
requests.request("PUT", urlPause, headers=headers, data = {})

