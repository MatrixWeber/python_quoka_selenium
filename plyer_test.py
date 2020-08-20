from plyer import notification, email, sms


def notify(title, message):
    notification.notify(title=title, message=message, app_name='Bot', timeout=10)
    # audio.play(file_path='C:/Users/Alex/Downloads/Eye.mp3')
    # tts.speak(message=name.text + standort.text)
    email.send(recipient='alexander.weber53@freenet.de', subject='Bot', text=message + ':' + title)
    # sms.send('+4917655378408', name.text + ':' + standort.text)
