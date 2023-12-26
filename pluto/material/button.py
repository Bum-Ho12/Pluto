'''file defines a button for the UI component framework'''
import skia

class Button:
    '''class that defines the button click component'''
    def __init__(self,text,on_click=None,style=None):
        self.text = text
        self.on_click = on_click
        self.style = style or {}

    def __call__(self, canvas,x,y):
        #pylint: disable = I1101
        paint = skia.Paint()
        paint.color = self.style.get('background',0xFFFFFFFF)
        canvas.drawRect(skia.Rect(x,y,x+100,y+50),paint)

        text_paint = skia.Paint()
        text_paint.color = self.style.get('text_color',0xFFFFFFFF)
        text_paint.text_size = self.style('text_size',16)

        canvas.drawerText(self.text,x+ self.style.get('padding',0), y+3,text_paint)
