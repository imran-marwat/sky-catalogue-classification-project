The SuperCOSMOS Sky Survey (SSS) consists of machine scans of photographic
plates - for more information see

http://www-wfau.roe.ac.uk/sss

The Sloan Digital Sky Survey (SDSS) consists of more recent CCD camera scans
of similar areas of sky with better image quality and greater depth (ie.
sensitivity) than the older photographic data - for more information see

http://www.sdss.org/

This archive file contains the following files:

                ReadMe - this file
               edr.dat - SDSS data for this field
 UKJ823/sssedrpair.dat - Paired SDSS/SSS object data from the blue passband
 UKR823/sssedrpair.dat -    "       "       "    "     "   "   red    "
 UKI823/sssedrpair.dat -    "       "       "    "     "   "  infrared
PAE0319/sssedrpair.dat -    "       "       "    "     "   "   red    "
      UKJ823/iam.ascii - SSS data (unpaired)
      UKR823/iam.ascii - SSS data (unpaired)
      UKI823/iam.ascii - SSS data (unpaired)
     PAE0319/iam.ascii - SSS data (unpaired)

(the PAE files contains early epoch photo data taken in the 1950s whereas
the first three use more recent photographic data). In each case, the data are
taken from one SSS field (# 823) which is at co-ordinates (0,0) in Right
Ascension & Declination.

In the paired files, the fields are as follows:

Fld  Description / units

  1  SSS Right Ascension / radians x 10^8
  2  SSS Declination / radians x 10^8
  3  SSS Object left extent (xmin) / 0.01 micron
  4  SSS Object right extent (xmax) / 0.01 micron
  5  SSS Object bottom extent (ymin) / 0.01 micron
  6  SSS Object top extent (ymax) / 0.01 micron
  7  SSS Total area / pixels (pixels are 10x10 micron^2)
  8  SSS Brightest intensity above sky / arbitrary intensity units
  9  SSS COSMAG instrumental magnitude / magnitude x1000
 10  SSS Sky intensity at object centroid / arbitrary intensity units
 11  SSS Intensity weighted X centroid / 0.01 micron
 12  SSS Intensity weighted Y centroid / 0.01 micron
 13  SSS Unweighted semi-major axis / 0.01 micron
 14  SSS Unweighted semi-minor axis / 0.01 micron
 15  SSS Unwieghted orientation / degrees
 16  SSS Weighted semi-major axis / 0.01 micron
 17  SSS Weighted semi-minor axis / 0.01 micron
 18  SSS Weighted orientation / degrees
 19  SSS Classification flag: 1=galaxy, 2=star, 3=unclassified, 4=noise
 20  SSS Celestial position angle / degrees
 21  SSS Area above areal profile threshold 1 / pixels
 22  SSS Area above areal profile threshold 2 / pixels
 23  SSS Area above areal profile threshold 3 / pixels
 24  SSS Area above areal profile threshold 4 / pixels
 25  SSS Area above areal profile threshold 5 / pixels
 26  SSS Area above areal profile threshold 6 / pixels
 27  SSS Area above areal profile threshold 7 / pixels
 28  SSS Area above areal profile threshold 8 / pixels
 29  SSS Blend flag: 0=isolated; -n = parent of n objects; +n=nth child of blend
 30  SSS Quality flag
 31  SSS N(0,1) stellar profile statistic x1000
 32  SSS Instrumental profile magnitude / magnitude x1000
 33  SSS Calibrated COSMAG (field 9) / magnitude
 34  SSS Calibrated profile magnitude (field 32) / magnitude
 35  SDSS Right Ascension / decimal degrees
 36  SDSS Declination / decimal degrees
 37  SDSS g' magnitude
 38  SDSS r' magnitude
 39  SDSS i' magnitude
 40  SDSS classification code / 6 = star, 3 = galaxy

In the unpaired files, the fields are as for fields 1 thru 34 in iam.ascii
files and as for fields 35 thru 40 for the file edr.dat

Fields irrelevant to classification of images in the SSS data are:

1,2,3,4,5,6,11,12,19,20

and probably fields 21 thru 28, since these are coded up in the statistic in
field 31. Combinations of fields that will be useful for classification
include

ellipticity e = 1 - b/a  (where b = field 17; a = field 16)

where anything with e > 0.33333 will not be an isolated star (but deblended
stars can have e > 0.33333 when near much brighter objects...)

and for bright galaxies (probably not a major consideration for this project)

filling factor G = area / (pi*a_u*b_u) (where area=field 7; a_u=13; b_u=14)

where bright objects will never be stars if G < 0.6 and are potentially galaxies
when G > 0.9 (bright means calibrated magnitude < 17 in this context). Note
also that for bright objects, the appropriate magnitude to use (either field
33 or 34) is class-dependent: if the object is stellar-like, then field 34 is
the one to use; if the object is not stellar like, then 33 is more appropriate.
This is not a major consideration for faint objects, since the calibrations
converge.

To see how good our default classification is, simply compare the SDSS
class (field 40) with the SSS class (field 19).

For more information on the SSS data, see the set of papers at

http://www-wfau.roe.ac.uk/sss/docs.html

- particularly Paper II.
