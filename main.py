import pygame, time, os, numpy as np

# initial function
pygame.init()

# config - title
pygame.display.set_caption("Juego de la vida, John Conway - @is-not-avaliable")

# more config
width, height = 700, 700

# create windows
screen = pygame.display.set_mode((height, width))

# bgcolor
bg = 25, 25, 25
screen.fill(bg)

# cells amount
nxC, nyC = 60, 60

# more about cells
dimCW = width / nxC
dimCH = height / nyC

# a jsdjasdiouwqeoiuqw oihsokd hoasoldhi21´8312u73yoihadoash
gameState = np.zeros((nxC, nyC))

# paused game
pauseExec = True

# control the end game
endGame = False

# amount
iteration = 0

clock = pygame.time.Clock()

# Main Loop:
while not endGame:

    newGameState = np.copy(gameState)
    screen.fill(bg)
    # delay
    time.sleep(0.1)

    # Listener event
    ev = pygame.event.get()

    # population info
    population = 0

    # some events to better exp
    for event in ev:
        if event.type == pygame.QUIT:
            endGame = True
            break

        if event.type == pygame.KEYDOWN:

            # scape = scape
            if event.key == pygame.K_ESCAPE:
                endGame = True
                break

            # restart function
            if event.key == pygame.K_r:
                iteration = 0
                gameState = np.zeros((nxC, nyC))
                newGameState = np.zeros((nxC, nyC))
                pauseExec = True
            else:
                pauseExec = not pauseExec

        # mouse listener
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY, = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not gameState[celX, celY]

    if not pauseExec:
        iteration += 1

    # other important loop
    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExec:

                # neighbor amount
                n_neigh = (
                    gameState[(x - 1) % nxC, (y - 1) % nyC]
                    + gameState[x % nxC, (y - 1) % nyC]
                    + gameState[(x + 1) % nxC, (y - 1) % nyC]
                    + gameState[(x - 1) % nxC, y % nyC]
                    + gameState[(x + 1) % nxC, y % nyC]
                    + gameState[(x - 1) % nxC, (y + 1) % nyC]
                    + gameState[x % nxC, (y + 1) % nyC]
                    + gameState[(x + 1) % nxC, (y + 1) % nyC]
                )

                #rules
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            # population increament
            if gameState[x, y] == 1:
                population += 1

            # polygon
            poly = [
                (int(x * dimCW), int(y * dimCH)),
                (int((x + 1) * dimCW), int(y * dimCH)),
                (int((x + 1) * dimCW), int((y + 1) * dimCH)),
                (int(x * dimCW), int((y + 1) * dimCH)),
            ]

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                if pauseExec:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 0)
                else:
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # updating title
    title = f"Juego de la vida, John Conway - @is-not-avaliable// Población: {population} - Generación: {iteration} // FPS: {clock.get_fps()}"
    if pauseExec:
        title += " - [PAUSED]"
    pygame.display.set_caption(title)

    # update gameState
    gameState = np.copy(newGameState)

    # show frames
    pygame.display.flip()

    # frame limit
    clock.tick(60)
