import yaml, pygame, random, glob, math, numpy
from Lifter import Lifter
from Basura import Basura

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

textures = [];
lifters = [];
basuras = [];
delta = 0;
t_rel = 0
semaforo_1_estado = numpy.zeros(1, dtype = numpy.int32)
D = numpy.zeros(1, dtype = list);


def GeneracionDeNodos():
	print("")

def loadSettingsYAML(File):
	class Settings: pass
	with open(File) as f:
		docs = yaml.load_all(f, Loader = yaml.FullLoader)
		for doc in docs:
			for k, v in doc.items():
				setattr(Settings, k, v)
	return Settings;


Settings = loadSettingsYAML("Settings.yaml");	
	
def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    #X axis in red
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(X_MIN,0.0,0.0)
    glVertex3f(X_MAX,0.0,0.0)
    glEnd()
    #Y axis in green
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,Y_MIN,0.0)
    glVertex3f(0.0,Y_MAX,0.0)
    glEnd()
    #Z axis in blue
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,0.0,Z_MIN)
    glVertex3f(0.0,0.0,Z_MAX)
    glEnd()
    glLineWidth(1.0)

def Texturas(filepath):
    # Arreglo para el manejo de texturas
    global textures;
    textures.append(glGenTextures(1))
    id = len(textures) - 1
    glBindTexture(GL_TEXTURE_2D, textures[id])
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    image = pygame.image.load(filepath).convert()
    w, h = image.get_rect().size
    image_data = pygame.image.tostring(image, "RGBA")
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D)
    
def Init(Options):
    global textures, basuras, lifters, semaforo_1_estado, D
    screen = pygame.display.set_mode( (Settings.screen_width, Settings.screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: cubos")
    

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(Settings.FOVY, Settings.screen_width/Settings.screen_height, Settings.ZNEAR, Settings.ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
    Settings.EYE_X,
    Settings.EYE_Y,
    Settings.EYE_Z,
    Settings.CENTER_X,
    Settings.CENTER_Y,
    Settings.CENTER_Z,
    Settings.UP_X,
    Settings.UP_Y,
    Settings.UP_Z)
    glClearColor(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
    for File in glob.glob(Settings.Materials + "*.*"):
        Texturas(File)
    
    # Posiciones inicales de los montacargas
    #Positions = numpy.zeros((Options.lifters, 3))
    Positions = numpy.random.rand(Options.lifters, 3)*70
    Positions[:,1] = 0
    #ositions = Positions.astype(numpy.int32)
    print(Positions)
    
    NodosCarga = Options.Basuras*[[70,0,70]];
    
    CurrentNode = 0;
    
    # Probar en parejas
    
    # rutas aqui ...
    # r1 = [0,1,2,3,4 , .... M^2 ]
    # r2 = numpy.random.rand(0,M^2, M^2);
    
    #Rutas.append(r1)
    #Rutas.append(r2)
   
    for i, p in enumerate(Positions):
        # i es el identificator del agente
        lifters.append(Lifter(Settings.DimBoard, 0.7, textures, i, p, CurrentNode, semaforo_1_estado, D ))
    
    for i, n in enumerate(NodosCarga):
        # i es el identificador de la carga: sirve para realizar el inventario
        basuras.append(Basura(Settings.DimBoard,1,textures,3, i, n))
        
def planoText():
    # activate textures
    glColor(1.0, 1.0, 1.0)
    #glEnable(GL_TEXTURE_2D)
    # front face
    #glBindTexture(GL_TEXTURE_2D, textures[0])  # Use the first texture
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(-Settings.DimBoard, 0, -Settings.DimBoard)
    
    glTexCoord2f(0.0, 1.0)
    glVertex3d(-Settings.DimBoard, 0, Settings.DimBoard)
    
    glTexCoord2f(1.0, 1.0)
    glVertex3d(Settings.DimBoard, 0, Settings.DimBoard)
    
    glTexCoord2f(1.0, 0.0)
    glVertex3d(Settings.DimBoard, 0, -Settings.DimBoard)
    
    glEnd()
    # glDisable(GL_TEXTURE_2D)

def checkCollisions():
    for c in lifters:
        for b in basuras:
            distance = math.sqrt(math.pow((b.Position[0] - c.Position[0]), 2) + math.pow((b.Position[2] - c.Position[2]), 2))
            if distance <= c.radiusCol:
                if c.status == "searching" and b.alive:
                    b.alive = False
                    c.status = "lifting"
                #print("Colision detectada")

def display():
    global lifters, basuras, delta
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    #Se dibuja cubos
    for obj in lifters:
        obj.draw()
        obj.update(delta)

    # Se dibuja el incinerador
    glColor3f(1.0, 0.5, 0.0)  # Color: Naranja
    square_size = 20.0  # Tamaño

    half_size = square_size / 2.0
    glBegin(GL_QUADS)
    glVertex3d(-half_size, 0.5, -half_size)
    glVertex3d(-half_size, 0.5, half_size)
    glVertex3d(half_size, 0.5, half_size)
    glVertex3d(half_size, 0.5, -half_size)
    glEnd()
    
    #Se dibujan basuras
    for obj in basuras:
        obj.draw()
        #obj.update()    
    #Axis()
    
    #Se dibuja el plano gris
    planoText()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_QUADS)
    glVertex3d(-Settings.DimBoard, 0, -Settings.DimBoard)
    glVertex3d(-Settings.DimBoard, 0, Settings.DimBoard)
    glVertex3d(Settings.DimBoard, 0, Settings.DimBoard)
    glVertex3d(Settings.DimBoard, 0, -Settings.DimBoard)
    glEnd()
    
    # Draw the walls bounding the plane
    wall_height = 50.0  # Adjust the wall height as needed
    
    glColor3f(0.8, 0.8, 0.8)  # Light gray color for walls
    
    # Draw the left wall
    glBegin(GL_QUADS)
    glVertex3d(-Settings.DimBoard, 0, -Settings.DimBoard)
    glVertex3d(-Settings.DimBoard, 0, Settings.DimBoard)
    glVertex3d(-Settings.DimBoard, wall_height, Settings.DimBoard)
    glVertex3d(-Settings.DimBoard, wall_height, -Settings.DimBoard)
    glEnd()
    
    # Draw the right wall
    glBegin(GL_QUADS)
    glVertex3d(Settings.DimBoard, 0, -Settings.DimBoard)
    glVertex3d(Settings.DimBoard, 0, Settings.DimBoard)
    glVertex3d(Settings.DimBoard, wall_height, Settings.DimBoard)
    glVertex3d(Settings.DimBoard, wall_height, -Settings.DimBoard)
    glEnd()
    
    # Draw the front wall
    glBegin(GL_QUADS)
    glVertex3d(-Settings.DimBoard, 0, Settings.DimBoard)
    glVertex3d(Settings.DimBoard, 0, Settings.DimBoard)
    glVertex3d(Settings.DimBoard, wall_height, Settings.DimBoard)
    glVertex3d(-Settings.DimBoard, wall_height, Settings.DimBoard)
    glEnd()
    
    # Draw the back wall
    glBegin(GL_QUADS)
    glVertex3d(-Settings.DimBoard, 0, -Settings.DimBoard)
    glVertex3d(Settings.DimBoard, 0, -Settings.DimBoard)
    glVertex3d(Settings.DimBoard, wall_height, -Settings.DimBoard)
    glVertex3d(-Settings.DimBoard, wall_height, -Settings.DimBoard)
    glEnd()

    checkCollisions()
    
def lookAt(theta):
    glLoadIdentity()
    rad = theta * math.pi / 180
    newX = Settings.EYE_X * math.cos(rad) + Settings.EYE_Z * math.sin(rad)
    newZ = -Settings.EYE_X * math.sin(rad) + Settings.EYE_Z * math.cos(rad)
    gluLookAt(
    newX,
    Settings.EYE_Y,
    newZ,
    Settings.CENTER_X,
    Settings.CENTER_Y,
    Settings.CENTER_Z,
    Settings.UP_X,
    Settings.UP_Y,
    Settings.UP_Z)	
    

def semaforo(Options):
	global t_rel
	global semaforo_1_estado
	global delta
	t0 = Options.t0
	t1 = Options.t1
	t2 = Options.t2
	
	t_rel += delta
	
	if t_rel < t0:
		print("Luz Verde")
		semaforo_1_estado[0] = 0
	elif t0 < t_rel and t_rel < (t0 + t1):
		print("Luz Amarilla")
		semaforo_1_estado[0] = 1
	elif t0 + t1 + t2 > t_rel:
		print("Luz Roja")
		semaforo_1_estado[0] = 2
	else:
		t_rel = 0
		semaforo_1_estado[0] = 0
	
		
	
def DistMat(lifters):
	global D
	n=len(lifters)
	D_mat = numpy.zeros((n,n));
	for i, a in enumerate(lifters):
		for j, b in enumerate (lifters):
			D_mat[i, j] = numpy.linalg.norm(a.Position-b.Position)	
	numpy.fill_diagonal(D_mat,numpy.inf)
	D[0] = D_mat;
    
    
def Simulacion(Options):
	# Variables para el control del observador
	global delta, D;
	theta = Options.theta
	radius = Options.radious
	delta = Options.Delta
	Init(Options);
	t_act = 0;
	while True:
		keys = pygame.key.get_pressed()  # Checking pressed keys
		t_act += delta;
		semaforo(Options)
		DistMat(lifters)
		print(D)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
					pygame.quit()	
					return
		if Options.T_max < t_act / 30:
					print("T_max reached")
					pygame.quit()	
					return
		if keys[pygame.K_RIGHT]:
			if theta > 359.0:
				theta = 0
			else:
				theta += 1.0
		lookAt(theta)
		if keys[pygame.K_LEFT]:
			if theta < 1.0:
				theta = 360.0;
			else:
				theta -= 1.0
		lookAt(theta)
		display()
		print("Tiempo total : %f" %(t_act / 30));
		display()
		pygame.display.flip()
		pygame.time.wait(10)

	#
	


