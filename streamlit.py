import streamlit as st
import pandas as pd
import datetime
import os

def main():
    st.title("Informations générales – Questionnaire")

    # Identification
    st.header("Identification")
    code_id = st.text_input("Code d’identification")
    num_grossesse = st.number_input("Numéro de la grossesse (premier, deuxième enfant etc...)", min_value=0, max_value=10, step=1)


    ages_enfants = []
    for i in range(int(num_grossesse)):  # boucle modulable selon num_grossesse
        ages_enfants.append(st.number_input( f"Âge de l'enfant {i+1} (laisser vide si pas d'enfant)",min_value=0, max_value=20, step=1, key=f"age_{i}"))
    
    date_accouchement = st.date_input("Date prévue accouchement", value=datetime.date.today())
    age_grossesse = st.text_input("Âge grossesse au moment de l’entretien (en mois ou semaines)")
    age_mere = st.text_input("Âge de la mère")
    lieu_naissance = st.text_input("Lieu de naissance de l’enfant (ville, pays)")
    profession_mere = st.text_input("Profession ou activité de la mère au moment de la grossesse")

    niveau_etude_mere = st.selectbox("Niveau d’étude de la mère", [
        "Jamais scolarisée", "École primaire", "Collège", "Lycée", "Diplômée Bac",
        "Bac+2", "Bac+5 et au-delà"
    ])

    langues_mere = st.text_input("Langues parlées par la mère (séparer par des virgules)")
    langue_maternelle_mere = st.text_input("Langue maternelle de la mère")
    lieu_naissance_parents_mere = st.text_input("Lieu de naissance des parents de la mère")

    # Infos complémentaires
    langue_gp_maternel = st.text_input("Langues parlées par le grand-père maternel")
    langue_gm_maternelle = st.text_input("Langues parlées par la grand-mère maternelle")

    poids_depart = st.number_input("Poids (kg) au démarrage de la grossesse", min_value=0, max_value=200, step=1)
    taille_depart = st.number_input("Taille (cm) au démarrage de la grossesse", min_value=0, max_value=200, step=1)

    lieu_vie = st.text_input("Lieu de vie (quartier, ville, pays)")
    avec_qui_vivez = st.text_input("Préciser avec qui vous vivez")

    # Informations concernant le père
    st.header("Informations concernant le père")
    profession_pere = st.text_input("Profession du père au moment de la grossesse")
    niveau_etude_pere = st.selectbox("Niveau d’étude du père", [
        "Jamais scolarisé", "École primaire", "Collège", "Lycée", "Diplômé Bac",
        "Bac+2", "Bac+5 et au-delà"
    ])
    age_pere = st.number_input("Age du père", min_value=20, max_value=60, step=1)
    lieu_naissance_pere = st.text_input("Lieu de naissance du père (ville, pays)")
    langues_pere = st.text_input("Langues parlées par le père (séparer par des virgules)")
    langue_maternelle_pere = st.text_input("Langue maternelle du père")
    lieu_naissance_parents_pere = st.text_input("Lieu de naissance des parents du père")
    langue_gp_pere = st.text_input("Langues parlées par le grand-père paternel")
    langue_gm_pere = st.text_input("Langues parlées par la grand-mère paternelle")

    # Rassembler toutes les données
    data = {
        "Code ID": code_id,
        "Numéro Grossesse": num_grossesse,
        "Ages enfants": [a for a in ages_enfants if a],
        "Date prévue accouchement": date_accouchement.strftime("%Y-%m-%d"),
        "Âge grossesse": age_grossesse,
        "Âge mère": age_mere,
        "Lieu naissance enfant": lieu_naissance,
        "Profession mère": profession_mere,
        "Niveau étude mère": niveau_etude_mere,
        "Langues mère": langues_mere,
        "Langue maternelle mère": langue_maternelle_mere,
        "Lieu naissance parents mère": lieu_naissance_parents_mere,
        "Langues GP maternel": langue_gp_maternel,
        "Langues GM maternelle": langue_gm_maternelle,
        "Poids départ (kg)": poids_depart,
        "Taille départ (cm)": taille_depart,
        "Lieu de vie": lieu_vie,
        "Avec qui vivez": avec_qui_vivez,
        "Profession père": profession_pere,
        "Niveau étude père": niveau_etude_pere,
        "Âge père": age_pere,
        "Lieu naissance père": lieu_naissance_pere,
        "Langues père": langues_pere,
        "Langue maternelle père": langue_maternelle_pere,
        "Lieu naissance parents père": lieu_naissance_parents_pere,
        "Langues GP paternel": langue_gp_pere,
        "Langues GM paternelle": langue_gm_pere,
    }

    # Sauvegarde
    if st.button("Sauvegarder en Excel"):
        filename = "informations_generales.xlsx"
        df = pd.DataFrame([data])
        if os.path.exists(filename):
            old_df = pd.read_excel(filename)
            df = pd.concat([old_df, df], ignore_index=True)
        df.to_excel(filename, index=False)
        st.success(f"Données sauvegardées dans {filename}")

if __name__ == "__main__":
    main()
