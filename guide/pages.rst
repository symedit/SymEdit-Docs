Using Pages
===========

Creating a New Page
-------------------

Pages are the main content of your website. Creating a new page will also
automatically add it to the navigation on your site. Pages only require
a `title`, a `name` (or slug) and `content`.

Field Descriptions
------------------

Below you can find the descriptions of all the fields for creating a `Page`.

Basic Tab
~~~~~~~~~

Title
   The title of your Page. This title is used in the navigation and in the title tag if you don't specify one in the `SEO` section.

Name
   The `name` field is used to determine the path to your `Page`. For instance, if your pages parent is the `root`, then a name of "about" would create a page located at `/about`. If you were to add a page whose parent was the "about" page you just created named "about-the-team" your page would be located at `/about/meet-the-team`. This field requires you to only use letters, numbers, underscores `_`, and hyphens `-`.

Parent
   This field helps structure your content into a tree. If you want your page to show up directly in the navigation, set your `parent` to "Root". If you try to set the `parent` of your page to itself, or something already in its lineage you will receive an error as this would create a loop.

Page Heading
   The contents of this field will show up at the top of your page typically in an `h1` tag.

Display
   Unchecking this field will prevent it from showing up in your navigation.

Template Tab
~~~~~~~~~~~~

There is only one field available on the `template` tab. Changing the template will change the layout of your page. If you would like to include Widgets
on your page then maybe choosing a template with a sidebar would be useful. The default is the "base" template and should be used unless you have
special design considerations.

SEO Tab
~~~~~~~

The SEO tab is for adding meta tags to your page.

Title
   This will change the text that is rendered in the `title` tag

Description
   Meta Description - What shows up in the description area for most search engines

Keywords
   Meta Keywords

Index
   Whether search engines should index this page

Follow
   Whether search engines should follow links from your page

Crawl
   Unchecking this box will prevent it from showing up in sitemap.xml


Summary Tab
~~~~~~~~~~~

The summary tab contains a field for the `summary` of your Page. This is not always used
and is not required. This filed can be used inside of other Widgets that show a listing
of pages. A typical use is for something like a "Services" page which has a brief
description of all of your services and then a full description when you go to the page.

Content Tab
~~~~~~~~~~~

The Content tab is home to the main content of your page. This is the most typical
field you will have to change.


Deleting a Page
~~~~~~~~~~~~~~~

Deleting a Page is fairly simple. Just navigation to `Content > List Pages`, click on the Page
you would like to delete then click the `Delete Page` button. You will be prompted to confirm
your action before the Page is deleted.

*Remember that you can always uncheck the `display` field for your Page so that it won't
appear in your navigation.*
