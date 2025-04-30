"""
Config class, mostly extended from ntlmrelayx
"""
from impacket.examples.ntlmrelayx.utils.config import NTLMRelayxConfig

class KrbRelayxConfig(NTLMRelayxConfig):
    def __init__(self):
        NTLMRelayxConfig.__init__(self)

        # Auth options
        self.dcip = None
        self.aeskey = None
        self.hashes = None
        self.password = None
        self.israwpassword = False
        self.salt = None

        # Krb options
        self.format = 'ccache'

        # LDAP options
        self.dumpdomain = True
        self.addda = True
        self.aclattack = True
        self.validateprivs = True
        self.escalateuser = None
        self.addcomputer = False
        self.delegateaccess = False

        # Custom options
        self.victim = None

        # Shadow Credentials attack options
        self.IsShadowCredentialsAttack = False
        self.ShadowCredentialsPFXPassword = None
        self.ShadowCredentialsExportType = None
        self.ShadowCredentialsOutfilePath = None

    # Make sure we have a fixed version of this to avoid incompatibilities with impacket
    def setLDAPOptions(self, dumpdomain, addda, aclattack, validateprivs, escalateuser, addcomputer, delegateaccess, dumplaps, dumpgmsa, dumpadcs, sid):
        self.dumpdomain = dumpdomain
        self.addda = addda
        self.aclattack = aclattack
        self.validateprivs = validateprivs
        self.escalateuser = escalateuser
        self.addcomputer = addcomputer
        self.delegateaccess = delegateaccess
        self.dumplaps = dumplaps
        self.dumpgmsa = dumpgmsa
        self.dumpadcs = dumpadcs
        self.sid = sid

    def setAuthOptions(self, aeskey, hashes, dcip, password, salt, israwpassword=False):
        self.dcip = dcip
        self.aeskey = aeskey
        self.hashes = hashes
        self.password = password
        self.salt = salt
        self.israwpassword = israwpassword

    def setKrbOptions(self, outformat, victim):
        self.format = outformat
        self.victim = victim

    def setIsShadowCredentialsAttack(self, IsShadowCredentialsAttack):
        self.IsShadowCredentialsAttack = IsShadowCredentialsAttack

    def setShadowCredentialsOptions(self, ShadowCredentialsTarget, ShadowCredentialsPFXPassword, ShadowCredentialsExportType, ShadowCredentialsOutfilePath):
        self.ShadowCredentialsTarget = ShadowCredentialsTarget
        self.ShadowCredentialsPFXPassword = ShadowCredentialsPFXPassword
        self.ShadowCredentialsExportType = ShadowCredentialsExportType
        self.ShadowCredentialsOutfilePath = ShadowCredentialsOutfilePath