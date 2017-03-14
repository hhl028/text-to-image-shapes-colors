import numpy as np
import cairo
import random
import math

image_path = 'shapes/images'
text_path = 'shapes/texts'

WIDTH = 64
HEIGHT = 64

colors = {
    'red': (1.0, 0.0, 0.0),
    'green': (0.0, 1.0, 0.0),
    'blue': (0.0, 0.0, 1.0),
    'yellow': (1.0, 1.0, 0.0),
    'orange': (1.0, 0.66, 0.0),
    'purple': (0.5, 0.0, 0.5),
    'black': (0.0, 0.0, 0.0),
    'white': (1.0, 1.0, 1.0)
}
colors_list = colors.items()

shapes = ['square', 'circle', 'triangle']

SQUARE_SIZE = 25
CIRCLE_RADIUS = 15
TRIANGLE_SIZE = 30

"""
formatting for text descriptions
0 - shape color
1 - background color
2 - shape
"""
desc_fmts = [
    "{0} {2} on a {1} background",
    "a {0} {2} on a {1} background",
    "a {2} colored {0} on a {1} background",
    "{2} that is {0} on a {1} background",
    "{2} that is colored {0} on a {1} background",
    "there is a {0} {2} on a {1} background",
    "there is a {2} colored {0} on a {1} background",
    "there is a {2} colored {0} on a background colored {1}",
    "the shape is a {2} colored {0} on a {1} background",
    "this {0} {2} is on a background that is {1}",
    "this {0} {2} is on a background colored {1}",
    "this {0} {2} is on a {1} background",
    "this {2} is {0} and the background is {1}",
    "this {2} is {0} on a {1} background",
    "this {2} is {0} and the background is colored {1}",
    "this {2} is colored {0} on a {1} background",
    "this {2} is colored {0} and the background is {1}",
    "this {2} is colored {0} and the background is colored {1}",
    "this {2} is colored {0} and there is a {1} background",
    "a {1} background with a {0} {2}",
    "a {1} background with a {2} that is {0}",
    "a {1} background with a {2} colored {0}",
    "a {1} background with a {2} that is colored {0}",
    "there is a {1} background with a {0} {2}",
    "there is a {1} background with a {2} that is {0}",
    "there is a {1} background with a {2} colored {0}",
    "there is a {1} background with a {2} that is colored {0}",
    "{1} background with a {0} {2}",
    "{1} background with a {2} that is {0}",
    "{1} background with a {2} that is {0}",
    "the background is {1} and the shape is a {0} {2}",
    "the background is {1} and the shape is a {2} colored {0}",
    "the background is colored {1} and the shape is a {0} {2}",
    "the background is colored {1} and the shape is a {2} colored {0}",
    "this background is {1} and the shape is a {0} {2}",
    "this background is {1} and the shape is a {2} colored {0}",
    "this background is colored {1} and the shape is a {0} {2}",
    "this background is colored {1} and the shape is a {2} colored {0}"
]


def main():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    for i in range(100):
        shape_col, shape_rgb, bg_col, bg_rgb = select_colors()
        #print(shape_col, shape_rgb, bg_col, bg_rgb)

        # draw background
        ctx.set_source_rgb(*bg_rgb)
        ctx.paint()

        # draw shape
        ctx.set_source_rgb(*shape_rgb)
        shape = draw_shape(ctx)

        file_name = '{:05d}'.format(i)
        
        surface.write_to_png('{}/{}.png'.format(image_path, file_name))

        # generate text descriptions
        gen_descriptions(file_name, shape_col, bg_col, shape)

        

        


# Returns color, rgb, color, rgb
def select_colors():
    cols = random.sample(colors_list, 2)
    return cols[0][0], cols[0][1], cols[1][0], cols[1][1]
        

# Returns string of shape
def draw_shape(ctx):
    # calculate offset
    x_offset = np.random.normal(scale=5.0)
    y_offset = np.random.normal(scale=5.0)

    # center + offset
    ctr_x = WIDTH / 2 + x_offset
    ctr_y = HEIGHT / 2 + y_offset

    # select a shape
    shape = random.choice(shapes)

    if shape == 'square':
        pos_x = ctr_x - SQUARE_SIZE / 2
        pos_y = ctr_y - SQUARE_SIZE / 2
        ctx.rectangle(pos_x, pos_y, SQUARE_SIZE, SQUARE_SIZE)
        ctx.fill()
    elif shape == 'circle':
        ctx.arc(ctr_x, ctr_y, CIRCLE_RADIUS, 0, 2*math.pi)
        ctx.fill()
    elif shape == 'triangle':
        h = TRIANGLE_SIZE / 2 * math.sqrt(3)
        ctx.move_to(ctr_x, ctr_y-h/2)
        ctx.line_to(ctr_x+TRIANGLE_SIZE/2, ctr_y+h/2)
        ctx.line_to(ctr_x-TRIANGLE_SIZE/2, ctr_y+h/2)
        ctx.fill()

    return shape

# Generates 10 text descriptions and writes them to a file
def gen_descriptions(file_name, shape_col, bg_color, shape):
    file_path = '{}/{}.txt'.format(text_path, file_name)
    with open(file_path, 'w+') as f:
        fmts = random.sample(desc_fmts, 10)
        for fmt in fmts:
            f.write('{}\n'.format(fmt.format(shape_col, bg_color, shape)))


if __name__ == '__main__':
    main()
