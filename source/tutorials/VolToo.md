# VolToo: VOLume TOOl for empirical assessment of landslide volumes \[[eo4alps](https://geohazards-tep.eu/#!pages/eo4alps)\]

by Terranum Sàrl (Switzerland)

:::{figure} assets/voltoo_logo.png
:width: 100px
:::

## 1. Introduction

**VolToo** is a tool for assessment of landslide source volumes taking into account their material types (soil, bedrock or undifferentiated). It uses empirical relationships linking landslide area to landslide volume, based on a global compilation of landslide inventories [^id8]. The **VolToo** service is mainly intended as pre-processing step in landslide hazard assessment, for example prior to landslide runout modelling using the **Flow-R** service [^id9]. **VolToo** is developed and maintained by Terranum Sàrl (Switzerland).

**VolToo** uses the global landslide dataset by Larsen et al. (2010) [^id8] for different landslide materials (soil, bedrock or undifferentiated) to assess the landslide volume for each landslide source area. Because of the huge spread in the empirical dataset (landslide volumes can span over two orders of magnitude for a given landslide area), **VolToo** assesses also the uncertainties on the volume assessment by computing the 50th, 75th and 95th percentile of the possible volume range.

:::{figure} assets/voltoo_principle.png
:align: center
:figclass: align-center
:width: 850px
:::

**Input specifications**

- Polygon shapefile or Geotiff raster file of landslide source areas:

  - Custom landslide source areas uploaded by user (e.g., polygons from a landslide inventory)
  - Landslide source areas created by other services on GEP, e.g., ALADIM-HR [^id10] or ALADIM-VHR [^id11].

:::{NOTE}
Make sure that the input file has a defined coordinate system (e.g., UTM, national grid or other any system with an EPSG code). The input file can be either as polygons (ideally single part polygons; multipart polygons will be automatically split into single polygons), or Geotiff raster files (ideally with a unique identifier as raster value).
:::

**Output specifications**

- **Landslide volume \[m3\]**: raster file of the landslide source areas with fixed classes of landslide volume in cubic meters (95th percentile) (mostly for preview in GEP)
- **VolToo landslide sources**: polygon shapefile with (additional) attributes computed by **VolToo** (i.e., landslide area, median volume, 75th percentile of volume, and 95th percentile of volume)
- Two compressed folders (TGZ files) containing these outputs as raw data (…output.tgz) or as preview files with fixed symbology (…preview.tgz)

## 2. VolToo model setup

### 2.1 Access the **VolToo** service on GEP

- Sign-in on the GEP portal: <https://geohazards-tep.eu/>
- Access the Thematic App containing the **VolToo** service, for example the **eo4alps-landslides** Thematic App.
- Open the tab *Processing services* from the right of the map and select the processing service **VolToo**.

:::{figure} assets/voltoo_processing_service.png
:align: center
:figclass: align-center
:width: 850px
:::

### 2.2 Preparation of input data

This section describes the preparation of input data required for the **VolToo** service.

- Upload the landslide source areas to your private storage using the **Upload Data** button in the menu bar on the top. From the drop-down list under *Target Repository*, select your GEP username and keep the default *Target path* (i.e., “/results”). If the source areas contain landslides in soil and bedrock, they should ideally be split into two separate landslide inventories prior to this upload. Upload the landslide source areas as ZIP file containing all files of the polygon shapefile or as Geotiff raster).

:::{NOTE}
This step is not required if the landslide source areas are provided as outputs of other GEP services.
:::

- Navigate to the Area of Interest (AOI) in the geobrowser map (e.g., Solalex in the southwestern Swiss Alps)
- Use the *Draw polygon* or *Draw rectangle* tools in the geobrowser (hover over the upper left corner of the map to display the tools) to define your AOI or the *wkt* tool to upload or use an existing AOI (upload of shapefile (.zip), KML (.kml/.kmz) or geojson (.json) or well-formed WKT code)

:::{NOTE}
This step is not mandatory if you want to compute the volume of all landslide source areas in the provided inventory.
:::

### 2.3 VolToo parameterization

This section describes the different parameters of the **VolToo** service on GEP.

- **Job title**: provide a meaningful title for the **VolToo** job, such as “VolToo \[Name of study area\] \[Material type\] \[Optional other parameters\]” (e.g., “VolToo Solalex Bedrock”).

:::{NOTE}
The date and time of the model run will be automatically added to the created output files (in UTC, Coordinated Universal Time).
:::

- **Area of Interest**: this optional parameter is used to define the processing extent indicated in longitude and latitude as text string in the format: “LongitudeMin,LatitudeMin,LongitudeMax,LatitudeMax” (no spaces) (e.g., “7.088,46.262,7.176,46.312”). Use the *magic wand* symbol to import the bounding box of the current selection polygon or rectangle as AOI (see above).

:::{NOTE}
If not specified, the entire landslide inventory will be processed.
:::

- **Landslides inventory**: specify the landslide source areas previously uploaded to the private storage on GEP (see above) or from outputs of other GEP services.

:::{NOTE}
To access the uploaded files in your private storage click on Private --> My Store in the menu bar on the top. If an AOI is defined in the geobrowser (using the *Draw polygon*, *Draw rectangle* or *wkt* tools) only the user datasets that intersect the AOI are shown. Select the appropriate file and drag-and-drop it to the matching field in the **VolToo** interface.
:::

- **Landslide material**: specify the landslide material type from the drop-down list (soil, bedrock or all). If the landslide inventory does not differentiate the material types, set to the landslide material to "all".
- Click on the *Run Job* button at the bottom of the **VolToo** interface.
- This automatically displays the *Job Info* window summarizing the parameters of the **VolToo** processing. The progress bar allows checking the processing.

:::{figure} assets/voltoo_parameters.png
:align: center
:figclass: align-center
:width: 350px
:::

:::{figure} assets/voltoo_jobinfo1.png
:align: center
:figclass: align-center
:width: 350px
:::

## 3. VolToo modelling results

- Check the modelling progress in the *Jobs* tab under “Processing Services” or in the detailed job information window (if necessary, refresh the job status by clicking on the status button)
- Once the **VolToo** model run is successfully completed, click on the *Show results* button at the bottom of the job information window.

:::{figure} assets/voltoo_jobinfo2.png
:align: center
:figclass: align-center
:width: 350px
:::

- The **VolToo** modelling results are displayed on the map of the geobrowser and listed in the *Results* tab in the window on the left side. The results comprise a rendered preview file of the landslide inventory with the empirical volumes. The results contain also two archive files (TGZ format that can be downloaded and directly opened on your computer): one with the raw outputs (…output.tgz) and one with the rendered preview files (…preview.tgz)

:::{figure} assets/voltoo_results.png
:align: center
:figclass: align-center
:width: 850px
:::

- To download the results, select the …output.tgz file in the “Results” tab and click on the folder icon “Show details” in the lower right corner. Then, click on the “Download” button in the lower left corner.
- Unpack the TGZ file and add the **VolToo** modelling results to your GIS software.

## 4. Feedback

Users are kindly invited to report any issue and problem encountered during the use of the **VolToo** service by issuing a ticket from their project support space on <https://helpdesk.terradue.com/> or sending an email to <mailto:support@terradue.com>
Suggestions and comments about the GEP service delivery are warmly welcomed on <mailto:contact@geohazards-tep.eu> to keep the service delivery on GEP as much as possible appealing, effective, and efficient.

## 5. Terms and Conditions

**Intellectual Property Right** | The Intellectual Property Right of the VolToo service (called “Service” hereafter) lies with Terranum Sàrl (Rue de l’Industrie 35b, CH-1030 Bussigny, Switzerland, called “Terranum”), if not differently specified. By using the Service, you agree to be bound by these *Terms and Conditions* and that they are enforceable like any written negotiated agreement signed by you. In case of any concern with these *Terms and Conditions*, please contact Terranum via <https://www.terranum.ch/en/about/> for additional information before using the Service.

**Use** | The Service is available to all GEP users according to a CC-BY license [^id12]. There is the possibility that users participate in the cost of service maintenance and operation: these costs are defined case-by-case among the Service provider, Terranum, the Ressource provider, Conectus/EOST, and the Platform operator, Terradue Srl.

**Results** | The results of the Service are freely shareable and adaptable with appropriate credits under the CC-BY license [^id12].

**Warranty and limitation of liability** | Terranum accepts no responsibility for the operation or performance of the Service. The entire risk of use and consequences of use of the Service falls completely on you and Terranum shall not be liable in any respect for any loss claims or injury alleged to have resulted from use of or in reliance on software product. In this respect, you shall indemnify and defend against any and all claims, including claims by third parties or by your employees, which arise directly or indirectly out of your use or operation of the Service. Terranum’s sole obligation under this warranty is to use reasonable efforts to correct any non-conforming software.
You acknowledge that you have read the foregoing disclaimers of warranty and limitation of liability and understand that you assume the entire risk of use of the Service. In no event will Terranum be liable to you for any damages, claims or costs whatsoever or any consequential, indirect, incidental damages, or any lost profits or lost savings, even if a Terranum representative has been advised of the possibility of such losses, damages, claims or costs or for any claim by any third party. Terranum will not be liable for any damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the Service, even if Terranum has been advised of the possibility of such damages. In any case, Terranum’s entire liability under any provision of this agreement shall be limited to the amount actually paid by you for the Service. The foregoing limitations and exclusions apply to the extent permitted by applicable law in your jurisdiction. Terranum’s aggregate liability and that of its suppliers under or in connection with this agreement shall be limited to the amount paid for the software, if any.

## 7. References

[^id8]: Larsen, I.J., Montgomery, D.R., Korup, O. (2010): Landslide erosion controlled by hillslope material. Nature Geoscience, 3, 247-251.

[^id9]: Flow-R: Flow Path Assessment of Gravitational Hazards at a Regional Scale. On-demand processing service on GEP: <https://docs.terradue.com/geohazards-tep/tutorials/Flow-R.html>

[^id10]: ALADIM-HR: Automatic LAndslide Detection and Inventory Mapping from multispectral S2 & L8 data. On-demand processing service on GEP: <https://docs.terradue.com/geohazards-tep/tutorials/aladim-hr.html>

[^id11]: ALADIM-VHR: Automatic LAndslide Detection and Inventory Mapping from multispectral Very-High Resolution data. On-demand processing service on GEP: <https://docs.terradue.com/geohazards-tep/tutorials/aladim_vhr.html>

[^id12]: Creative Commons Attribution 4.0 International (CC BY) licence: <https://creativecommons.org/licenses/by/4.0/>
