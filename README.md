
**In progress:**

Object detection via openCV for input mirroring and other stuff (theoretically).

Example of my OpenCV object detection in action:




https://github.com/suhuf/improved-engine/assets/105312929/d21ce58e-675f-4cc0-8b14-68a7c2a2832e



As you can see it is very slow at the moment, plan on changing this after getting the input mirroring format down and the ability to detect more objects (with labels)


**TO-DO List:**

Implement multi threading for multiple objects, perfomance is even worse when dealing with multiple objects

around 30% of the slow down is due to template matching, find a way to separate that.

Look for a quicker way to render/burn through the matching process
