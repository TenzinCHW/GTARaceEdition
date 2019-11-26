def parse_obj(fname):
    with open(fname) as f:
        obj_data = f.readlines()
        objects = []
        vertices = []
        for line in obj_data:
            line = line.strip().split(' ')
            dtype, data = line[0], line[1:]
            if dtype == 'o':
                try:
                    objects.append((obj_name, obj_faces))
                except:
                    pass
                obj_name = data
                obj_faces = []
            elif dtype == 'v':
                vertex = parse_vertex(data)
                vertices.append(vertex)
            elif dtype == 'f':
                face = parse_face(data, vertices)
                obj_faces.extend(face)
        return objects

    #t = line[0]
    #data = line.split.(' ')[1:]
    #if t == 'v':
    #    return parse_vertex(data)
    #elif t == 'f':
def parse_vertex(vertex_string_list):
    '''Parses a line of a vertex from an obj file and returns it as a 3-tuple of floats
    e.g. vertex_string_list = ['0.020355', '1.25034', '0.42563']
    output (0.020355, 1.25034, 0.42563)'''
    return tuple(float(p) for p in vertex_string_list)

def parse_face(face_string_list, vertices):
    '''Parses a line of a face from an obj file using the list of vertices (list of 3-tuples of floats)
    e.g. face_string_list = ['2//', '1//', '4//', '3//']
    output list of triangles (3-tuples of 3-tuples of floats)'''
    points = [int(pt.split('/')[0]) - 1 for pt in face_string_list] # Each point is somethng like '2//' so we want 1 as int (2 is indexed from 1)
    triangles = [tuple(vertices[points[i]] for i in range(3))] # Take first 3 points
    # Take the ith, (i+2)-th and (i+3)-th point as a triangle (triangle strip)
    # i.e. skip every 2nd, stop when (i+3) == len(points) - 1 i.e. last point
    for i in range(len(points) - 3):
        pi = points[i]
        pi2 = points[i+2]
        pi3 = points[i+3]
        triangle = vertices[pi], vertices[pi2], vertices[pi3]
        triangles.append(triangle)
    return triangles

def skip():
    pass

if __name__ == '__main__':
    outp = parse_obj('testdata.obj')
    print(outp)
