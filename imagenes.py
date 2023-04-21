######################
# Instrucciones de terminal
######################

#streamlit run app.py para iniciar la app
#Control+C para terminar desde el terminal
#Actualizar al ejecutar el programa: ≡ -> Settings -> Run on save

######################
# Datos importados
######################

#Datos importados de: https://huggingface.co/runwayml/stable-diffusion-v1-5

######################
# Import libraries
######################

import streamlit as st
import torch

# ######################
# Funciones auxiliares
# ######################

def pipe_callback(step: int, timestep: int, latents: torch.FloatTensor):

    with st.container():

        st.write(f'Vamos por la iteración {step}')
        st.progress(step*2) #bar_progress debe empezar con 0 y terminar en 100
        st.write(f'Quedan {timestep/100:.0f} segundos')

# ######################
# Configuración de página
# ######################

st.set_page_config(
    page_title="Images",
    layout="centered", #"wide" or "centered"
    initial_sidebar_state="collapsed", #"auto" or "expanded" or "collapsed"
    menu_items={
        'About': "# Generación de imagenes desde Stabble Difussion v1.5"
    }
)

######################
# Page Title
######################

st.title("Creación de Imagenes 🍆")

if True:

    model_id = "https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/main"

    option = st.radio('Modelo', ("Texto", "Imagen"), 0)

    prompt = st.text_input("Prompt","")
    prompt_negativo = st.text_input("Negatives","")

    enter = st.button('Enter', type = "primary")

    if option == "Texto" and enter:

            from diffusers import StableDiffusionPipeline

            pipe = StableDiffusionPipeline.from_pretrained(
                model_id,
                revision="fp16" if torch.cuda.is_available() else "fp32",
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32, 
                ).to("cuda")

            with st.empty():
                image_pipe = pipe(prompt, negative_prompt=prompt_negativo, width=728, height=728, callback = pipe_callback) #otras variables: guidance_scale=guidance_scale, num_inference_steps=steps
                st.write("FIN")


            imagen = image_pipe.images[0]

            st.image(imagen)



    if option == "Imagen":

        uploaded_file = st.file_uploader("Elige una imagen", type = ['png', 'jpg'], accept_multiple_files=False)

        if uploaded_file is not None:
            st.write(uploaded_file.name)
            st.image(uploaded_file)

        if enter:

            from diffusers import StableDiffusionImg2ImgPipeline
            from PIL import Image

            uploaded_file = Image.open(uploaded_file)

            pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
                    model_id,
                    revision="fp16" if torch.cuda.is_available() else "fp32",
                    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32, 
                    ).to("cuda")

            with st.empty():
                imagen = pipe(prompt, image=uploaded_file, negative_prompt=prompt_negativo, callback = pipe_callback).images[0]
                st.write("")

            st.image(imagen)









    if False:

        # ######################
        # App Github
        # ######################

        st.title("Titulo 12: App Github")

        "hay que abrirse una cuenta de Github y publicar todo para poder verlo online"
        "Los archivos de la carpeta .streamlit no se cargan porque es una carpeta oculta, hay que meterlos por tu cuenta"
        "secrets.toml no hay que añadirlo, eso solo es para trabajo local. en cambio, hay que ir a ≡ -> Setting -> Secrets y copiar con el formato .toml"
        "config.toml sí parece que funciona, pero tiene preferencia el usuario al elegir el color de la pagina (tema)"
        "Las modificaciones en About, Report a Bug y Get Help parecen tardar un poco más en cargar"


        #----------------------
        #A AÑADIR!!!
        #------------------------

        # ######################
        # Descarga
        # ######################

        st.download_button('Download image', imagen, file_name="prueba.png")

        with imagen as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="flower.png",
                    mime="image/png"
                )
