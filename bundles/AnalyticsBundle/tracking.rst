Tracking Entities
=================

Simple Track
------------

.. code-block:: php

    <?php

    // Get an entity
    $post = $repository->find(5);

    // Track it
    $this->get('symedit_analytics.tracker')->track($post);

Delayed Flush
-------------

Entities that are tracked are flushed from Doctrine during the Kernel::TERMINATE
event. This allows your application to return the response to the user as quickly
as possible without having to wait on the database.