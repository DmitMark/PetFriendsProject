# PetFriendsProject

# python -m pytest -v --driver chrome --driver-path c:\chromedriver.exe --alluredir=allureress tests/

curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"chat_id": "1222398185", "text": "This is a test from curl", "disable_notification": true}' \
     https://api.telegram.org/bot6452476818:AAFPmFoNYakI22vx3GjEaJLYJhwdahOz4mc/sendMessage

java "-DconfigFile=notifications/telegram.json" -jar notifications/allure-notifications-4.6.1.jar