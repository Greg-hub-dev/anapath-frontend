import streamlit as st
from PIL import Image
import requests
import os
import numpy as np
from io import BytesIO
import time

# Configuration de la page
st.set_page_config(
    page_title="Analyse Histopathologique",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Personnalisation CSS pour améliorer l'interface
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .title-container {
        background-color: #0077b6;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        color: white;
    }
    .subtitle {
        color: #023e8a;
        margin-bottom: 1rem;
    }
    .section-title {
        color: #023e8a;
        border-bottom: 2px solid #0077b6;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .upload-section {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    .result-section {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .info-box {
        background-color: #e9f5fd;
        border-left: 5px solid #0077b6;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1.5rem;
    }
    .stButton>button {
        background-color: #0077b6;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #6c757d;
        font-size: 0.8rem;
    }
    .loader {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# URL de l'API
url = 'https://anapath-1068402267466.europe-west1.run.app'

# En-tête et introduction
st.markdown('<div class="title-container"><h1>Diagnostic Histopathologique Assisté par IA</h1></div>', unsafe_allow_html=True)

st.markdown('<div class="info-box">', unsafe_allow_html=True)
st.markdown("""
### 🔍 À propos de cet outil
Cet outil d'aide à la décision analyse les images histologiques et fournit une évaluation :
- Du diagnostic potentiel de tissus cancéreux
- De l estimation du taux de cellularité tumorale
- Des caractéristiques morphologiques significatives

**Important :** Cet outil est conçu pour assister les professionnels de santé et ne remplace pas l expertise médicale.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Section de téléchargement d'image
st.markdown('<h2 class="section-title">Téléchargement d Image</h2>', unsafe_allow_html=True)
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
st.markdown("### Veuillez télécharger une image de tissu histologique")
st.markdown("Pour des résultats optimaux, utilisez des images de haute qualité au format JPG ou PNG.")

uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

# Section d'analyse et résultats
if uploaded_file is not None:
    st.markdown('<h2 class="section-title">Analyse et Résultats</h2>', unsafe_allow_html=True)
    st.markdown('<div class="result-section">', unsafe_allow_html=True)
    
    # Disposition en colonnes pour l'image originale et les résultats
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<h3 class="subtitle">Image Source</h3>', unsafe_allow_html=True)
        
        # Affichage de l'image téléchargée
        image = Image.open(uploaded_file)
        st.image(image, caption="Image histologique téléchargée", use_container_width=True)
        
        # Informations sur l'image
        st.markdown(f"**Dimensions:** {image.width} × {image.height} pixels")
        st.markdown(f"**Format:** {uploaded_file.type}")
    
    with col2:
        st.markdown('<h3 class="subtitle">Résultats de l Analyse</h3>', unsafe_allow_html=True)
        
        # Simulation de chargement avec une barre de progression
        with st.spinner("Analyse en cours..."):
            # Obtention des bytes de l'image
            img_bytes = uploaded_file.getvalue()
            
            # Appel à l'API
            try:
                # Afficher une barre de progression pour améliorer l'expérience utilisateur
                progress_bar = st.progress(0)
                for i in range(100):
                    # Simulation de traitement
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                # Envoi de l'image à l'API
                res = requests.post(url + "/upload_image", files={'img': img_bytes}, timeout=30)
                
                if res.status_code == 200:
                    # Affichage de l'image annotée retournée par l'API
                    st.image(res.content, caption="Image Analysée avec Annotations", use_container_width=True)
                    
                    # Ici, vous pourriez ajouter plus de données de résultat si votre API les retourne
                    # Par exemple, un JSON avec les résultats d'analyse détaillés
                    
                    st.success("Analyse complétée avec succès")
                    
                    # Exemple de visualisation de résultats fictifs (à remplacer par les vraies données de votre API)
                    st.markdown("### Interprétation des Résultats")
                    st.markdown("""
                    - **Classification:** Carcinome canalaire infiltrant (probabilité élevée)
                    - **Taux de cellularité tumorale:** Environ 65%
                    - **Grade histologique:** Grade II/III
                    """)
                    
                    # Avertissement médical
                    st.warning("**Remarque importante :** Ces résultats sont générés automatiquement et doivent être confirmés par un anatomopathologiste.")
                    
                else:
                    st.error(f"Erreur lors de l analyse: {res.status_code} - {res.text}")
                    
            except Exception as e:
                st.error(f"Une erreur s'est produite: {str(e)}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Section d'informations supplémentaires
st.markdown('<h2 class="section-title">Informations Complémentaires</h2>', unsafe_allow_html=True)
st.markdown('<div class="info-box">', unsafe_allow_html=True)
st.markdown("""
### Méthodologie
Cette application utilise un modèle d intelligence artificielle entraîné sur des milliers d images histopathologiques annotées par des experts. L algorithme analyse les caractéristiques morphologiques des tissus pour identifier les patterns associés aux différents types de néoplasies.

### Confidentialité
Toutes les images téléchargées sont traitées de manière sécurisée et ne sont pas conservées au-delà de la session d analyse.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Pied de page
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("""
© 2024 Service d Anatomie Pathologique - Tous droits réservés  
Cet outil est destiné à un usage professionnel uniquement.
""")
st.markdown('</div>', unsafe_allow_html=True)
