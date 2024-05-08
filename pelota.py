import pygame

class Pelota:
    def __init__(self):
        self.ball = pygame.image.load('imagenes/football.png')
        self.ball = self.ball.convert_alpha() # <--- quitar el fondo
        self.ball_rect = self.ball.get_rect() # <--- obtenido el rectángulo
        self.posicionX = 200 # <--- posición de inicio en X
        self.posicionY = 200 # <--- posición de inicio en Y
        self.velocidadX = 3.0 # <-- velocidad en X
        self.velocidadY = 3.0 # <-- velocidad en Y
    def posicion_inicial(self):
        self.ball_rect.topleft = (self.posicionX, self.posicionY)
    def moverse(self, ancho, alto):
        # posicionX es menor que 0 o posicionX + ancho de la pelota >= ancho de la pantalla
        if self.posicionX <= 0 or self.posicionX + self.ball.get_width() >= ancho:
            self.velocidadX *= -1 # velocidad en X se invierta
        # posicionY es menor que 0 o posicionY + alto de la pelota >= alto de la pantalla
        if self.posicionY <= 0 or self.posicionY + self.ball.get_height() >= alto:
            self.velocidadY *= -1 # velocidad en Y se invierte
        # posicion X aumenta velocidadX valor
        self.posicionX += self.velocidadX
        # posicion Y aumenta velocidadY valor
        self.posicionY += self.velocidadY
        # actualizamos o enviamos estos valores al rectángulo
        self.ball_rect[0] = self.posicionX
        self.ball_rect[1] = self.posicionY
