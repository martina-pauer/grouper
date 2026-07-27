from polygon import Polygon

class PolygonalImage:
    def __init__(self):
        '''
            Get Polygons from 2D
            image.
        '''
        self.polygons: int = 1
        self.positions: list[tuple[int]] = []
        
    def search_polygons(self, absolute_image_path: str):
        width_px: int = 0
        height_px: int = 0
        darkest_color: list[int] = []
        lighter_color: list[int] = []
        # Iterates over image pixels color with pillow help
        from PIL import Image
        colors = Image.open(absolute_image_path).convert('RGB')
        with open(absolute_image_path, 'rb') as image:
            for height in image.readlines():
                height_px += 1
                for width in height.replace('\n', '').__str__():
                    width_px += 1
                    # Search polygon
                    if ((width_px == 1) and (height_px == 1)):
                        darkest_color = list(colors.getpixel(width_px, height_px))
                        lighter_color = darkest_color
                    else:
                        state: bool = True
                        # Compare block to block each color aproximating to the objectives
                        for color in darkest_color:
                            state = (state and (int(color) < list(colors.getpixel(width_px, height_px))[darkest_color.index(color)]))
                        state = True
                        for color in lighter_color:
                            state = (state and (int(color) > list(colors.getpixel(width_px, height_px))[lighter_color.index(color)]))    
                        # Add position When color is Lighter
                        if state:
                            self.polygons += 1
                            self.positions.append((width_px, height_px))
    
    def get_polygons(self) -> list[Polygon]:
        '''
            From each position create
            equivalents polygons for image.
        '''
        import time
        # Give Consistent Name
        file_name: str = {time.strftime("%s")}
        del time
        # Use Saved Memory In The Loop
        for polygon in self.positions:
            graphics = Polygon()
            # Calc each Polygon Aspect To Determine Shape
            graphics.edges = abs(polygon[1] - polygon[0])
            graphics.vertices = (polygon[1] // polygon[0])
            graphics.faces = (graphics.vertices // graphics.edges)
            # Add polygon To The End
            graphics.draw(f'{file_name}')