class Polygon:
    def __init__(self):
        '''
            Define a polygon in 3D
            printing .3mf file
        '''
        # 2D Triangles By Defaut
        self.edges: int = 3
        self.vertices: int = 3
        self.faces: int = 1
        # How Much Pixels Has Each Edge
        self.size: int = 32
        
    def draw(self, file_name):
        '''
            Generate .3mf file adding
            only the polygon to the
            end of file.
        '''
        # Give Name   
        with open(f'model_from_image_{file_name}', 'wb') as model:
            for vertex in range(0, self.vertices):
                # Write byte to Add Vertex
                model.write(b'15')
                for faces in range(0, self.faces):
                    # Write byte to Add Face
                    model.write(b'3')
                for edge in range(0, self.edges):
                    # Write byte to Add Edge
                    model.write(b'4')