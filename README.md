# Expreviewer
A Ren'Py 7.6/8.1+ tool that allows the user to see how their `LayeredImage`s look like.

Simply place `expreviewer.rpy` somewhere in your game folder, launch the game, and press `shift + E`.

![screenshot0007](https://github.com/Elckarow/Expreviewer/assets/101005497/1f3730ef-3db2-4eb6-848a-bff0b3e9a260)

You'll quickly notice a few things:

* A list of tags in the top left corner (those are the tags that you've entered).
* A `Use custom layer` button in the top right corner (we'll get to it later (later as in 2 lines)).
* A UI stolen from the launcher (yes, totally).

The `amelia` button can't be clicked. That's because the tag isn't currently showing. The `Use custom layer` option allows the user to preview any tag. Turning it off will only allow this for showing tags. Useful for when you're coding expressions as it is.

Let's click on `aika`, shall we?

![screenshot0008](https://github.com/Elckarow/Expreviewer/assets/101005497/9c11ebef-30e6-4013-b6c9-0fb8330f031a)

Those two buttons, `turned` and `smug` are different `LayeredImage`s defined with the same tag.

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/2abf2e07-ab3e-42e6-afd8-37a9ab5813f0)

If a `LayeredImage` has been defined without anything else,

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/2b06d848-f3a0-44b2-866f-c7f8d5ba0d39)

a special value is used (internally) and `NONE` is displayed.

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/31ecf44e-0543-44a5-b50b-6028a2cee432)

If we click on `turned`,

![screenshot0010](https://github.com/Elckarow/Expreviewer/assets/101005497/bd70e60b-d22b-4c33-b953-d4f8f6218609)

we can see a bunch of stuff.

* A list of `group`s names. Those are the `group`s that are defined inside the `LayeredImage`. Clicking those `group`s will show every `attribute`s that has been defined inside that `group`.
* This `Current attributes` thing in the bottom right corner. As one would've guessed, it shows what `attribute`s are currently used.

Let's change some expressions. I want to close her mouth and put her ~~kid named~~ finger down:

![screenshot0011](https://github.com/Elckarow/Expreviewer/assets/101005497/5d2e1de5-04de-4ce4-a8e6-bd2469e37db2)

Pretty pog if i do say so myself.
And since a new context is created when calling the screen, leaving `expreviewer` will turn everything back to normal.

![screenshot0012](https://github.com/Elckarow/Expreviewer/assets/101005497/8b5e57b9-c3bd-4b7c-a1d1-c37bba33b946)

**_Credit Elckarow#8399 or i will haunt you_**

oh and here's what amelia looks like btw
![screenshot0013](https://github.com/Elckarow/Expreviewer/assets/101005497/354b6a1c-61f8-46a2-8984-8583c792f6fd)

both Amelia and Aika are from a DDLC Mod called `Doki Doki Undercurrents` and yours truly is part of the dev team (go play it https://undercurrentsmod.weebly.com/).
\#selfplug
