# Microfluidics

A repository to host microfluidic chip design schematics and fabrication procedures.

The designs are heavily based on published ones from the [Laboratory of Biological Network Characterization](http://lbnc.epfl.ch/index.html) (LBNC) in EPFL.

![](https://gitlab.com/acubesat/su/microfluidics/-/raw/master/assets/final.png "final AcubeSAT PDMS chip design")

## Resources

* Protocols and workflows for the wet lab/microfluidic experiments can be found [here](https://benchling.com/organizations/acubesat/).
* The [Wiki page](https://gitlab.com/acubesat/su/microfluidics/-/wikis/Design) contains documentation regarding the step-by-step design process.
* The published/initial microfluidic designs were acquired from/can be found [here](http://lbnc.epfl.ch/microfluidic_designs.html).

## Repository Structure

There are three folders of interest:
1. `lbnc`: contains the original lbnc design files
2. `biodisplay_sub` contains all subsequent modification files
3. `assets` contains screenshots of all designs

```
+---assets
|   +---biodisplay_sub
|   |   |   .gitattributes
|   |   |   biodisplay_sub.png
|   |   |
|   |   +---design_iterations
|   |   |   +---inlets_closer
|   |   |   |       .gitattributes
|   |   |   |       biodisplay_sub_inlets_closer.png
|   |   |   |       biodisplay_sub_inlets_closer_incr_dist.png
|   |   |   |
|   |   |   \---vacuum_line
|   |   |           .gitattributes
|   |   |           biodisplay_sub_vacuum_line.png
|   |   |           biodisplay_sub_vacuum_line_in_flow.png
|   |   |
|   |   \---testing
|   |           .gitattributes
|   |           biodisplay_sub_inlets_closer_incr_dist_test_flow.png
|   |           biodisplay_sub_inlets_closer_test_flow.png
|   |           biodisplay_sub_test_flow.png
|   |           biodisplay_sub_test_flow_control.png
|   |
|   \---lbnc
|           .gitattributes
|           biodisplay.png
|
+---biodisplay_sub
|   |   biodisplay_sub.dwg
|   |   biodisplay_sub.dxf
|   |
|   +---design_iterations
|   |   +---control_chambers_on_top
|   |   |       biodisplay_sub_control_chambers_on_top.dwg
|   |   |       biodisplay_sub_control_chambers_on_top.dxf
|   |   |
|   |   +---inlets_closer
|   |   |   |   biodisplay_sub_inlets_closer.dwg
|   |   |   |   biodisplay_sub_inlets_closer.dxf
|   |   |   |
|   |   |   \---incr_dist
|   |   |           biodisplay_sub_inlets_closer_incr_dist.dwg
|   |   |           biodisplay_sub_inlets_closer_incr_dist.dxf
|   |   |
|   |   \---vacuum_line
|   |           biodisplay_sub_vacuum_line.dwg
|   |           biodisplay_sub_vacuum_line.dxf
|   |           biodisplay_sub_vacuum_line_in_flow.dwg
|   |           biodisplay_sub_vacuum_line_in_flow.dxf
|   |
|   \---testing
|       |   biodisplay_sub_test_flow.dwg
|       |   biodisplay_sub_test_flow.dxf
|       |   biodisplay_sub_test_flow_control.dwg
|       |   biodisplay_sub_test_flow_control.dxf
|       |
|       \---inlets_closer
|           |   inlets_closer_test_flow.dwg
|           |   inlets_closer_test_flow.dxf
|           |
|           \---incr_dist
|               \---incr_dist_test_flow
|                       biodisplay_sub_inlets_closer_incr_dist_test_flow.dwg
|                       biodisplay_sub_inlets_closer_incr_dist_test_flow.dxf
|
\---lbnc
        biodisplay.cif
        biodisplay.dwg
        biodisplay.dxf
        biodisplay.gds
```
