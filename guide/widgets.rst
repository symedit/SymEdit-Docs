Using Widgets
=============

What Are Widgets?
-----------------

Widgets are small interchangeable "blocks" that you can assign to different parts of your site.
If you wanted to show your latest 3 blog posts, you could do that through a widget. If you
want to have the same picture or message in your sidebar on every page, a widget can do that.

What Is a "Widget Area?"
------------------------

A Widget Area is a section of your website where widgets will appear in the order that you choose.
Typically you will have 4 widget areas:

Featured
    Usually at the beginning of any page. This area is useful for adding callouts or an image gallery to the top of your pages.

Sidebar
    The sidebar shows up to the left or the right side of your page. You will typically need to choose a template with a sidebar in it for this widget area to appear.

Supplemental
    Usually just after the content of your page but above the footer.

Footer
    The very bottom of your website. This is typically used for contact information and newsletters signups.

Assigning A Widget to Pages
---------------------------

Each widget has a dropdown option for how you would like to determine its "associations." An
association is a string like `/`, `/blog`, `/5`. If you choose a visibility option of "Include on ALL Pages"
then your widget will appear on every page. This is good for things like the footer. In this case
none of the associations matter because it will show up regardless. If you choose "Include ONLY on specified"
then your widget will show on the pages you specify. If you choose `/` then it will only show up on your homepage,
if you choose `/blog` and your blog is located there, it will only show up on your blog. Finally if you choose
"Exclude ONLY on specified" then your widget will appear on every page EXCEPT the ones you specify.

Note that if you would like widgets to show up in your sidebar, you will need to choose a template for your
page that includes a sidebar, it will not automatically add the sidebar for you. You can change this on the
`Template` tab when editing a page, and can usually choose which side you would like the bar on.

Shortcode Reference
-------------------

Widgets can be embedded as shortcodes in most places. They look like this:

    [widget strategy=widget_type parameter=value]

Below is a reference for most widgets.

Recent Posts
~~~~~~~~~~~~

    [widget strategy=blog_recent_posts max=2]

`max` should be an integer 1 or greater. Use `latest_post` for a single post.

Latest Post
~~~~~~~~~~~

    [widget strategy=blog_latest_post show_image=0]

`show_image` can be 1 or 0, for true or false respectively.

Upcoming Events
~~~~~~~~~~~~~~~

    [widget strategy=upcoming_events max=3]

Social Sharing
~~~~~~~~~~~~~~

    [widget strategy=addthis]

Basic Contact Information
~~~~~~~~~~~~~~~~~~~~~~~~~

    [widget strategy=contact_info]

Google Map
~~~~~~~~~~

    [widget strategy=google_map address="123 Address Way, Birmingham AL"]

Image Gallery
~~~~~~~~~~~~~

    [widget strategy=gallery slider="gallery-slug"]

Slider
~~~~~~

    [widget strategy=slider slider="gallery-slug" thumbnails=1 stretch=1 controls=1]

`thumbnails`, `stretch`, and `controls` can be set to 1 or 0, for true or false respectively.