# Import Section
import time
import pyaudio
import openai
import winsound
import pyautogui as pg
from win10toast import ToastNotifier
from google.cloud import speech

pg.PAUSE = 0.5

toaster = ToastNotifier()
openai.api_key = "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"

links_for_websites={'youtube':'youtube.com',
                    'instagram':'instagram.com',
                    'twitter':'twitter.com',
                    'linkedin':'linkedin.com',
                    'facebook':'facebook.com',
                    'skillrack':'skillrack.com',
                    'velammal':'velammalitech.edu.in',
                    'sifytechnologies':'sifytechnologies.com',
                    '': '',
                   }

def type_words():
    text = speech_to_text(10, 'en-IN', 'type mode activated...', True, True)
    pg.typewrite(text, interval=0.05)

def get_info():
    prompt = speech_to_text(10, 'en-IN', 'get info mode...', True, True)
    output = chat_gpt(prompt)
    if output!=None:
        pg.write(output, interval=0.01)

def chat_gpt(prompt):
    prompt = prompt.strip()
    if prompt == 'get info about':
        return None
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 4000,
        n=1,
        stop=None,
        temperature=1
    )

    return response.choices[0].text


def open_application(app_name):
    time.sleep(1)
    pg.hotkey("win","r")
    pg.write(app_name)
    pg.press('enter')


def open_website(app_name, web_name):
    
    try:
        time.sleep(1)
        pg.hotkey('win', 'r')
        link = links_for_websites[web_name]
        pg.write(app_name +' ' + link)
    except:
        pass
    pg.press('enter')


# function for commands execution
def command_execution(user_command):
    print('I am in execution section')
    # chrome
    if user_command == None:
        return
    print('u said:'+user_command)
    if 'open' in user_command and 'application' in user_command:
        app_name = user_command.replace('open', '').replace('application', '').strip().replace(' ', '')
        open_application(app_name)
    elif 'open' in user_command and 'in browser' in user_command:
        web_name = user_command.replace('open', '').replace('in browser', '').strip().replace(' ', '')
        open_website('chrome', web_name)
    elif user_command == 'type now':
        type_words()
    elif user_command[:4] == 'type':
        text = user_command.replace('type', '').strip()
        pg.write(text, interval=0.05)
    elif user_command[:14] == 'getinfo':
        get_info()
    elif user_command[:5] == 'press':
        key = user_command.replace('press', '').strip()
        try:
            pg.press(key)
        except:
            pass
    elif user_command == 'open new window':
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
        pg.press('f1')
    elif user_command == 'unmute':
        pg.press('f1')
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
    elif user_command == 'go to search bar':
        pg.hotkey('ctrl', 'k')
    elif user_command == 'go to last tab':
        pg.hotkey('ctrl', '9')
    elif user_command == 'reset zoom':
        pg.hotkey('ctrl', '0')
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
    elif user_command == 'close application':
        pg.hotkey('alt', 'f4')

    # File Explorer
    elif user_command == 'delete':
        pg.press('delete')
    elif user_command == 'open file explorer':
        pg.hotkey('win', 'e')
    elif user_command == 'go to side bar':
        pg.hotkey('shift', 'tab')
    elif user_command == 'open a new file explorer':
        pg.hotkey('ctrl', 'n')
    elif user_command == 'create new folder':
        pg.hotkey('ctrl', 'shift', 'n')
    elif user_command == 'go to previous folder':
        pg.hotkey('alt', 'left')
    elif user_command == 'go to next folder':
        pg.hotkey('alt', 'right')
    elif user_command == 'rename':
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
    elif user_command == 'save file':
        pg.hotkey('ctrl', 's')
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
    elif user_command == 'open downloads folder in explorer':
        pg.hotkey('win','r')
        pg.write('explorer downloads')
        pg.press('enter')

    elif user_command == 'open documents folder in explorer':
        pg.hotkey('win','r')
        pg.write('explorer documents')
        pg.press('enter')

    elif 'open' in user_command and 'file' in user_command:
        pg.hotkey('ctrl', 'o')
        f_name = user_command.replace('open', '').replace('file', '').strip()
        pg.write(f_name)
        pg.press('enter')

    elif 'save as' in user_command:
        name = user_command.replace('save as', '').strip()
        pg.hotkey('ctrl', 'shift', 's')
        pg.write(name)
        pg.press('enter')

    elif 'rename as' in user_command:
        pg.hotkey('fn', 'f2')
        name = user_command.replace('rename as', '').strip()
        pg.write(name)
        pg.press('enter')

    elif 'create'in user_command and 'folder' in user_command:
        pg.hotkey('ctrl', 'shift', 'n')
        name = user_command.replace('create', '').replace('folder', '').strip()
        pg.write(name)
        pg.press('enter')

    

# function for speech to text conversion
def speech_to_text(sec, lan, announcement, punctuation_status, beep_status):
    # Set audio parameters
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = sec

    # Pyaudio instance
    audio = pyaudio.PyAudio()

    # Microphone stream
    stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

    if beep_status:
        winsound.Beep(500, 300)
    # Record audio data
    print(announcement)
    frames = b''
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames += data

    stream.stop_stream()
    stream.close()
    audio.terminate()

    try:
        # Loding credentials
        client = speech.SpeechClient.from_service_account_file('C:\\Users\\hp\\Desktop\\VACC\\Project\\credentials.json')
        
        # Audio
        audio = speech.RecognitionAudio(content=frames)
        
        # Configuration
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code=lan,
            enable_automatic_punctuation=punctuation_status
        )

        operation = client.long_running_recognize(config=config, audio=audio)
        print('google activated')
        response = operation.result(timeout=90)

        
        for result in response.results:
            # print("Transcript: {}".format(result.alternatives[0].transcript))
            text = result.alternatives[0].transcript


            
            if text != None:
                # pg.alert(text)
                # time.sleep(3)
                # pg.confirm(button='OK')
                toaster.show_toast('VACC', text, duration=5)
                return text.lower().strip()
            else:
                # pg.alert("Not Recognized")
                # time.sleep(3)
                # pg.confirm(button='OK')
                toaster.show_toast('VACC', text, duration=5)
                return None
    except:
        return None


# function for wake word detection
def wake_word_detection(wake_word):
    if wake_word == 'hey jenny':
        command = speech_to_text(4, 'en-IN', 'say command...', False, True)
        if command!= None:
            command_execution(command)


# Logic Building
while True:
    # wake_word = speech_to_text(4, 'en-US', 'Listening...', False, False)
    # wake_word_detection(wake_word)
    command = speech_to_text(4, 'en-IN', 'say command...', False, True)
    if command!= None:
        command_execution(command)



