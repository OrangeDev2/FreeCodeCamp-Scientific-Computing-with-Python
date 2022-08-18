class Rectangle:
  width = int()
  height = int()
  rectangle_string = str()

  def __init__(self, width, height):
    self.width = width
    self.height = height
    
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
    
    self.rectangle_string = f'Rectangle(width={self.width}, height={self.height})\n'
    
    if self.width > 50 or self.height > 50:
      return self.rectangle_string + "Too big for picture."
    else:
      for i in range(0, n_lines):
        display_picture += n_star + "\n"
      return self.rectangle_string + display_picture
    
  def get_amount_inside(self, shape):
    #if shape == 'rectangle':
    #  if self.width > self.height:
    return None



class Square:
  def __init__(self, side_length):
    print('')

  def set_side(self, side)
    self.side = side
