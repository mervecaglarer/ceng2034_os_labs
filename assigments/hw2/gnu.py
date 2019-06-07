#!/bin/sh
exec tail -n +3 $0   #This file provides to add GNU menu entries.


menuentry "MY UBUNTU"{

    set root=/home/merve/İndirilenler/ubuntu-18.04.2-desktop-amd64.iso
        linux /vmlinuz root=/home/merve/ubuntu-18.04.2-desktop-amd64.iso ro quiet splash $vt_handoff 
        initrd /initrd.img
}

