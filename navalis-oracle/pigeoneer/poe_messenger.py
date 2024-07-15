import time
import re
import json
from pathlib import Path
from flask_lib import send_flask_data as send

class Watcher():
    running = True

    def __init__(self, currency = ["divine", "chaos", "divines"], show_header=False, refresh_delay_secs=1):
        
        if show_header:
            self.header()
        self.refresh = refresh_delay_secs/10
        if len(currency) > 1:
            currency = "|".join(currency)
        self.pattern = r"(\d+)\s*({0})".format(currency)
        
    def follow(self, logfile):
        logfile.seek(0,2)
        while True:
            line = logfile.readline()
            if not line:
                time.sleep(self.refresh)
                continue
            yield line

    def header(self, title="Watcher", corners="+", edge_length=25, pad_level=1, sections=1):

        edge = f"{corners}{'-'*edge_length}{corners}"
        middle = lambda fill: fill.center(edge_length, " ")
        padding = middle(" ")
        if pad_level > 1:
            padding = "\n".join((middle(" ") for _ in range(pad_level)))
        
        for i in range(sections):
            print(edge)
            print(padding)
            print(middle(title))
            print(padding)
            if i == sections-1:
                print(edge)
        print('\n')

    def start(self, user_id, filename):
        while self.running:
            logfile = open(filename, "r")
            loglines = self.follow(logfile)
            for line in loglines:
                if '@From' in line:
                    match = re.findall(self.pattern, line.split('(stash')[0])
                    if match:
                        msg = {
                            'Trade Message': line.split(']')[1],
                            'Item': 'N\A',
                            'Sale Price': ' and '.join(map(lambda x:' '.join(x),match))
                        }
                        msg = '\n'.join(('**{0}** : {1}'.format(k,v) for k,v in msg.items()))
                        data = {
                            'message': msg, 
                            'user': user_id
                            }
                        send(data)

def main():

    with open('config.json', 'r') as file:
            data = json.load(file)
    user_id = data["USERS"][data["CURRENT_USER"]]
    filename = Path(data["POE_CLIENT_LOG"])
    
    watcher = Watcher()
    watcher.start(user_id, filename)

if __name__ == "__main__":
    main()