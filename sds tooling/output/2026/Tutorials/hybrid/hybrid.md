# Hybrid plugin example

A common question is how to bridge the gap to have tools inside the SDS2 model but make use of the .Net API?

Since the .Net API is currently headless, and it's not available within SDS2 itself, to do this you have to take a hybrid approach. Writing some of the code in python (to build the plugin itself, which will add toolbar buttons for SDS2 modeling). And the rest of the code in .Net building a standalone executable program. The Python plugin will run this program and the two "talk" over a named pipe.

To facilitate this we provide [an example plugin](../images/HybridSDS2Plugin.zip). This example plugin is ready for you to implement your program inside Program.cs within the visual studio (2015 or later) project. The plugin lets you ask SDS2 to perform selections and gives you back native .Net API handles.

You will want to rename the plugin before you're finished. It is only a starting point.

In the future, when the .Net API is available in SDS2 and it's possible to make tools directly with a pure .Net plugin, most of your code will already be in .Net working with the SDS2 .Net API.

This hybrid plugin is licensed under the MIT license. So users are free to grab it, manipulate it, and do not need to release source for their modifications.