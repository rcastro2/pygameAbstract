import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

def is_point_inside_rotated_rectangle(vertices, point):
  """
  This function checks if a point lies inside a rotated rectangle using the area method.

  Args:
      vertices: A list of four tuples representing the rectangle vertices in clockwise order.
      point: A tuple representing the point to be checked.

  Returns:
      True if the point is inside the rectangle, False otherwise.
  """

  # Calculate rectangle area (assuming we know width and height from vertices)
  width = max(vertex[0] for vertex in vertices) - min(vertex[0] for vertex in vertices)
  height = max(vertex[1] for vertex in vertices) - min(vertex[1] for vertex in vertices)
  rectangle_area = width * height

  # Calculate sum of triangle areas
  total_triangle_area = 0
  for i in range(len(vertices)):
    next_i = (i + 1) % len(vertices)
    current_vertex = vertices[i]
    next_vertex = vertices[next_i]
    triangle_area = 0.5 * abs((point[0] * next_vertex[1] + current_vertex[0] * point[1] + next_vertex[0] * current_vertex[1]) - (point[1] * next_vertex[0] + current_vertex[1] * point[0] + next_vertex[1] * current_vertex[0]))
    total_triangle_area += triangle_area

  # Check if point is inside based on area comparison
  return total_triangle_area <= rectangle_area

def is_inside_rotated_rectangle_aabb(vertices, point):
  """
  Checks if a point is inside a rotated rectangle using AABB and transformation 
  (handles general rotation).

  Args:
      vertices: List of tuples representing the four vertices of the rotated rectangle in clockwise or counter-clockwise order.
      point: Tuple representing the point to check.

  Returns:
      True if the point is inside the rotated rectangle, False otherwise.
  """
  min_x = min(vertex[0] for vertex in vertices)
  max_x = max(vertex[0] for vertex in vertices)
  min_y = min(vertex[1] for vertex in vertices)
  max_y = max(vertex[1] for vertex in vertices)

  # Check if point is outside AABB
  if point[0] < min_x or point[0] > max_x or point[1] < min_y or point[1] > max_y:
    return False

  # Calculate minimum enclosing rectangle (not necessarily axis-aligned)
  top_left = (min_x, min_y)
  bottom_right = (max_x, max_y)

  # Check if transformed point is inside minimum enclosing rectangle
  for vertex in vertices:
    top_left = (min(top_left[0], vertex[0]), min(top_left[1], vertex[1]))
    bottom_right = (max(bottom_right[0], vertex[0]), max(bottom_right[1], vertex[1]))

  width = bottom_right[0] - top_left[0]
  height = bottom_right[1] - top_left[1]
  return 0 <= point[0] - top_left[0] <= width and 0 <= point[1] - top_left[1] <= height

def is_inside_rotated_rectangle_triangles(vertices, point):
  """
  Checks if a point is inside a rotated rectangle using area of triangles.

  Args:
      vertices: List of tuples representing the four vertices of the rotated rectangle in clockwise or counter-clockwise order.
      point: Tuple representing the point to check.

  Returns:
      True if the point is inside the rotated rectangle, False otherwise.
  """
  def shoelace_formula(p1, p2):
    return (p1[0] * p2[1]) - (p1[1] * p2[0])

  total_area = 0
  for i in range(len(vertices)):
    next_i = (i + 1) % len(vertices)
    triangle_area = shoelace_formula(vertices[i], (point[0], point[1])) + shoelace_formula((point[0], point[1]), vertices[next_i])
    total_area += triangle_area

  # Check sign of total area based on winding order (assuming clockwise)
  return total_area > 0

def is_inside_rotated_rectangle_projection(vertices, point):
  """
  Checks if a point is inside a rotated rectangle using line segment projections.

  Args:
      vertices: List of tuples representing the four vertices of the rotated rectangle in clockwise or counter-clockwise order.
      point: Tuple representing the point to check.

  Returns:
      True if the point is inside the rotated rectangle, False otherwise.
  """
  def is_left(p0, p1, p2):
    # Check if point p2 is on the left side of the line segment formed by p0 and p1
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p1[1] - p0[1]) * (p2[0] - p0[0]) > 0

  for i in range(len(vertices)):
    next_i = (i + 1) % len(vertices)
    # Check if point is on the left side of all line segments formed by rectangle vertices
    if not is_left(vertices[i], vertices[next_i], point):
      return False

  return True


methods = [is_point_inside_rotated_rectangle, is_inside_rotated_rectangle_aabb, is_inside_rotated_rectangle_triangles, is_inside_rotated_rectangle_projection ]
game = Game(1600,900,"SAT Collision Dectecion")


rectangle1 = Shape("rectangle",game,30,300,blue)
rectangle1.moveTo(400,400)
print(rectangle1.points)

rectangle2 = Shape("rectangle",game,50,50,gray)
rectangle2.moveTo(500,500)

colors = [red,green,magenta,cyan]
def checkCollision():

    
    for i1 in range(len(rectangle1.points)):
        p1 = rectangle1.points[i1]
        pygame.draw.circle(game.screen,colors[i1],(p1[0],p1[1]),5)
        for i2 in range(len(rectangle2.points)):
            p2 = rectangle2.points[i2]
            pygame.draw.circle(game.screen,red,(p2[0],p2[1]),5)
            #is_point_inside_rotated_rectangle(vertices, point)

            if methods[0](rectangle1.points, p2):
                game.drawText("Hit",30,30, Font(red))
                return True
            else:
                game.drawText("Hit",30,30, Font(green))
            #print(p2)
            #break

while not game.over:
    game.processInput()
    game.clearBackground(white)

    rectangle1.draw()
    rectangle1.rotateBy(1)

    rectangle2.draw()
    checkCollision()
            
    game.update(30)
game.quit()
