---
substitutions:
  coordinator_icon: |-
    ```{image} ../includes/coordinator_icon.png
    ```
  get_param_from_map_button.png: |-
    ```{image} ../includes/get_param_from_map_button.png
    ```
  public_jobs: |-
    ```{image} ../includes/public_jobs.png
    ```
---

# Processing

:::{figure} ../includes/processing.png
:align: center
:figclass: img-container-border
:scale: 50%
:::

Select some products on the geobrowser, find an appropriate Web Procesing Service and immediately run it. Your job will be saved and accessible at any time.

## Discover existing WPS

To discover Web Processing Services:

1. Open the Processing Services tab by clicking on **Processing Services** on the right of the geobrowser's map.
2. Filter the services by writting on the **Filter services** input. By default, only 20 services are displayed.
3. Click on the service's icon to open it.
4. You can now see the description of the service as well as the list of associated parameters.

## Create a new job

To create a new job:

1. Select the service you want to use (see [Discover existing WPS]).
2. Fill in the different parameters needed by the service (see [Fill in parameters]).
3. Click on **Run Job**
4. To visualize the result of the job, see {doc}`Visualisation <visualisation>`

:::{figure} ../includes/runjob.png
:align: center
:figclass: img-container-border
:scale: 50%
:::

## Create a new job with Quotation mode

To create a new job:

1. Select the service using the quotation mode that you want to use (see [Discover existing WPS]).
2. Fill in the different parameters needed by the service (see [Fill in parameters]).
3. Click on **Calculate cost** to get an estimation of the wps job cost.
4. If you have enough credits on your account, you will be able to see the **Run job** button.
5. Click on **Run Job**
6. To visualize the result of the job, see {doc}`Visualisation <visualisation>`

:::{figure} ../includes/runjobquotation1.png
:align: center
:figclass: img-container-border
:scale: 50%
:::

:::{figure} ../includes/runjobquotation2.png
:align: center
:figclass: img-container-border
:scale: 50%
:::

## Coordinator job

When a job is triggered by a coordinator, the icon {{ coordinator_icon }} is added in the job view (job detailed view and in job list).

## Fill in parameters

A processing service takes as input a list of parameters, which are defined in the DescribeProcess function of the WPS service.
Parameters can be free text or can be selected from a list of possible values. When a default value is described in the DescribeProcess, it is automatically set in the parameter field and can of course be changed by the user if he wants to.
Besides, some specific parameters can be filled directly from the geobrowser:

- data input or files can be directly dragged from the Result tab or from the basket and dropped into the parameter input,
- geographic input (bounding box) value can be taken from the bbox selected on the map by clicking on the {{ get_param_from_map_button.png }} button,
- temporal input (start date, end date) can be taken from the time bar selection by clicking on the {{ get_param_from_map_button.png }} button,

## Access my jobs

To access my jobs:

1. Open the Processing Services tab by clicking on **Processing Services** on the right of the geobrowser's map.
2. Click on **Jobs** on top of the Processing Services tab.
3. The list of existing jobs (failed or success) is displayed.
4. Filter jobs using the dropdown list and selecting "show only mine".

:::{figure} ../includes/my_job_list.png
:figclass: img-border
:scale: 50 %
:::

5. Click on the job title.
6. You can now see details about the job.

## Access job result

:::{figure} ../includes/job_results.png
:figclass: img-border
:scale: 50 %
:::

To visualize job's result:

1. Select a job in the **Jobs** tab from the Processing services.
2. Click on the job title, the following infos will appear:

- **Job info**: main info about the job + access to the Status/Result location
- **Parameters**: list of used parameters
- **Results**: if specific actions on the result are available
- **XML Result**: XML result returned by the WPS

3. To visualize job's results on the map, please see {doc}`Discover data results from a processing job <data>`.

## Delete my jobs

To delete my jobs:

1. Open the Processing Services tab by clicking on **Processing Services** on the right of the geobrowser's map.
2. Click on **Jobs** on top of the Processing Services tab.
3. The list of existing jobs (failed or success) is displayed.
4. Filter your jobs using the dropdown list and selecting "show only mine" (you can delete only your jobs).
5. Put your mouse over the job, a small "x" appears on the right.
6. Click on the "x".
7. The job is deleted

:::{figure} ../includes/job_delete.png
:figclass: img-border
:scale: 50 %
:::

## Make my jobs public

To make my jobs public:

1. Go to the detail view of the job (see [Access my jobs]).
2. See {doc}`Share a job <sharing>`.

:::{tip}
On the job list, jobs with the icon {{ public_jobs }} are the jobs you made public.
:::

## Access public jobs

To access public jobs:

1. Open the Processing Services tab by clicking on **Processing Services** on the right of the geobrowser's map.
2. Click on **Jobs** on top of the Processing Services tab.
3. The list of existing jobs (failed or success) is displayed.
4. Filter jobs using the dropdown list and selecting "show only public".
5. Click on the job title.
6. You can now see details about the job.

## Get support or contact provider

Once you have processed a job, you will see on the detailed view of the job a tab named **Support**.
This tab will allow you to send an email to the support team will all details about your job, or (only in case of successful jobs) to the service provider.

:::{figure} ../includes/job_support.png
:figclass: img-border
:scale: 50 %
:::
