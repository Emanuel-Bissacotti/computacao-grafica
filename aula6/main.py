import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Configuração inicial do OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 800.0 / 600.0, 0.1, 100.0)  # Ajuste da tela para 800x600
    glMatrixMode(GL_MODELVIEW)

# Função para desenhar um quadrado com linhas
def draw_square_lines(x, y, zoom, rotation_x, rotation_y, rotation_z):
    glLoadIdentity()
    glTranslatef(x, y, zoom)  # Posição fixa
    glRotatef(rotation_x, 1, 0, 0)  # Rotação no eixo X
    glRotatef(rotation_y, 0, 1, 0)  # Rotação no eixo Y
    glRotatef(rotation_z, 0, 0, 1)
    glColor3f(1.0, 1.0, 1.0)  # Branco
    glBegin(GL_LINE_LOOP)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

# Função principal
def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)  # Ajuste para 800x600
    init()

    running = True
    pos_y = 0.0
    pos_x = 0.0
    zoom = -6.0
    rotation_y = 0
    rotation_x = 0
    rotation_z = 0.0
    rotate_up = False
    rotate_down = False
    rotate_left = False
    rotate_right = False
    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Se pressionar ESC
                    running = False # Sai do loop
                elif event.key == K_w: # Move para cima
                    pos_y += 0.1
                elif event.key == K_s: # Move para baixo
                    pos_y -= 0.1
                elif event.key == K_a: # Move para esquerda e rotaciona sentido anti-horário
                    pos_x -= 0.1
                elif event.key == K_d: # Move para direita e rotaciona sentido horário
                    pos_x += 0.1
                elif event.key == K_z: # Zoom out
                    zoom += 0.5
                elif event.key == K_x: # Zoom in
                    zoom -= 0.5
                elif event.key == K_UP:  # Rotação eixo X para cima
                    rotation_x += 5.0
                    rotate_up = not rotate_up
                elif event.key == K_DOWN:  # Rotação eixo X para baixo
                    rotation_x -= 5.0
                    rotate_down = not rotate_down
                elif event.key == K_LEFT:  # Rotação eixo Y para a esquerda
                    rotation_y -= 5.0
                    rotate_left = not rotate_left
                elif event.key == K_RIGHT:  # Rotação eixo Y para a direita
                    rotation_y += 5.0
                    rotate_right = not rotate_right
            
        if rotate_up:
            rotation_x += 1.0
        if rotate_down:
            rotation_x -= 1.0
        if rotate_left:
            rotation_y -= 1.0
        if rotate_right:
            rotation_y += 1.0
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_square_lines(pos_x, pos_y, zoom, rotation_x, rotation_y, rotation_z)
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()