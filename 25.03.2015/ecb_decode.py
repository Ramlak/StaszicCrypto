#!/usr/bin/python

# THIS IS ECB_DECODE

from Crypto.Cipher import AES
import os
from sys import stdin, stdout

os.chdir("/home/malware/ecb_decode")

welcome_message = """
Hi, this is our new simple encryption service.
It is very simple. In fact we don't support decryption :(
But I but you can retrieve our secret message anyway.
=========================================================
"""

stdout = os.fdopen(stdout.fileno(), 'w', 0)
key = open("/dev/urandom", "rb").read(16)
flag = open("flag.txt", "rb").readline()

def enhex(string):
	return string.encode('hex')

def unhex(string):
	return string.decode('hex')

def pad(string):
	add = (len(string)/16 + 1)*16 - len(string)
	result = string + "\x00" * add
	return result

def unpad(string):
	result = string
	while result.endswith("\x00"):
		result = result[:-1]
	return result

cipher = AES.new(key, AES.MODE_ECB)

stdout.write(welcome_message)

while True:
	stdout.write("Your string:")
	user_string = stdin.readline().strip()
	string_to_encrypt = pad(user_string+flag)
	stdout.write("Encrypted strings:" + enhex(cipher.encrypt(string_to_encrypt)) + "\n")