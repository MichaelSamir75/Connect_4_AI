from check_box import Checkbox
import pygame as pg
import PygameUtils as pu

def main():
    WIDTH = 800
    HEIGHT = 600
    display = pg.display.set_mode((WIDTH, HEIGHT))

    chkbox = Checkbox(display, 400, 400)
    checkb = pu.checkbox((200,200,200), 400, 400, 100, 100)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                quit()
            chkbox.update_checkbox(event)
            checkb.check(event)

        display.fill((200, 200, 200))
        chkbox.render_checkbox()
        checkb.draw()
        print(chkbox.is_checked())
        pg.display.flip()

if __name__ == '__main__': main()