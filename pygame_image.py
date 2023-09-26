import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    cg_img = pg.image.load("ex01/fig/3.png")
    cg_img = pg.transform.flip(cg_img,True,False)
    cg_img2 = pg.transform.rotozoom(cg_img,10,1.0)
    cg_imgs = [cg_img,cg_img2]
    tmr = 0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = tmr
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img,[1600-x,0])
        screen.blit(cg_imgs[tmr%2],[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()