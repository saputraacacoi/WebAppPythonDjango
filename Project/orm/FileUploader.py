import time
import os

def file_profile(instance, filename):
    ext = filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "%s.%s" % (str(milis), ext)
    return os.path.join('user/profile', filename)


def file_club(instance, filename):
    name, ext = filename.split('.')[0], filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "%s_%s.%s" % (name, str(milis), ext)
    return 'club/docs/{0}/{1}'.format(instance.club.id, filename)


def file_club_thumbnail(instance, filename):
    name, ext = filename.split('.')[0], filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "thumbnail_%s_%s.%s" % (name, str(milis), ext)
    return 'club/docs/{0}/thumnail/{1}'.format(instance.club.id, filename)


def file_member(instance, filename):
    ext = filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "user_%s_%s.%s" % (str(instance.user.id), str(milis), ext)
    return 'user_{0}/{1}'.format(instance.user.id, filename)