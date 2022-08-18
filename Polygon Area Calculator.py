class Rectangle():
  width = int()
  height = int()
  rectangle_string = str()

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
    
  def set_width(self, width):
    self.width = width
    
  def set_height(self, height):
    self.height = height
    
  def get_area(self):
    return self.width*self.height
    
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
    
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
    
  def get_picture(self):
    n_lines = self.height
    n_star = '*'*self.width
    display_picture = ''
    
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      for i in range(0, n_lines):
        display_picture += n_star + "\n"
      return display_picture
    
  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area()) # Credit to https://www.youtube.com/watch?v=sMVCsctweh4 for this line. Better than my while loop for subtracting area till 0


class Square(Rectangle):
  def __init__(self, side_length):
    self.width = side_length
    self.height = side_length

  def __str__(self):
    return f'Square(side={self.width})'

  def set_side(self, side):
    #self.side = side
    self.width = side
    self.height = side
