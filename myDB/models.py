from django.db import models
from django.contrib import admin
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple


from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from .widgets import Widget

from ckeditor.fields import RichTextField

from django.utils.html import format_html

from colorfield.fields import ColorField


#class Molecule(models.Model):
#    default_auto_field = 'django.db.models.AutoField'
#    nommolecule = models.CharField(max_length=200,default='any_name')
#    formule = models.CharField(max_length=200)

#    def __str__(self):
#        return self.nommolecule


class Prescription(models.Model):
    default_auto_field = 'django.db.models.AutoField'
    syndrome = models.CharField(max_length=200,default='')
    systeme = models.CharField(max_length=200,default='')
    symptomes = models.TextField(max_length=2000,default='')
    remarques = models.TextField(max_length=2000,default='',verbose_name='Effets thérapeutiques', null=True,blank=True)

    def __str__(self):
        return self.syndrome


class PlantePrescriptionJINGFANG(models.Model):
    default_auto_field = 'django.db.models.AutoField'
    plante = models.ForeignKey('Plante', on_delete=models.CASCADE)
    Prescription = models.ForeignKey('Prescription', on_delete=models.CASCADE)
    #quantite = models.IntegerField(default=1)
    quantite = models.CharField(max_length=10, null=True,blank=True)

    class Meta:
        verbose_name = ("Jing Fang Zhang Zhong Jing")
        verbose_name_plural = ("Jing Fang Zhang Zhong Jing")


class PlantePrescriptionZangfuQui(models.Model):
    default_auto_field = 'django.db.models.AutoField'
    plante = models.ForeignKey('Plante', on_delete=models.CASCADE)
    Prescription = models.ForeignKey('Prescription', on_delete=models.CASCADE)
    #quantite = models.IntegerField(default=1)
    quantite = models.CharField(max_length=10, null=True,blank=True)

    class Meta:
        verbose_name = ("Jing Fang Feng Shi Lun")
        verbose_name_plural = ("Jing Fang Feng Shi Lun")



#class Pathologie(models.Model):
#    default_auto_field = 'django.db.models.AutoField'
#    pathologie = models.CharField(max_length=200)
#    symptomes = models.CharField(max_length=200)

#    def __str__(self):
#        return self.pathologie


#class PathologiePreparation(models.Model):
#    default_auto_field = 'django.db.models.AutoField'
#    pathologie = models.ForeignKey('Pathologie', on_delete=models.CASCADE)
#    preparation = models.ForeignKey('Preparation', on_delete=models.CASCADE)

class FamillePlante(models.Model):
    default_auto_field = 'django.db.models.AutoField'
    famille_plante = models.CharField(max_length=30)

    def __str__(self):
        return str(self.famille_plante)

class Plante(models.Model):

    
    default_auto_field = 'django.db.models.AutoField'   
    substance_medicinale = models.CharField(max_length=200,verbose_name="Substance médicinale", null=True,blank=True)
    zang_fu = models.CharField(max_length=200,verbose_name="ZANG / FU", null=True,blank=True)
    famille_plante = models.ManyToManyField(FamillePlante)
    saveur = models.CharField(max_length=200,verbose_name="Saveur", null=True,blank=True)
    nature = models.CharField(max_length=200,verbose_name="Nature", null=True,blank=True)
    action = models.CharField(max_length=2000,verbose_name="Action", null=True,blank=True)
    posologie = models.TextField(max_length=2000,verbose_name="Posologie", null=True,blank=True)
    pao_zi = models.TextField(max_length=2000,verbose_name="Pao Zi", null=True,blank=True)
    contre_indications = models.TextField(max_length=2000,verbose_name="Contre-indications", null=True,blank=True)
    fonctions = models.TextField(max_length=2000,verbose_name="Fonctions", null=True,blank=True)
    cibles_clefs = models.TextField(max_length=2000,verbose_name="Cibles clefs", null=True,blank=True)
    indications = models.TextField(max_length=2000,verbose_name="Indications (= symptômes)", null=True,blank=True)
    textes_classiques = models.TextField(max_length=2000,verbose_name="Shen Nong Ben Cao Jing et autres textes classiques", null=True,blank=True)
    interets_therapeutiques = models.TextField(max_length=5000,verbose_name="Intérêts thérapeutiques", null=True,blank=True)
    ZZJ_HXS_FSL = models.TextField(max_length=2000,verbose_name="ZZJ - HXS - FSL", null=True,blank=True)
    pharmacopee_contemporaine = models.TextField(max_length=2000,verbose_name="Pharmacopée contemporaine", null=True,blank=True)
    precisions_PS = models.TextField(max_length=2000,verbose_name="Précisions PS", null=True,blank=True)
    grandes_combinaisons = models.TextField(max_length=2000,verbose_name="Grandes combinaisons", null=True,blank=True)
    incompatibilite_alimentaire = models.TextField(max_length=2000,verbose_name="Incompatibilité alimentaire", null=True,blank=True)
    prudence_medicamenteuse = models.TextField(max_length=2000,verbose_name="Prudence médicamenteuse", null=True,blank=True)
    contre_indications_medicamenteuses = models.TextField(max_length=2000,verbose_name="Contre-indications médicamenteuses", null=True,blank=True)

    
    class Meta:
        ordering = ['substance_medicinale'] 
    
    def __str__(self):
        return str(self.substance_medicinale)



class PlanteForm(ModelForm):

    class Meta:
        model = Plante
        fields = ("famille_plante",)

    def __init__(self, *args, **kwargs):

        super(PlanteForm, self).__init__(*args, **kwargs)

        self.fields["famille_plante"].widget = CheckboxSelectMultiple()
        self.fields["famille_plante"].queryset = Plante.objects.all()
    


class Diagnostic(models.Model):
    default_auto_field = 'django.db.models.AutoField'   
    syndrome_principal = models.CharField(max_length=2000,verbose_name="Syndrome principal", null=True,blank="")
    syndrome = models.TextField(max_length=2000,verbose_name="Syndrome", null=True,blank=True)
    causes = models.TextField(max_length=5000,verbose_name="Causes", null=True,blank=True)
    symptomes_explications = models.TextField(max_length=8000,verbose_name="Symptomes", null=True,blank=True)
    principes_traitements = models.TextField(max_length=2000,verbose_name="Principes de traitements", null=True,blank=True)

    points_acu = models.TextField(max_length=2000,verbose_name="Points acupuncture", null=True,blank=True)
    plantes = models.TextField(max_length=2000,verbose_name="Plantes", null=True,blank=True)
    prescriptions = models.TextField(max_length=2000,verbose_name="Prescriptions", null=True,blank=True)


    def __str__(self):
        return str(self.syndrome)


class Pathologie(models.Model):
    default_auto_field = 'django.db.models.AutoField'
    pathologie_name = models.CharField(max_length=200,verbose_name="Pathologie", null=True,blank="")

    class Meta:
        verbose_name = ("Pathologie")

    def __str__(self):
        return str(self.pathologie_name)

class PathologieCause(models.Model):
    default_auto_field = 'django.db.models.AutoField'
    patho = models.ForeignKey('Pathologie', on_delete=models.CASCADE)
    cause = models.CharField(max_length=2000,verbose_name="Cause", null=True,blank="")
    principe_therapeutique = models.CharField(max_length=2000,verbose_name="Principe therapeutique", null=True,blank="")
    explications = RichTextField(verbose_name="Explications", null=True,blank=True)
    symptome = RichTextField(max_length=2000,verbose_name="Symptome", null=True,blank="")
    #explications = models.TextField(max_length=2000,verbose_name="Explications", null=True,blank=True)
    traitement_acu = RichTextField(max_length=2000,verbose_name="Traitement acupuncture", null=True,blank=True)
    traitement_pharma = RichTextField(max_length=2000,verbose_name="Traitement pharmacopée", null=True,blank=True)
    explications_acu = RichTextField(verbose_name="Explications", null=True,blank=True)
    explications_pharma = RichTextField(verbose_name="Explications", null=True,blank=True)

    class Meta:
        verbose_name = ("Cause")

    def __str__(self):
        return str(self.cause)

        

#class PlanteFamillePlante(models.Model):
#    default_auto_field = 'django.db.models.AutoField'
#    plante = models.ForeignKey('Plante', on_delete=models.CASCADE)
#    famille_plante = models.ForeignKey('FamillePlante', on_delete=models.CASCADE)

#    def famille_plante_list(self):
#        return (self.famille_plante)

    
#class MoleculePreparationInline(admin.TabularInline):
#    model = MoleculePreparation
#    extra = 1



class PointGrandeZone(models.Model):
    default_auto_field = 'django.db.models.AutoField'
    grande_zone = models.CharField(max_length=30)

    def __str__(self):
        return str(self.grande_zone)


class PointZone(models.Model):
    default_auto_field = 'django.db.models.AutoField'
    grandeZone = models.ForeignKey('PointGrandeZone', on_delete=models.CASCADE)
    zone = models.CharField(max_length=30)
    

    def __str__(self):
        #return super().str(self.zone)
        return f"{self.grandeZone} - {self.zone}"


class Point(models.Model):
    default_auto_field = 'django.db.models.AutoField'
    zone = models.ForeignKey('PointZone', on_delete=models.CASCADE)
    point = models.CharField(max_length=100)
    color1 = ColorField(default='#FFFFFF',verbose_name="couleur 1")
    color2 = ColorField(default='#FFFFFF',verbose_name="couleur 2")
    image = models.ImageField(upload_to='images/', null=True,verbose_name="Schéma")
    #localisationAnatomique = models.CharField(max_length=100)
    maitreTungShenging = models.TextField(max_length=100,verbose_name="Me. Tung Shenging", null=True,blank=True)
    maitreTungIndicationTherapeutique = models.TextField(max_length=2000,verbose_name="Me. Tung Indication Therapeutique", null=True,blank=True)
    maitreHuShenging = models.TextField(max_length=100,verbose_name="Dr. HU Shenging", null=True,blank=True)
    maitreHuIndicationTherapeutique = models.TextField(max_length=2000,verbose_name="Dr. HU Indication Therapeutique", null=True,blank=True)
    maitreLaiShenging = models.TextField(max_length=100,verbose_name="Dr. Lai Shenging", null=True,blank=True)
    maitreLaiIndicationTherapeutique = models.TextField(max_length=2000,verbose_name="Dr. Lai Indication Therapeutique", null=True,blank=True)
   
    def __str__(self):
        return str(self.point)

    def image_tag(self):
        if self.image:
            return format_html('<a href="/media/%s" target="_blank"><img src="/media/%s" height="150" /></a>' % (self.image,self.image))
        return "-"
    image_tag.description = 'image'
    image_tag.short_description = 'schéma'
    image_tag.allow_tags = True

    def color1_tag(self):
        if self.color1:
            return format_html('<div style="width:20px;height:20px;background-color:%s"></div>' % self.color1)
        return "-"
    color1_tag.description = 'color1'
    color1_tag.short_description = 'couleur 1'
    color1_tag.allow_tags = True

    def color2_tag(self):
        if self.color2:
            return format_html('<div style="width:20px;height:20px;background-color:%s"></div>' % self.color2)
        return "-"
    color2_tag.description = 'color2'
    color2_tag.short_description = 'couleur 2'
    color2_tag.allow_tags = True