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

class ProfessionsEnum(Enum):
    ETUDIANT='Etudiant'
    PROFESSIONNEL='Professionnel'
    ETUDIANT_PRO='Etudiant Pro'
    STUDENT='Student'
    STUDENT_PRO='Student Pro'
    TEACHER='Teacher'
    TEACHER_PRO='Teacher Pro'

class StacksEnum(Enum):
    FRONTEND='Frontend'
    BACKEND='Backend'
    FULLSTACK='Fullstack'
    MOBILE='Mobile'
    DESIGN='Design'
    DATA='Data'
    ANALYTICS='Analytics'
    DEVOPS='Devops'
    QA='Qa'
    SECURITY='Security'
    MENTORING='Mentoring'
    EDUCATION='Education'
    MARKETING='Marketing'
    BUSINESS='Business'
    OTHER='Other'