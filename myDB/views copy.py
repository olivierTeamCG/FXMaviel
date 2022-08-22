from django.shortcuts import render, redirect
from django.forms import ModelForm, Textarea
from django import forms
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from .forms import Contact


from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton

from crispy_forms.layout import Submit, Layout, Div, Fieldset
from crispy_forms.bootstrap import TabHolder, Tab

#from django.core.mail import send_mail



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'registration-form'
        # Tu définis la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        # Tu crées l'affichage de ton formulaire
        self.helper.layout = Layout(
            # Le formulaire va contenir 3 onglets
            TabHolder(
                # Premier onglet
                Tab(
                    # Label de l'onglet
                    'Étape 1 - Identité',
                    # Liste des champs du modèle à afficher dans l'onglet
                    'nom',
                    'prenom',
                    # Tu rajoutes un bouton "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % "Suivant",
                        type='button',
                        css_class='btn-default col-md-offset-9 btnNext',
                    )

                ),
                # Deuxième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 2 - Adresse',
                    # Liste des champs à afficher
                    'date_naissance',
                    'lieu_naissance',
                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Précédent',
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Suivant',
                        type='button',
                        css_class='btn-default col-md-offset-8 btnNext',
                    )
                ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 3 - Validation',
                    # Liste des champs à afficher dont les champs supplémentaires
                    'cp',
                    'ville',
                    # Tu rajoutes des boutons "Précédent" et "Valider"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % "Précédent",
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-ok" \
                        aria-hidden="true"></span> %s' % "Valider",
                        type='submit',
                        css_class='btn-default col-md-offset-8'
                    )
                ),
            ),
        )

        #self.fields['nom'].label = "NOM"
        #self.fields['prenom'].label = "PRENOM"
        #self.fields['date_naissance'].label = "DATE de naissance"
        #self.fields['lieu_naissance'].label = "LIEU de naissance"
        #self.fields['situation_familiale'].label = "SITUATION FAMILIALE"
        #self.fields['nb_enfants'].label = "ENFANTS (nombres)"
        #self.fields['portable'].label = "PORTABLE"
        #self.fields['email'].label = "COURRIEL"
        #self.fields['adresse'].label = "ADRESSE POSTALE" 
        #self.fields['adresse'].help_text="(complète (pour livraison))"
        #self.fields['cp'].label = "CODE POSTAL"
        #self.fields['ville'].label = "VILLE"
        #self.fields['recommande_par'].label = "RECOMMANDÉ PAR"
        #Q1
        #self.fields['vous_ne_transpirez_jamais'].label = "Vous ne transpirez jamais, ou pratiquement jamais ?"


    class Meta:
        model = Contact
        #fields = ('nom', 'prenom', 'date_naissance','lieu_naissance','cp','ville')
        fields = '__all__'
        widgets = {'message': Textarea(attrs={'cols': 60, 'rows': 10}),}

def contact(request):
    # on instancie un formulaire
    form = ContactForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = ContactForm(request.POST)
        # on vérifie la validité du formulaire
        if form.is_valid():
            #send_mail(
            #    'Subject here',
            #    'Here is the message.',
            #    'auto@aaa.com',
            #    ['olivier.hansen34@gmail.com'],
            #    fail_silently=False,
            #)
            new_contact = form.save()
            # on prépare un nouveau message
            messages.success(request,'Nouveau contact '+new_contact.nom+' '+new_contact.prenom)
            #return redirect(reverse('detail', args=[new_contact.pk] ))
            context = {'pers': new_contact}
            return render(request,'detail.html', context)
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request,'contact.html', context)


def detail(request, cid):
    contact = Contact.objects.get(pk=cid)
    context = {'pers': contact}
    return render(request,'detail.html', context)

