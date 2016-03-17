# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:54:35 2016

@author: Amyn
"""

from ftplib import FTP, error_perm
import os, patoolib

pathname="<local path here>"

def ftpDownloader(Id,startID,endID,url="<url here>",user="<username here>",passwd="<password here>"):
    ftp=FTP(url)
    ftp.login(user,passwd)
    if not os.path.exists(pathname):
        os.makedirs(pathname)
    print(ftp.nlst())
    
    ftp.cwd("<ftp working durectory here>")
    os.chdir(pathname)
    
    for array in range(startID, endID+1):
        #Enter full path below, including start and stop IDs
        fullpath='<insert ftp path here>' % (array,Id,array)
        filename=os.path.basename(fullpath)
        try:
            with open(filename,'wb') as file:
                ftp.retrbinary('RETR %s' % fullpath, file.write)
                print("%s downloaded" % filename)
                if filename[-3:] == ".gz" or filename[-4:] == ".zip" or filename[-4:] == ".tar":
                    patoolib.extract_archive(filename,outdir="unpack")
        except error_perm:
            print("%s is not available" % filename)
            os.remove(filename)
    ftp.close()
