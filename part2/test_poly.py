
import math
from proj1 import Polygon, Polygons

def test_polygon():

    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                        'Exception expected, not received')
    except ValueError:
        pass 



    n = 3
    R = 1
    p = Polygon(n, R)

    assert str(p) == f"Polygon(n=3, R=1)", f'actual: {str(p)}'
    assert p.number_vertices == n, (f'actual: {p.number_vertices},'
                                    f'expected: {n}')
    assert p.circumradius == R, (f'actual: {p.circumradius}')

    assert p.interior_angle == 60

    rel_tol = 0.001
    abs_tol = 0.001

    n = 4
    R = 1
    p = Polygon(n, R)
    assert math.isclose(p.interior_angle, 90)
    assert math.isclose(p.area, 2.0, rel_tol=rel_tol, abs_tol=abs_tol), (f'actual: {p.area}, '
                                                                            f'expected: {2.0}')

    
    assert math.isclose(p.side_length, math.sqrt(2),
                            rel_tol=rel_tol, abs_tol=abs_tol)

    assert math.isclose(p.perimeter, 4*math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 0.707,
                            rel_tol=rel_tol, abs_tol=abs_tol)

    n = 6
    R = 2
    p = Polygon(n, R)
    assert math.isclose(p.interior_angle, 120)

    assert math.isclose(p.area, 10.3923, rel_tol=rel_tol, abs_tol=abs_tol), (f'actual: {p.area}, '
                                                                            f'expected: {10.3923}')

    
    assert math.isclose(p.side_length, 2,
                            rel_tol=rel_tol, abs_tol=abs_tol)

    assert math.isclose(p.perimeter, 12, rel_tol=rel_tol, abs_tol=abs_tol)

    assert math.isclose(p.apothem, 1.73205,
                            rel_tol=rel_tol, abs_tol=abs_tol)


    n = 12
    R = 3
    p = Polygon(n, R)
    assert math.isclose(p.interior_angle, 150)

    assert math.isclose(p.area, 27, rel_tol=rel_tol, abs_tol=abs_tol), (f'actual: {p.area}, '
                                                                            f'expected: {27.0}')

    
    assert math.isclose(p.side_length, 1.55291,
                            rel_tol=rel_tol, abs_tol=abs_tol)

    assert math.isclose(p.perimeter, 18.635, rel_tol=rel_tol, abs_tol=abs_tol)

    assert math.isclose(p.apothem, 2.89778,
                            rel_tol=rel_tol, abs_tol=abs_tol)
    
    
    p1  = Polygon(3, 10)
    p2  = Polygon(10, 10)
    p3  = Polygon(15, 10)
    p4  = Polygon(15, 100)
    p5  = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3 
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

    p = Polygon(9, 10)
    p.number_vertices = 3


    ##############Testing Polygon sequences ###########
    polygons = Polygons(8, 1)
    #print(polygons)#calls the __repr__ function
    #print(len(polygons))

    for p in polygons:
        #print(p)
        pass 

    for p in polygons[2:5]:
        #print(p)
        pass 
    for p in polygons[::-1]:
        #print(p)
        pass 

    polygons = Polygons(10, 1)
    #print(polygons.max_efficiency_polygon)

    #print([(p, p.area/p.perimeter) for p in polygons])
    #[print((p, p.area/p.perimeter)) for p in polygons]

    polygons = Polygons(500, 1)
    p = polygons.max_efficiency_polygon
    print(p.area)

    assert math.isclose(p.area, math.pi, rel_tol=rel_tol, abs_tol=abs_tol)




    



test_polygon()