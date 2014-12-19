#!/usr/bin/env python2.7

# estos son los directorios que pueden ser invocados utilizando este modulo

# 'xdg_publicshare_dir'
# 'xdg_download_dir' 
# 'xdg_music_dir' 
# 'xdg_videos_dir' 
# 'xdg_desktop_dir' 
# 'xdg_documents_dir' 
# 'xdg_templates_dir' 
# 'xdg_pictures_dir'

import os
import re
import io
import ConfigParser

from xdg.BaseDirectory import xdg_config_home


class XdgConfig(object):
    """obtener todas las configuraciones de los directorios xdg
       de forma transparente y almacenar los destinos como atributos del
       objeto"""
    def __init__(self):

        self.section = "XDG_USER_DIR"

        self.config = ConfigParser.RawConfigParser(allow_no_value=True)

        with open(os.path.join(xdg_config_home,"user-dirs.dirs")) as dirs:

            self.user_config = "[XDG_USER_DIR]\n" + dirs.read()

            self.user_config = re.sub('\$HOME', os.path.expanduser("~"),
                                         self.user_config)
            
            self.user_config = re.sub('"', '', self.user_config)

        self.config.readfp(io.BytesIO(self.user_config))
        
        self.xdg_dirs = self.getAllDirectory()

        self.mountpath = getMountDirectory()

    def getAllDirectory(self):

        DIRS = {}

        for i in  self.config.options(self.section):

            DIRS[i] = self.config.get(self.section,i)

        return DIRS

    def get(self,resource):

        if self.xdg_dirs.has_key(resource):
            response = self.xdg_dirs[resource]
        else:
            response = ""

        return response



def getMountDirectory():

    dist = os.uname()[3]
    user = os.environ['USER']

    if dist.count('Ubuntu'):

        mountpath = '/media/' + user
    else:
        mountpath = '/run/media/'+ user

    return mountpath