from enum import Enum

class GenderEnum(Enum):
    HOMME='Homme'
    FEMME='Femme'
    AUTRE='Autre'

class UserRoleEnum(Enum):
    SUPER_ADMIN='Super Admin'
    MENTOR='Mentor'
    PROTECTED='Protected'

class TypeResourcesEnum(Enum):
    MINI_BLOG='Mini Blog'
    QUESTION='Question'
    SESSION='Session'

class ResourcesStatusEnum(Enum):
    OPEN='OPEN'
    CLOSE='CLOSE'