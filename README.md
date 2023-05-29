# Expreviewer
A Ren'Py 7.4.5+ (haven't tested each version) tool that allows the user to see how their `LayeredImage`s look like.

Simply place `expreviewer.rpy` somewhere in your game folder, launch the game, and press `shift + E`.

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/bbc9ca50-685a-4d5d-aeeb-7ebfdf2a39c2)


You'll quickly notice a few things:

* A list of tags in the top left corner (those are the tags that you've entered in `expreviewer.rpy`).
* A `Use custom layer` button in the top right corner (we'll get to it later (later as in 2 lines)).
* A UI stolen from the launcher (yes, totally).

The `amelia` button can't be clicked. That's because the tag isn't currently showing. The `Use custom layer` option allows the user to preview any tag. Turning it off will only allow this for showing tags. Useful for when you're coding expressions as it is.

Let's click on `aika`, shall we?

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/ed18de8f-2987-4764-9344-977a4ac2f3d1)

Those two buttons, `turned` and `smug` are different `LayeredImage`s defined with the same tag.

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/567913fb-69f7-49dd-b754-d9ee0a72090b)

If a `LayeredImage` has been defined without anything else,

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/0c4c18c5-9f0a-4a2c-975a-685436f1a257)

a special value is used (internally) and `NONE` is displayed.

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/f5606709-b423-48fa-8313-3b2febdde2fc)

If we click on `turned`,

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/ed58c6d6-3d58-44aa-b36f-4794d3ef16ff)

we can see a bunch of stuff.

* A list of `group`s names. Those are the `group`s that are defined inside the `LayeredImage`. Clicking those `group`s will show every `attribute`s that has been defined inside that `group`.
* This `Current attributes` thing in the bottom right corner. As one would've guessed, it shows what `attribute`s are currently used.

Let's change some expressions. I want to close her mouth and put her ~~kid named~~ finger down:

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/11dd7b18-800c-4d68-a91b-dd4d49729807)

Pretty pog if i do say so myself.
And since a new context is created when calling the screen, leaving `expreviewer` will turn everything back to normal.

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/dcd5bf6d-a5c6-45d6-8303-df286c7c584f)

**_Credit Elckarow#8399 or i will haunt you_**

oh and here's what amelia looks like btw

![image](https://github.com/Elckarow/Expreviewer/assets/101005497/d86e38e9-8700-411e-b60a-b0148c69c85a)

both Amelia and Aika are from a DDLC Mod called `Doki Doki Undercurrents` and yours truly is part of the dev team (go play it https://undercurrentsmod.weebly.com/). \#selfplug
