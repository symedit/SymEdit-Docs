Running Reports
===============

.. code-block:: php

    <?php

    $reporter = $this->get('symedit_analytics.reporter');

    $popularPosts = $reporter->runReport('popular', array(
        'class' => 'SymEdit\Bundle\BlogBundle\Model\Post',
    ));

    // Returns in this format
    array(
        array(
            'object' => [Doctrine Entity],
            'visits' => 45
        ),
        // ...
    );

