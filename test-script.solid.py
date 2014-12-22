
figure          = (
    (
      (
      Cylinder(r=5, h=20, center=1)
      + Cube(10, 10, 20, center=1).rotate(0, 90, 0)
      )
    - Cylinder(r=3, h=20, center=1).rotate(90, 0, 0).resize(10, 0, 0)
    )
  * Sphere(r=10)
  )

figure_cut      = (
  figure.rotate(-60, -40, 30)
  )

def figure_proj(h, z):
  return (
    Linear_extrude(
      Projection(
        figure_cut,
        1
        ),
      h
      ).mirror(0, 0, 1).move(0, 0, -z)
    )

parts           = (
  (
    ~~figure_proj(20,   0)
    + figure_proj(0.1, 20).color("blue")
    + figure_cut.color("red")
    ),
  (
    Sphere(5)
    ),
  )
