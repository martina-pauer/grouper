from polygon import Polygon

class PolygonalImage:
    def __init__(self):
        '''
            Get Polygons from 2D
            image.
        '''
        self.polygons: int = 1
        self.positions: list[tuple[int]] = [(0, 0)]
        
    def search_polygons(self, absolute_image_path: str):
        width_px = 0
        height_px = 0
        with open(absolute_image_path, 'rb') as image:
            for height in image.readlines():
                height_px += 1
                for width in height.__str__():
                    width_px += 1
                    # Search polygon
                    self.polygons += 1
                    # Add position
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