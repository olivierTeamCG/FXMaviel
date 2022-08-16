from django.db import models

DEFAULT_FAMILLEPLANTE = (
    ('J-'),
    ('T-'),
    ('S-'),
    ('S+'),
    ('+M'),
    ('T+SH'),
    ('T+ZF')
)



for name in DEFAULT_FAMILLEPLANTE:
    famille_plante = FamillePlante(famille_plante=name)
    famille_plante.save()
