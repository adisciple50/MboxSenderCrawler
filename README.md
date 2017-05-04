# MboxSenderCrawler
Utility To Display And Save A List Of Email Senders From A Given .Mbox File

Just Run The Script And it will bring up a file picker dialogue.

this works for google's takeout service. useful for grabbing a list of people who know your email address, 
and a list of domains you may have to notify of a change of address.


## Installation

### Ubuntu

for those who are on ubuntu and/or people who are running wayland;
or if you get the error "ImportError: No module named '_tkinter'":

sudo apt-get install tk-dev tk tcl-dev tcl python3-tk python3-easygui

#### One-Liner Copy And Paste for the Ubuntu Linux Terminal.

sudo apt-get install tk-dev tk tcl-dev tcl python3-tk python3-easygui git && git clone https://github.com/deddokatana/MboxSenderCrawler.git && cd MboxSenderCrawler && python3 main.py

### Windows

there are many ways to do this. [Untested]

- aqcuire 'main.py' (git clone or zip download)
- unzip and/or change directory to MboxSenderCrawler
- in the windows command prompt: pip install easygui
- in the windows command prompt: python3 main.py 

in other words - install the easygui module and run main.py.

### Mac

sorry kids your own your own :D - pull requests to this readme are welcome.

I guess:
pip install easygui && git clone https://github.com/deddokatana/MboxSenderCrawler.git && cd MboxSenderCrawler && python3 main.py

### Gentoo && Other Linux

pip install easygui && git clone https://github.com/deddokatana/MboxSenderCrawler.git && cd MboxSenderCrawler && python3 main.py

Your Milage May vary, your very likely into rolling your own bins anyways.
