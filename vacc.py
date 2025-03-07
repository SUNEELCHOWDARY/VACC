# Import Section
import time
# import vlc
import pyautogui as pg
import pyaudio
from google.cloud import speech

list_of_applications=['chrome','notepad','file explorer','explorer','google chrome','command prompt','whatsapp']
list_of_websites=['youtube','instagram','facebook','twitter','linkedin','skillrack','velammal']
links_for_websites={'youtube':'youtube.com',
                    'instagram':'instagram.com',
                    'twitter':'twitter.com',
                    'linkedin':'linkedin.com',
                    'facebook':'facebook.com',
                    'skillrack':'skillrack.com',
                    'velammal':'velammal.org'
                   }

def open_application(app_name):
    time.sleep(1)
    pg.hotkey("win","r")
    pg.write(app_name)
    pg.press('enter')


def open_website(app_name, web_name):
    time.sleep(1)
    pg.hotkey('win', 'r')
    pg.write(app_name + ' ' + web_name)
    pg.press('enter')


# Playing sound
# def play_sound(file_path):
#     p = vlc.MediaPlayer(file_path)
#     p.play()


# function for commands execution
def command_execution(user_command):
    print('I am in execution section')
    # chrome
    if user_command == 'open new window':
        pg.hotkey('ctrl', 'n')
    elif user_command == 'open new window in incognito mode':
        pg.hotkey('ctrl', 'shift', 'n')
    elif user_command == 'open new tab':
        pg.hotkey('ctrl', 't')
    elif user_command == 'open history':
        pg.hotkey('ctrl', 'h')
    elif user_command == 'open bookmark manager':
        pg.hotkey('ctrl', 'shift', 'o')
    elif user_command == 'open chrome menu':
        pg.hotkey('alt', 'f')
    elif user_command == 'open chrome task manager':
        pg.hotkey('shift', 'esc')
    elif user_command == 'open previous window':
        pg.hotkey('alt', 'tab')
    elif user_command == 'open find bar':
        pg.hotkey('ctrl', 'f')
    elif user_command == 'open chrome task manager':
        pg.hotkey('shift', 'esc')
    elif user_command == 'open downloads':
        pg.hotkey('ctrl', 'j')
    elif user_command == 'bookmark this tab':
        pg.hotkey('ctrl', 'd')
    elif user_command == 'bookmark all tabs':
        pg.hotkey('ctrl', 'shift', 'd')
    elif user_command == 'show bookmark bar':
        pg.hotkey('ctrl', 'shift', 'b')
    elif user_command == 'zoom in':
        pg.hotkey('ctrl', '+')
    elif user_command == 'zoom out':
        pg.hotkey('ctrl', '-')
    elif user_command == 'select all':
        pg.hotkey('ctrl', 'a')
    elif user_command == 'copy text':
        pg.hotkey('ctrl', 'c')
    elif user_command == 'paste text':
        pg.hotkey('ctrl', 'v')
    elif user_command == 'mute':
        pg.press('f6')
    elif user_command == 'unmute':
        pg.press('f6')
    elif user_command == 'go to previous tab':
        pg.hotkey('ctrl', 'pagedown')
    elif user_command == 'go to next tab':
        pg.hotkey('ctrl', 'tab')
    elif user_command == 'cut text':
        pg.hotkey('ctrl', 'x')
    elif user_command == 'go to back page':
        pg.hotkey('alt', 'left')
    elif user_command == 'go to next page':
        pg.hotkey('alt', 'right')
    elif user_command == 'go to first tab':
        pg.hotkey('alt', '1')
    elif user_command == 'go to secong tab':
        pg.hotkey('alt', '2')
    elif user_command == 'go to third tab':
        pg.hotkey('alt', '3')
    elif user_command == 'go to fourth tab':
        pg.hotkey('alt', '4')
    elif user_command == 'go to fifth tab':
        pg.hotkey('alt', '5')
    elif user_command == 'go to search bar':
        pg.hotkey('ctrl', 'k')
    elif user_command == 'go to last tab':
        pg.hotkey('alt', '9')
    elif user_command == 'reset zoom':
        pg.hotkey('ctrl', '0')
    elif user_command == 'open file':
        pg.hotkey('ctrl', 'o')
    elif user_command == 'refresh present page':
        pg.hotkey('ctrl', 'r')
    elif user_command == 'save the present page':
        pg.hotkey('ctrl', 's')
    elif user_command == 'open source code':
        pg.hotkey('ctrl', 'u')
    elif user_command == 'reopen the last closed tab':
        pg.hotkey('ctrl', 'shift', 't')
    elif user_command == 'go to down of page':
        pg.press('space ')
    elif user_command == 'go to up of page':
        pg.hotkey('shift', 'space')
    elif user_command == 'stop loading tab':
        pg.press('esc')
    elif user_command == 'close present tab':
        pg.hotkey('ctrl', 'w')
    elif user_command == 'close present window':
        pg.hotkey('ctrl', 'shift', 'w')
    elif user_command == 'close chrome':
        pg.hotkey('alt', 'f4')

    # File Explorer
    elif user_command == 'open file explorer':
        pg.hotkey('win', 'e')
    elif user_command == 'go to side bar':
        pg.hotkey('shift', 'tab')
    elif user_command == 'open a new file explorer window':
        pg.hotkey('ctrl', 'n')
    elif user_command == 'close file explorer':
        pg.hotkey('ctrl', 'w')
    elif user_command == 'create new folder':
        pg.hotkey('ctrl', 'shift', 'n')
    elif user_command == 'go to previous folder':
        pg.hotkey('alt', 'left')
    elif user_command == 'go to next folder':
        pg.hotkey('alt', 'right')
    elif user_command == 'rename file':
        pg.hotkey('fn', 'f2')
    elif user_command == 'rename folder':
        pg.hotkey('fn', 'f2')
    elif user_command == 'go to address bar':
        pg.hotkey('ctrl', 'l')
    elif user_command == 'copy text':
        pg.hotkey('ctrl', 'c')
    elif user_command == 'copy selected file':
        pg.hotkey('ctrl', 'c')
    elif user_command == 'paste selected folder':
        pg.hotkey('ctrl', 'v')
    elif user_command == 'paste text':
        pg.hotkey('ctrl', 'v')
    elif user_command == 'search file':
        pg.hotkey('ctrl', 'f')
    elif user_command == 'change icons large':
        pg.hotkey('ctrl', 'shift', '2')
    elif user_command == 'change icons normal':
        pg.hotkey('ctrl', 'shift', '6')

        
    # Notepad
    elif user_command == 'create new file':
        pg.hotkey('ctrl', 'n')
    elif user_command == 'open file':
        pg.hotkey('ctrl', 'o')
    elif user_command == 'save file':
        pg.hotkey('ctrl', 's')
    elif user_command == 'save file as':
        pg.hotkey('ctrl', 'shift', 's')
    elif user_command == 'undo':
        pg.hotkey('ctrl', 'z')
    elif user_command == 'redo':
        pg.hotkey('ctrl', 'y')
    elif user_command == 'cut':
        pg.hotkey('ctrl', 'c')
    elif user_command == 'paste':
        pg.hotkey('ctrl', 'v')
    elif user_command == 'select all':
        pg.hotkey('ctrl', 'a')
    elif user_command == 'find':
        pg.hotkey('ctrl', 'f')
    elif user_command == 'close notepad':
        pg.hotkey('alt', 'f4')
    elif user_command == 'close file':
        pg.hotkey('ctrl', 'w')
    elif user_command == 'zoom in':
        pg.hotkey('ctrl', '+')
    elif user_command == 'zoom out':
        pg.hotkey('ctrl', '-')
    elif user_command == 'insert current date and time':
        pg.hotkey('fn', 'f5')
    elif user_command == 'close file':
        pg.hotkey('ctrl', 'w')
    elif user_command == 'go to end of line':
        pg.press('end')
    elif user_command == 'go to start of line':
        pg.press('home')
    elif user_command == 'move cursor one word to the left':
        pg.hotkey('ctrl', 'left')
    elif user_command == 'move cursor one word to the right':
        pg.hotkey('ctrl', 'right')
    elif user_command == 'restore default zoom level':
        pg.hotkey('ctrl', '0')
    elif user_command == 'select text from cursor to end':
        pg.hotkey('shift', 'end')
    elif user_command == 'select text from cursor to start':
        pg.hotkey('shift', 'home')
    elif user_command == 'save all files':
        pg.hotkey('ctrl', 'alt', 's')
    elif user_command == 'print':
        pg.hotkey('ctrl', 'p')
    elif user_command == 'close tab':
        pg.hotkey('ctrl', 'w')
    elif user_command == 'close window':
        pg.hotkey('ctrl', 'shift', 'w')
    elif user_command == 'delete selected text':
        pg.press('delete')
    elif user_command == 'find next':
        pg.press('f3')
    elif user_command == 'find previous':
        pg.hotkey('shift', 'f3')
    elif user_command == 'go to line':
        pg.hotkey('ctrl', 'g')
    elif user_command == 'go to first tab':
        pg.hotkey('ctrl', '1')
    elif user_command == 'go to second tab':
        pg.hotkey('ctrl', '2')
    elif user_command == 'go to third tab':
        pg.hotkey('ctrl', '3')
    elif user_command == 'go to fourth tab':
        pg.hotkey('ctrl', '4')
    elif user_command == 'go to fifth tab':
        pg.hotkey('ctrl', '5')
    elif user_command == 'go to sixth tab':
        pg.hotkey('ctrl', '6')
    elif user_command == 'go to seventh tab':
        pg.hotkey('ctrl', '7')
    elif user_command == 'go to eigth tab':
        pg.hotkey('ctrl', '8')
    elif user_command == 'go to last tab':
        pg.hotkey('ctrl', '9')
    elif user_command == 'create new line':
        pg.press('enter')
    elif user_command == 'go to next line':
        pg.press('down')
    elif user_command == 'go to previous line':
        pg.press('up')


# function for speech to text conversion
def speech_to_text():
    # Set audio parameters
    CHUNK = 1024
    FORMAT = pyaudio.paInt32
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 3

    # Pyaudio instance
    audio = pyaudio.PyAudio()

    print('stream not activated')
    # Microphone stream
    stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
    print('stream activated')

    # if music_file != None:
    #     play_sound('start_tune.mp3')
    # Record audio data
    print('read not completed')
    frames = b''
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames += data

    print('read completed')
    # Loding credentials
    client = speech.SpeechClient.from_service_account_file('credentials.json')

    # Audio
    audio = speech.RecognitionAudio(content=frames)

    # Configuration
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR32,
        sample_rate_hertz=RATE,
        language_code="en-US",
        enable_automatic_punctuation=False
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    response = operation.result(timeout=90)

    
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

        if result.alternatives[0].transcript != None:
            return result.alternatives[0].transcript.lower().strip()


# function for wake word detection
def wake_word_detection(wake_word):
    if wake_word == 'hey jenny':
        command = speech_to_text()
        command_execution(command)


# Logic Building
while True:
    wake_word = speech_to_text()
    wake_word_detection(wake_word)