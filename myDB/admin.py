from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import *
from .forms import *

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
    #list_filter = ['famille_plante', 'action']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


    def familles(self, obj):
        return ", ".join([p.famille_plante for p in obj.famille_plante.all()])


class FamillePlanteAdmin(ImportExportMixin,admin.ModelAdmin):
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
    search_fields = ['symptomes']
    list_display = ('syndrome','symptomes','systeme')
    #list_filter = ['symptomes', 'systeme']


class DiagnosticAdmin(ImportExportMixin,admin.ModelAdmin,CSSAdminMixin):
    search_fields = ['symptomes_explications']
    list_display = ('syndrome_principal','syndrome')
    #list_filter = ['symptomes', 'systeme']


class ContactAdmin(ImportExportMixin,admin.ModelAdmin,CSSAdminMixin):
    list_display = ('nom','prenom')


admin.site.register(Plante, PlanteAdmin)

admin.site.register(FamillePlante,FamillePlanteAdmin)

admin.site.register(Prescription, PrescriptionAdmin)


# necessaire pour importer des données
#admin.site.register(PlantePrescriptionJINGFANG,PlantePrescriptionJINGFANGAdmin)
#admin.site.register(PlantePrescriptionZangfuQui,PlantePrescriptionZangfuQuiAdmin)
#admin.site.register(PlanteFamillePlante,PlanteFamillePlanteAdmin)


admin.site.register(Contact,ContactAdmin)

admin.site.register(Diagnostic,DiagnosticAdmin)







