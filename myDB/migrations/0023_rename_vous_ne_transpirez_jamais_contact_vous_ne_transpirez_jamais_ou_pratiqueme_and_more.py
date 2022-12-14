# Generated by Django 4.0.6 on 2022-08-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0022_alter_contact_transpirez_vous_tres_facilement_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='vous_ne_transpirez_jamais',
            new_name='Vous_ne_transpirez_jamais_ou_pratiqueme',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='transpirez_vous_tres_facilement',
        ),
        migrations.AddField(
            model_name='contact',
            name='Aimez_vous_le_chaud',
            field=models.BooleanField(default=False, verbose_name='Aimez_vous le chaud ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Aimez_vous_le_froid_le_frais',
            field=models.BooleanField(default=False, verbose_name='Aimez_vous le froid, le frais ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Aimez_vous_le_vent',
            field=models.BooleanField(default=False, verbose_name='Aimez_vous le vent ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Aimez_vous_lhumidite',
            field=models.BooleanField(default=False, verbose_name='Aimez_vous lhumidité ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_cette_sensation_la_nuit',
            field=models.BooleanField(default=False, verbose_name='Avez_vous cette sensation la nuit ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_cette_sensation_le_jour',
            field=models.BooleanField(default=False, verbose_name='Avez_vous cette sensation le jour ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_de_la_fievre_regulierement',
            field=models.BooleanField(default=False, verbose_name='Avez_vous de la fièvre régulièrement ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_froid_a_tous_les_membres_infer',
            field=models.BooleanField(default=False, verbose_name='Avez_vous froid a tous les membres inférieurs ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_froid_au_ventre',
            field=models.BooleanField(default=False, verbose_name='Avez_vous froid au ventre ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_froid_aux_pieds_et_aux_mains',
            field=models.BooleanField(default=False, verbose_name='Avez_vous froid aux pieds et aux mains ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_froid_dans_le_dos',
            field=models.BooleanField(default=False, verbose_name='Avez_vous froid dans le dos ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_froid_dans_tout_le_corps',
            field=models.BooleanField(default=False, verbose_name='Avez_vous froid dans tout le corps ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_froid_quaux_pieds',
            field=models.BooleanField(default=False, verbose_name='Avez_vous froid quaux pieds ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_plutot_ou_toujours_chaud_tout',
            field=models.BooleanField(default=False, verbose_name='Avez_vous plutot ou toujours chaud, tout le temps ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_plutot_ou_toujours_froid',
            field=models.BooleanField(default=False, verbose_name='Avez_vous plutot ou toujours froid ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Avez_vous_une_sensation_de_SeCHERESSE',
            field=models.BooleanField(default=False, verbose_name='Avez_vous une sensation de SÈCHERESSE : '),
        ),
        migrations.AddField(
            model_name='contact',
            name='Combien',
            field=models.BooleanField(default=False, verbose_name='Combien ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Craignez_vous_le_chaud',
            field=models.BooleanField(default=False, verbose_name='Craignez_vous le chaud ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Craignez_vous_le_froid_le_frais',
            field=models.BooleanField(default=False, verbose_name='Craignez_vous le froid, le frais ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Craignez_vous_le_vent',
            field=models.BooleanField(default=False, verbose_name='Craignez_vous le vent ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Craignez_vous_les_courants_dair',
            field=models.BooleanField(default=False, verbose_name='Craignez_vous les courants dair ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Craignez_vous_lhumidite',
            field=models.BooleanField(default=False, verbose_name='Craignez_vous lhumidité ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Dans_la_bouche_la_langue',
            field=models.BooleanField(default=False, verbose_name='Dans la bouche, la langue'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Dans_la_gorge',
            field=models.BooleanField(default=False, verbose_name='Dans la gorge'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Dans_lapres_midi',
            field=models.BooleanField(default=False, verbose_name='Dans laprès_midi ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Dans_le_nez',
            field=models.BooleanField(default=False, verbose_name='Dans le nez'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Dans_les_yeux',
            field=models.BooleanField(default=False, verbose_name='Dans les yeux'),
        ),
        migrations.AddField(
            model_name='contact',
            name='LES_COURANTS_DAIR_LE_VENT',
            field=models.BooleanField(default=False, verbose_name='LES COURANTS DAIR _ LE VENT'),
        ),
        migrations.AddField(
            model_name='contact',
            name='LE_CHAUD',
            field=models.BooleanField(default=False, verbose_name='LE CHAUD'),
        ),
        migrations.AddField(
            model_name='contact',
            name='LE_FROID',
            field=models.BooleanField(default=False, verbose_name='LE FROID'),
        ),
        migrations.AddField(
            model_name='contact',
            name='LHUMIDITe',
            field=models.BooleanField(default=False, verbose_name='LHUMIDITÉ'),
        ),
        migrations.AddField(
            model_name='contact',
            name='La_nuit',
            field=models.BooleanField(default=False, verbose_name='La nuit ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Le_chaud_vous_est_il_indifferent',
            field=models.BooleanField(default=False, verbose_name='Le chaud vous est_il indifférent ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Le_froid_frais_vous_sont_ils_indifferent',
            field=models.BooleanField(default=False, verbose_name='Le froid/frais vous sont_ils indifférents ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Le_jour',
            field=models.BooleanField(default=False, verbose_name='Le jour ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Le_vent_vous_est_il_indifferent',
            field=models.BooleanField(default=False, verbose_name='Le vent vous est_il indifférent ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Lhumidite_vous_est_elle_indifferente',
            field=models.BooleanField(default=False, verbose_name='Lhumidité vous est_elle indifférente ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Quelle_est_votre_temperature_corporelle_jour',
            field=models.BooleanField(default=False, verbose_name='Quelle est votre température corporelle habituelle le jour ? '),
        ),
        migrations.AddField(
            model_name='contact',
            name='Quelle_est_votre_temperature_corporelle_nuit',
            field=models.BooleanField(default=False, verbose_name='Quelle est votre température corporelle habituelle la nuit ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='SENSATION_ALTERNeE_DE_CHAUD_ET_DE_FROID',
            field=models.BooleanField(default=False, verbose_name='SENSATION ALTERNÉE DE CHAUD ET DE FROID'),
        ),
        migrations.AddField(
            model_name='contact',
            name='SENSATION_DE_CHALEUR',
            field=models.BooleanField(default=False, verbose_name='SENSATION DE CHALEUR'),
        ),
        migrations.AddField(
            model_name='contact',
            name='SENSATION_DE_FROID',
            field=models.BooleanField(default=False, verbose_name='SENSATION DE FROID'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Sur_les_levres',
            field=models.BooleanField(default=False, verbose_name='Sur les lèvres'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Transpirez_vous_a_grosses_gouttes_cela',
            field=models.BooleanField(default=False, verbose_name='Transpirez_vous a grosses gouttes, cela dégouline ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Transpirez_vous_des_mains_et_ou_des_pied',
            field=models.BooleanField(default=False, verbose_name='Transpirez_vous des mains et/ou des pieds, sans cesse ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Transpirez_vous_du_visage',
            field=models.BooleanField(default=False, verbose_name='Transpirez_vous du visage ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Transpirez_vous_la_nuit',
            field=models.BooleanField(default=False, verbose_name='Transpirez_vous la nuit ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Transpirez_vous_quand_il_fait_chaud_ou_t',
            field=models.BooleanField(default=False, verbose_name='Transpirez_vous quand il fait chaud ou très chaud ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Transpirez_vous_quand_vous_faites_du_spo',
            field=models.BooleanField(default=False, verbose_name='Transpirez_vous quand vous faites du sport ou un effort soutenu ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Transpirez_vous_spontanement_sans_raiso',
            field=models.BooleanField(default=False, verbose_name='Transpirez_vous spontanément, sans raison, sans faire deffort ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Transpirez_vous_tres_facilement_au_moin',
            field=models.BooleanField(default=False, verbose_name='Transpirez_vous très facilement, au moindre effort ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vos_sensations_corporelles_de_CHALEUR_et',
            field=models.BooleanField(default=False, verbose_name='Vos sensations corporelles de CHALEUR et de FROID'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vos_sensations_par_rapport_au_temps',
            field=models.BooleanField(default=False, verbose_name='Vos sensations par rapport au TEMPS QUIL FAIT'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Votre_transpiration_est_elle_jaunatre_et',
            field=models.BooleanField(default=False, verbose_name='Votre transpiration est_elle jaunâtre et peut tacher vos vêtements ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Votre_transpiration_sent_elle_fort',
            field=models.BooleanField(default=False, verbose_name='Votre transpiration sent_elle fort ?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_ces_sensations_la_nuit',
            field=models.BooleanField(default=False, verbose_name='Vous avez ces sensations la nuit'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_ces_sensations_le_jour',
            field=models.BooleanField(default=False, verbose_name='Vous avez ces sensations le jour '),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_chaud_a_la_tête',
            field=models.BooleanField(default=False, verbose_name='Vous avez chaud a la tête'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_chaud_mais_que_par_moment',
            field=models.BooleanField(default=False, verbose_name='Vous avez chaud mais que par moment'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_chaud_puis_de_la_transpiratio',
            field=models.BooleanField(default=False, verbose_name='Vous avez chaud, puis de la transpiration sans sensation de froid'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_chaud_quand_il_fait_chaud_et',
            field=models.BooleanField(default=False, verbose_name='Vous avez chaud quand il fait chaud, et avez froid quand il fait froid.'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_chaud_seulement_aux_pieds',
            field=models.BooleanField(default=False, verbose_name='Vous avez chaud seulement aux pieds'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_chaud_une_partie_de_la_journee',
            field=models.BooleanField(default=False, verbose_name='Vous avez chaud une partie de la journée et froid lautre partie'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_de_la_chaleur_qui_part_du_bas',
            field=models.BooleanField(default=False, verbose_name='Vous avez de la chaleur qui part du bas de la poitrine et qui monte vers le haut'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_des_alternances_de_sensation_d',
            field=models.BooleanField(default=False, verbose_name='Vous avez des alternances de sensation de chaud et de froid'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_des_bouffees_de_chaleur_pendant',
            field=models.BooleanField(default=False, verbose_name='Vous avez des bouffées de chaleur pendant 1 minute puis très vite froid'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_des_bouffees_de_chaleur_pendant_bas',
            field=models.BooleanField(default=False, verbose_name='Vous avez des bouffées de chaleur pendant 1 minute puis TRÈS FROID EN BAS'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_des_bouffees_de_chaleur_suivie_de_frissons',
            field=models.BooleanField(default=False, verbose_name='Vous avez des bouffées de chaleur suivies de frissons ou de froid'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_des_bouffees_de_chaleur_suivie_de_transpiration',
            field=models.BooleanField(default=False, verbose_name='Vous avez des bouffées de chaleur suivies de transpiration mais pas de froid'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_en_même_temps_une_partie_du_co',
            field=models.BooleanField(default=False, verbose_name='Vous avez en même temps une partie du corps chaude et lautre froide'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_avez_soif',
            field=models.BooleanField(default=False, verbose_name='Vous avez soif'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_buvez_a_temperature_ambiante',
            field=models.BooleanField(default=False, verbose_name='Vous buvez a température ambiante'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_buvez_beaucoup_parce_que_vous_avez',
            field=models.BooleanField(default=False, verbose_name='Vous buvez beaucoup parce que vous avez toujours soif'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_buvez_chaud',
            field=models.BooleanField(default=False, verbose_name='Vous buvez chaud'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_buvez_froid',
            field=models.BooleanField(default=False, verbose_name='Vous buvez froid'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_navez_pas_soif',
            field=models.BooleanField(default=False, verbose_name='Vous navez pas soif'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Vous_vous_forcez_de_boire_15l_deau_par',
            field=models.BooleanField(default=False, verbose_name='Vous vous forcez de boire 1,5l deau par jour parce que vous pensez que cest bon pour votre organisme.'),
        ),
    ]
