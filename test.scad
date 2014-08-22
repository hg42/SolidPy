$fa=5;
$fs=1;

union()
  {
  union()
    {
    % translate([0.00,0.00,0.00]) mirror([0.00,0.00,1.00]) linear_extrude(height=20) projection(cut=true)rotate([-60, -40, 30]) intersection()
      {
      difference()
        {
        union()
          {
          cylinder(h=20, r=5, center = true);
          rotate([0, 90, 0]) cube(size=[10, 10, 20], center=true);
          }
        resize([10.00,0.00,0.00]) rotate([90, 0, 0]) cylinder(h=20, r=3, center = true);
        }
      sphere(r = 10);
      }
    color("blue") translate([0.00,0.00,-20.00]) mirror([0.00,0.00,1.00]) linear_extrude(height=0.1) projection(cut=true)rotate([-60, -40, 30]) intersection()
      {
      difference()
        {
        union()
          {
          cylinder(h=20, r=5, center = true);
          rotate([0, 90, 0]) cube(size=[10, 10, 20], center=true);
          }
        resize([10.00,0.00,0.00]) rotate([90, 0, 0]) cylinder(h=20, r=3, center = true);
        }
      sphere(r = 10);
      }
    }
  color("red") rotate([-60, -40, 30]) intersection()
    {
    difference()
      {
      union()
        {
        cylinder(h=20, r=5, center = true);
        rotate([0, 90, 0]) cube(size=[10, 10, 20], center=true);
        }
      resize([10.00,0.00,0.00]) rotate([90, 0, 0]) cylinder(h=20, r=3, center = true);
      }
    sphere(r = 10);
    }
  }
sphere(r = 5);
