
Defaults.showDiff = 1

figure           = (
  Cube(10, center=1)
  )

WBlock = 10
DT = 5

def Block(nx, ny, nz, cx=0, cy=0, cz=0, hx=0, hy=0, hz=0):
  wx = WBlock*nx
  wy = WBlock*ny
  wz = WBlock*nz
  if cx: cx = -wx/2
  if cy: cy = -wy/2
  if cz: cz = -wz/2
  block = Cube(wx, wy, wz)
  if hx: block = block - [Cylinder(r=DT/2, h=wx+Dh).rotate(0, 90, 0).move(-Do, iy*WBlock+WBlock/2, iz*WBlock+WBlock/2) for iy in range(0, ny) for iz in range(0, nz)]
  if hy: block = block - [Cylinder(r=DT/2, h=wy+Dh).rotate(-90, 0, 0).move(ix*WBlock+WBlock/2, -Do, iz*WBlock+WBlock/2) for ix in range(0, nx) for iz in range(0, nz)]
  if hz: block = block - [Cylinder(r=DT/2, h=wz+Dh).rotate(0, 0, 0).move(ix*WBlock+WBlock/2, iy*WBlock+WBlock/2, -Do) for ix in range(0, nx) for iy in range(0, ny)]
  if cx or cy or cz: block = block.move(cx, cy, cz)
  return block

nx = 1
ny = 5
nz = 1

parts           = (
  figure.color("blue")
  #- figure.move(7, 0, 0)
  #- figure.move(0, 7, 7)
  #- [
  #  figure.scale(1.01).move(7, 0, 0),
  #  figure.scale(1.01).rotate(45, 30, 30).move(-2, 7, 0)
  #  ]
  #- [figure.rotate(10*i, 10*i, 10*i).move(7, 0, 0) for i in range(0, 3)]
  #- [Cylinder(r=DT/2, h=WBlock+Dh).rotate(0, 90, 0).move(-Do, iy*WBlock+WBlock/2, iz*WBlock+WBlock/2) for iy in range(0, ny) for iz in range(0, nz)]
  #+ figure.color("green").move(20, 0, 0).rotate(0, 0, 90).mirror(0, 1, 0)
  #+ figure.scale(0.7).move(-20, 0, 0).color("red")
  + [
    figure.color("green").move(20, 0, 0).rotate(0, 0, 90).mirror(0, 1, 0),
    figure.scale(0.7).move(-20, 0, 0).color("red")
    ]
  + figure.move( 0, 0, -20)
  #+ Block(1, 5, 1,  1, 0, 1,  1, 1, 1).move(0, 0, 0)
  )
