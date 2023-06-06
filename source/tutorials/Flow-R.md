# Flow-R: Flow Path Assessment of Gravitational Hazards at a Regional Scale \[[eo4alps](https://geohazards-tep.eu/#!pages/eo4alps)\]

by Terranum Sàrl (Switzerland)

:::{figure} assets/flowr_logo.jpg
:width: 100px
:::

## 1. Introduction

**Flow-R** stands for “Flow path assessment of gravitational hazards at a Regional scale” and is developed and maintained by Terranum Sàrl (Switzerland), a spin-off of the University of Lausanne. **Flow-R** is a software for rapid, robust, and reliable propagation modeling of natural hazards. It allows for the assessment of the propagation extent based on several published empirical run-out models at local and regional scales. Details on the **Flow-R** model can be found in Horton et al. (2013) [^id19].
Up to now, **Flow-R** has been adapted to runout computations of:

- Debris flows
- Rockfalls
- Rock avalanches
- Shallow landslides
- Snow avalanches

The **Flow-R** service on GEP (hereafter called **Flow-R on GEP**) contains parameter presets for these hazard types calibrated for extreme events in the Alps. Using these hazard presets therefore leads to conservative propagation extents appropriated for susceptibility or indicative hazard mapping at regional scale. Terranum Sàrl provides, on-demand, advanced processing including calibration of propagation parameters to local landslide inventories and the distinction between extreme, rare, and current landslide events using susceptibility levels (<https://www.terranum.ch/en/consulting/natural-hazards/>). Section [4. Flow-R advanced processing] provides details on the advantages of the **Flow-R advanced** processing compared to the **Flow-R on GEP** propagation modelling.

**Input specifications & supported EO data**

- Digital Elevation Model (DEM):

  - Copernicus DEM Europe with 10 m cell size (official name: EEA-10 [^id20])
  - Copernicus DEM World with 30 m cell size (official name: GLO-30 [^id20])
  - Custom DEM uploaded by user

- Raster file of source areas:

  - Custom source areas uploaded by user (for example with the value of 1 for source area cells and 0 or NoData for all non-source areas)
  - Source areas created by other services on GEP

:::{NOTE}
As best practice, these input files should have square cells, a metric coordinate system (e.g., UTM or national grid), metric elevation values and ideally 10 m cell size. **Flow-R** handles differences in cell size or extent between the DEM and source areas, but the required regridding may lead to errors. Possible differences in projection system are handled in the **Flow-R** service by reprojecting the DEM in the coordinate system of the source areas.
:::

**Output specifications**

- **Flow-R Runout**: raster file of the runout extent
- **Flow-R Sources**: raster file of the source areas
- **DEM**: a hillshade of the DEM
- Two compressed folders (TGZ files) containing these outputs as raw data (…output.tgz) or as preview files with fixed symbology (…preview.tgz)

## 2. Flow-R model setup

### 2.1 Access the **Flow-R** service on GEP

- Sign-in on the GEP portal: <https://geohazards-tep.eu/>
- Access the Thematic App containing the **Flow-R** service, for example the **eo4alps-landslides** Thematic App.
- Open the tab *Processing services* from the right of the map and select the processing service **Flow-R**.

:::{figure} assets/flowr_processing_service.png
:align: center
:figclass: align-center
:width: 850px
:::

### 2.2 Preparation of input data

This section describes the preparation of input data required for the **Flow-R** service.

- Navigate to the Area of Interest (AOI) in the geobrowser map (e.g., Solalex in the southwestern Swiss Alps)
- Use the *Draw polygon* or *Draw rectangle* tools in the geobrowser (hover over the upper left corner of the map to display the tools) to define your AOI or the *wkt* tool to upload or use an existing AOI (upload of shapefile (.zip), KML (.kml/.kmz) or geojson (.json) or well-formed WKT code)

:::{NOTE}
This step is not mandatory but highly recommended, especially when a Copernicus DEM is used.
:::

:::{figure} assets/flowr_parameters1.png
:align: center
:figclass: align-center
:width: 850px
:::

- Upload the user-defined source areas and optionally a custom DEM to your private storage on the GEP using the **Upload Data** button in the menu bar on the top. From the drop-down list under *Target Repository*, select your GEP username and keep the default *Target path* (i.e., “/results”)

:::{NOTE}
This step is not required if the source areas are provided as outputs of other GEP services and if a provided DEM source is used (e.g., *Copernicus Europe (10 m)* or *Copernicus World (30 m)*).
:::

### 2.3 Flow-R parameterization

This section describes the different parameters of the **Flow-R** service on GEP.

- **Job title**: provide a meaningful title for the **Flow-R** model run, such as “Flow-R \[Name of study area\] \[Hazard type\] \[Optional other parameters\]” (e.g., “Flow-R Solalex Rockfall LocalDEM10”).

:::{NOTE}
The date and time of the model run will be automatically added to the created output files (in UTC, Coordinated Universal Time).
:::

- **Area of Interest**: this optional parameter is used to define the processing extent indicated in longitude and latitude as text string in the format: “LongitudeMin,LatitudeMin,LongitudeMax,LatitudeMax” (no spaces) (e.g., “7.088,46.262,7.176,46.312”). Use the *magic wand* symbol to import the bounding box of the current selection polygon or rectangle as AOI (see above).

:::{NOTE}
If not specified, the **Area of Interest** is cropped to the user-uploaded DEM (if *Upload local DEM* is chosen as **DEM Source**) or to the **Source areas** (if *Copernicus Europe (10 m)* or *Copernicus World (30 m)* are chosen as **DEM Source**).
:::

- **DEM Source**: choose the data source of the DEM from the drop-down list, i.e., *Copernicus Europe (10 m)* (10 m cell size) [^id20], *Copernicus World (30 m)* (30 m cell size) [^id20] or *Upload local DEM*.

:::{NOTE}
If *Copernicus Europe (10 m)* is selected as *DEM Source* but not available over the chosen AOI, the **Flow-R** service automatically switches to the *Copernicus World (30 m)* DEM.
:::

- **Input third-party DEM**: specify the user-provided DEM previously uploaded to the private storage on GEP (see above). This parameter is only required if the *Upload local DEM* is selected under **DEM Source**.
- **Source areas**: specify the source areas of the mass movement previously uploaded to the private storage on GEP (see above) or from outputs of other GEP services.

:::{NOTE}
To access the uploaded files in your private storage click on Private --> My Store in the menu bar on the top. If an AOI is defined in the geobrowser (using the *Draw polygon*, *Draw rectangle* or *wkt* tools) only the user datasets that intersect the AOI are shown. Select the appropriate file and drag-and-drop it to the matching field in the **Flow-R** interface.
:::

- **Hazard (preset)**: choose the appropriate hazard type and parameter set from the drop-down list. Details on the currently implemented hazard types are provided in section [2.4 Flow-R hazard types].

- **Sources selection criteria – Condition**: select the logical condition (=, >, >=, \<, or \<=) from the drop-down list used to filter the provided source areas (in combination with the numerical value specified under **Sources selection criteria – Value**).

- **Sources selection criteria – Value**: specify the value used to filter the provided source areas (in combination with the logical condition specified under Sources selection criteria – Condition ).

:::{NOTE}
The input source areas can contain different numerical values (integer only), representing for example different levels of susceptibility/hazard or different mass movement types. Using the **Sources selection criteria** parameters allows processing only specific sources. Usually, the source areas have a value of 1, while non-source pixels have a value of 0 or NoData. In that case, the default condition (>=) and value (1) will consider all source areas for the propagation.
:::

- Click on the *Run Job* button at the bottom of the **Flow-R** interface.
- This automatically displays the *Job Info* window summarizing the parameters of the **Flow-R** processing. The progress bar allows checking the progress of the processing.

:::{figure} assets/flowr_parameters2.png
:align: center
:figclass: align-center
:width: 350px
:::

:::{figure} assets/flowr_jobinfo1.png
:align: center
:figclass: align-center
:width: 350px
:::

### 2.4 Flow-R hazard types

**Flow-R on GEP** contains parameter presets for these various hazard types calibrated for extreme events in the Alps. For the explanation of the various model parameters, the user is referred to the complete description of **Flow-R** in Horton et al. (2013) [^id19]. Following hazard presets are currently implemented:

- **Debris flows (Conservative)** for debris flows in Alpine torrents (permanent or intermittent): simplified friction-limited model (SFLM) with reach angle 10° and maximum velocity 15 m/s, Holmgren (1994) modified direction algorithm [^id19] [^id21] with exponent x=3 and height modification dh=2 m, and persistence algorithm with default weights
- **Debris flows (Large torrents)** for debris flows in large torrents: SFLM with reach angle 3° and maximum velocity 15 m/s, Holmgren modified direction algorithm with exponent x=2 and height modification dh=2 m, and persistence algorithm with default weights
- **Rockfall (Conservative)** for fragmental rockfalls (up to few m³ in volume): SFLM with reach angle 32° and maximum velocity 30 m/s, Holmgren modified direction algorithm with exponent x=1 and height modification dh=1 m, and persistence algorithm with Gamma (2000) [^id22] weights
- **Shallow landslide (Mudflow)** for superficial landslides transforming into mudflows: SFLM with reach angle 19° and maximum velocity 8 m/s, Holmgren modified direction algorithm with exponent x=24 and height modification dh=1 m, and persistence algorithm with cosine weights
- **Shallow landslide (Roto-translational slide)** for superficial landslides without transformation into mudflows: SFLM with reach angle 27° and maximum velocity 2 m/s, Holmgren modified direction algorithm with exponent x=18 and height modification dh=1 m, and persistence algorithm with cosine weights
- **Rock avalanches (volume \< 120,000)** for large rock slope failures involving a volume of rock smaller than 120,000 m³: SFLM with reach angle 30° and no velocity limit, Holmgren modified direction algorithm with exponent x=1 and height modification dh=10 m, and persistence algorithm with memory effect over 30 cells and an opening of 240°.
- **Rock avalanches (volume: 80,000 – 400,000)**: parameters as above with a reach angle of 25°.
- **Rock avalanches (volume: 250,000 – 1,200,000)**: parameters as above with a reach angle of 22°.
- **Rock avalanches (volume: 800,000 – 4,000,000)**: parameters as above with a reach angle of 19°.
- **Rock avalanches (volume: 2,500,000 – 12,000,000)**: parameters as above with a reach angle of 16°.
- **Rock avalanches (volume: 8,000,000 – 40,000,000)**: parameters as above with a reach angle of 14°.
- **Rock avalanches (volume: 25,000,000 – 120,000,000)**: parameters as above with a reach angle of 12°.
- **Snow avalanches (Powder Conservative)** for powder snow avalanches in the Alps: Perla (1980) [^id23] model with friction parameter mu=0.3 and mass-to-drag ratio md=2500, Holmgren modified direction algorithm with exponent x=4 and height modification dh=5 m, and persistence algorithm with default weights

:::{NOTE}
Additional information on the types of hazards (materials, failure mechanisms, and propagation behaviors implied) is detailed in Hungr et al. (2014) [^id24].
:::

:::{NOTE}
These hazard presents lead to conservative propagation extents appropriated for susceptibility or indicative hazard mapping at regional scale. Terranum Sàrl provides on-demand, advanced processing including calibration of propagation parameters to local landslide inventories and the distinction between extreme, rare, and current landslide events using susceptibility levels (<https://www.terranum.ch/en/consulting/natural-hazards/>). Section [4. Flow-R advanced processing] provides details on the advantages of the **Flow-R  advanced** processing compared to **Flow-R on GEP** propagation modelling.
:::

## 3. Flow-R modelling results

- Check the modelling progress in the *Jobs* tab under “Processing Services” or in the detailed job information window (if necessary, refresh the job status by clicking on the status button)
- Once the **Flow-R** model run is successfully completed, click on the *Show results* button at the bottom of the job information window.

:::{NOTE}
Clicking on the *Contact Service Provider* button under “Commercial Support” opens the contact form for **Flow-R advanced** modelling as detailed in section [4. Flow-R advanced processing].
:::

:::{figure} assets/flowr_jobinfo2.png
:align: center
:figclass: align-center
:width: 350px
:::

- The **Flow-R** modelling results are displayed on the map of the geobrowser and listed in the *Results* tab in the window on the left side. The results comprise a hillshade of the DEM, the source areas, and the runout areas. Moreover, the results contain two archive files (TGZ format that can be downloaded and directly opened on your computer): one with the raw outputs (…output.tgz) and one with the rendered preview files (…preview.tgz)

:::{NOTE}
The runout areas are binary maps with the value of 1 for areas reached by the mass movement and the value of 0 for areas not reached. These runout areas discard pixels with a maximum reach susceptibility smaller than 0.005 (see Horton et al. (2013) [^id19] for details).
:::

:::{figure} assets/flowr_results.png
:align: center
:figclass: align-center
:width: 850px
:::

- To download the results, select the output.tgz file in the “Results” tab and click on the folder icon “Show details” in the lower right corner. Then, click on the “Download” button in the lower left corner.
- Unpack the TGZ file and add the Flow-R modelling results to your GIS software.

:::{figure} assets/flowr_results_download.png
:align: center
:figclass: align-center
:width: 650px
:::

## 4. Flow-R advanced processing

The **Flow-R on GEP** service uses predefined parameter sets for the different hazard types calibrated for extreme events in the Alps (see section [2.4 Flow-R hazard types]), which lead to conservative propagation extents. Terranum, as service provider and developper of **Flow-R**, offers on-demand customized processing. This **Flow-R advanced** modelling is tailored to the user's study area, requirements and available data. **Flow-R advanced** is based on extensive calibration and customization of model parameters, using for example databases and maps of past landslide events in the area of interest. Compared to the outputs of **Flow-R on GEP**, **Flow-R advanced** processing results include:

- Multiple runout areas distinguishing extreme events from rare and current scenarios
- Assess the reach susceptibility and preferential runout paths
- Highlight the runout area for each source area individually
- Assess the effect of protective forests on the runout areas
- Integration of the failure susceptibility of landslide source areas
- Filtering of anthropogenic source areas or very small runout areas

Moreover, Terranum has broad expertise in the assessment of source areas for all relevant landslide types.

:::{figure} assets/flowr_advanced_comparison.png
:align: center
:figclass: align-center
:width: 850px
:::

### Interested by **Flow-R advanced** processing?

If you want to complement results of a processed **Flow-R on GEP** job with Terranum's advanced processing, send a request to Terranum by clicking on the *Contact Service Provider* button under “Commercial Support” in the detailed job information window.

:::{figure} assets/flowr_advanced_contact.png
:align: center
:figclass: align-center
:width: 350px
:::

This opens the contact form for **Flow-R advanced** modelling, which automatically includes the parameterization of the selected **Flow-R** job. Please provide additional information about your request, particularly the study area, required scale/resolution, relevant hazard types and a brief description of available input data (DEM, source areas, datasets for calibration and validation etc.). Ideally, copy the text below and paste it into the *User's notes* section of the contact form:

I am requesting a quote for Flow-R advanced processing based on this Flow-R job:

- Area of interest: \[please specify\]
- Study scale/resolution: \[ \] Medium (25m, 1:500'000) / \[ \] High (10m, 1:25'000) / \[ \] Very high (5m, 1:10'000)
- Hazard type: \[ \] Shallow landslide / \[ \] Mudflow / \[ \] Debris flow / \[ \] Rockfall / \[ \] Rock avalanche / \[ \] Snow avalanche
- Available geodatasets: \[ \] Landslide inventory / \[ \] Local DEM / \[ \] Geological map / \[ \] Land-use map
- Additional information: \[please add\]
- Contact information: \[please specify your name, institution and e-mail address\]

:::{figure} assets/flowr_contact_service_provider.png
:align: center
:figclass: align-center
:width: 700px
:::

:::{NOTE}
For any questions about **Flow-R advanced** processing, you may contact Terranum via <https://www.terranum.ch/en/about/>
:::

## 5. Feedback

Users are kindly invited to report any issue and problem encountered during the use of the **Flow-R** service by issuing a ticket from their project support space on <https://helpdesk.terradue.com/> or sending an email to <mailto:support@terradue.com>
Suggestions and comments about the GEP service delivery are warmly welcomed on <mailto:contact@geohazards-tep.eu> to keep the service delivery on GEP as much as possible appealing, effective, and efficient.

## 6. Terms and Conditions

**Intellectual Property Right** | The Intellectual Property Right of the Flow-R service (called “Service” hereafter) lies with Terranum Sàrl (Rue de l’Industrie 35b, CH-1030 Bussigny, Switzerland, called “Terranum”), if not differently specified. By using the Service, you agree to be bound by these *Terms and Conditions* and that they are enforceable like any written negotiated agreement signed by you. In case of any concern with these *Terms and Conditions*, please contact Terranum via <https://www.terranum.ch/en/about/> for additional information before using the Service.

**Use** | The Service is available to all GEP users according to a CC-BY license [^id25]. There is the possibility that users participate in the cost of service maintenance and operation: these costs are defined case-by-case among the Service provider, Terranum, the Ressource provider, Conectus/EOST, and the Platform operator, Terradue Srl.

**Results** | The results of the Service are freely shareable and adaptable with appropriate credits under the CC-BY license [^id25].

**Warranty and limitation of liability** | Terranum accepts no responsibility for the operation or performance of the Service. The entire risk of use and consequences of use of the Service falls completely on you and Terranum shall not be liable in any respect for any loss claims or injury alleged to have resulted from use of or in reliance on software product. In this respect, you shall indemnify and defend against any and all claims, including claims by third parties or by your employees, which arise directly or indirectly out of your use or operation of the Service. Terranum’s sole obligation under this warranty is to use reasonable efforts to correct any non-conforming software.
You acknowledge that you have read the foregoing disclaimers of warranty and limitation of liability and understand that you assume the entire risk of use of the Service. In no event will Terranum be liable to you for any damages, claims or costs whatsoever or any consequential, indirect, incidental damages, or any lost profits or lost savings, even if a Terranum representative has been advised of the possibility of such losses, damages, claims or costs or for any claim by any third party. Terranum will not be liable for any damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the Service, even if Terranum has been advised of the possibility of such damages. In any case, Terranum’s entire liability under any provision of this agreement shall be limited to the amount actually paid by you for the Service. The foregoing limitations and exclusions apply to the extent permitted by applicable law in your jurisdiction. Terranum’s aggregate liability and that of its suppliers under or in connection with this agreement shall be limited to the amount paid for the software, if any.

## 7. References

[^id19]: Horton, P., Jaboyedoff, M., Rudaz, B., and Zimmermann, M. (2013): Flow-R, a model for susceptibility mapping of debris flows and other gravitational hazards at a regional scale. Natural Hazards Earth System Sciences 13, 869-885, doi:10.5194/nhess-13-869-2013.

[^id20]: ESA (2021): Copernicus DEM - Global and European Digital Elevation Model (COP-DEM). Website of the European Space Agency, <https://spacedata.copernicus.eu/web/cscda/dataset-details?articleId=394198>

[^id21]: Holmgren, P. (1994): Multiple flow direction algorithms for runoff modelling in grid based elevation models: An empirical evaluation. Hydrol. Process. 8, 327–334, doi:10.1002/hyp.3360080405.

[^id22]: Gamma, P. (200): dfwalk – Ein Murgang-Simulationsprogramm zur Gefahrenzonierung. PhD thesis, Geographisches Institut der Universität Bern (in German).

[^id23]: Perla, R., Cheng, T.T., and McClung, D.M. (1980): A two-parameter model of snow-avalanche motion. J. Glaciol. 26, 197–207.

[^id24]: Hungr, O., Leroueil, S., and Picarelli, L. (2014): The Varnes classification of landslide types, an update. Landslides. 11, 167-194.

[^id25]: Creative Commons Attribution 4.0 International (CC BY) licence: <https://creativecommons.org/licenses/by/4.0/>
