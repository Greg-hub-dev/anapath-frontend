import streamlit as st
from PIL import Image
import requests
import os
import numpy as np
import io
import base64
import json
import time
import streamlit.components.v1 as components

# URL de l'API
url = 'https://anapath-demo2-1068402267466.europe-west1.run.app'

st.set_page_config(
    page_title="Analyse Histopathologique",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply the custom CSS
st.markdown(
"""
    <style>
    @keyframes fade-in {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    @keyframes fade-out {
        0% {
            opacity: 1;
        }
        100% {
            opacity: 0;
        }
    }

    * {
        margin: 0;
        padding: 0;
        max-width: 100%;
    }

    .stApp {
        background-color:#effbfc;
    }

    .stSidebar {
        background: linear-gradient(#e0f7fa, #caf1f6, #b4ecf3);
        position: fixed;
        width: 80px;
    }
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown("""
    <style>
        .header {
            position: relative;
            width: 100%;
            bottom: 20px;
        }
        .header img {
            width: 160px;
            height: 160px;
        }
        .header h3 {
            position: absolute;
            top: 50%;
            left: 20%;
            color: #0077b6;
            transform: translate(-15%, -50%);
            font-size: 45px;
            margin: 0;
        }

        .header p {
            position: absolute;
            top: 82%;
            left: 22%;
            color: #023e8a;
            transform: translate(-15%, -50%);
            font-size: 25px;
            margin: 0;
        }
    </style>

    <div class="header">
        <img src="https://raw.githubusercontent.com/Greg-hub-dev/anapath-frontend/main/images/site/Logo_anapath.png" alt="Logo">
        <h3>Diagnostic Anapath</h3>
        <p>Diagnostic Histopathologique Assisté par IA</p>
    </div>
""", unsafe_allow_html=True)

# Navbar Section
# Sidebar Navigation
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Go to", options=["Home", "Analyse et Résultats"])


# HOME
if navigation == "Home":
    st.header("Home")

    st.markdown("""
    <style>
        .carousel img{
            height: 400px;
            width: 800px;
        }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
### 🔍 À propos de cet outil
Cet outil d'aide à la décision analyse les images histologiques et fournit une évaluation :
- Du diagnostic potentiel de tissus cancéreux
- De l estimation du taux de cellularité tumorale
- Des caractéristiques morphologiques significatives
    """, unsafe_allow_html=True)

    st.warning("""
        IMPORTANT: Cet outil est conçu pour assister les professionnels de santé et ne
        remplace pas l'expertise médicale.
    """)

    carousel_html = """

    <div id="carouselExampleIndicators" class="carousel slide">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
            <div class="carousel-item active">
            <img src="https://raw.githubusercontent.com/Greg-hub-dev/anapath-frontend/main/images/pres/slide1.PNG" class="d-block w-100" alt="Slide 1">
            </div>
            <div class="carousel-item">
            <img src="https://raw.githubusercontent.com/Greg-hub-dev/anapath-frontend/main/images/pres/slide2.PNG" class="d-block w-100" alt="Slide 2">
            </div>
            <div class="carousel-item">
            <img src="https://raw.githubusercontent.com/Greg-hub-dev/anapath-frontend/main/images/pres/slide3.PNG" class="d-block w-100" alt="Slide 3">
            </div>
            <div class="carousel-item">
            <img src="https://raw.githubusercontent.com/Greg-hub-dev/anapath-frontend/main/images/pres/slide4.PNG" class="d-block w-100" alt="Slide 3">
            </div>
            <div class="carousel-item">
            <img src="https://raw.githubusercontent.com/Greg-hub-dev/anapath-frontend/main/images/pres/slide5.PNG" class="d-block w-100" alt="Slide 3">
            </div>
            <div class="carousel-item">
            <img src="https://raw.githubusercontent.com/Greg-hub-dev/anapath-frontend/main/images/pres/slide6.PNG" class="d-block w-100" alt="Slide 3">
            </div>
            <div class="carousel-item">
            <img src="https://raw.githubusercontent.com/Greg-hub-dev/anapath-frontend/main/images/pres/slide7.PNG" class="d-block w-100" alt="Slide 3">
            </div>
            <div class="carousel-item">
            <img src="https://raw.githubusercontent.com/Greg-hub-dev/anapath-frontend/main/images/pres/slide8.PNG" class="d-block w-100" alt="Slide 3">
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        """

    st.components.v1.html(carousel_html, height=450)

    st.markdown("""
### Méthodologie
Cette application utilise un modèle d intelligence artificielle entraîné sur des milliers d images histopathologiques annotées par des experts. L algorithme analyse les caractéristiques morphologiques des tissus pour identifier les patterns associés aux différents types de néoplasies.
    """, unsafe_allow_html=True)

    st.markdown("""
### Confidentialité
Toutes les images téléchargées sont traitées de manière sécurisée et ne sont pas conservées au-delà de la session d analyse.
    """, unsafe_allow_html=True)



# ANALYSE et RESULTATS
elif navigation == "Analyse et Résultats":
    st.header("Analyse et Résultats")

    col1, col2= st.columns(2)

# Card 1 - téléchargement de l'image
    with col1:
        st.markdown("""
        <div style="border: 1px solid #ddd; margin-bottom: 20px; border-radius: 5px; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <div style="text-align: center; font-size: 20px; background-color: #f8f9fa; padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd;">
                Téléchargement d'Image
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
            <div style="padding: 5px;">
                <p style="font-size: 16px; color: #555;">Veuillez télécharger une image de tissu histologique</p>
            </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

        st.markdown("""
            <div style="padding: 15px;">
                <p style="font-size: 13px; color: #555;">Pour des résultats optimaux, utilisez des images de haute qualité au format JPG ou PNG.</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)



# Card 2 - restituition de l'image
    with col2:
        st.markdown("""
        <div style="border: 1px solid #ddd; margin-bottom: 20px; border-radius: 5px; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <div style="text-align: center; font-size: 20px; background-color: #f8f9fa; padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd;">
                Image Source
            </div>
        </div>
            """, unsafe_allow_html=True)

         # Affichage de l'image téléchargée
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Image histologique téléchargée", use_container_width=True)

            # Informations sur l'image
            st.markdown(f"**Dimensions:** {image.width} × {image.height} pixels")
            st.markdown(f"**Format:** {uploaded_file.type}")



    col3, col4, col5 = st.columns([3,0.5,3])

# Card 3 - Résultats du modèle
    with col3:
        st.markdown("""
        <div style="border: 1px solid #ddd; margin-bottom: 20px; border-radius: 5px; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <div style="text-align: center; font-size: 20px; background-color: #f8f9fa; padding: 10px;font-weight: bold; border-bottom: 1px solid #ddd;">
                Résultats de l'Analyse
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
            <div style="padding: 15px;">

            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

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
                    #st.image(res.content, caption="Image Analysée avec Annotations", use_container_width=True)

                    
                    result_data = res.headers
                    diag=result_data.get('diag')
                    st.markdown("### **Microbiopsie d'une lésion du sein gauche (externe) :**")
                    st.markdown("")
                    st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;**Diagnostic:** {result_data.get('diag')}")
                    if res.headers.get('p_class_d') == 'tumor':
                        st.markdown("&nbsp;&nbsp;&nbsp;carcinome infiltrant de type non spécifique - Échantillon tumoral inclus en paraffine pour génétique somatique")
                        st.markdown("&nbsp;&nbsp;&nbsp;Absence de facteur confondant à type de nécrose, fibrose, ou mucine.")
                        st.markdown(f"&nbsp;&nbsp;&nbsp;**Intervalle de confiance pour le diagnostic :** {"{:.2f}".format(float(result_data.get('c_diag')) * 100)} %")
                        st.markdown(f"&nbsp;&nbsp;&nbsp;**Pourcentage de cellules tumorales dans la zone sélectionnée** {result_data.get('p_class_tx').upper()}")
                        st.markdown(f"&nbsp;&nbsp;&nbsp;**Intervalle de confiance pour le Taux de Cellularité:** {"{:.2f}".format(float(result_data.get('c_tx')) * 100)} %")
                    else:
                        st.markdown(f"&nbsp;&nbsp;&nbsp;**Intervalle de confiance pour le diagnostic :** {"{:.2f}".format(float(result_data.get('c_diag')) * 100)} %")
                    st.success("Analyse complétée avec succès")

                else:
                    st.error(f"Erreur lors de l'analyse: {res.status_code} - {res.text}")
                    
            except Exception as e:
                st.error(f"Une erreur s'est produite: {str(e)}")



# Card 4 - VS
    with col4:
        st.markdown("""
            <div>
                <p style="padding-top: 100px; text-align: center; font-size: 30px; font-weight: bold, color: #555;">VS</p>
            </div>
        """, unsafe_allow_html=True)


# Card 5 - Interprétation par Claude
    with col5:
        st.markdown("""
        <div style="border: 1px solid #ddd; margin-bottom: 20px; border-radius: 5px; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <div style="text-align: center; font-size: 20px; background-color: #f8f9fa; padding: 10px;font-weight: bold; border-bottom: 1px solid #ddd;">
                Analyse Complémentaire
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
            <div style="padding: 15px;">

            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)


        def get_image_base64(path):
            with open(path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode('utf-8')


        def get_claude_interpretation(api_key: str, image_bytes: bytes, technical_data: dict) -> dict:

                # Ouvrir l'image à partir des bytes
            with Image.open(io.BytesIO(image_bytes)) as img:
                # Préserver le ratio d'aspect
                width, height = img.size
                if width > 512 or height > 256:
                    ratio = min(512/width, 256/height)
                    new_width = int(width * ratio)
                    new_height = int(height * ratio)
                    img = img.resize((new_width, new_height), Image.LANCZOS)
                # Convertir en JPEG et encoder en base64
                buffer = io.BytesIO()
                img.convert('RGB').save(buffer, format="JPEG", quality=100)
                buffer.seek(0)
                encoded_image = base64.b64encode(buffer.read()).decode('utf-8')

            # Détection du type MIME réel
            if image_bytes.startswith(b'\xff\xd8'):
                media_type = "image/jpeg"
            elif image_bytes.startswith(b'\x89PNG'):
                media_type = "image/png"
            else:
                raise ValueError("Format d'image non supporté (seuls JPEG/PNG sont acceptés)")

            # Prompt plus clair
            system_prompt = f"""
            [SYSTÈME]
            Vous êtes un anatomopathologiste senior. Analysez cette image histologique et fournissez :
            1. Diagnostic complet (cancéreux/non)
            2. Estimation de la cellularité tumorale
            3. Grade histologique
            4. Caractéristiques morphologiques clés"""

            user_prompt = f"""[RÉSULTATS TECHNIQUES]
            {json.dumps(technical_data, indent=2)}
            [EXIGENCES]
            Répondez UNIQUEMENT au format JSON suivant:
            {{
                "diagnostic": {{
                    "conclusion": str,
                    "probabilite": float,
                    "confiance": str
                }},
                "cellularite": str,
                "grade": str,
                "caracteristiques": [str, str, str],
                "notes": str
            }}
            """
            headers = {
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            }
            payload = {
                "model": "claude-3-7-sonnet-20250219",
                "max_tokens": 1000,
                "system": system_prompt,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/jpeg",
                                    "data": encoded_image
                                }
                            },
                            {
                                "type": "text",
                                "text": user_prompt
                            }
                        ]
                    }
                ]
            }
            try:
                response = requests.post(
                    "https://api.anthropic.com/v1/messages",
                    headers=headers,
                    json=payload,
                    timeout=60  # Légère augmentation du timeout
                )
                # Enregistrer la réponse pour débogage
                print(f"Status code: {response.status_code}")
                if response.status_code != 200:
                    print(f"Erreur API: {response.text}")
                    response.raise_for_status()
                response_json = response.json()
                response_text = response_json["content"][0]["text"]
                # Extraction plus robuste du JSON
                import re
                json_match = re.search(r'```(?:json)?(.*?)```', response_text, re.DOTALL)
                if json_match:
                    json_text = json_match.group(1).strip()
                else:
                    json_text = response_text.strip()
                return json.loads(json_text)
            except requests.exceptions.HTTPError as e:
                print(f"Erreur HTTP: {e}")
                raise
            except requests.exceptions.RequestException as e:
                print(f"Erreur de requête: {e}")
                raise
            except json.JSONDecodeError as e:
                print(f"Erreur JSON: {e}")
                print(f"Texte reçu: {response_text}")
                raise
            except Exception as e:
                print(f"Erreur inattendue: {e}")
                raise


        if uploaded_file is not None:
            img_bytes = uploaded_file.getvalue()

            with st.spinner("Interprétation des résultats par Claude..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(i + 1)

                api_key = st.secrets["CLAUDE_API_KEY"]
                # Créer un dictionnaire minimal avec le diagnostic pour Claude
                technical_data = {
                    "diagnostic": diag,
                    "probability": "Non spécifiée",
                    "cellularity": "Non spécifiée",
                    "grade": "Non spécifié"
                            }
                claude_analysis = get_claude_interpretation(api_key, img_bytes, technical_data)

                if claude_analysis:
                    st.markdown("### 📝 Interprétation médicale")
                    with st.container():
                        st.markdown(f"""
                            <div class="claude-interpretation">
                                <div class="result-item">
                                    <span class="result-label">Diagnostic principal:</span> {claude_analysis['diagnostic']['conclusion']}
                                </div>
                                    <div class="result-item">
                                        <span class="result-label">Niveau de confiance:</span> {claude_analysis['diagnostic']['confiance']}
                                    </div>
                                    <div class="result-item">
                                        <span class="result-label">Caractéristiques clés:</span><br>
                                            {chr(10).join([f"- {feat}" for feat in claude_analysis['caracteristiques']])}
                                    </div>
                                    <div class="result-item">
                                        <span class="result-label">Recommandations:</span> {claude_analysis['notes']}
                                    </div>
                            </div>
                                    """, unsafe_allow_html=True)

                else:
                    st.error(f"Erreur lors de l'analyse (code {result_data.status_code})")


            st.markdown('</div>', unsafe_allow_html=True)



# Section feedback
    with st.container():
        st.markdown("### Évaluation des résultats")
        st.caption("Votre feedback nous aide à améliorer le système")
        if 'feedback_submitted' not in st.session_state:
            st.session_state.feedback_submitted = False

        if not st.session_state.feedback_submitted:
            col1, col2, col3, col4 = st.columns([1,1,1,1])

        with col1:
            if st.button("👍 Résultat correct"):
                try:
                    feedback_data = {
                        "image_id": uploaded_file.name,
                        "feedback": "positive",
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    requests.post(url + "/feedback", json=feedback_data)
                    st.session_state.feedback_submitted = True
                    st.success("Merci pour votre retour positif!")
                except Exception as e:
                    st.error(f"Erreur: {str(e)}")
        with col2:
            if st.button("👎 Résultat incorrect"):
                st.session_state.show_feedback_form = True

        if hasattr(st.session_state, 'show_feedback_form') and st.session_state.show_feedback_form:
            feedback_comment = st.text_area("Veuillez préciser ce qui semble incorrect")
            if st.button("Envoyer commentaire"):
                try:
                    feedback_data = {
                        "image_id": uploaded_file.name,
                        "feedback": "negative",
                        "comment": feedback_comment,
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    requests.post(url + "/feedback", json=feedback_data)
                    st.session_state.feedback_submitted = True
                    st.success("Merci pour votre retour constructif!")
                except Exception as e:
                    st.error(f"Erreur: {str(e)}")
        else:
            st.info("Merci pour votre feedback!")


    # Avertissement médical
    st.markdown(
    """
    <div style="
        text-align: center;
        padding: 15px;
        background-color: #fff3cd;
        color: #856404;
        border: 1px solid #ffeeba;
        border-radius: 5px;">
        ⚠️ <strong>Remarque importante :</strong> Ces résultats sont générés automatiquement et doivent être confirmés et validés par un anatomopathologiste.
    </div>
    """,
    unsafe_allow_html=True)

# Footer Section
st.markdown("""
<style>
    footer {
        text-align: center;
        background-color: #effbfc;
        height: 60px;
        padding: 10px;
        width: 100%;
        position: sticky;
    }

    footer a {
        text-decoration: none;
        color: #effbfc;
    }

    footer a:hover {
        color: black;
    }
</style>

""", unsafe_allow_html=True)


st.markdown("""
    <footer>
        <center>
            <div class="footer">
                <a href="#">&copy; 2024 Service d'Anatomie Pathologique - Tous droits réservés</a>
                <p>Cet outil est destiné à un usage professionnel uniquement.</p>
            </div>
        </center>
    </footer>
""", unsafe_allow_html=True)
