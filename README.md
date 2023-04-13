# LN Tipbot
This is a simple c-lightning application for demo purposes. Via a Telegram bot donors can create invoices for donations.

see 
https://lightning.readthedocs.io/lightningd-rpc.7.html
https://core.telegram.org/bots/api
https://docs.python.org/3/tutorial/venv.html

Obtain a bot token from botfather.
Open a terminal on your node, e.g. ```ssh bitcoin@raspberrypi```. 
The user (here 'bitcoin') must have access to the unix socket. 
Download the repository e.g. ```wget https://github.com/lcoholic/ln-tipbot/archive/refs/heads/main.zip && unzip main.zip && rm main.zip```.
Enter your rpc socket path and bot token in the config.py file and change the start message in main.py. 
Install python if you don't have it. 
Create a virtual environment ```python -m venv .venv```. 
Activate the virtual environment ```source .venv/bin/activate```. 
Now you can install the required libraries in the virtual environment ```pip install -r requirements.txt```. 
Start in background with ```python main.py &```. 
See the process and its id (PID) e.g. ```ps -a | grep python``` and kill it if you want ```kill PID```.
