# Deploy your processor in the platform

If you completed properly the previous steps and integrated successfully your processor in the [Sandbox](http://docs.terradue.com/developer-sandbox/), you should now have a processor ready to be deployed on the platform.

Ensure the follwoing points are completed to be sure your processor is ready for deployment

- You have performed a successful run of your apllication workflow on your sandbox
- All your code is properly commited on the develop branch of your github repository (e.g. <https://github.com/geohazards-tep/dcs>-\<your_processor>)
- The README page of your github repository <https://github.com/geohazards-tep/dcs>-\<your_processor> has the badge `build passed`

If you can check all the previous items, you can deploy you processor to a production cluster.

## Locate your community cluster

A community cluster is a set of nodes provisioned by an ICT provider for the community. Refer to the ICT provider or the community manager of your community to locate the address of the cluster's endpoint for the deployment.

A typical cluster deployment endpoints is like this:

`https://caprera.terradue.com/production/processor/deploy`

You simply open the URL in your web browser

## Find and deploy your released processor workflows

The previous URL in your web browser shall ask you for a username and API key

:::{note}
Your API key is available in your Terradue Cloud Platform profile at <https://www.terradue.com/portal/settings/apikey>.
:::

Once properly entered with your credentials, you will see on or more workflows listed with their deployment status.
Simply clicking on them you can deploy or undeploy the workflow on the cluster.

Once a workflow is deployed, you are able to use it directly from the portal in the thematic application called [Test my processor](https://geohazards-tep.eu/geobrowser/?id=testproc).

:::{figure} ../../includes/testproc.png
:width: 70%
:::
