#################################
#  PROJECT EULER - PROBLEM 174  #
#################################
import time
# Let rects[(w, h)] denote the number of rectangles we can find inside a
# cross-hatched grid of dimensions w (width) and h (height). Note first of all
# that, by symmetry, rects[(w, h)] = rects[(h, w)], hence we can assume that w
# >= h. The idea of the solution below is to proceed by induction. More
# precisely, to compute rects[(w, h)] with w >= h, consider separately those
# rectangles which intersect the first 1 x h column and those that do not. The
# latter can be seen as rectangles in a (w - 1) x h grid, the number of
# which we assume has already been computed. So it remains only to compute the
# former. The number of non-diagonal rectangles, i.e., whose sides are parallel
# to the x- and y-axes and which intersect the first column is easily computed:
# any such rectangle is determined by a choice of two distinct vertices among h
# possibilities along the left edge, together with its width, which can be any
# number between 1 and w. Thus, the number of such rectangles is:
# (1) (h + 1) * h * w // 2
# Now consider the diagonal rectangles. They are of two types: those that have
# a vertex on the left edge of the grid, and those that have a vertex between
# the left edge (x = 0) and the leftmost inner vertical edge (x = 1). In either
# case, the rectangle is determined by a choice of such a vertex together with
# its two dimensions. However, we need to take care that our choice of
# dimensions will not cause the rectangle to run "out of bounds" with respect
# to the grid.

# Consider first a rectangle having a vertex along the left vertical edge of
# the grid. There are (h + 1) possible vertices, given by their y-coordinates k
# which can vary between 0 and h. For each such vertex, we have 2 * (h - k)
# possibilities for the dimension parallel to the line y = x (before we
# reach the top edge) and 2 * k possibilities for the dimension parallel to the
# line y = -x (before we reach the bottom edge); no matter which of these
# choices we take, we will never trespass the right edge since w >= h by
# hypothesis. Thus all of them are valid, and we have a total of
# (2) Sum_{1<= k <= h - 1} k * (h -k)
# rectangles of this type.  Moreover, the value of this sum is easily computed
# explicitly using the formula for the sum of the first (h - 1) square numbers.

# Now consider a rectangle having a vertex of coordinate (1/2, -1/2 + k) for
# some k between 1 and h. Again we need to choose its dimensions carefully so
# as not to run out of bounds. For the dimension parallel to the line y = x we
# now have 2 * (h - k) + 1 possibilities before reaching the top edge, and for
# the dimension parallel to y = -x we have 2 * k - 1 choices before reaching
# the bottom edge. However, if try to pick the maximum dimension in both cases
# _and if w == h_, then we will go past the right edge by 1/2, so we need to
# (3') Sum_{1 <= k <= h} (2 * k - 1) * [2 * (h - k) + 1] - 1        (if w == h)
# rectangles of this type. Finally, notice that we can also compute these sums
# explicitly using the well-known formula for the sum of the first h square
# numbers. The program below is a straightforward implementation of these
# formulas.


start = time.time()

MAX_HEIGHT = 43
MAX_WIDTH = 47

rects = {}
# rects[(width, height)] stores the number of rectangles in a grid
# of dimensions width x height.

# By symmetry, it suffices to consider the case where w >= h.
for h in range(1, MAX_HEIGHT + 1):
    for w in range(h, MAX_WIDTH + 1):
        if h == 1 and w == 1:
            rects[(w, h)] = 1
        elif h == 1:
            # In this case there will be no diagonal rectangles.
            rects[(w, h)] = rects[(w - 1, h)] + w + 1
            rects[(h, w)] = rects[(w, h)]
        elif w == h:
            # The formulas here come from equations (1), (2) and (3') above,
            # where (2) + (3') has already been simplified using pen and paper.
            rects[(w, h)] = rects[(w - 1, h)] \
                    + (h + 1) * h * w // 2 \
                    + 4 * h**2 * (h - 1) \
                    - 4 * h * (h - 1) * (2 * h - 1) // 3
        elif w > h:
            # The formulas here come from equations (1), (2) and (3) above,
            # where (2) + (3) has already been simplified using pen and paper.
            rects[(w, h)] = rects[(w - 1, h)] \
                    + (h + 1) * h * w // 2 \
                    + 4 * h**2 * (h - 1) \
                    - 4 * h * (h - 1) * (2 * h - 1) // 3 \
                    + h
            rects[(h, w)] = rects[(w, h)]


# Now we just sum the number of rectangles over all possible dimensions.
answer = 0
for height in range(1, MAX_HEIGHT + 1):
    for width in range(1, MAX_WIDTH + 1):
        answer += rects[(width, height)]
print(answer)
end = time.time()
print(f"Program runtime: {end - start} seconds")
