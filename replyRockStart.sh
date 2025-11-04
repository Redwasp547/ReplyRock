#!/bin/bash
clear
screen -S replyRockConsole -dm python3 /home/discordadmin/replyRock/main.py
clear
sleep 1
screen -r replyRockConsole
