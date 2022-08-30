from django.shortcuts import render, redirect
from django.forms import ModelForm, Textarea
from django import forms
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from .forms import Contact


from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

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
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
                Fieldset('Questionnaire général',
                        'nom',
                        'prenom',
                        'date_naissance',
                        'lieu_naissance',
                        'situation_familiale',
                        'nb_enfants',
                        'portable',
                        'email',
                        'adresse',
                        'cp',
                        'ville',
                        'recommande_par',
                        '_mef93',
                        '_mef93bis',
                        'Traitement_1',
                        'Traitement_2',
                        'Traitement_3',
                        'Traitement_4',
                        '_mef94',
                        '_mef95',
                        'Operation_1',
                        'Operation_2',
                        'Operation_3',
                        '_mef96',
                        '_mef97',
                        'Motif_1',
                        'Motif_2',
                        'Motif_3',
                        'Medecin',
                        Fieldset('1- DESCRIPTION DÉTAILLÉE DU MOTIF N°1',
                        'M1_Quel_est_le_diagnostic',
                        'M1_Examens_Medicaux',
                        'M1_Traitements_en_rapport_avec_le_motif',
                        'M1_Quel_medicament_A_quel_dosage_Quelle',
                        'M1_Traitements_en_rapport_avec_le_motif',
                        'M1_Quel_medicament_A_quel_dosage_Quelle',
                        'M1_Traitements_en_rapport_avec_le_motif',
                        'M1_Quel_medicament_A_quel_dosage_Quelle',
                        'M1_Traitements_en_rapport_avec_le_motif',
                        'M1_Quel_medicament_A_quel_dosage_Quelle',
                        'M1_AMeLIORATION_Questce_qui_ameliore',
                        'M1_AGGRAVATION_Questce_qui_aggrave',
                        'M1_DEPUIS_QUAND_souffrezvous_des_symptome',
                        'M1_CAUSES_CIRCONSTANCES_INITIALES_des_symp',),
                        Fieldset('2- DESCRIPTION DÉTAILLÉE DU MOTIF N°2',
                        'M2_Quel_est_le_diagnostic',
                        'M2_Examens_Medicaux',
                        'M2_Traitements_en_rapport_avec_le_motif',
                        'M2_Quel_medicament_A_quel_dosage_Quelle',
                        'M2_Traitements_en_rapport_avec_le_motif',
                        'M2_Quel_medicament_A_quel_dosage_Quelle',
                        'M2_Traitements_en_rapport_avec_le_motif',
                        'M2_Quel_medicament_A_quel_dosage_Quelle',
                        'M2_Traitements_en_rapport_avec_le_motif',
                        'M2_Quel_medicament_A_quel_dosage_Quelle',
                        'M2_AMeLIORATION_Questce_qui_ameliore',
                        'M2_AGGRAVATION_Questce_qui_aggrave',
                        'M2_DEPUIS_QUAND_souffrezvous_des_symptome',
                        'M2_CAUSES_CIRCONSTANCES_INITIALES_des_symp',),
                        Fieldset('3- DESCRIPTION DÉTAILLÉE DU MOTIF N°3',
                        'M3_Quel_est_le_diagnostic',
                        'M3_Examens_Medicaux',
                        'M3_Traitements_en_rapport_avec_le_motif',
                        'M3_Quel_medicament_A_quel_dosage_Quelle',
                        'M3_Traitements_en_rapport_avec_le_motif',
                        'M3_Quel_medicament_A_quel_dosage_Quelle',
                        'M3_Traitements_en_rapport_avec_le_motif',
                        'M3_Quel_medicament_A_quel_dosage_Quelle',
                        'M3_Traitements_en_rapport_avec_le_motif',
                        'M3_Quel_medicament_A_quel_dosage_Quelle',
                        'M3_AMeLIORATION_Questce_qui_ameliore',
                        'M3_AGGRAVATION_Questce_qui_aggrave',
                        'M3_DEPUIS_QUAND_souffrezvous_des_symptome',
                        'M3_CAUSES_CIRCONSTANCES_INITIALES_des_symp',),),
                Fieldset('Questionnaire Emotion',
                        '_mef85',
                        '_mef86',
                        'etre_SOUCIEUX_ANXIEUX',
                        '_mef87',
                        'etre_TRISTE',
                        '_mef88',
                        'avoir_PEUR',
                        '_mef89',
                        'etre_EXAGEREMENT_JOYEUX_ou_TRISTE',
                        '_mef90',
                        'etre_en_COLERE',
                        '_mef91',
                        'Commentaires_f8_1',
                        '_mef92',
                        'etes_vous_en_conflit_affectif',
                        'etes_vous_en_deuil',
                        'etes_vous_en_tension_dans_votre_sphere',
                        'etes_vous_en_procedure_judiciaire',
                        'Commentaires_f8_2',),
                Fieldset('Questionnaire 1 : Transpiration',
                        '_mef3','_mef4',
                        'Vous_ne_transpirez_jamais_ou_pratiqueme',
                        'Transpirez_vous_tres_facilement_au_moin',
                        'Transpirez_vous_spontanement_sans_raiso',
                        'Transpirez_vous_a_grosses_gouttes_cela',
                        'Transpirez_vous_quand_il_fait_chaud_ou_t',
                        'Transpirez_vous_quand_vous_faites_du_spo',
                        'Votre_transpiration_sent_elle_fort',
                        'Votre_transpiration_est_elle_jaunatre_et',
                        'Transpirez_vous_des_mains_et_ou_des_pied',
                        'Transpirez_vous_la_nuit',
                        'Transpirez_vous_du_visage',
                        'Commentaires_f1_1',
                        '_mef5',
                        '_mef6',
                        'Craignez_vous_les_courants_dair',
                        'Craignez_vous_le_vent',
                        'Aimez_vous_le_vent',
                        'Le_vent_vous_est_il_indifferent',
                        '_mef7',
                        'Craignez_vous_le_froid_le_frais',
                        'Aimez_vous_le_froid_le_frais',
                        'Le_froid_frais_vous_sont_ils_indifferent',
                        '_mef8',
                        'Craignez_vous_lhumidite',
                        'Aimez_vous_lhumidite',
                        'Lhumidite_vous_est_elle_indifferente',
                        '_mef9',
                        'Craignez_vous_le_chaud',
                        'Aimez_vous_le_chaud',
                        'Le_chaud_vous_est_il_indifferent',
                        'Commentaires_f1_2',
                        '_mef10',
                        '_mef11',
                        'Avez_vous_plutot_ou_toujours_froid',
                        'Avez_vous_froid_aux_pieds_et_aux_mains',
                        'Avez_vous_froid_quaux_pieds',
                        'Avez_vous_froid_au_ventre',
                        'Avez_vous_froid_a_tous_les_membres_infer',
                        'Avez_vous_froid_dans_tout_le_corps',
                        'Avez_vous_froid_dans_le_dos',
                        'Avez_vous_cette_sensation_le_jour',
                        'Avez_vous_cette_sensation_la_nuit',
                        '_mef13',
                        'Avez_vous_plutot_ou_toujours_chaud_tout',
                        'Vous_avez_chaud_a_la_tête',
                        'Vous_avez_chaud_mais_que_par_moment',
                        'Vous_avez_chaud_seulement_aux_pieds',
                        'Vous_avez_de_la_chaleur_qui_part_du_bas',
                        'Vous_avez_chaud_puis_de_la_transpiratio',
                        'Vous_avez_ces_sensations_le_jour',
                        'Vous_avez_ces_sensations_la_nuit',
                        '_mef14',
                        'Vous_avez_des_alternances_de_sensation_d',
                        'Vous_avez_des_bouffees_de_chaleur_suivie_de_frissons',
                        'Vous_avez_des_bouffees_de_chaleur_suivie_de_transpiration',
                        'Vous_avez_des_bouffees_de_chaleur_pendant',
                        'Vous_avez_des_bouffees_de_chaleur_pendant_bas',
                        'Vous_avez_chaud_une_partie_de_la_journee',
                        'Vous_avez_en_même_temps_une_partie_du_co',
                        'Vous_avez_chaud_quand_il_fait_chaud_et',
                        'Vous_avez_ces_sensations_le_jour',
                        'Vous_avez_ces_sensations_la_nuit',
                        'Commentaires_f1_3',
                        '_mef14bis',
                        'Dans_la_bouche_la_langue',
                        'Dans_la_gorge',
                        'Sur_les_levres',
                        'Dans_le_nez',
                        'Dans_les_yeux',
                        'Commentaires_f1_4'
                        '_mef15',
                        'Quelle_est_votre_temperature_corporelle_jour',
                        'Quelle_est_votre_temperature_corporelle_nuit',
                        'Avez_vous_de_la_fievre_regulierement',
                        'La_nuit',
                        'Le_jour',
                        'Dans_lapres_midi',
                        'Combien',
                        'Commentaires_f1_5',
                        '_mef16',
                        'Vous_avez_soif',
                        'Vous_navez_pas_soif',
                        'Vous_buvez_beaucoup_parce_que_vous_avez',
                        'Vous_buvez_a_temperature_ambiante',
                        'Vous_buvez_chaud',
                        'Vous_buvez_froid',
                        'Vous_vous_forcez_de_boire_15l_deau_par',
                        'Commentaires_f1_6',),
                        Fieldset('Questionnaire 2 : Transpiration',
                        '_mef17','_mef18','_mef19','_mef20',
                        'Globalement_dans_toutes_les_articulation',
                        'La_nuque_le_cou_le_rachis_cervical',
                        'Les_trapezes_entre_le_cou_et_les_epaule',
                        'Le_haut_du_dos',
                        'Le_milieu_du_dos',
                        'Le_bas_du_dos_rachis_lombaire',
                        'La_poitrine',
                        'Labdomen',
                        'Les_cotes',
                        'Les_epaules',
                        'les_coudes',
                        'les_poignets_mains_doigts',
                        'Les_hanches',
                        'Les_genoux',
                        'Les_chevilles',
                        'Les_pieds',
                        'La_tete',
                        'Les_oreilles',
                        'Les_yeux',
                        'Le_nez',
                        'la_bouche',
                        'Commentaires_f2_1',
                        '_mef21',
                        'calme_douleur_La_nuit',
                        'calme_douleur_Le_jour',
                        'calme_douleur_Le_chaud',
                        'calme_douleur_Le_froid',
                        'calme_douleur_Le_mouvement',
                        'calme_douleur_La_pression_le_massage',
                        'Commentaires_f2_2',
                        '_mef22',
                        'augmente_douleur_La_nuit',
                        'augmente_douleur_Le_jour',
                        'augmente_douleur_Le_chaud',
                        'augmente_douleur_Le_froid',
                        'augmente_douleur_Le_mouvement',
                        'augmente_douleur_La_pression_le_massage',
                        'Commentaires_f2_3',
                        '_mef23',
                        'Les_articulations_douloureuses_sont_froi',
                        'Les_articulations_douloureuses_sont_chau',
                        'Les_articulations_douloureuses_sont_roug',
                        'Les_articulations_douloureuses_sont_enfl',
                        'Commentaires_f2_4',
                        '_mef24',
                        '_mef24',
                        'Commentaires_f2_5',
                        '_mef26',
                        'Certaines_parties_de_votre_peau_vous_dem',
                        'La_demangeaison_est_elle_insupportable',
                        'La_ou_cela_vous_demange_cela_est_il_cha',
                        'La_ou_cela_vous_demange_cela_est_il_rou',
                        'La_ou_cela_vous_demange_y_a_t_il_des_cl',
                        'La_ou_cela_vous_demange_y_a_t_il_des_cl',
                        'La_ou_cela_vous_demange_cela_suinte_t_i',
                        'Commentaires_f2_6',
                        '_mef27',
                        'Avez_vous_des_tics_des_tremblements',
                        'Avez_vous_des_crampes',
                        'Avez_vous_des_engourdissements',
                        'Avez_vous_des_spasmes',
                        'Avez_vous_des_tendinites',
                        'Avez_vous_des_myalgies_douleur_dans_les',
                        'Le_jour',
                        'La_nuit',
                        'Commentaires_f2_7',
                        '_mef28',
                        'Avez_vous_des_vertiges',
                        'Avez_vous_des_acouphenes',
                        'Avez_vous_des_migraines_un_seul_et_meme',
                        'Avez_vous_des_maux_de_tete_ou_cephalee',
                        'Avez_vous_le_nez_bouche',
                        'Avez_vous_le_nez_qui_coule',
                        'Avez_vous_des_mucosites_gorge_nez_bou',
                        'Avez_vous_des_eternuements',
                        'Avez_vous_perdu_lodorat',
                        'Commentaires_f2_8',
                        '_mef29',
                        'Avez_vous_dans_la_bouche_un_gout_amer',
                        'Avez_vous_dans_la_bouche_un_gout_metalli',
                        'Avez_vous_dans_la_bouche_un_autre_gout_a',
                        'Avez_vous_perdu_le_gout',
                        '#Commentaires_f2_9',),
                        Fieldset('Questionnaire 3 : Thorax',
                        '_mef31','_mef32','_mef33',
                        'Avez_vous_de_la_toux',
                        'Avez_vous_une_gene_ou_de_la_difficulte_a',
                        'Ressentez_vous_une_oppression_thoracique',
                        'Ressentez_vous_une_oppression_au_niveau',
                        'Ressentez_vous_une_oppression_au_niveau',
                        'Avez_vous_des_palpitations_cardiaques',
                        'Combien_de_pulsations_cardiaques_avez_vo',
                        'Commentaires_f3_1',
                        '_mef34','_mef35',
                        'Avez_vous_labdomen_dans_son_ensemble_mou',
                        'Avez_vous_labdomen_dans_son_ensemble_dur',
                        'Aimez_vous_la_chaleur_sur_labdomen',
                        'Vous_ne_supportez_pas_la_chaleur_sur_la',
                        'Avez_vous_la_partie_abdominale_au_dessus',
                        'Avez_vous_des_rots',
                        'Avez_vous_le_plexus_solaire_tendu_voire',
                        'Avez_vous_la_partie_abdominale_en_dessou',
                        'Avez_vous_des_gaz',
                        'Avez_vous_des_borborygmes',
                        'Commentaires_f3_2',
                        '_mef36','_mef37',
                        'Vos_urines_sont_elles_nombreuses',
                        'Vos_urines_sont_elles_en_grandes_quantit',
                        'Vos_urines_sont_elles_en_petite_quantite',
                        'Vos_urines_sont_elles_frequentes',
                        'Vos_urines_ont_elles_une_odeur',
                        'Vos_urines_sont_elles_claires',
                        'Vos_urines_sont_elles_foncees',
                        'Vos_urines_sont_elles_troubles',
                        'Vos_urines_sont_elles_difficiles_a_evacu',
                        'Urinez_vous_la_nuit',
                        'Combien_de_fois_la_nuit',
                        'Commentaires_f3_3',
                        '_mef38','_mef39',
                        'Allez_vous_chaque_jour_a_la_selle',
                        'Allez_vous_plusieurs_fois_par_jour_a_la',
                        'Tous_les_combien_de_jours_y_allez_vous',
                        'Vos_selles_sont_elles_liquides',
                        'Vos_selles_sont_elles_defaites',
                        'Les_aliments_ne_sont_ils_pas_digeres',
                        'Vos_selles_sont_elles_molles',
                        'Vos_selles_sont_elles_dures',
                        'Vos_selles_sont_elles_seches',
                        'Vos_selles_sont_elles_seches_comme_des_b',
                        'Vos_selles_sentent_elles_excessivement_f',
                        'Vos_selles_sont_elles_douloureuses',
                        'Vos_selles_sont_elles_abondantes',
                        'Vos_selles_sont_elles_peu_abondantes',
                        'Il_y_a_du_sang_dans_vos_selles',
                        'Commentaires_f3_4',
                        '_mef40','_mef41','_mef42',),
                        Fieldset('Questionnaire 4 : Votre sommeil',
                        'Avez_vous_tandance_a_etre_facilement_rev',
                        '_mef43',
                        'Souffrez_vous_dinsomnies',
                        '_mef44',
                        'Souffrez_vous_de_somnolence_dhypersomn',
                        '_mef45',
                        'Faites_vous_des_reves_perturbant_votre_s',
                        '_mef46',
                        'Faites_vous_des_cauchemars',
                        '_mef47',
                        'Commentaires_f4_1',
                        '_mef48',
                        'Vous_sentez_vous_fatigue_en_ce_moment',
                        'Vous_sentez_vous_tres_souvent_fatigue',
                        'Vous_sentez_vous_epuise_au_point_de_dev',
                        'Vous_sentez_vous_tres_souvent_epuise_au',
                        'Avez_vous_des_coups_de_barre_A_quelles',
                        'Votre_fatigue_ou_la_situez_vous',
                        'Commentaires_f4_2',
                        '_mef49',
                        'A_des_medicaments',
                        'Lesquels',
                        'A_des_aliments',
                        'Lesquels',
                        'Respiratoires',
                        'Lesquels',
                        'De_contact',
                        'Lesquels',
                        'Commentaires_f4_3',
                        '_mef50',
                        'Tabac',
                        'Cafe',
                        'The',
                        'Drogue',
                        'Medicaments',
                        'Sucre',
                        'Sale',
                        'Sodas',
                        'Commentaires_f4_4',),
                        Fieldset('Questionnaire 5 : Gynecologie',
                        '_mef52',
                        'etes_vous_menopausee',
                        'Avez_vous_un_traitement_hormonal',
                        'Lequel',
                        'Avez_vous_un_moyen_de_contraception_chim',
                        'Avez_vous_un_moyen_de_contraception_uniq',
                        'Avez_vous_un_moyen_de_contraception_mixt',
                        'Vous_navez_pas_de_moyen_de_contraceptio',
                        '_mef53',
                        'Votre_cycle_est_il_regulier',
                        'Votre_cycle_est_il_irregulier',
                        'Votre_cycle_est_il_toujours_court_moins',
                        'Votre_cycle_est_toujours_long_plus_de_2',
                        'Votre_cycle_est_il_quelques_fois_court_e',
                        'Commentaires_f5_1',
                        '_mef54',
                        'Vos_regles_durent_elles_7_jours_et_plus',
                        'Vos_regles_durent_elles_au_maximum_3_jou',
                        'Vos_regles_durent_elles_entre_4_a_6_jour',
                        'Commentaires_f5_2',
                        '_mef55',
                        'Vos_regles_sont_elles_hemorragiques',
                        'Vos_regles_sont_elles_abondantes',
                        'Vos_regles_sont_elles_peu_abondantes',
                        'La_quantite_de_sang_vous_semble_t_elle_n',
                        'Commentaires_f5_3',
                        '_mef56',
                        'Votre_sang_est_il_sombre',
                        'Votre_sang_est_il_pourpre',
                        'Votre_sang_est_il_rouge_vif',
                        'Votre_sang_est_il_rose_pâle',
                        'Votre_sang_est_il_tres_clair',
                        'Commentaires_f5_4',
                        '_mef57',
                        'Avez_vous_des_caillots_dans_vos_regles',
                        'Votre_sang_est_il_epais',
                        'Votre_sang_est_il_collant_gluant',
                        'Votre_sang_est_il_tres_liquide_tres_flu',
                        'Commentaires_f5_5',
                        '_mef58',
                        'Avez_vous_des_douleurs_liees_aux_regles',
                        'Avez_vous_des_douleurs_AVANT_les_regles',
                        'Avez_vous_des_douleurs_PENDANT_les_regle',
                        'Avez_vous_des_douleurs_APReS_les_regles',
                        'Avez_vous_des_douleurs_au_moment_de_lov',
                        'Commentaires_f5_6',
                        '_mef59',
                        'Avez_vous_des_MAUX_DE_TeTE',
                        'Avez_vous_des_douleurs_aux_SEINS',
                        'Avez_vous_des_douleurs_au_VENTRE',
                        'Avez_vous_des_douleurs_au_BAS_DU_DOS',
                        'Commentaires_f5_7',
                        '_mef60',
                        'Vos_douleurs_sont_elles_sourdes',
                        'Vos_douleurs_ressemblent_elles_a_des_cou',
                        'Vos_douleurs_ressemblent_elles_a_une_pre',
                        'Avez_vous_une_sensation_de_froid_dans_le',
                        'Apres_les_regles_etes_vous_fatiguee',
                        'Commentaires_f5_8',
                        '_mef61',
                        'Par_de_la_chaleur_bouillotte_ou_autre',
                        'Par_des_medicaments',
                        'Vous_ne_faites_rien_et_attendez_que_cela',
                        'Commentaires_f5_9',
                        '_mef62',
                        'Avez_vous_des_hemorragies_uterine_en_DEH',
                        'Avez_vous_une_absence_de_flux_menstruel',
                        'Avez_vous_des_pertes_leucorrhees',
                        'Sont_elles_translucides_comme_du_blanc_d',
                        'Sont_elles_blanchâtres',
                        'Sont_elles_plutôt_jaunes_ordorantes',
                        'Sont_elles_striees_de_sang',
                        'Avez_vous_des_mycoses',
                        'Avez_vous_des_infections',
                        'Commentaires_f5_10',),
                        Fieldset('Questionnaire 6 : DIGESTION',
                        '_mef64','_mef65'
                        'Manquez_vous_dappetit',
                        'etes_vous_souvent_fatigue_apres_le_rep',
                        'Avez_vous_une_digestion_lente',
                        'Avez_vous_parfois_des_ballonnements',
                        'Avez_vous_des_selles_molles',
                        'Avez_vous_des_traces_daliments_non_di',
                        'Avez_vous_des_fringales_de_sucre',
                        'Preferez_vous_boire_chaud',
                        'Avez_vous_parfois_la_bouche_pâteuse',
                        'Avez_vous_le_teint_pâle_terne',
                        'Prenez_vous_facilement_du_poids',
                        'Avez_vous_les_levres_pâles',
                        'Avez_vous_la_tete_lourde',
                        'Avez_vous_le_sentiment_davoir_perdu_l',
                        'Commentaires_f6_1',
                        '_mef66',
                        'Craignez_vous_le_froid_ou_avez_vous_le',
                        'Avez_vous_de_la_diarrhee',
                        'Avez_vous_les_selles_liquides_et_peu_o',
                        'Avez_vous_le_teint_pale_ou_la_langue_p',
                        'Souffrez_vous_doedemes',
                        'Commentaires_f6_2',
                        '_mef67',
                        'Souffrez_vous_de_sensation_de_douleur',
                        'Soupirez_vous_souvent',
                        'Eprouvez_vous_le_besoin_de_bailler_ou',
                        'Vous_mettez_vous_souvent_en_colere_et',
                        'Souffrez_vous_dun_etat_depressif',
                        'Avez_vous_un_syndrome_premenstruel',
                        'Souffrez_vous_dune_colopathie_fonctio',
                        'Commentaires_f6_3',
                        '_mef68',
                        'Souffrez_vous_de_douleurs_a_lestomac',
                        'Avez_vous_des_regurgitacions_acides',
                        'Avez_vous_frequemment_des_hoquets',
                        'Avez_vous_frequemment_des_eructations',
                        'Vomissez_vous_parfois',
                        'Avez_vous_parfois_des_nausees',
                        'Avez_vous_des_borborygmes_bruits_au',
                        'Commentaires_f6_4',
                        '_mef69',
                        'Avez_vous_un_degout_pour_la_nourriture',
                        'Avez_vous_des_eructations_fetides_ou_q',
                        'Avez_vous_mauvaise_haleine',
                        'Avez_vous_des_vomissements_daliments',
                        'Avez_vous_une_digestion_tres_lourde_et',
                        'Est_ce_que_lenduit_de_votre_langue_a',
                        'Commentaires_f6_5',
                        '_mef70',
                        'Avez_vous_souvent_faim_et_un_fort_appe',
                        'Etes_vous_plutot_attire_par_des_boisso',
                        'Avez_vous_une_digestion_rapide',
                        'Avez_vous_une_mauvaise_haleine',
                        'Etes_vous_constipe',
                        'Souffrez_vous_de_sensations_de_brulure',
                        'Souffrez_vous_de_gingivite',
                        'Commentaires_f6_6',
                        '_mef71',
                        'Avez_vous_faim_sans_desir_de_manger',
                        'Avez_vous_une_diminution_de_lappetit',
                        'Soufrez_vous_de_douleur_legere_sourde',
                        'Avez_vous_des_levres_seches_brulees_o',
                        'Avez_vous_les_selles_seches',
                        'Avez_vous_la_langue_et_la_gorge_seche',
                        'Souffrez_vous_de_transpiration_nocturn',
                        'Commentaires_f6_7',
                        '_mef72',
                        'Avez_vous_une_sensation_de_froid_dans',
                        'Avez_vous_une_douleur_de_lestomac_acc',
                        'Cette_douleur_est_elle_aggravee_par_le',
                        'Souffrez_vous_de_vomissements_de_liqui',
                        'Commentaires_f6_8',
                        '_mef73',
                        'Avez_vous_une_distension_et_une_douleu',
                        'Avez_vous_de_lirritabilite_de_la_col',
                        'Avez_vous_des_eructations_et_hoquets_f',
                        'Souffrez_vous_dune_sensation_de_gene',
                        'Est_ce_que_vos_troubles_digestifs_sont',
                        'Commentaires_f6_9',
                        '#',),
                        Fieldset('Questionnaire 7 : DOULEURS_ARTICULAIRES',
                        '_mef74','_mef75','_mef76','_mef77',
                        'La_douleur_est_elle_mobile_changeante',
                        'Les_articulations_ont_elles_perdues_de_l',
                        'Detestez_vous_le_vent_les_courants_dai',
                        'Avez_vous_en_meme_temps_de_la_fievre_et',
                        'Avez_vous_des_courbatures_generalisees',
                        '_mef78',
                        'La_douleur_est_elle_severe_fixe_locali',
                        'La_douleur_est_elle_aggravee_par_le_froi',
                        'Avez_vous_une_sensation_de_froid_dans_la',
                        'Y_a_t_il_de_la_rougeur_une_sensation_de',
                        'Votre_articulation_douloureuse_bouge',
                        'Votre_douleur_est_elle_aggravee_a_la_pre',
                        '_mef79',
                        'La_douleur_est_elle_localisee_avec_une',
                        'Le_froid_ou_lhumidite_augmentent_ils_la',
                        'La_douleur_est_elle_peu_violente_mais_pe',
                        'Les_articulations_ont_elles_des_oedemes',
                        'La_mobilite_des_articulations_est_elle_l',
                        'Y_a_t_il_une_rougeur_locale',
                        '_mef80',
                        'La_douleur_est_elle_severe_avec_une_sen',
                        'La_douleur_est_elle_aggravee_par_la_chal',
                        'La_douleur_est_elle_amelioree_par_le_fro',
                        'Avez_vous_perdu_la_mobilite_dune_ou_plu',
                        'Avez_vous_de_la_fievre_de_la_soif_etes',
                        '_mef81',
                        'La_douleur_est_elle_peu_severe_mais_chro',
                        'La_douleur_est_elle_aggravee_par_le_mouv',
                        'Avez_vous_des_spasmes_musculaires_tendi',
                        'Avez_vous_des_sensations_de_fourmillemen',
                        'Avez_vous_perdu_de_la_force_musculaire',
                        'Avez_vous_des_raideurs_musculaires',
                        'Vous_sentez_vous_fatigue_avez_vous_le_s',
                        'Avez_vous_des_etourdissements_peu_ou_pa',
                        '_mef82',
                        'Vos_articulations_sont_elles_douloureuse',
                        'La_douleur_est_elle_aggravee_la_nuit',
                        'La_douleur_est_elle_aggravee_par_le_mouv',
                        'Avez_vous_une_sensation_de_chaleur_local',
                        'Vos_articulations_sont_elles_deformees_a',
                        'Ce_sont_surtout_les_hanches_qui_sont_tou',
                        'Ce_sont_surtout_les_genoux_qui_sont_touc',
                        'Ce_sont_surtout_la_region_lombaire',
                        'Avez_vous_de_la_fievre_en_fin_dapres_mi',
                        'Transpirez_vous_la_nuit',
                        'Avez_vous_des_acouphenes_des_vertiges',
                        '_mef83',
                        'Les_articulations_sont_elles_douloureuse',
                        'La_douleur_est_elle_aggravee_par_le_froi',
                        'Les_douleurs_sont_elles_surtout_situees',
                        'Craignez_vous_le_froid',
                        'Vos_membres_sont_ils_froids',
                        'Etes_vous_fatigue',
                        'Avez_vous_des_selles_molles',
                        'Urinez_vous_souvent_abondamment_et_de_c',
                        'Commentaires_f7_1',),
        )
        

        self.helper.add_input(Submit('submit', 'Submit')) 
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
        #fields = ('nom', 'prenom', 'date_naissance','lieu_naissance','situation_familiale','nb_enfants','portable','email','adresse','cp','ville','recommande_par','vous_ne_transpirez_jamais')
        
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

