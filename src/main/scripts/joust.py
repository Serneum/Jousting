from jousting.round.controller import Controller
from jousting.player.knight import Knight

# pygame.init()
#
# FPS = 60
# fpsClock = pygame.time.Clock()
#
# WHITE = (255, 255, 255)
#
# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello World')
# player = pygame.image.load('stickfigure.png').convert_alpha()
# player = pygame.transform.scale(player, (50, 50))
# pX = 20
# pY = 20
#
# def handle_movement():
#     global pX
#     global pY
#
#     pressed = pygame.key.get_pressed()
#     if pressed[K_w]:
#         pY -= 1
#     if pressed[K_s]:
#         pY += 1
#     if pressed[K_a]:
#         pX -= 1
#     if pressed[K_d]:
#         pX += 1

p1 = Knight("Lancelot")
p2 = Knight("Percival")
controller = Controller(p1, p2)
controller.do_game()

# while True:
#     DISPLAYSURF.fill(WHITE)
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#
#     handle_movement()
#
#     DISPLAYSURF.blit(player, (pX, pY))
#     pygame.display.update()
#     fpsClock.tick(FPS)


