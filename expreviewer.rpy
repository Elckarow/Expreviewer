# Credit Elckarow#8399
init python in expreviewer: 
    from renpy import store
    from store import config, layeredimage

    layer = "expreviewer"

    config.detached_layers.append(layer)

    # enter your image tags here
    # only works for layeredimages because fuck you
    tags = [
        # "monika",
        # "sayori",
        # "yuri",
        # "natsuki"
    ]

    characters = { }
    # "monika": {"forward": [("outfits", [ ]), ("left", [ ]), ...], "lean": [(...)]}
    # tag: {rest: [(group name, attribute name list)], ...}

    layeredimageproxy_depth = 1

    def get_layeredimage(name):
        l = renpy.get_registered_image(name)

        for _ in range(layeredimageproxy_depth):
            if isinstance(l, layeredimage.LayeredImageProxy):
                l = l.image
                
        if not isinstance(l, layeredimage.LayeredImage): return None
        return l

    def get_layeredimage_groups(l, attributes=False): # list[tuple[str, layeredimage.Attribute]] | list[str]
        last_group = None

        rv = [ ]
        attr_names = set() 
        # might have a lot of attributes
        # so we use a set

        if isinstance(l, basestring): l = get_layeredimage(tuple(l.split()))
        if l is None: return rv

        for attr in l.attributes:
            if not isinstance(attr, layeredimage.Attribute): continue

            if not attributes:
                if attr.group != last_group:
                    last_group = attr.group
                    rv.append(attr.group)
            else:
                if attr.group != last_group:
                    last_group = attr.group    
                    rv.append((attr.group, [ ]))

                current_attributes = rv[-1][1]
                if attr.attribute in attr_names: continue
                attr_names.add(attr.attribute)
                current_attributes.append(attr)

        return rv

    _no_rest = "_expreviewer_no_rest"

    @config.start_callbacks.append
    def __populate_characters():
        def get_rest_and_groups(tag):
            for name, image in renpy.display.image.images.items():
                _tag, tag_rest = name[0], name[1:]
                if _tag != tag: continue
                if not tag_rest: tag_rest = (_no_rest,)
                                
                l = get_layeredimage(name)
                if l is None: continue
                                        # :yurimelt:
                yield " ".join(tag_rest), [(group, [attr.attribute for attr in attributes]) for group, attributes in get_layeredimage_groups(l, True)]

        for tag in tags:
            d = characters.setdefault(tag, { })
            for tag_rest, groups in get_rest_and_groups(tag):
                d[tag_rest] = groups
        
    def get_layeredimage_group_attribute_showing(name, group, layer="master"):
        """
        Returns the attribute in the group `group` that is showing (or the 1st default attribute in that group)
        for the layeredimage `name` on the layer `layer`, or `None` if one couldn't be found / the layeredimage isn't showing.
        """
        _name = name.split()
        tag, rest = _name[0], _name[1:]
        showing = renpy.get_attributes(layer=layer, tag=tag)
        if showing is None: return None
        if not all(a in showing for a in rest): return None # not the right layeredimage

        l = get_layeredimage(name)
        if l is None: return None

        for _group, attributes in get_layeredimage_groups(l, True):
            if _group == group:
                break
        else:
            return None # layeredimage has no group named `group` 

        default = None

        for attr in attributes:
            if attr.attribute in showing:
                return attr.attribute
            if attr.default and default is None:
                default = attr.attribute

        return default
    
    def open():
        if not config.developer: return
        if renpy.context()._menu: return
        window = store._window
        store._window_hide(None)
        renpy.checkpoint()
        rv = renpy.invoke_in_new_context(renpy.call_screen, "expreviewer")
        renpy.rollback(True)
        store._window_auto = True
        store._window = window
        return rv
    
    config.overlay_functions.append(lambda: renpy.ui.add(renpy.Keymap(expreviewer=store.Function(open))))
    config.keymap["expreviewer"] = ["shift_K_e"]

transform _expreviewer:
    subpixel True zoom 0.8
    xalign 0.5 yanchor 1.0 ypos 1.03

# my brain hurts
# this can be optimized but fuck off i aint going over that a 2nd time
screen expreviewer():
    # consts
    default exp_characters = expreviewer.characters
    default _at_list = [_expreviewer]
    default _ui = True # except this :TardLilly:
    default _ui_trans_time = 0.3
    default _crop_trans_time = 0.3

    default last_tag_selected = None
    default tag_selected = None
    default tag_rest_selected = None

    default groups_scrolled = set()

    default use_custom_layer = False

    $ name = None # defaults to None, set later when a tag_rest is selected

    $ layer_to_use = ("master" if not use_custom_layer else expreviewer.layer)
    $ showing_tags = renpy.get_showing_tags(layer_to_use) 

    if use_custom_layer:
        add "#fdfdfd"
    else:
        add "#000"
    
    add Layer(layer_to_use)

    style_prefix "expreviewer"

    showif _ui:
        frame:
            at transform:
                subpixel True xpos 0.0
                on appear:
                    xanchor 1.0 alpha 0.0
                    easein _ui_trans_time xanchor 0.0 alpha 1.0
                on show:
                    easein _ui_trans_time xanchor 0.0 alpha 1.0
                on hide:
                    easeout _ui_trans_time xanchor 1.0 alpha 0.0
            
            if tag_selected is None:
                viewport:
                    xfill True ysize 0.6
                    mousewheel True draggable True

                    if not exp_characters:
                        text "No layeredimages have been stored :("
                    else:
                        vbox spacing 10:
                            for tag in exp_characters:
                                textbutton tag action (
                                    If(last_tag_selected != tag,
                                        true=(
                                            SetScreenVariable("tag_rest_selected", None),
                                            Function(groups_scrolled.clear)
                                        )
                                    ),
                                    SetScreenVariable("tag_selected", tag),
                                    SelectedIf(tag_selected == tag)
                                ):
                                    sensitive use_custom_layer or tag in showing_tags
                
                textbutton "leave expreviewer" action Return() align (0.0, 1.0)
            
            else:                     # can return `None`                        so we need to handle that case
                $ showing_attributes = (renpy.get_attributes(layer=layer_to_use, tag=tag_selected) or ())
                $ tag_selected_is_showing = tag_selected in showing_tags

                viewport:
                    xfill True yfill True
                    mousewheel True draggable True

                    vbox xfill True spacing 20 first_spacing 10:
                        fixed yfit True:
                            textbutton "<" action (SetScreenVariable("last_tag_selected", tag_selected), SetScreenVariable("tag_selected", None), SelectedIf(False))
                            text tag_selected xalign 0.5 text_align 0.5

                        hbox:
                            box_wrap True box_wrap_spacing 10
                            spacing 15 xalign 0.5
                            for tag_rest in exp_characters[tag_selected]:
                                textbutton (tag_rest if tag_rest != expreviewer._no_rest else "NONE"):
                                    action (
                                        SelectedIf(tag_rest_selected == tag_rest),
                                        SetScreenVariable("tag_rest_selected", (None if tag_rest_selected == tag_rest else tag_rest)),
                                        Function(groups_scrolled.clear),
                                        If(
                                            use_custom_layer and not tag_selected_is_showing,
                                            true=Function(renpy.scene, layer_to_use)
                                        ),
                                        Function(
                                            renpy.show,
                                            tag_selected + " " + (tag_rest if tag_rest != expreviewer._no_rest else ""),
                                            layer=layer_to_use,
                                            at_list=(
                                                _at_list
                                                if not tag_selected_is_showing
                                                else [] # always used when `not use_custom_layer`
                                            )
                                        ),
                                    )

                        if tag_rest_selected is not None:
                            $ name = tag_selected + " " + (tag_rest_selected if tag_rest_selected != expreviewer._no_rest else "")

                            vbox spacing 25:
                                for group, attributes in exp_characters[tag_selected][tag_rest_selected]:
                                    $ is_group_scrolled = group in groups_scrolled

                                    vbox spacing 3:
                                        button:
                                            hbox:
                                                text ">":
                                                    at transform:
                                                        subpixel True align (0.5, 0.5)
                                                        # no interpolation the 1st time (which is what we want)
                                                        ease _crop_trans_time matrixtransform (RotateMatrix(0, 0, 90) if is_group_scrolled else RotateMatrix(0, 0, 0)) # im such a fraud
                                                null width 5
                                                text group yalign 0.5

                                            action ToggleSetMembership(groups_scrolled, group)

                                        showif is_group_scrolled:
                                            vbox spacing 0:
                                                at transform:
                                                    subpixel True crop_relative True
                                                    crop (0.0, 0.0, 1.0, 0.0)
                                                    on appear:
                                                        crop (0.0, 0.0, 1.0, 1.0)
                                                    on show:
                                                        ease _crop_trans_time crop (0.0, 0.0, 1.0, 1.0)
                                                    on hide:
                                                        ease _crop_trans_time crop (0.0, 0.0, 1.0, 0.0)
                                                        
                                                for attr in attributes:
                                                    textbutton attr action (
                                                        If(
                                                            attr not in showing_attributes,
                                                            Function(renpy.show, name + " " + attr,  layer=layer_to_use),
                                                            Function(renpy.show, name + " -" + attr, layer=layer_to_use)
                                                        ),
                                                        SelectedIf(attr == expreviewer.get_layeredimage_group_attribute_showing(name, group, layer=layer_to_use))
                                                    ) 
        
        frame:
            at transform:
                subpixel True xpos 1.0
                on appear:
                    xanchor 0.0 alpha 0.0
                    easein _ui_trans_time xanchor 1.0 alpha 1.0
                on show:
                    easein _ui_trans_time xanchor 1.0 alpha 1.0
                on hide:
                    easeout _ui_trans_time xanchor 0.0 alpha 0.0
            
            vbox spacing 10 first_spacing 50:
                textbutton "Use custom layer" action (
                    SelectedIf(use_custom_layer),
                    ToggleScreenVariable("use_custom_layer"),
                    SetScreenVariable("last_tag_selected", None),
                    SetScreenVariable("tag_selected", None),
                    SetScreenVariable("tag_rest_selected", None),
                    Function(groups_scrolled.clear)
                )
            
            python:
                _name = name
                if _name is None and last_tag_selected is not None and tag_rest_selected is not None:
                    _name = last_tag_selected + " " + (tag_rest_selected if tag_rest_selected != expreviewer._no_rest else "")
            
            vbox yalign 1.0 spacing 2:
                text "Current attributes" size 22 color "#fff"

                if _name is None:
                    text "None" size 20 color "#888888"
                else:
                    hbox spacing 5 box_wrap True box_wrap_spacing 0:
                        for group in expreviewer.get_layeredimage_groups(_name):
                            $ group_attribute_showing = expreviewer.get_layeredimage_group_attribute_showing(_name, group, layer=layer_to_use)
                            if group_attribute_showing is not None:
                                text group_attribute_showing size 20 color "#888888"

            text "Press 'SPACE' (or right-click) to hide the UI.":
                color "#fff" size 22
                at transform:
                    subpixel True yalign 0.5
                    xpos 1.0 xanchor 0.0 alpha 0.0
                    pause _ui_trans_time
                    easein 0.5 xanchor 1.0 alpha 1.0
                    pause 1.2
                    easeout 0.5 xanchor 0.0 alpha 0.0
    
    key ["K_SPACE", "mouseup_3"] action ToggleScreenVariable("_ui")
    if not _ui:
        key "mouseup_1" action SetScreenVariable("_ui", True)

# We stealin' that launcher UI
style expreviewer_frame is empty:
    background "#131619"
    ysize 1.0
    padding (20, 20)
    xsize 300

style expreviewer_base_text is empty:
    color "#fff"
    font "DejaVuSans.ttf"
    line_leading 0 line_spacing 0

style expreviewer_text is expreviewer_base_text:
    size 26
    color "#0066cc"

style expreviewer_button is empty
style expreviewer_button_text is expreviewer_base_text:
    color "#888888"
    hover_color "#67a4ff"
    selected_color "#fff"
    insensitive_color "#4d4d4d"
    size 20

style expreviewer_vbox is empty
style expreviewer_hbox is empty
style expreviewer_viewport is empty
style expreviewer_fixed is empty