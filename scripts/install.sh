#!/bin/sh

# someday this will do the install
# for now, consider it just notes

sudo apt-get install emacs mpd git python3-mpd

cd /etc/systemd/system;
ln -s /home/tell/proj/astreambox/scripts/astreambox.service .

systemctl enable astreambox
systemctl start astreambox

