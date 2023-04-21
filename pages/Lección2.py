import streamlit as st

st.set_page_config(
    page_title="Lecciones nuevas",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/7/79/Logo-maranosa.jpg",
    menu_items={
        'About': "john@example.com"
    }
)

# ######################
# Visualización de datos
# ######################

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2. ❄️")

st.title("Titulo 1: Visualización de datos")
"La matoría necesitan de pandas:"
"**st.dataframe** - muestra una tabla interactiva"
"**st.table** - muestra una tabla estatica"

st.header("Sección 1.1: Estilo Métrica")
st.metric('x1', value=99.2, delta='p value = 0.02', delta_color='normal')
st.metric('x2', value=47.3, delta='p value = 0.07', delta_color='inverse')

st.header("Sección 1.2: Estilo Json")
"La forma de mostrar listas y diccionarios (aunque se hace de forma automatica)"
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
} , expanded = True )

# ######################
# Más heramientas de entrada
# ######################

st.title("Titulo 2: Más heramientas de entrada")

st.header("Sección 2.1: NumberBox")
number = st.number_input('Insert a number', value = 1)
number
""
"Se puede modificar el número sin usar + ó -"
"Puedes fijar el aumento con la variable step"
"Puedes fijar valor máximo, mínimo y por defecto"
"Se puede deshabilitar"
"Puedes fijar el formato mostrado de salida, rollo %i, %f %g ..."
"Además puedes elegir entre int y float"

st.header("Sección 2.2: TimeBox")
t = st.time_input('Set an alarm for')
t

"Aunque funciona solo, utiliza una estructura de datos del paquete datetime"

st.header("Sección 2.3: DateBox")
d = st.date_input("When\'s your birthday")
st.write('Your birthday is:', d)

"Aunque funciona solo, utiliza una estructura de datos del paquete datetime"

st.header("Sección 2.4: ColorBox")
color = st.color_picker('Pick A Color', value = '#00f900')
st.write('The current color is', color)

# ######################
# Entrada de archivos
# ######################

st.title("Titulo 3: Entrada de archivos")

st.header("Sección 3.1: Descarga")
text_contents = "This is some text"
st.download_button('Download some text', text_contents, file_name="Texto_de_prueba")

with open("flower.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
          )

st.header("Sección 3.2: Carga")
uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=False)
if uploaded_file is not None:
    st.write(uploaded_file.name)

    texto = uploaded_file.read()

    st.write(str(texto, 'utf-8') + "-hola")


st.header("Sección 3.3: Cámara")
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)   

# ######################
# Multimedia: Audio e Imagenes
# ######################

st.title("Titulo 4: Multimedia - Audio, Imagen y Vídeo")

st.header("Sección 4.1: Imagen")

"De internet"
st.image("https://www.tecnolivo.eu/wp-content/uploads/2018/01/Inta_logo.jpg")
"De memoria"
imagen_file = open("itm.jpg","rb")
imagen_bytes = imagen_file.read()
st.image(imagen_bytes)

st.header("Sección 4.2: Video")

"De internet"
st.video("https://www.youtube.com/watch?v=67lnjV6SrFw", start_time=3)
"De memoria"
video_file = open("cine.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

"Hay una opcion para empezar en el momento que se quiera del video con la variable start_time"
"Hay que indicarle en que segundo empezar, con int"

st.header("Sección 4.3: Audio")

audio_file = open("pokemon.mp3","rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes)

"Ahora viene el audio de un video:"

audio_file = open("cine.mp4","rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes)

# ######################
# Tabs
# ######################

st.title("Titulo 5: Pestañas")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

tab2.write("hola pescado")

with tab3:
   st.header("An owl")
   st.write("hola caracola")

# ######################
# Expander
# ######################

st.title("Titulo 6: Expander")

with st.expander("See explanation"):
    st.write("hola caracola")
    st.image("https://static.streamlit.io/examples/dice.jpg")

# ######################
# Estructuras internas
# ######################

st.title("Titulo 7: Estructuras internas")
st.header("Sección 7.1: Container")

"Permite crear una sección interna "
"1"
c = st.container()
"2"
c.write("3-")
"4"
c.write("5-")
"6"

st.header("Sección 7.2: Vacío")

"Crea un container que solo puede contener un elemento a la vez, borrando lo anterior"
"Se puede añadir un elemento con with o usando un metodo interno, como .write(·)"

boton1 = st.button('Empezar')
if boton1:
    from time import sleep

    with st.empty():
        for seconds in range(60):
            st.write(f"⏳ {seconds} seconds have passed")
            sleep(1)
        st.write("✔️ 1 minute over!")

# ######################
# Animaciones internas
# ######################

st.title("Titulo 8: Animaciones internas")
boton_globos = st.button('Globos')
if boton_globos:
    st.balloons()
boton_nieve = st.button('Nieve')
if boton_nieve:
    st.snow()

# ######################
# Estructuras de control
# ######################

st.title("Titulo 9: Estructuras de control")

"st.stop(·) detiene la ejecución"
"st.experimental_rerun(·) recarga el script"

st.header("Sección 9.1: Formularios")

"Engloba en un container todos los elementos incluidos, y se ejecutan juntos cuando pulsas el boton"

form = st.form("Formulario 1") #principio

slider1 = form.slider("Slider1")
slider2 = form.slider("Slider2")

form.form_submit_button("OK") #obligatorio, va al final

st.write(slider1,slider2)

# ######################
# Obtener parametros
# ######################

st.title("Titulo 10: Obtener parametros")

st.experimental_get_query_params()
{"show_map": ["True"], "selected": ["asia", "america"]}

# ######################
# Usuario y contraseña
# ######################

st.title("Titulo 11: Usuario y contraseña")

# Everything in this section will be available as an environment variable 

st.text("Se pueden guardar variables en un archivo secreto aparte. ")
st.text("El archivo debe llamarse .streamlit/secrets.toml ") #Carpeta .streamlit, Nombre secrets, Extensión: .toml
st.text(''' Se accede a las variables a través de una orden st.secret[·]
que funciona de forma parecida a st.session_state[·]''')

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("Cocacola (pertenece a una seccion):", st.secrets["seccion"]["cocacola"])
st.write("Bebida (es un numero):", st.secrets["seccion"]["bebida"])

st.text("Se pueden crear casillas con el formato de contraseña, \n  independientemente de lo que hagamos con ellas: ")

contraseña = st.text_input("Password", type="password")
"Aquí se mostrara tu contraseña" if contraseña == "" else "Tu contraseña es: *" + contraseña +"*"

st.text("El formato contraseña solo es valido para el textbox pequeño.")

# ######################
# App Github
# ######################

st.title("Titulo 12: App Github")

"hay que abrirse una cuenta de Github y publicar todo para poder verlo online"
"Los archivos de la carpeta .streamlit no se cargan porque es una carpeta oculta, hay que meterlos por tu cuenta"
"secrets.toml no hay que añadirlo, eso solo es para trabajo local. en cambio, hay que ir a ≡ -> Setting -> Secrets y copiar con el formato .toml"
"config.toml sí parece que funciona, pero tiene preferencia el usuario al elegir el color de la pagina (tema)"
"Las modificaciones en About, Report a Bug y Get Help parecen tardar un poco más en cargar"

# ######################
# Otros II
# ######################

st.title("Titulo 13: Otros II - Streamlit web")

"Implementar una aplicación / Deploy an app"
"https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app"

"Share your app"
"https://docs.streamlit.io/streamlit-community-cloud/get-started/share-your-app"

"Cloud / Get started"
"https://streamlit.io/cloud"


# ######################
# Hoja de cálculo
# ######################

st.title("Titulo 14: Hoja de cálculo")

from gsheetsdb import connect

conn = connect()
@st.cache(ttl=600) # Uses st.cache to only rerun when the query changes or after 10 min.

def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")





