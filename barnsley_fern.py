from tkinter import Tk, Canvas
import random
from typing import   List, NamedTuple, Tuple, Iterator, TypeVar

'''
برنامه زیر پترن برنزلی را رسم می کند. برای اینکه زمان اجرا کم شود
ابتدا نقاط تک تک رسم میشوند ولی به تدریج تعداد نقاط رسم شده در هر 
سیکل افزایش می یابد. با تصاعد10% .برای اینکه بتوان چندین نقطه همزمان
رسم شود کلاس مای کانواس  از روی کانواس ساخته شد تا متد مس اوال که 
قابلیت رسم چند نقطه همزمان را دارد تعریف گردد.
'''
NUMBER_OF_POINT = 300000

T = TypeVar('T')

class Point(NamedTuple):
    x: float 
    y: float

class MyCanvas(Canvas):
    
    def __init__(self,*arg,**kwa) -> None:
        super().__init__(*arg,**kwa)
    def mass_oval(self,point_list:List[Tuple[float,float]],fill: str)->None:
        '''
        this method draw list of point on canvas
        '''
        for point in point_list:
            self.create_oval(point.x,point.y,point.x+1,point.y+1,fill = fill)    


def barnsly(x_start: int, y_start:int)->Iterator[Tuple[float,float]]:
    '''
    this generator calculate point cordination base on barnsly equation
    and yeild as a Point tuple
    x_start and y_start are start cordination on canvas
    '''
    
    point = Point(0,0)
    
    while True:
        r = random.random()  
        r = r * 100
        xn = point.x
        yn = point.y
        if r < 1:  
            point = Point(0,0.16 * yn)
        elif r < 86:
            point = Point(0.85 * xn + 0.04 * yn,
                          -0.04 * xn + 0.85 * yn + 1.6)
        elif r < 93:
            point = Point(0.20 * xn - 0.26 * yn,
                          0.23 * xn + 0.22 * yn + 1.6)
        else:
            point = Point(-0.15 * xn + 0.28 * yn,
                           0.26 * xn + 0.24 * yn + 0.44)

        regulate_point = Point(65*point.x+x_start,
                               37*point.y+y_start)
       
        yield regulate_point

def get_item(generator:Iterator[T], number_of_item: int)->List[T]:
    '''
    return n item from generator
    '''
    l:List[T] = []
    for _ in range(number_of_item):
        l.append(next(generator))
    return l

master = Tk()
w = MyCanvas(master,width = 600, height = 600)
w.pack()
point = barnsly(300,100) 

i = 0 
def show():
    global i

    if i < NUMBER_OF_POINT:
        number_of_point = int(i/10)+1 #define number of point that pass to oval
        points = get_item(point,number_of_point)
        w.mass_oval(points,fill = 'GREEN')
        w.after(1,show)
        i +=number_of_point
        
    else:
        pass

show()
master.mainloop()

