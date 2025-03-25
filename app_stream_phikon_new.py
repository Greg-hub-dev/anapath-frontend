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
url = 'https://anapath-demo-1068402267466.europe-west1.run.app'

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
    @import url('https://fonts.googleapis.com/css2?family=Akaya+Kanadaka&display=swap');

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

    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown("""
    <style>
        .header {
            position: relative;
            width: 100%;
        }
        .header img {
            width: 100%;
            height: 150px;
        }
        .header h3 {
            position: absolute;
            top: 50%;
            left: 25%;
            transform: translate(-15%, -50%);
            color: black;
            font-family: "Akaya Kanadaka", system-ui;
            font-weight: 300;
            text-shadow: 5px 10px 20px #e7c6ff;
            font-size: 41px;
            margin: 0;
        }
    </style>

    <div class="header">
        <img src="https://raw.githubusercontent.com/Greg-hub-dev/anapath-frontend/main/tile_02174_c174_r0_c9_small.png" alt="Logo">
        <h3>DIAGNOSTIC HISTOPATHOLOGIQUE ASSISTÉ PAR IA</h3>
    </div>
""", unsafe_allow_html=True)

# Navbar Section
# Sidebar Navigation
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Go to", options=["Home", "Analyse et Résultats", "Informations complémentaires"])


# HOME
if navigation == "Home":
    st.header("Home")
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

    col1, col2, col3 = st.columns([2, 2, 2])

# Card 1 in the first column
    with col1:
        st.markdown("""
        <div style="border: 1px solid #ddd; margin-bottom: 20px; border-radius: 5px; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <div style="text-align: center; background-color: #f8f9fa; padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd;">
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



# Card 2 in the second column
    with col2:
        st.markdown("""
        <div style="border: 1px solid #ddd; margin-bottom: 20px; border-radius: 5px; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <div style="text-align: center; background-color: #f8f9fa; padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd;">
                Image Source
            </div>
        </div>
            """, unsafe_allow_html=True)

            # Affichage de l'image téléchargée
        image = Image.open(uploaded_file)
        st.image(image, caption="Image histologique téléchargée", use_container_width=True)

            # Informations sur l'image
        st.markdown(f"**Dimensions:** {image.width} × {image.height} pixels")
        st.markdown(f"**Format:** {uploaded_file.type}")


# Card 3 in the third column
    with col3:
        st.markdown("""
        <div style="border: 1px solid #ddd; margin-bottom: 20px; border-radius: 5px; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <div style="text-align: center; background-color: #f8f9fa; padding: 10px;font-weight: bold; border-bottom: 1px solid #ddd;">
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
                    st.image(res.content, caption="Image Analysée avec Annotations", use_container_width=True)

                    st.success("Analyse complétée avec succès")

                    # Avertissement médical
                    st.warning("**Remarque importante :** Ces résultats sont générés automatiquement et doivent être confirmés par un anatomopathologiste.")

                    prediction = res.json()

                    pred_res = prediction['X-Prediction-Result']
                    pred_pdiag = prediction['p_diag']
                    pred_ptx = prediction['p_tx']
                    pred_pclassd = prediction['p_class_d']
                    pred_pclasstx = prediction['p_class_tx']
                    pred_cdiag = prediction['c_diag']
                    pred_ctx = prediction['c_tx']


                    st.write(f'Diagnostique: ${pred_res}')
                    st.write(f'Diagnostique: ${pred_pdiag}')
                    st.write(f'Diagnostique: ${pred_ptx}')
                    st.write(f'Diagnostique: ${pred_pclassd}')
                    st.write(f'Diagnostique: ${pred_pclasstx}')
                    st.write(f'Diagnostique: ${pred_cdiag}')
                    st.write(f'Diagnostique: ${pred_ctx}')

                else:
                    st.error(f"Erreur lors de l'analyse: {res.status_code} - {res.text}")

            except Exception as e:
                st.error(f"Une erreur s'est produite: {str(e)}")


        st.markdown('</div>', unsafe_allow_html=True)








# Informations complémentaires (Diagnostic IA)
elif navigation == "Informations complémentaires":
    st.header("Informations complémentaires")
    # Add Analyse page content

    def get_claude_interpretation(api_key: str, image_bytes: bytes, technical_data: dict) -> dict:
        """Fonction pour l'interprétation par Claude"""
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



# Footer Section
st.markdown("""
<style>
    footer {
        text-align: center;
        background: linear-gradient(to right, #e7c6ff 0%, #ffd6ff 50%, #e7c6ff 100%);
        height: 60px;
        padding: 10px;
        width: 100%;
        margin-bottom: -100px;
    }

    footer a {
        text-decoration: none;
        color: #5b0893;
    }

    footer a:hover {
        color: black;
    }

    .title_footer {
        color: black;
        font-family: "Akaya Kanadaka", system-ui;
        font-style: normal;
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
