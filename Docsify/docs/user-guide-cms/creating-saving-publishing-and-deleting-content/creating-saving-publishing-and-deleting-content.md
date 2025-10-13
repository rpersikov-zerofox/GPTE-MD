# Creating, Saving, Publishing and Deleting content

## Creating Content

Strapi introduces the content management interface that supports input of text, numbers, media, etc., allows formatting with markdown and provides the preview option for created content. The content fields are configured for the collection or single types beforehand through the Content-Types Builder.

To add a new entry and display its combination of fields:

1.  Click on the **Add new entry** button.
2.  Fill in the fields of the component.

![Creating New Entries](/assets/Creating-New-Entries.jpg)

### Translating content

With the Internationalization plugin installed, it is possible to manage content using more than one language.

It is possible to switch locales using the Internationalization box.

![Switching Locales](/assets/Switching-Locales.jpg)

The icons displayed next to every field indicate whether the field can be translated or not:

- ![Content Can Be Translated](/assets/Content-Can-Be-Translated.png) - If the field is marked with **the globe icon**, the field can be translated;

<!-- -->

- ![Content Can Not Be Translated](/assets/Content-Can-NOT-Be-Translated.png) - If the field is marked with **the crossed out globe icon**, the field cannot be translated: its content stays the same for every locale (i.e. changing the value of a non-localizable field changes it for all other locales).

To translate content in another locale:

1.  Access the edit view of your collection or single type.
2.  In the Internationalization box click on the *Locales* drop-down list.
3.  Choose the language you want to translate your content into.
4.  Translate your content by filling up your content-type\'s fields.

## Saving, publishing and deleting content

Content can have 2 statuses: **draft or published**. You can see the current status indicated on the right of the interface, below the Information box.

By default, each newly created content is a draft. Drafts can be modified and saved at will, using the **Save** button on the top right corner of the edit view, until they are ready to be published.

### Publishing a draft

To publish a draft, click on the **Publish** button in the top right corner of the content editor.

When a content is not a draft anymore, but has been published, it is indicated on the right of the interface, below the Information box.

![Publishing a Draft](/assets/Publish-Content.png)

### Unpublishing content

Published content can be unpublished, switching back to being drafts again.

To unpublish content, click on the **Unpublish** button in the top right corner of the content editor.

![Unpublishing Content](/assets/Unpublish-Content.png)

### Deleting content

You can delete content by deleting any entry of a collection type, or the default entry of a single type.

1.  In the edit view of the entry, click on the **Delete this entry** button, located at the bottom of the right side of the interface.
2.  In the window that pops up, click on the **Yes, confirm** button to confirm the deletion.

You can copy, delete, and edit entries from the list view of a collection type. Select one of the corresponding icons on the entry row in the list to perform these actions.

You also have the possibility to delete multiple entries at the same time. To do so, select your entries massively to delete by ticking the checkbox on the entry. Then, click on **Delete selected** located right below the header of the table.

:::: warning
::: title
Warning
:::

If the Internationalization plugin is installed, entries can only be deleted for one locale at the time.
::::
