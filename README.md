# pyCAD

## Project Description
This is a library for **OpenCAD**, an open source software for computer aided drafting (CAD) along with providing powerful tools and automation for engineers, architects and alike. This library provides everything one needs for manipulating OpenCAD objects. 

### Project Owner(s)
* Szabolcs Pasztor
* Alex Lord

### Target Audience
* Szabolcs Pasztor

### Method of Communication
[Github Issues](https://guides.github.com/features/issues/)
### Goals
* Provide **File Management** (I.E. File open, close, read and write). Files will be in [JSON](http://www.w3schools.com/json/) format for now.
* Files should be able to contain **basic CAD objects** such as:
    * *Point: An object with an x value, y value, elevation and a handle.*
    * *Line: A tuple of points and a handle.*
    * *Polyline: A dictionary of line objects with the key being the handle with a direction and a rank for values.
* Allow operations or **commands** to be performed that interface with these objects through their handles. Commands to include are:
    * *Point: Create a point from specified paramaters.*
    * *Polyline: Create a polyline from specified paramters.*
    * *List: Show the poperties of any object specified.*
    * *Edit: Edit the properties of any object specified.*
    * *Offset: Create a polyline as an offset from another specified polyline.*
    * *Join: Combine multiple polylines to one polyline.*
    * *Break: Break apart a polyline at a specified point. This point needs to lie on the polyline in space but does not need to be a point in the list (I.E. can be inbetween points.*

### Antigoals
* The JSON fille format was chosen out of convenience. It is temporary and should not be built with long term use in mind.

### Related Software
* [Everything this guy makes](https://readthedocs.org/profiles/mozman/)
* [Teigha](https://www.opendesign.com/)
* [Lot's of companies on this list](https://www.opendesign.com/member-showcase)

### Time Estimate
### Tolerances
