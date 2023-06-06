# GDM-OPT-ETQ: Multiple Pairwise Image Correlation of OPTical images for EarThQuake analysis

```{image} assets/GDM-OPT-ETQ.png
```

**GDM-OPT** stands for Ground Deformation Monitoring with OPtical image Time-series. The service is developed and maintained by CNRS/EOST (Strasbourg) with contribution of IGN/Matis (Marne-la-Vallée) and CNRS/IPGP (Paris). The service allows the processing of optical image pairs for the monitoring of Earth surface deformation.

**GDM-OPT-ETQ** stands for Earthquake-triggered crustal deformation. It is designed for **quantifiying co-seismic deformation along faults triggered by large magnitude earthquakes**. It enables the on-demand processing of Sentinel-2 image time series. It provides 1) a module for image matching of multiple image pairs susing pixel and sub-pixel image correlation or optical flow, 2) a module for image pairs geometrical correction and filtering, and 3) a module for the spatio-temporal analysis of surface motion. It builds on the MicMac (IGN/Matis; Rosu et al., 2015 \[1\]), GeFolki (ONERA; Brigot et al., 2016 \[2\]), CO-REGIS (CNRS/EOST; Stumpf et al., 2017 \[3\]),
MPIC (Stumpf et al., 2018 \[4\]) and FMask (Texas Tech University; Qiu et al., 2019 \[5\]) algorithms. The service is designed for the processing of a maximum of 4 Sentinel-2 images with 2 images before the earthquake (pre-event) and 2 images after the event (post-event). It is an on-demand service tailored for quantifying co-seismic deformation from a limited number of images and a few number of parameters which makes it easy to use by non-experts.

**EO sources**:

> - Sentinel-2 MSI L1C

**Outputs**

Four **service outputs** are provided for visualization on GEP:

- **Mean displacement magnitude:** It consists of a GeoTIFF image representing the mean displacement magnitude over all time steps. The unit is in  *m*. The naming convention is *MM_Mean_displ_magnitude_tile_date1_to_dateN.tif*
- **Mean displacement:** TIt consists of two GeoTIFF images representing the mean displacement in the E−W and N−S direction. The unit is in *m*. The naming convention is *MM_Mean_displacement_EW_tile_date1_to_dateN.tif* and *MM_Mean_displacement_NS_tile_date1_to_dateN.tif*.
- **Quality:** It consists of a GeoTIFF image representing the percentage, per pixel, of the pairs with a correlation score *NCC > minimum correlation threshold*.

Four **service output folders** are provided for download by the user:

- **Analysis:** Folder containing the four products described above in float GeoTIFF file formats.
- **Displacements:** Folder containing the correlation grids and the corrected and filtered displacement field grids.
  : - **Corrected displacement fields for each time step:** Float GeoTIFF files representing the measured displacement among the two respective input images in pixels in E-W direction (East is positive) and N-S direction (South is positive) after application of the corrections selected by the user. The naming conventions are *MM_EW_displ_tile_date1_vs_date2_corrected.tif* and *MM_NS_displ_tile_date1_vs_date2_corrected.tif* respectively.
    - **Filtered displacement fields for each time step:** Float GeoTIFF files representing the measured displacements among the two respective input images in pixels in E-W direction (East is positive) and N-S direction (South is positive) after filtering. The naming conventions are *MM_EW_displ_tile_date1_vs_date2_FILTER_Displmax.tif* and *MM_NS_displ_tile_date1_vs_date2_FILTER_Displmax.tif* respectively.
    - **Correlation scores:**  Folder containing 8-bit GeoTIFF images representing the correlation score for each time step with the correlation coefficient \[0,1\] quantized in the range \[128,255\]. The naming convention is *MM_Corr_tile_date1_date2.tif*.
- **Masks:** Folder containing the masks used in the processing.
  : - **Decorrelation mask:**  8-bit GeoTIFF image representing the decorrelation mask for each time step. The naming convention is *tile_date1_date2_decorrel_mask.tif*.
    - **Cloud mask:** 8-bit GeoTIFF images representing the cloud mask for each time step. Six flags are indicated: 0 = clear sky pixel; 1 = null; 2 = cloud pixel; 3 = cloud shadow pixel; 4 = snow pixel; 5 = water pixel. The naming convention is: *Tile_date_spectral_mask.tif*.
    - **Slope mask:** 8-bit GeoTIFF images representing the slope mask. The naming convention is: *Tile_slope_mask_mask.tif*
- **Preview:** Folder containing the four browse products of the analysis folder.

% **Convention:** The displacement and the mean velocity products are displayed with the following convention: in the **Forward** mode, **Positive values** are towards the **South** and the **East**; in the **Forward+Backward** mode, the products of the **Backward** time direction have opposite signs as compared to the ones in the **Forward** time direction.

______________________________________________________________________

The tutorial introduces the use of the **GDM-OPT-ETQ** service for the quantification of co-seismic motion. To this end we will process Sentinel-2 images acquired before and after the Ridgecrest earthquake sequence (California, USA, 2019).

## Select the processing service

- Login to the platform (see {doc}`user <../community-guide/user>` section)
- Go to the Geobrowser, expand the panel “Processing services” on the right hand side and select the processing service “GDM-OPT-ETQ”:

:::{figure} assets/tuto_mpicetq_1.png
:align: center
:figclass: align-center
:width: 750px
:::

This will display the service panel including several tunable parameters.

:::{figure} assets/tuto_mpicetq_2.png
:align: center
:figclass: align-center
:width: 750px
:::

## Use case: Analysis of the July 2019 Ridgecrest Earthquake sequence

### Select input data

The Geobrowser offers multiple ways to search a large variety of EO-based dataset and the user should refer to the {doc}`Geobrowser <../community-guide/platform/geobrowser>` section for a general introduction.
For this tutorial we will use a data package which is accessible through the "Data Packages" tab on the upper left of the screen. If you type "Ridgecrest" into the search box you should be able to find a data package named "Ridgecrest_2019_S2_2im". Alternatively you can access the [Ridgecrest data package] directly by clicking on the link:
.. `` _`Ridgecrest datapackage` ``: <https://geohazards-tep.eu/t2api/share?url=https%3A%2F%2Fgeohazards-tep.eu%2Ft2api%2Fdata%2Fpackage%2Fsearch%3Fid%3DRidgecrest_2019_S2_2im>

:::{figure} assets/tuto_mpicetq_3.png
:align: center
:figclass: align-center
:width: 750px
:::

Click on the data package, hold Shift and Drag and Drop all four products in the *Sentinel-2 products* field in the service panel on the right:

:::{figure} assets/tuto_mpicetq_4.png
:align: center
:figclass: align-center
:width: 750px
:::

:::{Warning}
Sentinel-2 datasets distributed before 27 September 2016 contain multiple tiles. For such datasets the *Geobrowser* currently returns several results including both the original multi-tile dataset and a preview of the footprints of the tiles. For processing, you must select **only** the original multi-tile datasets. For datasets after 27 September 2016, there is no such ambiguity.
:::

### Set the processing parameters

There are 16 processing parameters that can be adjusted. A short explanation of the parameter is provided when hovering over the parameter fields.

- **DEM:** Defines the Digital Elevation Model used for filtering the displacement fields. The *Merit* [^id11] and the *COP-DEM_GLO-30* [^id12] are available to GEP users. The default DEM is the Merit DEM.
- **Sentinel-2 band:** Defines the Sentinel-2 band for matching. The option *B04* is recommended since the red band is also used for band to band co-registration by the ESA Sentinel-2 production center.
- **Split date:** Is an optional parameter of the form "yyyy-MM-dd" which will split the time series into two subsets. Pairs will only be formed among members of different subsets. This is particularly interesting in the case of quantifying co-seismic displacement. The default value is left empty.
- **Minimum matching range:** Defines the minimum matching range for creating the image pairs. The matching range is expressed in *acquisitions* so if a minimum range is set to 1, all the images (N) will be paired with at least the next image in time (N+1). The default value is set to 1.
- **Maximum matching range:** Defines the maximum matching range for creating the image pairs. The matching range is expressed in *acquisitions* so if a maximum range is set to 2, all the images (N) will be paired with at most the next second image in time (N+2). The default value is set to 5.
- **Matching direction:** Define the time direction for the matching. If *Forward* is selected, the pairs are only created in the time direction. If *Forward+Backward* is selected, the pairs will be created in both directions (i.e. time and reverse time direction). The default value is set to *Forward*.

:::{Warning}
Choosing the *Forward+Backward* option has to be carefully considered by the user as it increases the number of pairs created and hence, the computing time and resources.
:::

- **Window size:** Controls the size of the template used for matching. It controls the neighborhood around the central pixel. The minimum value is 1 (3x3 pixels) and the maximum value is 7 (15x15 pixels). The default value is *3* (7x7 pixels). A smaller window size allow better reconstructing small scale variations but can lead to more noise. Vice versa, larger window sizes lead to greater robustness against noise but smooth small scale details. For large scale motion such as co-seismic slip, we recommend to use large window sizes.
- **Decorrelation threshold:** Discards the matches with a correlation coefficient below a value expressed in the range \[0,1\]. The default value is *0.2*.
- **Spatial matching range:** Defines the search range in pixel for finding matches based on the template. The actual search range is computed from this parameter as round(Spatial matching range/0.8)+2. The parameter has to be adjusted according to the maximum expected displacement taking into account possible coregistration biases of the input images.
- **Regularization parameter:** Similar to the window size, controls the smoothness of the expected motion field. Increasing the regularization parameter puts greater emphasis on a smooth motion field where neighboring pixels will have similar displacement values. For large scale features such as co-seismic displacement, large value lead to smoother and less noisy results. The default value is *0.3*.
- **Use a direction for regularization:** By default the regularization is isotropic but the user can choose a direction for the regularization meaning the displacement field will constrain a smooth gradient in this direction.
- **Direction of the fault plane / Teta0:** Direction for the regularization, in the case of strike-slip earthquake and if the a priori known, it is recommended to chose the direction of the fault (with East Teta0=0).
- **Snow mask:** If set to *True*, the areas of the images covered by snow are masked. The default value is set to *True*.
- **Cloud mask:** If set to *True*, the areas of the images covered by clouds are masked. The default value is set to *True*.
- **Slope mask range minimum:** The pixels located on terrain slopes with a slope angle larger than the value set with the parameter are filtered out in the products. By default, the parameter is set to *80*, so pixels located on slopes with angle larger than 80 degrees are filtered.
- **Slope mask range maximum:** The pixels located on terrain slopes with a slope angle smaller than the value set with the parameter are filtered out in the products. By default, the parameter is set to *90* degrees, so pixels located on slopes with angle between *Slope mask range minimum* and 90 degrees are filtered.
- **Apply correction and filtering:** If set to *True*, the geometric corrections (as described in [^id8] )and the filtering (as described in [^id9]) are applied. They are highly recommended for any use case and are applied by default.
- **Apply correction and filtering:** If set to *True*, the jitter undulation observed in Sentinel-2 images are filtered out [^id13]. This correction is recommended for displacement fields with large spatial wavelength like co-seismic displacemnet fields. By default, the paratemeter is *True* and the correction is applied.

### Run the job

- You are good to go. Click on the button *Run Job* at the bottom of the right panel.

:::{figure} assets/tuto_mpicetq_5.png
:align: center
:figclass: align-center
:width: 750px
:::

- Once the job has finished, click on the *Show results* button to obtain a list of products for visualization.

:::{note}
The products in the *Geobrowser* are previews. The user needs to download the results for further analysis and interpretation.
:::

:::{figure} assets/tuto_mpicetq_6.png
:align: center
:figclass: align-center
:width: 750px
:::

### Disclaimer

The GDM-OPT services are scientific softwares provided at the best <mailto:CNRS/ForM@Ter> (EOST/A2S) knowledge according to state-of-the-art image matching algorithms. No warranty is provided on the processors and results of the services. <mailto:CNRS/ForM@Ter> (EOST/A2S) is not responsible for any software inaccuracies, bugs, errors and misuse. Generated results have a defined accuracy according to the relevant scientific publications available in the literature. Result accuracy is estimated on a statistical basis. Provided results are not validated by <mailto:CNRS/ForM@Ter>  and, indeed, it is user responsibility to validate them. <mailto:CNRS/ForM@Ter>  is not responsible for the use, quality, accuracy and interpretation of results and products that are generated by using the processors and services provided within the platform. <mailto:CNRS/ForM@Ter>  is not responsible for the use, quality, accuracy and interpretation of third party results, products and services derived from the use of the  processors and services. <mailto:CNRS/ForM@Ter>  is not responsible of possible outages of the provided services. <mailto:CNRS/ForM@Ter>   is not responsible of any kind of third party loss derived from service outage, result inaccuracies, software errors of the provided services and products. The maintenance, update and user support are provided by EOST/A2S free of charge and at best effort. EOST/A2S is not responsible for any consequence derived from delays on replies to user requests or support inaccuracies.

- **CNRS**: Centre National de la Recherche Scientifique / French National Research Council
- **ForM@Ter**: Pôle Terre Solide / Solid Earth Centre
- **EOST**: Ecole et Observatoire des Sciences de la Terre / School and Observatory of Earth Sciences
- **A2S**: Application de Surveillance par Satellite / Application Satellite Survey

## References

[^id6]: Rosu, A. M., Pierrot-Deseilligny, M., Delorme, A., Binet, R., & Klinger, Y. (2015). Measurement of ground displacement from optical satellite image correlation using the free open-source software MicMac. ISPRS Journal of Photogrammetry and Remote Sensing, 100, 48-59.

[^id7]: Brigot, G., Colin-Koeniguer, E., Plyer, A., & Janez, F. (2016). Adaptation and evaluation of an optical flow method applied to coregistration of forest remote sensing images. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 9(7), 2923-2939.

[^id8]: Stumpf, A., Malet, J.-P. and Delacourt, C. (2017). Correlation of satellite image time-series for the detection and monitoring of slow-moving landslides. Remote Sensing of Environment, 189: 40-55. DOI:10.1016/j.rse.2016.11.007

[^id9]: Stumpf, A., Michéa, D. Malet, J.-P. (2018). Improved co-registration of Sentinel-2 and Landsat-8 imagery for Earth surface motion measurements. Remote Sensing, 10, 160. DOI:10.3390/rs10020160

[^id10]: Qiu, S., Zhu, Z., & He, B. (2019). Fmask 4.0: Improved cloud and cloud shadow detection in Landsats 4–8 and Sentinel-2 imagery. Remote sensing of environment, 231, 111205.

[^id11]: Yamazaki D., Ikeshima, D., Tawatari, R., Yamaguchi, T., O'Loughlin, F., Neal, J.-C., Sampson, C.C., Kanae, S., and Bates, P.D. (2017). A high accuracy map of global terrain elevations. Geophysical Research Letters, 44: 5844-5853, DOI:10.1002/2017GL072874

[^id12]: Copernicus Services Coordinated Interface / CSCI (2020). Copernicus DEM - Global and European Digital Elevation Model (COP-DEM). <https://spacedata.copernicus.eu/web/cscda/dataset-details?articleId=394198>

[^id13]: Provost, F., Michéa, D., Malet J.-P., Boissier, E., Pointal, E., Stumpf, A., Pacini F., Doin M.-P., Lacroix, P., Proy, C., Bally, P. Terrain deformation measurements from optical satellite imagery: the MPIC-OPT processing services for geohazards monitoring. Remote Sensing of Environment.Volume 274, 2022, 112949, ISSN 0034-4257, <https://doi.org/10.1016/j.rse.2022.112949>.
