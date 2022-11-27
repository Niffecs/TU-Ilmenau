#!/usr/bin/env python3

import os
import ftplib
import sys
import hashlib
import shutil

# Load env
FILE = sys.argv[1]
HOST = os.environ["FTP_SERVER"]
USER = os.environ["FTP_USER"]
PWD = os.environ["FTP_PWD"]


# Test PDF
if not "pdf" in FILE:
    print("no pdf")
    sys.exit(-1)

# Create Hash file
hash = hashlib.md5(sys.argv[1][:-4].encode('utf-8')).hexdigest()
shutil.copyfile(FILE, f"{hash}.pdf")
FILE2 = f"{hash}.pdf"


# FTP Gedoens
ftp = ftplib.FTP(HOST, USER, PWD)
ftp.encoding = "utf-8"
with open(FILE, "rb") as file:
    ftp.storbinary(f"STOR {FILE}", file)
ftp.cwd("loader")
with open(FILE2, "rb") as file:
    ftp.storbinary(f"STOR {FILE2}", file)