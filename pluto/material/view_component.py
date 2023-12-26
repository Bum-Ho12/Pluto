'''
file that defines the View UI basic component
'''
import skia

class View():
    '''class defines the View component of the basic UI framework'''
    def __init__(self, children=None,style =None) -> None:
        '''initialize'''
        self.children = children or []
        self.style = style or{}

    def __call__(self,canvas,x,y):
        #pylint: disable = I1101
        '''renders View'''
        background_color = self.style.get('background_color',0xFFFFFFFF)
        margin = self.style.get('margin',0)
        padding = self.style.get('padding',0)

        #Drawing background
        paint = skia.Paint()
        paint.color = background_color
        canvas.drawRect(skia.Rect(x,y,x+100,y+ 50),paint)

        # applying padding and margin
        x+= padding
        y += padding

        for child in self.children:
            child.render(canvas,x+margin,y+margin)
