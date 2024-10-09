from ursina import *
import pandas as pd
import numpy as np
import random as rd
import csv

app = Ursina()

current_scene = None

def scene_logo():
    global current_scene
    current_scene = "logo"

    scene.clear()

    logo_entity = Entity(model='quad', texture='logo', scale=(12,4), position=(0, 0, 0))
    logo_base = Entity(model = 'quad', color = color.black, scale = (20,10), position = (0,0,1))
    logo_entity.blink(duration = 3)
    invoke(scene_inicial, delay = 3)

def scene_menu():
    global current_scene
    current_scene = "menu"

    scene.clear()

    # Path to your CSV file
    file_path = "50planetas"

    global df
    # Reading the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Display all columns
    pd.set_option('display.max_columns', None)

    # LIST OF TEXT
    facts = ("It is a gas giant exoplanet that orbits a K-type star. It takes 1 days to complete one orbit of its star, and is 0.01782 AU from its star. Its discovery was announced in 2020.",

    "It is a gas giant exoplanet that orbits an F-type star. It takes 19.4 days to complete one orbit of its star, and is 0.154 AU from its star. Its discovery was announced in 2013.",

    "It is a gas giant exoplanet that orbits a G-type star. It takes 69.3 days to complete one orbit of its star, and is 0.347 AU from its star. Its discovery was announced in 2024.",

    "It is a gas giant exoplanet that orbits an F-type star. It takes 4.1 days to complete one orbit of its star, and is 0.05524 AU from its star. Its discovery was announced in 2008.",

    "It is a Neptune-like exoplanet that orbits an M-type star. It takes 5.1 days to complete one orbit of its star, and is 0.04825 AU from its star. Its discovery was announced in 2022.",

    "A close exoplanet with a secret: a lack of methane on this hot world. GJ 436 b is a Neptune-sized exoplanet that orbits an M-type star.",

    "It is a Neptune-like exoplanet that orbits a G-type star. Its mass is 7.08 Earths, it takes 8.4 days to complete one orbit of its star, and is 0.0806 AU from its star. Its discovery was announced in 2018.",

    "It is a gas giant exoplanet that orbits a K-type star. It takes 1.3 days to complete one orbit of its star, and is 0.022 AU from its star. Its discovery was announced in 2016.",

    "It is a gas giant exoplanet that orbits an unknown-type star. It takes 5.6 years to complete one orbit of its star, and is 1.08 AU from its star. Its discovery was announced in 2018.",

    "It is a super Earth exoplanet that orbits a G-type star. It takes 82.3 days to complete one orbit of its star, and is 0.3679 AU from its star. Its discovery was announced in 2016.",

    "It is a Neptune-like exoplanet that orbits a K-type star. It takes 13.6 days to complete one orbit of its star, and is 0.1039 AU from its star. Its discovery was announced in 2016.",

    "It is a super Earth exoplanet that orbits a G-type star. It takes 11.3 days to complete one orbit of its star, and is 0.1041 AU from its star. Its discovery was announced in 2014.",

    "It is a terrestrial exoplanet that orbits an F-type star. It takes 5.6 days to complete one orbit of its star, and is 0.0659 AU from its star. Its discovery was announced in 2016.",

    "It is a super Earth exoplanet that orbits an F-type star. It takes 1.7 days to complete one orbit of its star, and is 0.02778 AU from its star. Its discovery was announced in 2014.",

    "It is a super Earth exoplanet that orbits an F-type star. It takes 10.5 days to complete one orbit of its star, and is 0.0997 AU from its star. Its discovery was announced in 2020.",

    "It is a super Earth exoplanet that orbits a G-type star. It takes 6.2 days to complete one orbit of its star, and is 0.0666 AU from its star. Its discovery was announced in 2016.",

    "It is a super Earth exoplanet that orbits a K-type star. It takes 24.8 days to complete one orbit of its star, and is 0.153 AU from its star. Its discovery was announced in 2016.",

    "It is a Neptune-like exoplanet that orbits a K-type star. It takes 5.3 days to complete one orbit of its star, and is 0.0671 AU from its star. Its discovery was announced in 2016.",

    "It is a Neptune-like exoplanet that orbits an F-type star. It takes 9 days to complete one orbit of its star, and is 0.08 AU from its star. Its discovery was announced in 2014.",

    "It is a gas giant exoplanet that orbits a K-type star. It takes 148.6 days to complete one orbit of its star, and is 0.61 AU from its star. Its discovery was announced in 2015.",

    "It is a gas giant exoplanet that orbits a K-type star. It takes 148.6 days to complete one orbit of its star, and is 0.61 AU from its star. Its discovery was announced in 2015.")

    # Define arrays
    d = df["sy_dist"]
    ra = df["ra"]
    ra2 = ra * np.pi/180
    dec = df["dec"]
    dec2 =  dec * np.pi/180
    mass_nan = df["pl_bmasse"]
    age_nan = df["st_age"]
    mass =  mass_nan.fillna("Not known")
    age = age_nan.fillna("Not known")
    stellar_mass = df["st_mass"]


    x = d*np.cos(ra)
    y = d*np.sin(ra)
    z = np.zeros(21)
    exo_position = np.column_stack((x, y, z))

    names = df["pl_name"].tolist()

    # Function to wrap text manually based on a specified width
    global wrap_text
    def wrap_text(text, max_width=30):
        words = text.split(' ')
        wrapped_lines = []
        current_line = ""
        
        for word in words:
            if len(current_line) + len(word) + 1 > max_width:  # +1 for space
                wrapped_lines.append(current_line)
                current_line = word
            else:
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word

        wrapped_lines.append(current_line)  # Add the last line
        return '\n'.join(wrapped_lines)

    background = Entity(model='quad', scale=(10000, 10000), color=color.white, position=(0, 2500, 1000), texture ="skybox_image.jpg")

    # Create the border first, with a slight negative z value to push it behind
    global textbox_border
    textbox_border = Entity(model='quad', scale=(1550, 2750), color=color.white, position=(-1700, 0, -1), visible=False)

    # Create the textbox background (quad) with a higher z value to appear in front of the border
    global textbox_bg
    textbox_bg = Entity(model='quad', scale=(1500, 2700), color=color.black, position=(-1675, 0, -100), visible=False)

    # Create the text as a child of the textbox background, so it moves with the box
    global tooltip
    tooltip = Text(text="", parent=textbox_bg, position=(-1000, 0, -3000), scale=2, visible=False, origin=(0, 0))

    # Create Earth
    global Earth, text_earth, exoplanets
    Earth = Entity(model='sphere', position=(0, 0, 100), scale=80, collider='box', texture="earth.jpg")
    text_earth = Text(text="Earth",  position=(0, 0.04, -300), scale=1, visible=False)

    camera.position = (0,0,-8000)
    camera.clip_plane_far = 20000 
    

    exoplanets = []
    global nombre_plan_ir
    
    # Create a sphere for each point in the scatter data and add a collider
    for i, point in enumerate(exo_position):
        x, y, z = point
        point_entity = Entity(model='sphere', color=color.orange, position=(x, y, 100), scale=40, collider='box', texture="grass")
        point_entity.point_data = (x, y, z)  # Store the point's data
        point_entity.name_data = names[i]  # Store the name of the planet
        point_entity.dist_data = d[i]
        point_entity.mass_data = mass[i]
        point_entity.stmass_data = stellar_mass[i]
        point_entity.age_data = age[i]
        point_entity.facts = facts[i]
        point_entity.dec_data = dec2[i]
        point_entity.ra_data = ra2[i]
        exoplanets.append(point_entity)
        if names[i] == "TOI-620 b" or names[i] == "HIP 65 A b" or names[i] == "GJ 436 b":
            point_entity.enabled = False
        else: 
            pass
        
        def on_click(planet=point_entity):
            print(f"{planet.name_data}\n Dec:{point_entity.dec_data}\n Ra: {point_entity.ra_data}\nDistance: {point_entity.dist_data}")
            scene_planeta(nombre_plan_ir = planet.name_data,
                      dec_planeta_tierra = point_entity.dec_data,
                      ra_planeta_tierra = point_entity.ra_data,
                      dist_planeta_tierra = point_entity.dist_data)
            
        point_entity.on_click = on_click













global button



def scene_planeta(nombre_plan_ir, dec_planeta_tierra, ra_planeta_tierra, dist_planeta_tierra):
    global current_scene, SUPER_NOMBRE
    SUPER_NOMBRE = nombre_plan_ir
    current_scene = "planeta"

    scene.clear()
    ############################################# CONSTANTES ###########################################

    DIST_REF = 5
    PI = 3.1415965


    def vec3_to_spherical(vec3):
        x, y, z = vec3.x, vec3.y, vec3.z
        r = np.sqrt(x**2 + y**2 + z**2)  # Calculate the radius
        
        # Calculate theta and phi
        theta = np.arccos(y / r)  # Angle from the positive Y-axis
        phi = np.arctan2(z, x)    # Angle in the X-Z plane
        
        return theta, phi

    def spherical_to_vec3(dist, theta, phi):
        x = dist*np.sin(theta)*np.cos(phi)
        y = dist*np.cos(theta)
        z = dist*np.sin(theta)*np.sin(phi)
        sol = Vec3(x,y,z)
        return sol


    ##################################  FIRST PERSON CHARACTER CONTROLLER ####################################
    class FirstPersonController(Entity):
        def __init__(self, **kwargs):
            self.cursor = Entity(parent=camera.ui, model='quad', color=color.red, scale=.008, rotation_z=45)
            super().__init__()
            self.speed = 5
            self.height = 2
            self.camera_pivot = Entity(parent=self, y=self.height)

            camera.parent = self.camera_pivot
            camera.position = (0,0,0)
            camera.rotation = (0,0,0)
            camera.fov = 90
            mouse.locked = True
            self.mouse_sensitivity = Vec2(40, 40)

            self.gravity = 0
            self.grounded = False
            self.jump_height = 2
            self.jump_up_duration = .5
            self.fall_after = .35 # will interrupt jump up
            self.jumping = False
            self.air_time = 0

            self.traverse_target = scene     # by default, it will collide with everything. change this to change the raycasts' traverse targets.
            self.ignore_list = [self, ]
            self.on_destroy = self.on_disable

            for key, value in kwargs.items():
                setattr(self, key ,value)

            # make sure we don't fall through the ground if we start inside it
            if self.gravity:
                ray = raycast(self.world_position+(0,self.height,0), self.down, traverse_target=self.traverse_target, ignore=self.ignore_list)
                if ray.hit:
                    self.y = ray.world_point.y


        def update(self):
            self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]

            self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
            self.camera_pivot.rotation_x= clamp(self.camera_pivot.rotation_x, -90, 90)

            self.direction = Vec3(
                self.forward * (held_keys['w'] - held_keys['s'])
                + self.right * (held_keys['d'] - held_keys['a'])
                ).normalized()

            feet_ray = raycast(self.position+Vec3(0,0.5,0), self.direction, traverse_target=self.traverse_target, ignore=self.ignore_list, distance=.5, debug=False)
            head_ray = raycast(self.position+Vec3(0,self.height-.1,0), self.direction, traverse_target=self.traverse_target, ignore=self.ignore_list, distance=.5, debug=False)
            if not feet_ray.hit and not head_ray.hit:
                move_amount = self.direction * time.dt * self.speed

                if raycast(self.position+Vec3(-.0,1,0), Vec3(1,0,0), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                    move_amount[0] = min(move_amount[0], 0)
                if raycast(self.position+Vec3(-.0,1,0), Vec3(-1,0,0), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                    move_amount[0] = max(move_amount[0], 0)
                if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,1), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                    move_amount[2] = min(move_amount[2], 0)
                if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,-1), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                    move_amount[2] = max(move_amount[2], 0)
                self.position += move_amount

                # self.position += self.direction * self.speed * time.dt


            if self.gravity:
                # gravity
                ray = raycast(self.world_position+(0,self.height,0), self.down, traverse_target=self.traverse_target, ignore=self.ignore_list)

                if ray.distance <= self.height+.1:
                    if not self.grounded:
                        self.land()
                    self.grounded = True
                    # make sure it's not a wall and that the point is not too far up
                    if ray.world_normal.y > .7 and ray.world_point.y - self.world_y < .5: # walk up slope
                        self.y = ray.world_point[1]
                    return
                else:
                    self.grounded = False

                # if not on ground and not on way up in jump, fall
                self.y -= min(self.air_time, ray.distance-.05) * time.dt * 100
                self.air_time += time.dt * .25 * self.gravity



        def on_enable(self):
            mouse.locked = True
            self.cursor.enabled = True
            # restore parent and position/rotation from before disablem in case you moved the camera in the meantime.
            if hasattr(self, 'camera_pivot') and hasattr(self, '_original_camera_transform'):
                camera.parent = self.camera_pivot
                camera.transform = self._original_camera_transform


        def on_disable(self):
            mouse.locked = False
            self.cursor.enabled = False
            self._original_camera_transform = camera.transform  # store original position and rotation
            camera.world_parent = scene


    global player
    player = FirstPersonController()

    #################################################################################################################################




    ########################## CREAR ARCHIVO DE GUARDADO DE CONSTELACIONES ########################

    global inp1, b1, rectas, nombre_guardar
    nombre_guardar = nombre_plan_ir
    inp1 = InputField()
    inp1.color = color.rgb(0.27,0.46,0.5)
    inp1.tooltip = Tooltip("Input your File save name")
    b1 = Button(scale = (0.2,0.05), y = -0.1, text = 'Submit name', color = color.rgb(0.27,0.46,0.5))

    inp1.enabled = False
    b1.enabled = False

    def crear_archivo():
        global inp1, b1, rectas
        print(inp1.text)
        inp1.enabled = False
        b1.enabled = False

        with open(f"{inp1.text}.csv", 'w', newline='') as file:
            escritor = csv.writer(file)

            # Escribir encabezados, incluyendo el nombre del planeta
            escritor.writerow(['Identif 1', 'Theta 1', 'Phi 1', 'Dist 1' , 'Identif 2', 'Theta 2', 'Phi 2', 'Dist 2' , 'Nombre Planeta'])

            for recta in rectas:
                temporal = [recta.est_1.identif, recta.est_1.theta, recta.est_1.phi, recta.est_1.dist,
                            recta.est_2.identif, recta.est_2.theta, recta.est_2.phi, recta.est_2.dist,
                            nombre_guardar]  # Agregar el nombre del planeta aquí
                escritor.writerow(temporal)  # Cambiar a writerow para escribir una sola fila

        cambiar_pausa()

        
        
    b1.on_click = crear_archivo

    global pause_menu_bg
    def guardar_constelaciones():
        global pause_menu_bg
        pause_menu_bg.enabled = False
        inp1.enabled = True
        b1.enabled = True





    ###############################################################################################





    ######################################## IMPORTAR CONSTELACIONES #########################################
    global inp2, b2
    
    inp2 = InputField()
    inp2.tooltip = Tooltip("Input your File save name")
    inp2.color = color.rgb(0.27,0.46,0.5)
    b2 = Button(scale = (0.2,0.05), y = -0.1, text = 'Submit name')

    inp2.enabled = False
    b2.enabled = False



    def dibujar_constelaciones():
        global rectas, estrellas_lista, inp2, b2, nombre_plan_ir, SUPER_NOMBRE

        # Leer el archivo CSV con pandas
        try:
            df2 = pd.read_csv(f"{inp2.text}.csv")
        except FileNotFoundError:
            print("Archivo no encontrado. Asegúrate de que el archivo existe en el directorio.")
            return
        
        # Limpiar las rectas actuales si es necesario
        for recta in rectas:
            destroy(recta)
        rectas.clear()

        # Iterar sobre las filas del CSV y reconstruir las rectas
        # Lista para almacenar estrellas auxiliares que se crean
        estrellas_auxiliares = []

        for index, row in df2.iterrows():
            print(f"INDEX: {index}")
            identif_1 = row['Identif 1']
            theta_1 = row['Theta 1']
            phi_1 = row['Phi 1']
            dist_1 = row['Dist 1']
            identif_2 = row['Identif 2']
            theta_2 = row['Theta 2']
            phi_2 = row['Phi 2']
            dist_2 = row['Dist 2']
            nombre_planeta = row['Nombre Planeta']  # Guardar el nombre del planeta si es necesario
            print(nombre_planeta)

            
            ra_p = df.loc[df['pl_name'] == nombre_planeta, 'ra']
            dec_p = df.loc[df['pl_name'] == nombre_planeta, 'dec']
            dist_p = df.loc[df['pl_name'] == nombre_planeta, 'sy_dist']

            ra_p_prima = df.loc[df['pl_name'] == SUPER_NOMBRE, 'ra']
            dec_p_prima = df.loc[df['pl_name'] ==SUPER_NOMBRE, 'dec']
            dist_p_prima = df.loc[df['pl_name'] == SUPER_NOMBRE, 'sy_dist']

            vec_p = spherical_to_vec3(dist_p,dec_p,ra_p)
            vec_p_prima = spherical_to_vec3(dist_p_prima,dec_p_prima,ra_p_prima)

            vec_p_a_p_prima = vec_p - vec_p_prima





            vec_e_1_p = spherical_to_vec3(dist_1,theta_1,phi_1)
            vec_e_2_p = spherical_to_vec3(dist_2,theta_2,phi_2)      

            vec_e_1_prima = vec_e_1_p + vec_p_a_p_prima
            vec_e_2_prima = vec_e_2_p + vec_p_a_p_prima

            theta_aux_e_1,phi_aux_e_1 = vec3_to_spherical(vec_e_1_prima)
            theta_aux_e_2, phi_aux_e_2 = vec3_to_spherical(vec_e_2_prima)
            
            estrella_aux_1 = Estrella('1', theta_aux_e_1, phi_aux_e_1, 0.1, color.green, 1)
            
            estrella_aux_2 = Estrella('2', theta_aux_e_2, phi_aux_e_2, 0.1, color.green, 1)

            recta_guay = crear_recta(estrella_aux_1, estrella_aux_2, color = color.orange)
            
            
        

        cambiar_pausa()
        inp2.enabled = False
        b2.enabled = False
        print("Constelaciones importadas correctamente.")
        

    b2.on_click = dibujar_constelaciones

    def importar_constelaciones():
        global inp2, b2, pause_menu_bg
        pause_menu_bg.enabled = False
        inp2.enabled = True
        b2.enabled = True
        
        
        # Pedir el nombre del archivo de CSV
        nombre_archivo = inp2.text

        





    ####################################################### CREAR RECTAS ############################################################
    global rectas
    rectas = []

    class Recta(Entity):
        def __init__(self, est_1, est_2, color):
            super().__init__()
            self.est_1 = est_1
            self.est_2 = est_2
            self.model = 'cube'
            self.collider = 'cube'
            self.color = color
            self.color_inic = color
            self.scale = (0.01,0.01,(est_1.position-est_2.position).length())
            self.position = (est_1.position+est_2.position)/2
            self.look_at(est_2.position)
            self.on_click= self.destruir

        def update(self):
            if self.hovered:
                self.color = color.yellow
            else:
                self.color = self.color_inic

        def destruir(self):
            rectas.remove(self)
            destroy(self)

    def crear_recta(est_1,est_2, color):  # Crear rectas dados dos Vec3 posiciones
        rectas.append(Recta(est_1,est_2, color))

        


    ##################################################################################################################################



    ##################################### MENÚ DE PAUSA ##################################

    # Crear un fondo gris transparente
    pause_menu_bg = Entity(
        parent=camera.ui,
        model='quad',
        color=color.rgba(0, 0, 0, 0.1),  # Fondo grisáceo con transparencia
        scale=(1.5, 1),
        enabled=False  # Oculto al inicio
    )
    global cambiar_pausa, button
    def cambiar_pausa():
        application.paused = not application.paused
        mouse.locked = not application.paused
        mouse.visible = application.paused
        pause_menu_bg.enabled = application.paused
        button.enabled = application.paused
        
    # Crear botón de reanudar
    resume_button = Button(
        text='Continue',
        color=color.orange,
        scale=(0.3, 0.05),
        position=(0, 0.1),
        parent=pause_menu_bg,
        on_click = cambiar_pausa  # Función para reanudar el juego
    )

    # Crear botón que no hace nada
    nothing_button = Button(
        text='Save all your constellations',
        color=color.orange,
        scale=(0.3, 0.05),
        position=(0, 0),
        parent=pause_menu_bg,
        on_click = guardar_constelaciones
    )




    # Crear botón que importa constelaciones
    importar_button = Button(
        text='Import constellations from a .csv',
        color=color.orange,
        scale=(0.3, 0.05),
        position=(0, -0.1),
        parent=pause_menu_bg,
        on_click = importar_constelaciones
    )



    ############################################################ DEFINIR CLASE ESTRELLA ##############################################
    global primera_estrella, segunda_estrella
    primera_estrella, segunda_estrella = 0, 0

    class Estrella(Entity):
        def __init__(self, identif , theta, phi, scale, color_inic, dist):
            super().__init__()
            self.theta = theta
            self.identif = identif
            self.phi = phi
            self.model = 'sphere'
            self.collider = 'sphere'
            self.color_original = color_inic
            self.color = color_inic
            self.dist = dist
            self.scale = scale
            self.position = (DIST_REF * np.sin(self.theta) * np.cos(self.phi)
                , DIST_REF * np.cos(self.theta)
                , DIST_REF * np.sin(self.theta) * np.sin(self.phi)
                )
            self.on_click = self.empezar_recta


        def update(self):
            if self.hovered or primera_estrella == self:
                self.color = color.orange
            else:
                self.color = self.color_original
                
        def empezar_recta(self):
            global primera_estrella
            global segunda_estrella
        
            if primera_estrella == 0:
                primera_estrella = self
            else:
                segunda_estrella = self
                crear_recta(primera_estrella, segunda_estrella, color.rgba(0.486,0.796,1,1))
                primera_estrella = 0
                segunda_estrella = 0


    ###############################################################################################


    ############################################### ZOOM ###########################################
    global zoom_activo
    zoom_activo = True
    global cambiar_zoom
    def cambiar_zoom():
        global zoom_activo, player
        zoom_activo = not zoom_activo
        if zoom_activo:
            camera.fov = 100
            player.mouse_sensitivity = Vec2(40,40)
        else:
            camera.fov = 30
            player.mouse_sensitivity = Vec2(10,10)
        
    ###############################################################################################






    ###################################################################################################################################################################



    #%% Esferas fantasma

    global estrellas_lista
    
    spheresf = []
    estrellas_lista = []
    thetas_plotear = []
    phis_plotear = []
    distancias_plotear = []

    

    estrellas_dataframe = pd.read_csv(f"{nombre_plan_ir}")

    phis_esferas = np.array(estrellas_dataframe['ra'].tolist())
    thetas_esferas = np.array(estrellas_dataframe['dec'].tolist())
    NUM_ESTRELLAS = len(estrellas_dataframe)
    parallax_array = np.array(estrellas_dataframe['parallax'].tolist())
    distancias_array = 10000/parallax_array



    # generacion de magnitudes
    random_magnitudes = np.array(estrellas_dataframe['phot_g_mean_mag'].tolist())
    identificadores_estrellas = np.array(estrellas_dataframe['designation'].tolist())

    # magnitudes -> 0-1
    a, b = 6, 1.69 #maxima y minima magnitud
    c, d = 0, 1 #minima y maxima transparencia
    e, f = 0.01, 0.1 #min y max radios
    magnitudes_transparencia = [(c + (x - a) * (d - c) / (b - a)) for x in random_magnitudes]
    magnitudes_radios = [(e + (x - a) * (f - e) / (4*(b - a))) for x in random_magnitudes]









    for i in range(NUM_ESTRELLAS):
        ra_estrella_tierra = phis_esferas[i]
        dec_estrella_tierra = thetas_esferas[i]
        dist_estrella_tierra = distancias_array[i]
        
        vector_estrella_tierra = Vec3( dist_estrella_tierra*np.sin(dec_estrella_tierra)*np.cos(ra_estrella_tierra)
            ,dist_estrella_tierra*np.cos(dec_estrella_tierra)
            ,dist_estrella_tierra*np.sin(dec_estrella_tierra)*np.sin(ra_estrella_tierra)
            )

        vector_planeta_tierra = Vec3(dist_planeta_tierra*np.sin(dec_planeta_tierra)*np.cos(ra_planeta_tierra)
            ,dist_estrella_tierra*np.cos(dec_planeta_tierra)
            ,dist_estrella_tierra*np.sin(dec_planeta_tierra)*np.sin(ra_planeta_tierra)
            )

        vector_planeta_estrella = vector_planeta_tierra - vector_estrella_tierra


        theta_provisional, phi_provisional = vec3_to_spherical(vector_planeta_estrella)
        thetas_plotear.append(theta_provisional)
        phis_plotear.append(phi_provisional)
        distancias_plotear.append((vector_planeta_estrella.x**2 + vector_planeta_estrella.y**2 + vector_planeta_estrella.z**2)**(0.5))


        spheresf.append(Estrella(identificadores_estrellas[i],thetas_plotear[i],phis_plotear[i], magnitudes_radios[i]*1.3, color.rgba(1,1,1,max(0.05,min(magnitudes_transparencia[i]-0.2,0.1))),
                                 distancias_plotear[i]))
        estrellas_lista.append(Estrella(identificadores_estrellas[i],thetas_plotear[i],phis_plotear[i], magnitudes_radios[i], color.rgba(1,1,1,magnitudes_transparencia[i]),
                                        distancias_plotear[i]))


    sphere = Entity(model='sphere', color=color.orange, scale=5, position=(10, 0, 10), collider='sphere', emissive_color=color.yellow)




    #--------------------------CONTAMINACION-------------------------------


    esferon = Entity(model='sky_dome', scale=(DIST_REF, DIST_REF, DIST_REF), position=(0, 0, 0), color=color.gray, alpha=0)
    esferon.enabled = False

    
    megaesferon = Entity(model='sky_dome', scale = (2*DIST_REF, 2*DIST_REF, 2*DIST_REF), position= (0,0,0), color = color.black,  alpha=0.8)
    megaesferon.enabled = False

    def toggle_spheres():
        """Toggle the visibility of esferon and megaesferon."""
        esferon.enabled = not esferon.enabled
        megaesferon.enabled = not megaesferon.enabled
        button.text = "Not contamination" if esferon.enabled else "Contamination"

    # Create the button
    button = Button(text='Contamination', position=(-0.6, -0.4), scale=(0.3,0.05) , color=color.blue, on_click=toggle_spheres)
    button.enabled = False


    ##############################################    Crear Fondo Nocturno orientado segun el planeta   ########################################################

    skybox_image = load_texture("galaxia.jpg")  #imagenes que funcionan (cb-sunset-pano-ext.jpg), ()
    Sky(texture=skybox_image)
    Entity(
        model='sphere', 
        texture=skybox_image, 
        scale=500, 
        double_sided=True  # This ensures the texture is visible from the inside.
    )




def scene_creditos():
    global current_scene
    current_scene = "creditos"
    scene.clear()

    fondo_creditos = fondo_scene_inic = Entity(model='quad', texture='galaxia.jpg', scale=(20, 10), position=(0, 0, 1))
    Button(text='BACK', text_size= 1, scale=(0.3, 0.1), position=(0, -0.4), color=color.black90, on_click = scene_inicial)
    
    Text(text="TEAM MEMBERS: \n -----------\n PABLO COLOMER LLÓPEZ \n ÓSCAR HERVÁS PETIT \n ALEJANDRO RUIZ MARTINEZ \n ÒSCAR DELGADO FORT \n JOAN BALMÓN ANTÓN \n ÓSCAR CAMACHO BARREDA",
    position=(0, 0), origin=(0, 0), scale=3, color=color.blue)











def scene_educativa_presentacio():
    global current_scene
    current_scene = "educativa"
    scene.clear()

    global diapo, fondo, lista_nombres_diapos, next_boton, back_boton
    diapo = 0
    lista_nombres_diapos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    scene.clear()

    fondo = Entity(model='quad', texture=lista_nombres_diapos[diapo], position=(0, 0, 1), scale=(15.8, 8.7))

    def siguiente_diapo():
        global diapo, fondo, lista_nombres_diapos, next_boton, back_boton

        if current_scene != "educativa":  # Verificar si la escena ya ha cambiado
            return  # Si no estamos en la escena educativa, no hacer nada

        if diapo < len(lista_nombres_diapos) - 1:  # Verificar si no es la última diapositiva
            diapo += 1
            destroy(fondo)
            fondo = Entity(model='quad', texture=lista_nombres_diapos[diapo], position=(0, 0, 1), scale=(15.8, 8.7))
            print(fondo)
        else:
            # Si estamos en la última diapositiva, llamamos a otra función
            fin_presentacion()

        # Mostrar/ocultar botón de retroceso dependiendo de la diapositiva
        if back_boton:  # Verificar que el botón aún existe antes de acceder a él
            back_boton.visible = diapo > 0

    def anterior_diapo():
        global diapo, fondo, lista_nombres_diapos
        if current_scene != "educativa":  # Verificar si la escena ya ha cambiado
            return  # Si no estamos en la escena educativa, no hacer nada

        if diapo > 0:  # Evitar que se pase del primer índice
            diapo -= 1
            destroy(fondo)
            fondo = Entity(model='quad', texture=lista_nombres_diapos[diapo], position=(0, 0, 1), scale=(15.8, 8.7))
            print(fondo)

        # Mostrar/ocultar botón de retroceso dependiendo de la diapositiva
        if back_boton:  # Verificar que el botón aún existe antes de acceder a él
            back_boton.visible = diapo > 0

    def fin_presentacion():
        scene_inicial()  # Cambiar a la escena inicial

    next_boton = Button(texture="right_arrow", color=color.white, position=(0.6, -0.4, 0), scale=(0.4, 0.2), on_click=siguiente_diapo)
    back_boton = Button(texture="right_arrow", rotation_z=180, color=color.white, position=(0.2, -0.4, 0), scale=(0.4, 0.2), on_click=anterior_diapo)

    # Ocultar el botón de retroceso en la primera diapositiva
    back_boton.visible = diapo > 0

def scene_inicial():
    global current_scene
    current_scene = "inicial"

    scene.clear()

    fondo_scene_inic = Entity(model='quad', texture='galaxia.jpg', scale=(20, 10), position=(0, 0, 1))
    Button(text='LEARN TO USE', scale=(0.3, 0.1), position=(0, 0.3), color=color.blue, on_click=scene_educativa_presentacio)
    Button(text='EXPLORE', scale=(0.3, 0.1), position=(0, 0), color=color.blue, on_click=scene_menu)  # Actualizado para mostrar exoplanetas
    Button(text='CREDITS', scale=(0.3, 0.1), position=(0, -0.3), color=color.blue, on_click=scene_creditos)






#### Inputs general ######
def input(key):
    if key == 'p' and current_scene == "planeta":
        cambiar_pausa()
    if key == 'z' and current_scene == "planeta":
        cambiar_zoom()


################### Update general ######



# Function to update the tooltip based on mouse hover
def update():
    global current_scene, tooltip
    if current_scene == "menu":
        hovered_entity = mouse.hovered_entity
        Earth.rotation_y += time.dt * 50
            

        if hovered_entity == Earth:
            Earth.scale = 300  # Make Earth larger when hovered
            text_earth.visible = True
            text_earth.position = (-0.03, -0.075, -500)
        else:
            Earth.scale = 80  # Reset scale of Earth when not hovered
            text_earth.visible = False


        for planet in exoplanets:
            planet.rotation_z += time.dt * rd.randint(10, 100)
            planet.rotation_x += time.dt * 10
            if not hovered_entity or hovered_entity != planet:
                planet.scale = 60  # Reset to original scale
                planet.color = color.orange  # Reset to original color


        if hovered_entity and hasattr(hovered_entity, 'point_data'):
            # Change the planet's size and color when hovered
            hovered_entity.scale = 100  # Make the planet larger
            hovered_entity.color = color.red  # Change to a different color
            # Update the text with the hovered point's data formatted to one decimal place
            name_planet = hovered_entity.name_data
            distance_mod = hovered_entity.dist_data
            mass_planet = hovered_entity.mass_data
            age_planet = hovered_entity.age_data
            fact_planet = hovered_entity.facts
            st_mass = hovered_entity.stmass_data
            # Wrap the fact text to fit within the textbox
            fact_wrapped = wrap_text(fact_planet, max_width=35)  # Adjust max_width based on textbox size
            fact_planet = hovered_entity.facts

            tooltip.text = f"{name_planet}\n{'-' * 30}\n{fact_wrapped} \n \n Position (pc): {distance_mod:.1f}\n \n Mass (M_Earth): {mass_planet}\n \n Stellar Mass (M_Sun): {st_mass} \n \n Stellar Age (Gyr): {age_planet}"
            # Change the planet's size and color when hovered
            hovered_entity.scale = 300  # Make the planet larger
            hovered_entity.color = color.red  # Change to a different color
            # Show the textbox, border, and tooltip
            tooltip.visible = True
            textbox_bg.visible = True
            textbox_border.visible = True
                

            #  Offset the textbox from the mouse position (displacement)
            #displacement = (50, 20)  # Adjust these values for desired offset
            #textbox_bg.position = (mouse.x + displacement[0], mouse.y + displacement[1], 0)  # Set z = 0
            #textbox_border.position = (textbox_bg.position[0], textbox_bg.position[1], 100)  # Behind
                
            tooltip.position = (0.05, 0.04, -500)  # Keep the text centered inside the background
        else:
            # Hide the textbox, border, and tooltip when not hovering over a point
            tooltip.visible = False
            textbox_bg.visible = False
            textbox_border.visible = False









# Inicia en la primera escena
scene_logo()

# Ejecuta la aplicación
app.run()
