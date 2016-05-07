# pyCAD

## Project Description
This is a prototype for **OpenCAD**, an open source software for computer aided drafting (CAD) along with providing powerful tools and automation for engineers, architects and alike. OpenCAD's philosophy is to reduce mundane tasks in pumping out a massive plan-set with one hell of a deadline, by letting the drafter do simple drafting once again. OpenCAD feels as simple as pen on paper with a scale while providing a considerable amount of complexity and automation and the users direction.

This prototype will be used to understand the grand structure of the program and potential challenges that may come up in the development. It provides very basic functionality that is hardly what one would expect from full on CAD software for simplicity and the sake of time.

### Project Owner(s)
* Szabolcs Pasztor
* Alex Lord

### Target Audience
* Szabolcs Pasztor (If I'm not happy with the product, I won't work on it.)
* Any current CAD users that use:
    * AutoCAD
    * BricsCAD
    * Microstation
* Any potentential CAD users such as:
    * Civil Engineers
    * Architects
    * Landscapers
    * Old timers who currently draft by hand.

### Method of Communication
[Github Issues](https://guides.github.com/features/issues/)
### Goals
* Provide a **command console** for interacting with the program.
* Said command console will give access to the **python interpreter** with no limitations.
* Provide **File Management** (I.E. File open, close, read and write). Files will be in [JSON](http://www.w3schools.com/json/) format for now.
* Files should be able to contain **basic CAD objects** such as:
    * *Point: An object with an x value, y value, elevation and a handle.*
    * *Polyline: A list of points and a handle.*
* Allow operations or **commands** to be performed that interface with these objects through their handles. Commands to include are:
    * *Point: Create a point from specified paramaters.*
    * *Polyline: Create a polyline from specified paramters.*
    * *List: Show the poperties of any object specified.*
    * *Edit: Edit the properties of any object specified.*
    * *Offset: Create a polyline as an offset from another specified polyline.*
    * *Join: Combine multiple polylines to one polyline.*
    * *Break: Break apart a polyline at a specified point. This point needs to lie on the polyline in space but does not need to be a point in the list (I.E. can be inbetween points.*
* Allow for one to enter **bad input** that doesn't do anything.
* Allow for one to **undo** whatever a command just did.
* Allow for one to **cancel the current active command** which would interrupt the current command, stop it and undo any work it did.
* Create a strategy for continous development after the prototype's completion.

### Antigoals
* This will not have any visual interface. All input validation will happen via unit tests.
* This is not a fully functioning piece of CAD software. Key components such as a visual interface, layers and text will not be implemented for this is simply just a prototype to get the ball rolling.
* The JSON fille format was chosen out of convenience. It is temporary and should not be built with long term use in mind.

### Related Software
* AutoCAD
* OpenSCAD
* FreeCAD
* Microstation
* SolidWorks
* Antimony

### Time Estimate
### Tolerances
How the the program looks is not important as long as what the program does is correct and it follows common sense. This does not include the actual code however unless it conflicts with one of the antigoals.
