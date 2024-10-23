import streamlit as st
from deep_translator import GoogleTranslator
import pdfkit

# Fonction pour traduire le texte
def translate_text(text, target_language):
    translator = GoogleTranslator(source='auto', target=target_language)
    translation = translator.translate(text)
    return translation

def is_valid_email(email):
    # Une simple vérification de la validité de l'e-mail
    return '@' in email and '.' in email

def main():
    # Sélection de la langue cible
    target_languages = {"Français": "fr", "Anglais": "en", "Espagnol": "es", "Portugais": "pt", "Arabe": "ar"}
    target_language = target_languages[st.sidebar.selectbox("Language:", list(target_languages.keys()))]

    # Affichage de la photo de profil dans la barre latérale
    image_url = "https://raw.githubusercontent.com/yohannesclaudealvin/hakizimana-/main/Scripts/IMG_3074.JPG"
    st.sidebar.image(image_url, width=150)

    # Traduire le titre de la page
    st.title(translate_text("Profil de HAKIZIMANA JEAN CLAUDE", target_language))
    st.write(translate_text("🇧🇮 Salut, je suis HAKIZIMANA JEAN CLAUDE.", target_language))
    st.write(translate_text("@YOHANNES", target_language))
    st.write(translate_text("Ingénieur en Télécommunications et en Hydrologie, spécialiste en apprentissage automatique du Burundi 🇧🇮", target_language))

    # Contenu détaillé
    st.write(translate_text("⚒️ Mes intérêts sont la Science des données 🔬, MLOps 🧠⚙️, la Technologie Cloud ☁️, Analyste IT-Climate, Hydrologue, Météorologue, Data Scientist, Administrateur de base de données et système, et ainsi l'Enseignement 👨🏽‍🏫.", target_language))
    st.write(translate_text("Je suis également compétent en Hydrologie, Climatologie et Prévision météorologique.", target_language))
    st.write(translate_text("En hydrologie, je suis familier avec des modèles tels que le modèle de pluie-débit, le modèle de Muskingum, et le modèle de distribution de probabilité de précipitations.", target_language))
    st.write(translate_text("En climatologie, j'ai de l'expérience avec l'analyse de séries chronologiques climatiques, la modélisation climatique régionale et l'utilisation de modèles tels que le modèle ARIMA.", target_language))
    st.write(translate_text("Pour la prévision météorologique, j'ai une connaissance pratique des modèles de prévision numérique du temps (NWP) tels que le modèle européen ECMWF et le modèle américain GFS.", target_language))
    st.write(translate_text("✍🏿 J'écris mes notes d'apprentissage, tutoriels et réflexions [ici](lien_de_votre_choix).", target_language))
    st.write(translate_text("🎥 Je réalise des vidéos sur la Science des données et l'IA en français [ici](lien_de_votre_choix).", target_language))
    st.write(translate_text("🇫🇷✍🏾 J'écris également en français [ici](lien_de_votre_choix). L'anglais 🏴 est ma troisième langue. Le kirundi est la première 🇧🇮🤷‍♂️", target_language))
    st.write(translate_text("💁‍♂️ Vous voulez en savoir plus sur moi ? Jetez un coup d'œil à ma [Page À Propos](lien_vers_votre_page_a_propos).", target_language))
    st.write(translate_text("🤝 Vous voulez me contacter ? Voici mes adresses e-mail : [ici](mailto:alvinhakizimana@gmail.com) et [ici](mailto:alvinjeanclaude@yahoo.co.uk).", target_language))
    st.write(translate_text("Vous pouvez aussi me retrouver sur LinkedIn : [ici](https://www.linkedin.com/in/hakizimana-jean-claude-714195163/)", target_language))
    st.write(translate_text("Et sur GitHub : [ici](https://github.com/yohannesclaudealvin)", target_language))

    st.title(translate_text("Résumé Professionnel", target_language))

    # Informations générales
    st.write(translate_text("""
    Je suis un professionnel polyvalent en télécommunications et en hydrologie, titulaire d'un Ingéniorat en télécommunications et d'une maîtrise en hydrologie. Je suis spécialisé en Data science, en modélisation et prévision Climatiques et Météorologiques et suis certifié en télécommunications et réseaux.
    """, target_language))

    # Éducation et formation
    st.header(translate_text("ÉDUCATION ET FORMATION", target_language))
    st.write(translate_text("""
    M.Sc. Hydrologie quantitative - 2021-Dec 2023
    Centre d'excellence africain pour l'eau et l'assainissement de l’Institut National de l'Eau (INE) Université d'Abomey Calavi République du Bénin.
    B.Tech. Ingénieur Technique en Télécommunications - 2011-2016
    Institut Supérieur des Technologies, Burundi.
    """, target_language))

    # Certifications
    st.subheader(translate_text("CERTIFICATIONS", target_language))
    st.write(translate_text("""
    - Machine Learning en météorologie et climat (ECMWF, IFAB) – en ligne - Janvier – Avril 2023
    - Modélisation mathématique, application aux sciences actuarielles et à la santé publique (écoles mathématiques africaines) - 19 – 30 Sept 2022
    - Introduction au Calcul Haute Performance (Université d'Abomey Calavi & IMSP) - 19-23 Juin 2023
    - Formation de formateurs en réseaux informatiques sur l'administration réseau sous Windows serveur 2012&2016 et serveur Ubuntu et centos7 (Softcenter, Fondation Mvura et Dipcom France) - Sept – Nov 2018
    - Certification en gestion des télécommunications au Centre d'excellence en technologies des télécommunications et Gestion (CETTM), Mumbai, INDE - Fév – Avril 2019
    - Formation académique sur les compétences rédactionnelles (RUFORUM) - 18 Août – 01 Sept 2023
    - Formation sur les statistiques avancées et la conception expérimentale utilisant le langage de programmation R (RUFORUM) - 14 – 18 Août 2022
    - Formation à la rédaction de propositions (RUFORUM)
    """, target_language))

    # Expérience professionnelle
    st.header(translate_text("EXPÉRIENCE PROFESSIONNELLE", target_language))
    st.write(translate_text("""
     Prévisionniste - Institut Géographique du Burundi (IGEBU), Mars 2024, Département d'Hydrométéorologie et Agro climatologie
     Stage - Agence pour la Sécurité de la Navigation Aérienne en Afrique et à Madagascar – ASECNA - Août 2023 – Nov 2023
     Stage - Régie de Production et de Distribution d'eau et d'électricité – REGIDESO - Août 2022
     Stage - Institut Géographique du Burundi (IGEBU), Sept 2022, Département d'Hydrométéorologie et Agroclimatologie
     Technicien supérieur - CFCIB (Chambre Fédérale de Commerce et d'Industrie du Burundi), Juillet 2018 – Nov 2021
    """, target_language))

    # Engagements bénévoles
    st.header(translate_text("ENGAGEMENTS DES BÉNÉVOLES", target_language))
    st.write(translate_text("""
     Technicien bénévole - Ushindi Business Telecom (décodeur et FAI), 15 Oct 2015 – 15 Jan 2016, Bukavu et Goma
     Stagiaire bénévole - Réseaux Nationaux de Télécommunications par Satellite au Sud Kivu / Bukavu, 13 Juillet - 13 Oct 2015
    """, target_language))

    # Expériences de recherche
    st.header(translate_text("EXPÉRIENCES DE RECHERCHE", target_language))
    st.write(translate_text("""
     - Évaluation Des Scénarii De Turbinage Du Barrage de JIJI Mulembwe, en cours - Jan 2024
     - Développement d'un Modèle Simplifié de Prédiction des Précipitations au Burundi (mémoire de master), en cours - 2022-Nov 2023
     - Améliorer la gestion des données climatiques et météorologiques des services d'Hydrométéorologie et d'Agro-climatologie du Burundi, non publié - Oct 2022
    """, target_language))

    # Subventions et prix
    st.header(translate_text("SUBVENTIONS ET PRIX", target_language))
    st.write(translate_text("""
     - 7ème Atelier Régional Ace Impact (Reporter Médias Sociaux), 5 au 7 Oct 2022, Kinshasa, RDC
    """, target_language))

    # Contact
    st.header(translate_text("CONTACT", target_language))
    st.write(translate_text("Courriel : alvinhakizimana@gmail.com / alvinjeanclaude@yahoo.co.uk", target_language))
    st.write(translate_text("Téléphone : +257-79735017-61338212", target_language))

    # Téléchargement du CV
    st.sidebar.header(translate_text("Télécharger le CV", target_language))

    # Ajouter un bouton pour télécharger le CV
    if st.sidebar.button(translate_text("Télécharger en PDF", target_language)):
        # Générer le PDF à partir du contenu
        pdf_content = st.markdown(f"""
            # Profil de HAKIZIMANA JEAN CLAUDE
            {translate_text("🇧🇮 Salut, je suis HAKIZIMANA JEAN CLAUDE.", target_language)}
            {translate_text("Ingénieur en Télécommunications et en Hydrologie, spécialiste en apprentissage automatique du Burundi 🇧🇮", target_language)}

            ## Résumé Professionnel
            {translate_text("Je suis un professionnel polyvalent en télécommunications et en hydrologie, titulaire d'un Ingéniorat en télécommunications et d'une maîtrise en hydrologie.", target_language)}
            
            ## Éducation et formation
            ### ÉDUCATION ET FORMATION
            {translate_text("M.Sc. Hydrologie quantitative - 2021-Dec 2023", target_language)}
            {translate_text("B.Tech. Ingénieur Technique en Télécommunications - 2011-2016", target_language)}
            
            ### CERTIFICATIONS
            {translate_text("Machine Learning en météorologie et climat (ECMWF, IFAB) – en ligne - Janvier – Avril 2023", target_language)}

            ## EXPÉRIENCE PROFESSIONNELLE
            {translate_text("Prévisionniste - Institut Géographique du Burundi (IGEBU), Mars 2024", target_language)}
            
            ## ENGAGEMENTS DES BÉNÉVOLES
            {translate_text("Technicien bénévole - Ushindi Business Telecom", target_language)}
            
            ## EXPÉRIENCES DE RECHERCHE
            {translate_text("Évaluation Des Scénarii De Turbinage Du Barrage de JIJI Mulembwe", target_language)}
            
            ## CONTACT
            {translate_text("Courriel : alvinhakizimana@gmail.com / alvinjeanclaude@yahoo.co.uk", target_language)}
        """)

        pdf_file = pdfkit.from_string(pdf_content, False)
        st.download_button(translate_text("Télécharger CV PDF", target_language), pdf_file, "cv.pdf")

if __name__ == "__main__":
    main()
