import pygame
import sys
import random
from pygame.locals import *

# Constants
#   Screen Sizes
WINDOWWIDTH = 1023
WINDOWHEIGHT = 682

#   Colours
RED = (255, 0, 0)
DARKGREEN = (0, 185, 0)
WHITE = (255, 255, 255)

# Variables
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Blackjack (IST Assignment)")

#   Images
cardBackImage = pygame.image.load("Images\\CardBack.png")
tableCardPlaceImage = pygame.image.load("Images\\TableCardPlace.png")

#       Spades Images
aceOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\AceOfSpades.png")
twoOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\TwoOfSpades.png")
threeOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\ThreeOfSpades.png")
fourOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\FourOfSpades.png")
fiveOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\FiveOfSpades.png")
sixOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\SixOfSpades.png")
sevenOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\SevenOfSpades.png")
eightOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\EightOfSpades.png")
nineOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\NineOfSpades.png")
tenOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\TenOfSpades.png")
jackOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\JackOfSpades.png")
queenOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\QueenOfSpades.png")
kingOfSpadesImage = pygame.image.load("Images\\Cards\\Spades\\KingOfSpades.png")
spadeImages = [None, aceOfSpadesImage, twoOfSpadesImage, threeOfSpadesImage, fourOfSpadesImage, fiveOfSpadesImage, sixOfSpadesImage, sevenOfSpadesImage, eightOfSpadesImage, nineOfSpadesImage, tenOfSpadesImage, jackOfSpadesImage, queenOfSpadesImage, kingOfSpadesImage]

#       Clubs Images
aceOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\AceOfClubs.png")
twoOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\TwoOfClubs.png")
threeOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\ThreeOfClubs.png")
fourOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\FourOfClubs.png")
fiveOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\FiveOfClubs.png")
sixOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\SixOfClubs.png")
sevenOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\SevenOfClubs.png")
eightOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\EightOfClubs.png")
nineOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\NineOfClubs.png")
tenOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\TenOfClubs.png")
jackOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\JackOfClubs.png")
queenOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\QueenOfClubs.png")
kingOfClubsImage = pygame.image.load("Images\\Cards\\Clubs\\KingOfClubs.png")
clubImages = [None, aceOfClubsImage, twoOfClubsImage, threeOfClubsImage, fourOfClubsImage, fiveOfClubsImage, sixOfClubsImage, sevenOfClubsImage, eightOfClubsImage, nineOfClubsImage, tenOfClubsImage, jackOfClubsImage, queenOfClubsImage, kingOfClubsImage]

aceOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\AceOfDiamonds.png")
twoOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\TwoOfDiamonds.png")
threeOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\ThreeOfDiamonds.png")
fourOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\FourOfDiamonds.png")
fiveOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\FiveOfDiamonds.png")
sixOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\SixOfDiamonds.png")
sevenOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\SevenOfDiamonds.png")
eightOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\EightOfDiamonds.png")
nineOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\NineOfDiamonds.png")
tenOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\TenOfDiamonds.png")
jackOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\JackOfDiamonds.png")
queenOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\QueenOfDiamonds.png")
kingOfDiamondsImage = pygame.image.load("Images\\Cards\\Diamonds\\KingOfDiamonds.png")
diamondImages = [None, aceOfDiamondsImage, twoOfDiamondsImage, threeOfDiamondsImage, fourOfDiamondsImage, fiveOfDiamondsImage, sixOfDiamondsImage, sevenOfDiamondsImage, eightOfDiamondsImage, nineOfDiamondsImage, tenOfDiamondsImage, jackOfDiamondsImage, queenOfDiamondsImage, kingOfDiamondsImage]

aceOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\AceOfHearts.png")
twoOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\TwoOfHearts.png")
threeOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\ThreeOfHearts.png")
fourOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\FourOfHearts.png")
fiveOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\FiveOfHearts.png")
sixOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\SixOfHearts.png")
sevenOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\SevenOfHearts.png")
eightOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\EightOfHearts.png")
nineOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\NineOfHearts.png")
tenOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\TenOfHearts.png")
jackOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\JackOfHearts.png")
queenOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\QueenOfHearts.png")
kingOfHeartsImage = pygame.image.load("Images\\Cards\\Hearts\\KingOfHearts.png")
heartImages = [None, aceOfHeartsImage, twoOfHeartsImage, threeOfHeartsImage, fourOfHeartsImage, fiveOfHeartsImage, sixOfHeartsImage, sevenOfHeartsImage, eightOfHeartsImage, nineOfHeartsImage, tenOfHeartsImage, jackOfHeartsImage, queenOfHeartsImage, kingOfHeartsImage]

cardImages = [None, spadeImages, clubImages, diamondImages, heartImages]

#   Font
pygame.font.init()
font1 = pygame.font.SysFont("Times New Roman", 40, False, False)
font2 = pygame.font.SysFont("Times New Roman", 20, False, True)

#   Sound
playSound = pygame.mixer
playSound.init()
calm1 = playSound.Sound("Sounds\\Music\\calm1.ogg")
calm2 = playSound.Sound("Sounds\\Music\\calm2.ogg")
calm1.set_volume(1.0)
calm1.play(-1, 0, 1)

cardsDrawn = []
def RandomCardGenerator():
    redraw = True
    while redraw:
        cardNumber = random.randint(1,13)
        suit = random.randint(1,4)
        card = (cardNumber, suit)
        redraw = False
        for oldCard in cardsDrawn:
            if card == oldCard:
                redraw = True;
                break

    return card

def CardValue(card):
    if card[0] > 10:
        return 10
    if card[0] == 1:
        return 11
    return card[0]

def CalculateScore(card1, card2, card3, card4, card5):
    score = 0;
    if card1 != None:
        score += CardValue(card1)
    if card2 != None:
        score += CardValue(card2)
    if card3 != None:
        score += CardValue(card3)
    if card4 != None:
        score += CardValue(card4)
    if card5 != None:
        score += CardValue(card5)
    print("Score: %s" % (score))
    return score

def Terminate():
    pygame.font.quit()
    pygame.quit()
    sys.exit()

def DrawCard(card, visible, rect):
    if visible:
        print("suit: " + str(card[1]) + ", card=" + str(card[0]))
        cardImage = cardImages[card[1]][card[0]]
    else:
        cardImage = cardBackImage
    windowSurface.blit(cardImage, rect)


def init():
    global dealerCard
    global dealerCard2
    global dealerCard3
    global dealerCard4
    global dealerCard5
    global playerCard
    global playerCard2
    global playerCard3
    global playerCard4
    global playerCard5

    global dealerCardValues
    global playerCardValues

    global firstCard
    global secondCard
    global thirdCard
    global fourthCard
    global fifthCard

    global dealerFirstCard
    global dealerSecondCard
    global dealerThirdCard
    global dealerFourthCard
    global dealerFifthCard

    global folded
    global dealerFolded

    global busted
    global dealerBusted

    global blackjack

    #   Fill Surface
    windowSurface.fill(DARKGREEN)

    #   Create Random Cards
    dealerCard = RandomCardGenerator()
    dealerCard2 = RandomCardGenerator()
    dealerCard3 = RandomCardGenerator()
    dealerCard4 = RandomCardGenerator()
    dealerCard5 = RandomCardGenerator()
    playerCard = RandomCardGenerator()
    playerCard2 = RandomCardGenerator()
    playerCard3 = RandomCardGenerator()
    playerCard4 = RandomCardGenerator()
    playerCard5 = RandomCardGenerator()

    #   Texture Table Spaces (Dealer)
    windowSurface.blit(tableCardPlaceImage, dealerTableSpace)
    windowSurface.blit(tableCardPlaceImage, dealerTableSpace2)
    windowSurface.blit(tableCardPlaceImage, dealerTableSpace3)
    windowSurface.blit(tableCardPlaceImage, dealerTableSpace4)
    windowSurface.blit(tableCardPlaceImage, dealerTableSpace5)

    #   Texture Table Spaces (Player)
    windowSurface.blit(tableCardPlaceImage, playerTableSpace)
    windowSurface.blit(tableCardPlaceImage, playerTableSpace2)
    windowSurface.blit(tableCardPlaceImage, playerTableSpace3)
    windowSurface.blit(tableCardPlaceImage, playerTableSpace4)
    windowSurface.blit(tableCardPlaceImage, playerTableSpace5)

    # Card states
    firstCard = True
    secondCard = True
    thirdCard = False
    fourthCard = False
    fifthCard = False

    dealerFirstCard = True
    dealerSecondCard = True
    dealerThirdCard = False
    dealerFourthCard = False
    dealerFifthCard = False
    #   Check if Folded
    folded = False
    dealerFolded = False

    #   Check if Busted
    busted = False
    dealerBusted = False

    #   Check if Blackjack
    blackjack = False

    #   Assign Values to and Texture Dealer Cards
    DrawCard(dealerCard, False, dealerRect1)
    DrawCard(dealerCard2, True, dealerRect2)

    #   Assign Values to and Texture Dealer Cards
    DrawCard(playerCard, True, playerRect1)
    DrawCard(playerCard2, True, playerRect2)

    dealerCardValues = CalculateScore(dealerCard, dealerCard2, None, None, None)
    playerCardValues = CalculateScore(playerCard, playerCard2, None, None, None)

    pygame.display.update()

    return


# Game Loop

#   Create Table Spaces (Dealer)
dealerTableSpace = pygame.draw.rect(windowSurface, DARKGREEN, (127, 111, 85, 120), 0)
dealerTableSpace2 = pygame.draw.rect(windowSurface, DARKGREEN, (287, 111, 85, 120), 0)
dealerTableSpace3 = pygame.draw.rect(windowSurface, DARKGREEN, (447, 111, 85, 120), 0)
dealerTableSpace4 = pygame.draw.rect(windowSurface, DARKGREEN, (607, 111, 85, 120), 0)
dealerTableSpace5 = pygame.draw.rect(windowSurface, DARKGREEN, (767, 111, 85, 120), 0)

#   Create Table Spaces (Player)
playerTableSpace = pygame.draw.rect(windowSurface, DARKGREEN, (127, 411, 85, 120), 0)
playerTableSpace2 = pygame.draw.rect(windowSurface, DARKGREEN, (287, 411, 85, 120), 0)
playerTableSpace3 = pygame.draw.rect(windowSurface, DARKGREEN, (447, 411, 85, 120), 0)
playerTableSpace4 = pygame.draw.rect(windowSurface, DARKGREEN, (607, 411, 85, 120), 0)
playerTableSpace5 = pygame.draw.rect(windowSurface, DARKGREEN, (767, 411, 85, 120), 0)

#   Create Dealer Card Rectangles
dealerRect1 = pygame.draw.rect(windowSurface, RED, (138, 121, 60, 100), 0)
dealerRect2 = pygame.draw.rect(windowSurface, RED, (298, 121, 60, 100), 0)

#   Create Player Card Rectangles
playerRect1 = pygame.draw.rect(windowSurface, RED, (138, 421, 60, 100), 0)
playerRect2 = pygame.draw.rect(windowSurface, RED, (298, 421, 60, 100), 0)

# Pre-render text
bustText = font1.render("BUST!!!", 1, WHITE)
youWinText = font1.render("YOU WIN!", 1, WHITE)
youLostText = font1.render("YOU LOST!", 1, WHITE)
blackjackText = font1.render("BLACKJACK!", 1, WHITE)
tieText = font1.render("TIE!", 1, WHITE)
instructionsTextLn1 = font2.render('Press "H" to draw a card (get hit).', 1, WHITE)
instructionsTextLn2 = font2.render('Press "F" to stop drawing (fold).', 1, WHITE)
instructionsTextLn3 = font2.render('Press "Esc" to exit.', 1, WHITE)

while True:
    init()

    windowSurface.blit(instructionsTextLn1, (707, 601))
    windowSurface.blit(instructionsTextLn2, (707, 621))
    windowSurface.blit(instructionsTextLn3, (707, 641))


    #   Dealer and Player Card Values
    dealerCardValues = CalculateScore(dealerCard, dealerCard2, None, None, None)
    playerCardValues = CalculateScore(playerCard, playerCard2, None, None, None)

    gameOver = False
    while not gameOver:
        for event in pygame.event.get():
            if event.type == QUIT:
                Terminate()
            pygame.display.update()

        for event in pygame.event.get():
            if playerCard == (11, 1) and playerCard2 == (1, 1) or playerCard == (11, 1) and playerCard2 == (1, 2) or playerCard == (11, 1) and playerCard2 == (1, 3) or playerCard == (11, 1) and playerCard2 == (1, 4) or playerCard == (12, 1) and playerCard2 == (1, 1) or playerCard == (12, 1) and playerCard2 == (1, 2) or playerCard == (12, 1) and playerCard2 == (1, 3) or playerCard == (12, 1) and playerCard2 == (1, 4) or playerCard == (13, 1) and playerCard2 == (1, 1) or playerCard == (13, 1) and playerCard2 == (1, 2) or playerCard == (13, 1) and playerCard2 == (1, 3) or playerCard == (13, 1) and playerCard2 == (1, 4):
                blackjack = True
                windowSurface.blit(blackjackText, (421, 281))
            if playerCard2 == (11, 1) and playerCard == (1, 1) or playerCard2 == (11, 1) and playerCard == (1, 2) or playerCard2 == (11, 1) and playerCard == (1, 3) or playerCard2 == (11, 1) and playerCard == (1, 4) or playerCard2 == (12, 1) and playerCard == (1, 1) or playerCard2 == (12, 1) and playerCard == (1, 2) or playerCard2 == (12, 1) and playerCard == (1, 3) or playerCard2 == (12, 1) and playerCard == (1, 4) or playerCard2 == (13, 1) and playerCard == (1, 1) or playerCard2 == (13, 1) and playerCard == (1, 2) or playerCard2 == (13, 1) and playerCard == (1, 3) or playerCard2 == (13, 1) and playerCard == (1, 4):
                blackjack = True
                windowSurface.blit(blackjackText, (421, 281))

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                        Terminate()

            if not gameOver and event.type == KEYDOWN and blackjack == False:
                playerCardValues = CalculateScore(playerCard, playerCard2, None, None, None)

                if playerCardValues == 22:
                    playerCard = RandomCardGenerator()
                    playerCard2 = RandomCardGenerator()

                if event.key == ord("h"):
                    if fourthCard == True and fifthCard == False:
                        playerRect5 = pygame.draw.rect(windowSurface, RED, (778, 421, 60, 100), 0)
                        DrawCard(playerCard5, True, playerRect5)
                        pygame.display.update()
                        playerCardValues = CalculateScore(playerCard, playerCard2, playerCard3, playerCard4, playerCard5)
                        fifthCard = True

                    if thirdCard == True and fourthCard == False:
                        playerRect4 = pygame.draw.rect(windowSurface, RED, (618, 421, 60, 100), 0)
                        DrawCard(playerCard4, True, playerRect4)
                        pygame.display.update()
                        playerCardValues = CalculateScore(playerCard, playerCard2, playerCard3, playerCard4, None)
                        fourthCard = True

                    if secondCard == True and thirdCard == False:
                        playerRect3 = pygame.draw.rect(windowSurface, RED, (458, 421, 60, 100), 0)
                        DrawCard(playerCard3, True, playerRect3)
                        pygame.display.update()
                        playerCardValues = CalculateScore(playerCard, playerCard2, playerCard3, None, None)
                        thirdCard = True

                    if playerCardValues > 21:
                        busted = True
                        if busted == True:
                            windowSurface.blit(bustText, (421, 281))
                        DrawCard(dealerCard, True, dealerRect1)
                        pygame.display.update()
                        pygame.time.wait(3000);
                        gameOver = True;

                if event.key == ord("f"):
                    DrawCard(dealerCard, True, dealerRect1)
                    pygame.display.update()

                    if dealerSecondCard == True and dealerThirdCard == False and dealerCardValues < 17 and dealerCardValues < playerCardValues:
                        pygame.time.wait(1500);
                        dealerRect3 = pygame.draw.rect(windowSurface, RED, (458, 121, 60, 100), 0)
                        DrawCard(dealerCard3, True, dealerRect3)
                        pygame.display.update()
                        dealerCardValues = CalculateScore(dealerCard, dealerCard2, dealerCard3, None, None)
                        dealerThirdCard = True

                    if dealerThirdCard == True and dealerFourthCard == False and dealerCardValues < 17 and dealerCardValues < playerCardValues:
                        pygame.time.wait(1500);
                        dealerRect4 = pygame.draw.rect(windowSurface, RED, (618, 121, 60, 100), 0)
                        DrawCard(dealerCard4, True, dealerRect4)
                        pygame.display.update()
                        dealerCardValues = CalculateScore(dealerCard, dealerCard2, dealerCard3, dealerCard4, None)
                        dealerFourthCard = True

                    if dealerFourthCard == True and dealerFifthCard == False and dealerCardValues < 17 and dealerCardValues < playerCardValues:
                        pygame.time.wait(1500);
                        dealerRect5 = pygame.draw.rect(windowSurface, RED, (778, 121, 60, 100), 0)
                        DrawCard(dealerCard5, True, dealerCard5)
                        pygame.display.update()
                        dealerCardValues = CalculateScore(dealerCard, dealerCard2, dealerCard3, dealerCard4, dealerCard5)
                        dealerFifthCard = True

                    if dealerCardValues > 21 or playerCardValues > dealerCardValues:
                        windowSurface.blit(youWinText, (421, 281))
                        pygame.time.wait(3000)
                        gameOver = True
                    elif playerCardValues == dealerCardValues:
                        windowSurface.blit(tieText, (421, 281))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        gameOver = True
                    elif playerCardValues < 21 and playerCardValues > dealerCardValues:
                        windowSurface.blit(youWinText, (421, 281))
                    elif bust == False:
                        windowSurface.blit(youLostText, (421, 281))
                        gameOver = True
                    pygame.display.update()
                    pygame.time.wait(3000)

            if event.type == QUIT:
                Terminate()

