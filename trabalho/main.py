import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

DISPLAY = (800, 600)
FOV = 45
ZOOM_INCR = 1.1
MOVE_STEP = 0.2
ROT_STEP = 5

zoom = 1.0
rot_x = rot_y = 0
pos_cubo = [-2.5, 0.0]
pos_triangulo = [0.0, 0.0]
pos_piramide = [2.5, 0.0]

def init():
    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOV, DISPLAY[0] / DISPLAY[1], 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_cubo():
    vertices = [
        [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1],
        [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1]
    ]
    faces = [
        (0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4),
        (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5)
    ]
    cores = [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (0,1,1), (1,0,1)]
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(cores[i])
        for vert in face:
            glVertex3fv(vertices[vert])
    glEnd()

def draw_triangulo():
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, 0)
    glVertex3f(1, -1, 0)
    glEnd()

def draw_piramide():
    vertices = [
        [0, 1, 0], [1, -1, 1], [-1, -1, 1],
        [-1, -1, -1], [1, -1, -1]
    ]
    faces = [
        (0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1),
        (1, 2, 3, 4)
    ]
    cores = [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (0.5,0.5,0.5)]
    for i, face in enumerate(faces):
        glBegin(GL_TRIANGLES if len(face)==3 else GL_QUADS)
        glColor3fv(cores[i])
        for vert in face:
            glVertex3fv(vertices[vert])
        glEnd()

def renderizar_objeto(func, pos):
    glPushMatrix()
    glTranslatef(pos[0], pos[1], -8)
    glScalef(zoom, zoom, zoom)
    glRotatef(rot_x, 1, 0, 0)
    glRotatef(rot_y, 0, 1, 0)
    func()
    glPopMatrix()

def mover_global(dx, dy, opcao):
    if opcao in ["1", "3", "5"]:
        pos_cubo[0] += dx
        pos_cubo[1] += dy
    if opcao in ["2", "3", "5"]:
        pos_triangulo[0] += dx
        pos_triangulo[1] += dy
    if opcao in ["4", "5"]:
        pos_piramide[0] += dx
        pos_piramide[1] += dy

def main():
    global zoom, rot_x, rot_y
    global pos_cubo, pos_triangulo, pos_piramide

    print("\nMENU DE OPÇÕES:")
    print("1 - Cubo")
    print("2 - Triângulo")
    print("3 - Cubo + Triângulo")
    print("4 - Pirâmide")
    print("5 - Cubo + Triângulo + Pirâmide")
    print("6 - Controle individual dos três objetos")

    opcao = input("Escolha uma opção (1 a 6): ")

    pygame.init()
    pygame.display.set_mode(DISPLAY, DOUBLEBUF | OPENGL)
    init()

    pos_cubo[:] = [-2.5, 0.0]
    pos_triangulo[:] = [0.0, 0.0]
    pos_piramide[:] = [2.5, 0.0]

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == QUIT or (evento.type == KEYDOWN and evento.key == K_ESCAPE):
                rodando = False

            elif evento.type == KEYDOWN:
                if evento.key == K_z:
                    zoom *= ZOOM_INCR
                elif evento.key == K_x:
                    zoom /= ZOOM_INCR
                elif evento.key == K_q:
                    rot_x += ROT_STEP
                elif evento.key == K_e:
                    rot_x -= ROT_STEP
                elif evento.key == K_r:
                    rot_y += ROT_STEP
                elif evento.key == K_f:
                    rot_y -= ROT_STEP

                elif evento.key == K_w:
                    mover_global(0, MOVE_STEP, opcao)
                elif evento.key == K_s:
                    mover_global(0, -MOVE_STEP, opcao)
                elif evento.key == K_a:
                    mover_global(-MOVE_STEP, 0, opcao)
                elif evento.key == K_d:
                    mover_global(MOVE_STEP, 0, opcao)

                elif opcao == "6":
                    if evento.key == K_i:
                        pos_cubo[1] += MOVE_STEP
                    elif evento.key == K_k:
                        pos_cubo[1] -= MOVE_STEP
                    elif evento.key == K_j:
                        pos_cubo[0] -= MOVE_STEP
                    elif evento.key == K_l:
                        pos_cubo[0] += MOVE_STEP

                    elif evento.key == K_g:
                        pos_triangulo[1] += MOVE_STEP
                    elif evento.key == K_b:
                        pos_triangulo[1] -= MOVE_STEP
                    elif evento.key == K_v:
                        pos_triangulo[0] -= MOVE_STEP
                    elif evento.key == K_n:
                        pos_triangulo[0] += MOVE_STEP

                    elif evento.key == K_UP:
                        pos_piramide[1] += MOVE_STEP
                    elif evento.key == K_DOWN:
                        pos_piramide[1] -= MOVE_STEP
                    elif evento.key == K_LEFT:
                        pos_piramide[0] -= MOVE_STEP
                    elif evento.key == K_RIGHT:
                        pos_piramide[0] += MOVE_STEP

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if opcao == "1":
            renderizar_objeto(draw_cubo, pos_cubo)
        elif opcao == "2":
            renderizar_objeto(draw_triangulo, pos_triangulo)
        elif opcao == "3":
            renderizar_objeto(draw_cubo, pos_cubo)
            renderizar_objeto(draw_triangulo, pos_triangulo)
        elif opcao == "4":
            renderizar_objeto(draw_piramide, pos_piramide)
        elif opcao in ["5", "6"]:
            renderizar_objeto(draw_cubo, pos_cubo)
            renderizar_objeto(draw_triangulo, pos_triangulo)
            renderizar_objeto(draw_piramide, pos_piramide)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
