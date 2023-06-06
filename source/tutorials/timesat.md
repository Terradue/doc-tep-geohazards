# TimeSAT - Ground motion pattern detection and classification in satellite image time series

:::{figure} assets/tuto_timesat_icon.png
:width: 100px
:::

**TimeSAT**

Satellite image time series and derived products are increasingly available thanks to the launch of Earth Observation missions which aim at providing a coverage of the Earth every few days with high spatial resolution. The high revisit time of Copernicus (Sentinel-1, Sentinel-2) and Landsat satellites allow for the setup of systematic calculation of ground motion products, opening the way to science and operational monitoring capacities of geohazards. Many services are deployed in order to offer to users systematic or on-demand calculation of optical and InSAR time series products representing ground deformation.
Satellite-derived products and services (e.g. EGMS; EPOS satellite products; GEP, Comet and ARIA services, etc) for the processing of SAR and optical imagery allow accessing displacement/velocity time series over large areas and time periods. Exploiting these datasets (stacks of interferograms, PSInSAR time series, optical derived ground motion, possibly organized in datacubes) necessitates the development of post-processing tools in order to combine the datasets and investigate the spatial and temporal behavior of the studied variables.

TimeSAT is a service developed by CNRS-EOST (Strasbourg, France) for classifying ground motion displacement time series in specific behaviors/patterns, detect changes in the time series (increase, decrease, periodicity) and identify spatial clusters of homogeneous styles of ground motion. The service currently allows ingesting PSInSAR and SBAS InSAR time series and optical offset-tracking time series. It consists of:

1. A module for data pre-processing (advanced Savitzky-Golay filtering, data subset masking);
2. A module for time series classification, for which several processing workflows are possible:

> - Mode 1 / supervised: The classification in pre-defined distinctive patterns (uncorrelated trend, linear trend, quadratic trend, bilinear trend) based on a sequence of conditional statistical tests,
> - Mode 2 / unsupervised: The classification using a combination of principal component analysis (IPA) and independent component analysis (ICA) to detect and classify specific patterns.

TimeSAT allows the processing of time series non structured and unevenly distributed in time and in space. The workflow is computationally optimized and parallelised and is implemented on the Mésocentre/HPC infrastructure of the University of Strasbourg. Thanks to the parallelization and scaling of the code, the processing of about 1 million time series (pixel, PS/DS points) of 5 a years period lasts less than 2 hours.

TimeSAT Pre-processing is using Python librairies based on [^id12] and [^id13],

TimeSAT Mode 1 implements part of the supervised classification approach described in [^id14] using advanced statistical tests [^id15], [^id16], [^id17],

TimeSAT Mode 2 implements unsupervised classification approaches such as those used by [^id18], [^id19] and [^id20].

**EO sources supported**:

> - PSInSAR (Snapping FullRes, SqueeSAR, or any other PSInSAR methods) and SBAS InSAR time series. Format: standard Comma-Separated Values (.csv) format in geographic coordinates.
> - Optical offset-tracking time series (GDM-OPT-SLIDE, GDM-OPT-ICE, or any other offset tracking methods). Format: standard Comma-Separated Values (.csv) format in geographic coordinates.

**Output specifications**

> - Mode 1 / supervised classification: Format: standard Comma-Separated Values (.csv) format in geographic coordinates.
>
> - Mode 2 / unsupervised classification: Format: standard Comma-Separated Values (CSV) format in geographic coordinates.
>
> - One report (.pdf file) summarizing the processing and presenting statistics on the results.

______________________________________________________________________

**Processing workflows**

:::{figure} assets/timesat_tuto_img1.png
:align: center
:figclass: align-center
:width: 750px
:::

:::{figure} assets/timesat_tuto_img2.png
:align: center
:width: 350px
:::

This tutorial introduces to the use of the ground motion classification service TimeSAT.

There are two versions available for the service (basic, advanced). This tutorial describes all the parameters and details the ones associated with the advanced version of the service.

## Select the processing service

- Login to the platform (see {doc}`user <../community-guide/user>` section)
- Go to the Geobrowser, expand the panel “Processing services” on the right hand side and select the processing service TimeSAT”:

:::{figure} assets/timesat_tuto_img3.png
:align: center
:figclass: align-center
:width: 750px
:::

This will display the service panel including several (22 for the advanced mode, 13 for the basic mode) pre-defined parameters which can be adapted.

This figure displays all the parameters; the advanced parameters are indicated in grey color.

:::{figure} assets/timesat_tuto_img4.png
:align: center
:figclass: align-center
:width: 750px
:::

## Select input data

Select My store from the Private pulldown menu:

:::{figure} assets/timesat_tuto_img5.png
:align: center
:figclass: align-center
:width: 750px
:::

Drop the archive in the field of the service panel named "Input file":

:::{figure} assets/timesat_tuto_img6.png
:align: center
:figclass: align-center
:width: 750px
:::

## Set the processing parameters

Some processing parameters can be adjusted. When hovering over the parameter fields, you will see a short explanation for each of the parameters.

**General**
: - **Job title:** Defines the title of the job
  - **Input data:** Input data in csv or kml format
  - **Time series classification approach:** Type of classification approach (e.g. supervised / mode 1 or unsupervised /mode 2 pattern identification or both)

**Data selection**
: - **Use RoI (Region Of Interest)** If set to *True* the spatial data selection is activated
  - **Region Of Interest bounding box** Define the bounding box of the Region of Interest (RoI)
  - **Slope mask** If set to *True* the data selection based on the slope in activated (Slope computed using Copernicus DEM)
  - **Slope mask: range minimum / maximum** Defines the slope range for which the points are keeping
  - **Minimum quality threshold (coherence or correlation)** Defines a minimum InSAR interferogram coherence OR coefficient of correlation for image correlation for which the points are keeping

**Pre-processing**
: - **Pre-processing: Length of filtering window for outlier removal** Defines the length of the sliding window for outlier removal using Hampel identifier
  - **Pre-processing: Standard deviation value for outlier removal** Defines the number of standard deviations to detect the outlier using Hampel identifier
  - **Pre-processing: Length of filtering window for time series smoothing** Defines the length of filtering window (Savitzky-Golay filter): the value must be less than or equal to the number of dates in the time series
  - **Pre-processing: Polynomial order for time series smoothing** Defines the order of the polynomial used for sample fitting (Savitzky-Golay filter): the value must be less than the length of the filtering window.

**Mode 1: Supervised classification**
: - **Supervised classification: Linear term level of significance** Defines the linear ANOVA test threshold (α1): the time series is classified as uncorrelated pattern if α1 \< p-value.
  - **Supervised classification: Quadratic term level of significance** Defines the quadratic ANOVA test threshold (α2): the time series is classified as linear pattern if α2 \< p-value.
  - **Supervised classification: Piecewise linear pattern level of significance** Defines the BIC threshold (Bth): the time series is classified as piecewise linear pattern if the minimum BIC of segmented regression models is less than the BIC of quadratic and linear models and if the evidence ratio is > Bth.
  - **Supervised classification: Value for testing the significance of the discontinuity at the break point** Defines the significance of vertical jump at the break point for segmented regression models
  - **Supervised classification: Value for testing the significance of velocity change** Defines the linear ANOVA test threshold (α3): the velocity change is significant if there is a significant linear trend in the second part of the time series after linear modeling of the first part of the time series (α3 \< p-value).

**Mode 2: Unsupervised classification**
: - **Unsupervised classification: PCA explained variance (used to determine the component number)** Defines the desired percentage of explained variance by the usupervised analysis. It will allow to estimate the number of necessary components.

Non-expert users are advised to keep the default values or to use the basic version of the code.

### Run the job

- You are good to go. Click on the button *Run Job* at the bottom of the right panel. Depending on the allocated resources the execution will require a few hours to terminate.

:::{figure} assets/timesat_tuto_img7.png
:align: center
:figclass: align-center
:width: 750px
:::

- Once the job has finished, click on the *Show results* button to get a list and a pre-visualization of the results.

:::{note}
The pre-visualization in the *Geobrowser* is only a preview. To generate this preview the csv files are rasterized with a resolution of 0.0001°. For further analysis and post-processing, the results have to be donwloaded.
:::

:::{figure} assets/timesat_tuto_img8.png
:align: center
:figclass: align-center
:width: 750px
:::

- Example of the classification obtained with Timesat / Mode 1 over the Jegihorn Landslide (Switzerland) with PSInSAR time series (SqueeSAR processing by TRE-Altamira.

:::{figure} assets/timesat_tuto_img9.png
:align: center
:figclass: align-center
:width: 750px
:::

:::{figure} assets/timesat_tuto_img10.png
:align: center
:figclass: align-center
:width: 750px
:::

## References

[^id12]: Savitzky, A, Golay, MJE (1964). Smoothing and Differentiation of Data by Simplified Least Squares Procedures, Anal. Chem., 36(8), 1627-1639

[^id13]: Davies, L., U. Gather, U. (1993). The identification of multiple outliers, Journal of the American Statistical Association, 88 (1993), pp. 782-792

[^id14]: Berti, M., Corsini, A., Franceschini, S., Iannacone, J.P. (2013): Automated classification of Persistent Scatterers Interferometry time series, Nat. Hazards Earth Syst. Sci., 13, 1945–1958, <https://doi.org/10.5194/nhess-13-1945-2013>.

[^id15]: Davis, J. C.: Statistics and Data Analysis in Geology, John Wiley and Sons, New York, USA, 1986.

[^id16]: Main, I.G., Leonard, T., Papasouliotis, O., Hatton, C. G., and Meredith, P.G. (1999). One slope or two? Detecting statistically significant breaks of slope in geophysical data with application to fracture scaling relationships, Geophys. Res. Lett., 26, 2801–2804.

[^id17]: Schwarz, G.: Estimating the dimension of a model, Ann. Statistics, 6, 461–464, 1978.

[^id18]: Gaddes, M.E., Hooper, A., Bagnardi, M., Inman, H., & Albino, F. (2018). Blind signal separation methods for InSAR: The potential to automatically detect and monitor signals of volcanic deformation. Journal of Geophysical Research: Solid Earth, 123, 226–251. <https://doi.org/10.1029/2018JB016210>

[^id19]: Gaddes, M.E., Hooper, A., & Bagnardi, M. (2019). Using machine learning to automatically detect volcanic unrest in a time series of interferograms. Journal of Geophysical Research: Solid Earth, 124, 12304– 12322. <https://doi.org/10.1029/2019JB017519>

[^id20]: Ebmeier, S.K. (2016). Application of independent component analysis to multitemporal InSAR data with volcanic case studies, J. Geophys. Res. Solid Earth, 121, 8970– 8986, doi:10.1002/2016JB013765.
