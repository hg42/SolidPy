$fa=5;
$fs=1;

union()
  {
mirror([0.00,1.00,0.00]) rotate([0, 0, 90]) translate([20.00,0.00,0.00]) color("green") cube(size=[10, 10, 10], center=true);
color("red") translate([-20.00,0.00,0.00]) scale([0.70,0.70,0.70]) cube(size=[10, 10, 10], center=true);
color("blue") cube(size=[10, 10, 10], center=true);
translate([0.00,0.00,-20.00]) cube(size=[10, 10, 10], center=true);
translate([0.00,0.00,0.00]) translate([-5.00,0.00,-5.00]) difference()
  {
cube(size=[10, 50, 10], center=false);
translate([-0.05,5.00,5.00]) rotate([0, 90, 0]) cylinder(h=10.1, r=2);
translate([-0.05,15.00,5.00]) rotate([0, 90, 0]) cylinder(h=10.1, r=2);
translate([-0.05,25.00,5.00]) rotate([0, 90, 0]) cylinder(h=10.1, r=2);
translate([-0.05,35.00,5.00]) rotate([0, 90, 0]) cylinder(h=10.1, r=2);
translate([-0.05,45.00,5.00]) rotate([0, 90, 0]) cylinder(h=10.1, r=2);
union()
  {
translate([5.00,-0.05,5.00]) rotate([-90, 0, 0]) cylinder(h=50.1, r=2);
  }
union()
  {
translate([5.00,5.00,-0.05]) rotate([0, 0, 0]) cylinder(h=10.1, r=2);
translate([5.00,15.00,-0.05]) rotate([0, 0, 0]) cylinder(h=10.1, r=2);
translate([5.00,25.00,-0.05]) rotate([0, 0, 0]) cylinder(h=10.1, r=2);
translate([5.00,35.00,-0.05]) rotate([0, 0, 0]) cylinder(h=10.1, r=2);
translate([5.00,45.00,-0.05]) rotate([0, 0, 0]) cylinder(h=10.1, r=2);
  }
  }
  }
