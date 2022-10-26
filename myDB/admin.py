from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import *
from .forms import ContactFX, ContactFrancois

admin.site.site_header = "Base de donnée FX - Administration"
admin.site.site_header = "Base de donnée FX - Administration"
admin.site.site_title = "Base de donnée FX - Administration"
admin.site.index_title = "Base de donnée FX - Administration"
admin.site.enable_nav_sidebar = True


class CSSAdminMixin(object):
    class Media:
        css = {
            'all': ('css/admin.css',),
        }
        js = (
            '/static/js/jsPerso.js',
        ) 





#class PathologiePreparationAdminInline(admin.TabularInline):
#    model = PathologiePreparation
    

#class PathologieAdmin(ImportExportMixin,admin.ModelAdmin):
#    inlines = (PathologiePreparationAdminInline,)
#    search_fields = ['pathologie', 'symptomes'] 
    
# list_filter = ['pathologie', 'symptomes'] 

#class PlanteFamillePlanteAdmin(ImportExportMixin,admin.ModelAdmin):
#    model = PlanteFamillePlante

#    list_display = ('get_plante_famille','famille_plante_list')

#    def get_plante_famille(self, obj):
#        return obj.famille_plante.famille_plante

#class PlanteFamillePlanteAdminInline(admin.TabularInline):
#    model = PlanteFamillePlante



class PlanteAdmin(ImportExportMixin,admin.ModelAdmin,CSSAdminMixin):
    #inlines = (PlanteFamillePlanteAdminInline,)

    list_display = ('substance_medicinale', 'action','familles')
    search_fields = ['saveur','nature','famille_plante__famille_plante']
    #list_filter = ['famille_plante', 'action']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


    def familles(self, obj):
        return ", ".join([p.famille_plante for p in obj.famille_plante.all()])


class FamillePlanteAdmin(ImportExportMixin,admin.ModelAdmin,CSSAdminMixin):
    model = FamillePlante
    


class PlantePrescriptionJINGFANGAdmin(ImportExportMixin,admin.ModelAdmin):
    model = PlantePrescriptionJINGFANG
    extra=0

class PlantePrescriptionZangfuQuiAdmin(ImportExportMixin,admin.ModelAdmin):
    model = PlantePrescriptionZangfuQui
    extra=0


class PlantePrescriptionJINGFANGAdminInline(admin.TabularInline):
    model = PlantePrescriptionJINGFANG
    extra=5

class PlantePrescriptionZangfuQuiAdminInline(admin.TabularInline):
    model = PlantePrescriptionZangfuQui
    extra=5


class PrescriptionAdmin(ImportExportMixin,admin.ModelAdmin,CSSAdminMixin):
    inlines = (PlantePrescriptionJINGFANGAdminInline,PlantePrescriptionZangfuQuiAdminInline,)
    search_fields = ['symptomes','systeme']
    list_display = ('syndrome','symptomes','systeme')
    list_filter = ['systeme']





##################################################
##############  Pathologie      ##################
##################################################

class PathologieCauseAdminInline(admin.StackedInline):
    model = PathologieCause
    extra=0


class PathologieAdmin(ImportExportMixin,admin.ModelAdmin,CSSAdminMixin):
    inlines = (PathologieCauseAdminInline,)

    list_display = ('pathologie_name',)
    search_fields = ['pathologie_name','pathologiecause__explications','pathologiecause__symptome','pathologiecause__principe_therapeutique']
    #search_fields = ['pathologie_name','pathologiecause__symptome']
    #list_filter = ['famille_plante', 'action']
    #formfield_overrides = {
    #    models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    #}


admin.site.register(Pathologie,PathologieAdmin)

##################################################
##############  Diagnostic      ##################
##################################################


class DiagnosticAdmin(ImportExportMixin,admin.ModelAdmin,CSSAdminMixin):
    search_fields = ['symptomes_explications','syndrome_principal','syndrome','plantes']
    list_display = ('syndrome_principal','syndrome')
    #list_filter = ['systeme']


##################################################
##############  Contacts        ##################
##################################################

class ContactFXAdmin(ImportExportMixin,admin.ModelAdmin,CSSAdminMixin):
    list_display = ('nom','prenom')

class ContactFrancoisAdmin(ImportExportMixin,admin.ModelAdmin,CSSAdminMixin):
    list_display = ('nom','prenom')





admin.site.register(Plante, PlanteAdmin)

admin.site.register(FamillePlante,FamillePlanteAdmin)

admin.site.register(Prescription, PrescriptionAdmin)


# necessaire pour importer des données
#admin.site.register(PlantePrescriptionJINGFANG,PlantePrescriptionJINGFANGAdmin)
#admin.site.register(PlantePrescriptionZangfuQui,PlantePrescriptionZangfuQuiAdmin)
#admin.site.register(PlanteFamillePlante,PlanteFamillePlanteAdmin)


admin.site.register(ContactFX,ContactFXAdmin)

admin.site.register(ContactFrancois,ContactFrancoisAdmin)

admin.site.register(Diagnostic,DiagnosticAdmin)










