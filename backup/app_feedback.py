import streamlit as st
from PIL import Image
import requests
import os
import numpy as np
from io import BytesIO
import time
import json
import streamlit.components.v1 as components

# Section menu
with open("index.html", "r") as file:
    html_content = file.read()
components.html(html_content, height=500)



