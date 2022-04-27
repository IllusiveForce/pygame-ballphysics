import pygame as pg
pg.init()
gameDisplay=pg.display.set_mode((800,500))

cx=400
cy=20
mouserectpos=(0,0)
mouserect=pg.Rect(1,1,1,1)
circle=pg.Rect(10,10,10,1)
clock=pg.time.Clock()

mouseHeld=False
accel=10
xAccel=0
previouscx=0
previouscy=0
ctr=0

font=pg.font.Font(None,20)

color1=0
color2=0
color3=0

while True:
 
  ctr+=1
  previouscx=cx
  gameDisplay.fill((254,254,254))
  floorRect=pg.draw.rect(gameDisplay,(0,0,0),pg.Rect(0,490,800,10))
  wallRect=pg.draw.rect(gameDisplay,(0,0,0),pg.Rect(790,0,100,500))
  wallRect2=pg.draw.rect(gameDisplay,(0,0,0),pg.Rect(-90,0,100,500))
  buttonRect=pg.draw.rect(gameDisplay,(0,200,200),pg.Rect(10,10,100,50))
  ballDistanceFromFloor=490-cy
  gameDisplay.blit(font.render('Get New Ball',False,(255,255,255)),(60-font.render('Get New Ball',False,(255,255,255)).get_width()/2,35-font.render('Get New Ball',False,(255,255,255)).get_height()/2))
  for event in pg.event.get():
    if event.type==pg.QUIT:
      pg.quit()
    if event.type==pg.MOUSEMOTION:
      mouserectpos=event.pos
    if event.type==pg.MOUSEBUTTONDOWN:
      if event.button==1:
        if mouserect.colliderect(circle):
          mouseHeld=True
        if mouserect.colliderect(buttonRect):
          previouscx=100
          previouxcy=300
          cx=100
          cy=300
          accel=0
          xAccel=0
       
    if event.type==pg.MOUSEBUTTONUP:
      if event.button==1:
        mouseHeld=False
  circle=pg.draw.circle(gameDisplay,(0,color1,color2),(cx,cy),20)
  mouserect=pg.Rect(mouserectpos,(10,10))
  cx+=xAccel

  if cx>800:
    cx=800
  if cx<0:
    cx=0
 
  if circle.colliderect(wallRect) and xAccel>0:
    xAccel=xAccel*-1
  if circle.colliderect(wallRect2) and xAccel<0:
    xAccel=xAccel*-1
 
  if cy+10>490:
    cy=490-10
  if mouseHeld:
    cx=mouserectpos[0]
    cy=mouserectpos[1]
    accel=0
  if not mouseHeld and not circle.colliderect(floorRect):
    cy+=accel
    accel+=1
  if circle.colliderect(floorRect):
    if accel>8:
      accel=accel*-1
    else:
      if not mouseHeld:
        cy=481
    print(accel)
    cy-=10
  if accel<0:
    accel+=2
  clock.tick(40)
  if not (circle.colliderect(wallRect) or circle.colliderect(wallRect2)):
    xAccel=cx-previouscx
  if xAccel>0 and ctr%5==0:
    xAccel-=1
  if xAccel<0 and ctr%5==0:
    xAccel+=1
   
  pg.display.update()
