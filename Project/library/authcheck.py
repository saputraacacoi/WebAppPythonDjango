from orm.models import PenCab, PenClub, Anggota

class AuthCheck:

    @staticmethod
    def isSuperUser(user):
        if user.is_superuser:
            return True
        else:
            return False
    @staticmethod
    def isPenCab(user):
        if user.is_staff:
            try:
                user.pencab
                return True
            except PenCab.DoesNotExist:
                return False
        else:
            return False
    @staticmethod
    def isPenClub(user):
        if user.is_staff:
            try:
                user.penclub
                return True
            except PenClub.DoesNotExist:
                return False
        else:
            return False
    @staticmethod
    def isAnggota(user):
            try:
                user.anggota
                return True
            except Anggota.DoesNotExist:
                return False       