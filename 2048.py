from random import randint

class My_2048(object):

  def __init__(self):
    self.view_contant = ['    ', '    ', '    ', '    ', ]
    self.sort_list = ['', '', '', '']

  def get_view_str(self):
    view_str = ''
    for i in self.view_contant:
      view_str += i
    return view_str



  def popup_post_char(self, post, popup_char):
    curr_post = 0
    for i in xrange(len(self.view_contant)):
      for j in xrange(len(self.view_contant[0])):
        if ' ' == self.view_contant[i][j]:
          if curr_post == post:
            self.view_contant[i] = self.view_contant[i][:j] + popup_char + self.view_contant[i][j + 1:]
            return
          curr_post += 1

  def do_popup_single(self, blank_count):
    post = randint(0, blank_count - 1)
    popup_char = ['a', 'b'][randint(0, 1)]
    self.popup_post_char(post, popup_char)
    pass

  def do_popup_twice(self, blank_count):
    post = randint(0, blank_count - 1)
    post_2 = post
    while post == post_2:
      post_2 = randint(0, blank_count - 1)
    popup_char = ['a', 'b'][randint(0, 1)]
    popup_char_2 = ['a', 'b'][randint(0, 1)]
    self.popup_post_char(post, popup_char)
    self.popup_post_char(post_2, popup_char_2)


    pass

  def get_blank_count(self):
    view_str = self.get_view_str()
    print view_str
    view_str_list = list(view_str)
    view_str_list.sort()

    for i in xrange(len(view_str_list)):
      if not ' ' == view_str_list[i]:
        return i
    return 16

  def do_popup(self):
    blank_count = self.get_blank_count()
    if blank_count > 8 and 0 == randint(0, 1):
      self.do_popup_twice(blank_count)
    elif blank_count > 0:
      self.do_popup_single(blank_count)


  def do_sort_line(self, l):
    
    result = False

    no_blank_line = ''
    for i in self.sort_list[l]:
      if not ' ' == i:
        no_blank_line += i
    if not no_blank_line == self.sort_list[l][:len(no_blank_line)]:
      self.sort_list[l] = no_blank_line + '   '[len(no_blank_line) - 1:]
      result = True

    for i in xrange(len(self.sort_list[l]) - 1):
      curr_char = self.sort_list[l][i]
      if not ' ' == curr_char and curr_char == self.sort_list[l][i + 1]:
        print 'plus**'
        self.sort_list[l] = self.sort_list[l][0:i] + chr(ord(curr_char) + 1) + ' ' + self.sort_list[l][i + 2:]
        result = False

    no_blank_line = ''
    for i in self.sort_list[l]:
      if not ' ' == i:
        no_blank_line += i
    if not no_blank_line == self.sort_list[l][:len(no_blank_line)]:
      self.sort_list[l] = no_blank_line + '   '[len(no_blank_line) - 1:]
      result = True


    return result

  def do_sort_list(self):
    go_on_sort = False
    for i in xrange(len(self.sort_list)):
      go_on_sort = self.do_sort_line(i)
    if go_on_sort:
      self.do_sort_list()

  def do_slide_up(self):
    self.sort_list = ['', '', '', '']
    for i in xrange(len(self.view_contant)):
      for j in xrange(len(self.view_contant[0])):
        self.sort_list[i] += self.view_contant[j][i]
    self.do_sort_list()
    for i in xrange(len(self.view_contant)):
      for j in xrange(len(self.view_contant[0])):
        self.view_contant[j] = self.view_contant[j][:i] + self.sort_list[i][j] + self.view_contant[j][i + 1:]


  def do_slide_down(self):
    self.sort_list = ['', '', '', '']
    for i in xrange(len(self.view_contant)):
      for j in xrange(len(self.view_contant[0])):
        self.sort_list[i] += self.view_contant[len(self.view_contant[0]) - 1 - j][i]
    self.do_sort_list()
    for i in xrange(len(self.view_contant)):
      for j in xrange(len(self.view_contant[0])):
        self.view_contant[j] = self.view_contant[j][:i] + self.sort_list[i][len(self.view_contant[0]) - 1 - j] + self.view_contant[j][i + 1:]

  def do_slide_left(self):
    self.sort_list = ['', '', '', '']
    for i in xrange(len(self.view_contant)):
      self.sort_list[i] = self.view_contant[i]
    self.do_sort_list()
    for i in xrange(len(self.view_contant)):
      self.view_contant[i] = self.sort_list[i]

  def do_slide_right(self):
    self.sort_list = ['', '', '', '']
    for i in xrange(len(self.view_contant)):
      for j in xrange(len(self.view_contant[0])):
        self.sort_list[i] += self.view_contant[i][len(self.view_contant[0]) - 1 - j]
    self.do_sort_list()
    for i in xrange(len(self.view_contant)):
      for j in xrange(len(self.view_contant[0])):
        self.view_contant[i] = self.view_contant[i][:j] + self.sort_list[i][len(self.view_contant[0]) - 1 - j] + self.view_contant[i][j + 1:]
    pass

  def do_slide(self, slide):

    curr_view = [i for i in self.view_contant]
    if 'i' == slide:
      self.do_slide_up()
    elif 'k' == slide:
      self.do_slide_down()
    elif 'j' == slide:
      self.do_slide_left()
    elif 'l' == slide:
      self.do_slide_right()
    the_same = True
    for i in xrange(len(curr_view)):
      if not curr_view[i] == self.view_contant[i]:
        the_same = False
    if not the_same:
      self.do_popup()
    self.do_dump()

  def do_dump(self):
    self.dump()
    pass

  def dump(self):
    view = ('''
      +---+---+---+---+
      | 1 | 1 | 1 | 1 |
      +---+---+---+---+
      | 1 | 1 | 1 | 1 |
      +---+---+---+---+
      | 1 | 1 | 1 | 1 |
      +---+---+---+---+
      | 1 | 1 | 1 | 1 |
      +---+---+---+---+

      ''')

    post_list = [33, 37, 41, 45, 81, 85, 89, 93, 129, 133, 137, 141, 177, 181, 185, 189]
    if 16 == self.get_blank_count():
      self.do_popup_twice(16)
    view_str = self.get_view_str()
    for i in xrange(len(post_list)):
      view = view[:post_list[i]] + view_str[i] + view[post_list[i] + 1:]



    print view

    print 'blank: ' + str(self.get_blank_count())

    valid_input = False
    while(not valid_input):
      slide = raw_input()
      if slide in 'ikjl':
        valid_input = True

    self.do_slide(slide)


def main():
  a = My_2048();
  a.dump()
  pass

if __name__ == '__main__':
   main() 