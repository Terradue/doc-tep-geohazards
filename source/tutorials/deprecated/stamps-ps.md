# StaMPS Permanent Scatterer processing

This service (\[StaMPS Permanent Scatterer GitHub\](<https://github.com/Terradue/doc-tep-geohazards/blob/develop/source/tutorials/stamps-ps.rst>)) was made available in the GEP processing services list as part of the GEP Early Adopters Programme (2016-2020).

```{image} assets/tuto_stamps_icon.png
```

**StaMPS Permanent Scatterer**

StaMPS (Stanford Method for Persistent Scatterers) is a software package that implements an InSAR persistent scatterer (PS) method developed to work even in terrains devoid of man-made structures and/or undergoing non-steady deformation. This processing service is the StaMPS Permanent Scatterer (PS).

**EO sources supported**:

> - Envisat ASAR Image Mode Level 0 (ASA_IM\_\_1P)

**Output specifications**

> - matlab files

______________________________________________________________________

This processing service is in beta phase.

This processing service uses the StaMPS [^f1] version 3.3b1, patched:

- Includes computation of Oscillator drift from ENVISAT ASAR imagery, which led to orbital ramps (Estimation of Spatially-Correlated-Look-Angle becomes therefore unnecessary during StaMPS processing step 7, i.e. scla_deramp parameter is set to 'n').
- StaMPS output folder is compatible with the TRAIN toolbox for atmospheric correction (<http://davidbekaert.com/>)

The processing follows in principle the manual of StaMPS [^f2]:

- **Focalization**: done by ROI-PAC [^f3]
- **Area selection**: full frame is used
- **Automatic Master selection**: uses the script master_select from StaMPS to choose optimal master based on temporal  and spatial baseline as well as Doppler shift
- **IFG-generation**: done by DORIS (version 4.02) [^f4] using the scripts provided by StaMPS package:
  : - step_coarse run with 500 windows in order to assure proper coarse correlation also in presence of water in the scenes
    - step_coreg_simple used for fine-coregistration
    - a final check on CPM_data files for every slave in order to exclude scenes with failed co-registration is included (i.e. CPM_data > 4 Kbyte)
    - resampling, ifg generation and geocoding is done by standard StaMPS-Doris scripts.
- **stack preparation (i.e. mt_prep script)**
  : - amplitude dispersion: 0.42
    - mt_prep 0.42 5 4 50 200
- **StaMPS processing**:
  : - density_rand: 5
    - weed_zero: 'y'
    - StaMPS steps conducted : 1-8
- **published output**:
  \* DEM
  \* StaMPS folder containing all necessary matlab files to open it again in matlab and StaMPS

For plotting and exporting of IFGs, velocities & time series see Chapter 9 of StaMPS manual.

## Select the processing

- Login to the platform (see {doc}`user <../community-guide/user>` section)
- Select the processing service “StaMPS Permanent Scatterer”:

:::{figure} assets/tuto_stamps_ps_1.png
:align: center
:figclass: align-center
:width: 750px
:::

The "StaMPS Permanent Scatterer" panel is displayed with parameters values to be filled-in.

## Fill the parameters

We have prepared a public Data Package with a stack of Envisat ASAR Image Mode Level 0 (ASA_IM\_\_0P) track 336 over Istanbul.
The Data Package is called "Istanbul StaMPS", select it from the Data Package list.

### Slave product reference

Load the public Data Package called "Instanbul StaMPS". Click on "select all". Then drag the selection over the field labelled "Slave product references of the SAR stack to process".

:::{figure} assets/tuto_stamps_ps_2.png
:align: center
:figclass: align-center
:width: 750px
:::

### Orbit files

Select the orbit file type to use with the SAR stack to process.

For Envisat ASAR, select:

- Precise orbit state vectors: **VOR**

:::{figure} assets/tuto_stamps_ps_3.png
:align: center
:figclass: align-center
:width: 750px
:::

### Master product reference

Select the candidate Master (it can be any product of the stack)

- in this tutorial, simply drag and drop the file as in the picture below (track 336) in the *Candidate master product reference* field:

:::{figure} assets/tuto_stamps_ps_6.png
:align: center
:figclass: align-center
:width: 750px
:::

## Run the job

- Click on the button Run Job and see the Running Job

:::{figure} assets/tuto_stamps_ps_7.png
:align: center
:figclass: align-center
:width: 750px
:::

- After about 22 hours, see the Successful Job:

:::{figure} assets/tuto_stamps_ps_8.png
:align: center
:figclass: align-center
:width: 750px
:::

## Reprocess on your own

If you have a working matlab environment, you can treat the downloaded folder as if you would have processed it locally.

The most compute-intensive processing steps of StaMPS are 2 & 3. Those are for the preliminary selection of stable scatterers.
If you are not happy with your results, it is however recommended to start with step 4 or higher, e.g.:

```matlab
stamps(4,4)
```

### Check for bad interferograms:

For getting general information on the interferograms (i.e. baseline, estimated noise), which gives you a good indication of bad interferograms, do:

```matlab
ps_info
```

To check for wrapped and unwrapped interferograms in order to identify unreliable ones and exclude them, you can proceed like this:

```matlab
ps_plot('w')
ps_plot('u')
```

```matlab
setparm('drop_ifg',[ “Number of IFG” ])
```

Then re-run StaMPS from step 3 (it may take a while though) or from step 4 (faster).

### Lowering noise in your data:

PS Weeding (Chapter 6.4 of StaMPS manual)

- play around with the parameters weed_standard_dev as well as weed_max_noise using:

```matlab
setparm
```

- re-run from step 4 until the end:

```matlab
stamps(4,8)
```

PS Merge (Chapter 6.5 of StaMPS manual)

This is another way of reducing noise is to resample your data

- use the parameters merge_resample_size (in m) and merge_standard_dev to denoise to your needs
- re-run from step 5 until the end

:::{note}
If you change merge_resample_size, you also should consider changing the unwrap grid for step 6
:::

### Spatio-temporal filtering (Chapter 6.8 of StaMPS manual)

StaMPS step 8 filters the data in a way to address noise coming from atmosferic disturbances. It is steered by 2 parameters: scn_wavelength and scn_time_win
For the StaMPS Permanent Scatterer processing service, standard parameters from StaMPS are used.

It is however warmly recommended to adjust those parameters according to your dataset. The parameter scn_wavelength reflects the spatial filter, while scn_time_win addresses the temporal component. Play around with these parameters in order to achieve the desired result.

```{rubric} Footnotes
```

[^f1]: [StaMPS website](http://homepages.see.leeds.ac.uk/~earahoo/stamps/)

[^f2]: [StaMPS user manual](http://homepages.see.leeds.ac.uk/~earahoo/stamps/StaMPS_Manual_v3.3b1.pdf)

[^f3]: [ROI_PAC website](http://aws.roipac.org/cgi-bin/moin.cgi)

[^f4]: [DORIS website](http://doris.tudelft.nl/)
