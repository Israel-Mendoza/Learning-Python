"""Backup Module"""

import os
import zipfile
import shutil
import time
import threading

from ftplib import FTP
from ftpsync.targets import FsTarget
from ftpsync.ftp_target import FtpTarget
from ftpsync.synchronizers import UploadSynchronizer
from termcolor import colored

from base import Base

class Backup(Base):
    """Backup Class"""

    __omit = []

    @classmethod
    def __init__(cls, bf, database):
        super(Backup, cls).__init__()
        cls.__list = cls.readcfg(bf + '.ini')
        cls.__svrf = bf + '.ftp'
        cls.__database = database
        Backup.__omit = []

    @classmethod
    def __numfiles(cls, fld):
        return sum([len(files) for r, d, files in os.walk(fld)])

    @classmethod
    def __chkftpfld(cls, remotefolder, server, user, password):
        if not Base.hasended():
            ftp = FTP(server)
            ftp.login(user, password)
            try:
                ftp.cwd(remotefolder)
            except BaseException, err:
                Base.log(str(err), True)
                ftp.mkd(remotefolder)
            ftp.close()

    @classmethod
    def __doftp(cls, localfolder, remotefolder, server, color):
        stats = {}
        count = 0
        if not Base.hasended() and localfolder != '' and remotefolder != '':
            if cls.__numfiles(localfolder) > 0:
                msg = '>> FTPing files from: ' + localfolder
                print colored(msg, color)
                Base.log(msg, False)
                try:
                    svr = server['ftp']
                    usr = server['user']
                    pwd = server['pwd']
                    local = FsTarget(localfolder)
                    cls.__chkftpfld(remotefolder, svr, usr, pwd)
                    remote = FtpTarget(remotefolder, svr, username=usr, password=pwd, tls=False)
                    opts = {'force': True, 'delete_unmatched': True, 'verbose': 3}
                    sync = UploadSynchronizer(local, remote, opts)
                    sync.run()
                    stats = sync.get_stats()
                    remote.close()
                except BaseException, err:
                    Base.log(str(err), True)
                    msg = 'Failed FTPing to: ' + remotefolder
                    print colored(msg, 'red')
                    Base.log(msg + ' -> ' + str(err), True)
                finally:
                    if bool(stats):
                        count = stats['upload_files_written']
                    output = '>> ' + str(count) + ' files FTPed successfully to: ' + remotefolder
                    print colored(output, 'green')
                    Base.log(output, False)
        return count

    @classmethod
    def __delfile(cls, fitem):
        if not Base.hasended():
            if not fitem is None:
                if os.path.isfile(fitem):
                    os.remove(fitem)

    @classmethod
    def __md5db(cls, fname, source_folder, subdir, usedb):
        if usedb == False:
            return True
        checksum = cls.md5(os.path.join(subdir, fname), 'md5short')
        return cls.__database.savefiledb(fname, source_folder, subdir, checksum)

    @classmethod
    def __openzip(cls, chkmd5, target_zip):
        result = None
        if not Base.hasended():
            if chkmd5:
                if not os.path.isfile(target_zip):
                    result = zipfile.ZipFile(target_zip, 'w', allowZip64=True)
                else:
                    result = zipfile.ZipFile(target_zip, 'a', allowZip64=True)
            else:
                result = zipfile.ZipFile(target_zip, 'w', allowZip64=True)
        return result

    @classmethod
    def __corezip(cls, chkmd5, params, fname, subdir, usedb):
        zipf = params[0]
        count = params[1]
        total = params[2]
        color = params[3]
        sourcef = params[4]
        numfile = params[5]
        if not Base.hasended():
            if chkmd5:
                if cls.__md5db(fname, sourcef, subdir, usedb):
                    if not cls.__isomitted(fname, sourcef):
                        finzip = os.path.join(subdir, fname)
                        count += 1
                        cls.progress(color, numfile, total, fname)
                        zipf.write(finzip)
                    else:
                        msg = fname + ' -> skipped (omitted)'
                        cls.progress(color, numfile, total, msg)
                        Base.log(msg, False)
                else:
                    msg = fname + ' -> skipped (unchanged)'
                    cls.progress(color, numfile, total, msg)
                    Base.log(msg, False)
            else:
                if not cls.__isomitted(fname, sourcef):
                    finzip = os.path.join(subdir, fname)
                    count += 1
                    cls.progress(color, numfile, total, fname)
                    zipf.write(finzip)
                else:
                    msg = fname + ' -> skipped (omitted)'
                    cls.progress(color, numfile, total, msg)
                    Base.log(msg, False)
        return count

    @classmethod
    def __adddttofilename(cls, fname):
        datet = str(time.strftime("%Y%m%d-%H%M%S"))
        if '%%' in fname:
            fname = fname.replace('%%', datet)
        return fname

    @classmethod
    def __checkmd5(cls, fname):
        result = False
        if '%%' in fname:
            result = True
        return result

    @classmethod
    def __mddir(cls, target_zip):
        if not Base.hasended():
            dirname = os.path.dirname(os.path.abspath(target_zip))
            if not os.path.exists(dirname):
                os.makedirs(dirname)

    @classmethod
    def __closezip1(cls, zipf, count, target_zip, err):
        try:
            count -= 1
            zipf.close()
            cls.__delfile(target_zip)
            msg = 'Failed zipping to: ' + target_zip
            print colored(msg, 'red')
            Base.log(msg + ' -> ' + str(err), True)
        except IOError, ioerror:
            msg = 'Failed closing: ' + target_zip + \
                ' -> ' + str(ioerror)
            print colored(msg, 'red')
            Base.log(msg, True)
        return count

    @classmethod
    def __closezip2(cls, zipf, count, target_zip):
        try:
            print colored('Writing... ' + target_zip, 'green')
            zipf.close()
            msg = '>> ' + str(count) + ' files zipped successfully to: '
            print colored(msg + target_zip, 'green')
            Base.log(msg + target_zip, False)
        except IOError, ioerror:
            msg = 'Failed closing: ' + target_zip + \
                ' -> ' + str(ioerror)
            print colored(msg, 'red')
            Base.log(msg, True)

    @classmethod
    def __closezip3(cls, zipf, target_zip):
        try:
            zipf.close()
            if os.path.isfile(target_zip):
                msg = 'No zip created, nothing changed'
                print colored(msg, 'cyan')
                Base.log(msg, False)
                os.remove(target_zip)
        except IOError, ioerror:
            msg = 'Failed closing: ' + target_zip + \
                ' -> ' + str(ioerror)
            print colored(msg, 'red')
            Base.log(msg, True)

    @classmethod
    def	__dozip(cls, source_folder, target_zip, color, usedb):
        count = 0
        numfile = 0
        chkmd5 = cls.__checkmd5(target_zip)
        target_zip = cls.__adddttofilename(target_zip)
        cls.__mddir(target_zip)
        total = cls.__numfiles(source_folder)
        zipf = None
        if not Base.hasended() and total > 0 and source_folder != '' and target_zip != '':
            msg = '>> Zipping files from: ' + source_folder
            print colored(msg, color)
            Base.log(msg, False)
            try:
                zipf = cls.__openzip(chkmd5, target_zip)
                for subdir, dirs, files in os.walk(source_folder):
                    if Base.hasended():
                        break
                    cls.nothing(str(len(dirs)))
                    for fname in files:
                        if Base.hasended():
                            break
                        numfile += 1
                        params = (zipf, count, total, color, source_folder, numfile)
                        count = cls.__corezip(chkmd5, params, fname, subdir, usedb)
            except BaseException, err:
                count = cls.__closezip1(zipf, count, target_zip, err)
            finally:
                try:
                    if count > 0 and count <= total:
                        cls.__closezip2(zipf, count, target_zip)
                    elif count == 0:
                        cls.__closezip3(zipf, target_zip)
                except IOError, ioerror:
                    msg = 'Failed writing: ' + target_zip + \
                        ' -> ' + str(ioerror)
                    print colored(msg, 'red')
                    Base.log(msg, True)
        return count

    @classmethod
    def __mergepaths(cls, path1, path2):
        pieces = []
        parts1, tail1 = os.path.splitdrive(path1)
        parts2, tail2 = os.path.splitdrive(path2)
        result = path2
        parts1 = tail1.split("\\") if "\\" in tail1 else tail1.split("/")
        parts2 = tail2.split("\\") if "\\" in tail2 else tail2.split("/")
        for pitem in parts1:
            if pitem != '':
                if not pitem in parts2:
                    pieces.append(pitem)
        for piece in pieces:
            result = os.path.join(result, piece)
        return result

    @classmethod
    def __corebuildcopy(cls, source_folder, target_folder, force, color, usedb):
        copylist = []
        item = 0
        if not Base.hasended():
            for subdir, dirs, files in os.walk(source_folder):
                cls.nothing(str(len(dirs)))
                item = 0
                total = len(files)
                for fname in files:
                    if Base.hasended():
                        break
                    origin = os.path.join(subdir, fname)
                    dest = cls.__mergepaths(origin, target_folder)
                    if not cls.__isomitted(fname, subdir):
                        if force or cls.__md5db(fname, source_folder, subdir, usedb):
                            result = origin + '|' + dest + '|' + '>>c'
                            cls.progress(color, item, total, 'Inspecting -> ' + fname + ' (for copy)')
                        else:
                            result = origin + '|' + dest + '|' + '<<s'
                            cls.progress(color, item, total, 'Inspecting -> ' + fname + ' (for skipping)')
                    else:
                        result = origin + '|' + dest + '|' + '<<o'
                        cls.progress(color, item, total, 'Inspecting -> ' + fname + ' (for ommitting)')
                    item += 1
                    copylist.append(result)
        return copylist

    @classmethod
    def __coredocopy(cls, sources, color, total, usedb):
        copylist = []
        source_folder = sources[0]
        target_folder = sources[1]
        force = sources[2]
        numfile = sources[3]
        count = sources[4]
        if not Base.hasended():
            copylist = cls.__corebuildcopy(source_folder, target_folder, force, color, usedb)
            for copyitem in copylist:
                if Base.hasended():
                    return count
                numfile += 1
                copyparts = copyitem.split('|')
                fname = copyparts[0]
                dest = os.path.dirname(copyparts[1])
                if copyparts[2].strip() == '>>c':
                    if not os.path.exists(dest):
                        os.makedirs(dest)
                    count += 1
                    cls.progress(color, numfile, total, os.path.basename(fname))
                    shutil.copy2(fname, dest)
                    #os.system('cp ' + fname + ' ' + dest)
                elif copyparts[2].strip() == '>>o':
                    msg = os.path.basename(fname)\
                        + ' -> skipped (omitted)'
                    cls.progress(color, numfile, total, msg)
                    Base.log(msg, False)
                else:
                    msg = os.path.basename(fname)\
                        + ' -> skipped (unchanged)'
                    cls.progress(color, numfile, total, msg)
                    Base.log(msg, False)
        return count

    @classmethod
    def	__docopy(cls, source_folder, target_folder, color, force, usedb):
        count = 0
        total = cls.__numfiles(source_folder)
        if not Base.hasended() and source_folder != '' and target_folder != '':
            if total > 0:
                msg = '>> File copy from: ' + source_folder
                print colored(msg, color)
                Base.log(msg, False)
                try:
                    sources = (source_folder, target_folder, force, 0, count)
                    count = cls.__coredocopy(sources, color, total, usedb)
                except IOError, ioerr:
                    count -= 1
                    msg = 'Failed copying to: ' + target_folder + ' -> '+ \
                        str(ioerr)
                    print colored(msg, 'red')
                    Base.log(msg, True)
                finally:
                    if count > 0 and count <= total:
                        msg = '>> ' + str(count) + ' files copied successfully to: '
                        print colored(msg + target_folder, 'green')
                        Base.log(msg + target_folder, False)
        return count

    @classmethod
    def __procftp(cls, prts, svr):
        count = 0
        if not Base.hasended():
            sss = cls.readcfg(svr)
            for ssline in sss:
                if Base.hasended():
                    break
                elif '|' in ssline:
                    sitem = ssline.split('|')
                    numparts = len(sitem)
                    if numparts > 0:
                        server = {'ftp': sitem[0], 'user': sitem[1], 'pwd': sitem[2]}
                        count += cls.__doftp(prts[0], prts[3], server, prts[4])
        return count

    @classmethod
    def __isomitted(cls, filename, source_folder):
        result = False
        ff = os.path.join(source_folder, filename)
        extension = os.path.splitext(filename)[1]
        if any(extension.lower() == s for s in Backup.__omit):
            result = True
        if result == False:
            for omit in Backup.__omit:
                if omit.lower() in ff.lower():
                    result = True
                    break
        return result

    @classmethod
    def __getomitted(cls, sourcef):
        """__getomitted"""
        Backup.__omit = []
        result = sourcef
        if ',' in sourcef:
            parts = sourcef.split(',')
            idx = 1
            for pitem in parts:
                if idx > 1:
                    Backup.__omit.append(pitem.lower())
                else:
                    result = pitem
                idx += 1
        return result

    @classmethod
    def run(cls, usedb):
        """Run"""
        items = cls.__list
        svr = cls.__svrf
        count = 0
        for fitem in items:
            if Base.hasended():
                break
            elif '|' in fitem:
                prts = fitem.split('|')
                sourcef = cls.__getomitted(prts[0])
                if 'db@' in sourcef:
                    sourcef = sourcef.replace('db@', '')
                    usedb = True
                if prts[5].strip() == 'z':
                    count += cls.__dozip(sourcef, prts[2], cls.validcolor(prts[4]), usedb)
                elif prts[5].strip() == 'f':
                    count += cls.__procftp(prts, svr)
                elif prts[5].strip() == 'c':
                    count += cls.__docopy(sourcef, prts[1], cls.validcolor(prts[4]), False, usedb)
                elif prts[5].strip() == 'x':
                    count += cls.__docopy(sourcef, prts[1], cls.validcolor(prts[4]), True, usedb)
        return count
