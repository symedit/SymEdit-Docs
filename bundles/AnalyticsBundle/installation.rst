Installation
============

Download via composer
---------------------

.. code-block:: bash

    $ composer require "symedit/analytics-bundle"

Add Bundle to Kernel
--------------------

.. code-block:: php

    <?php

    // app/AppKernel.php

    public function registerBundles()
    {
        $bundles = array(
            // ...
            new SymEdit\Bundle\AnalyticsBundle\SymEditAnalyticsBundle(),
            // ...
        );
    }

Update Doctrine Schema
----------------------

.. code-block:: bash

    $ php app/console doctrine:schema:update --dump-sql
    $ php app/console doctrine:schema:update --force
