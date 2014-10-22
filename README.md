ckap
====

[EN] Python script to generate raster charts.

[ES] Script Python para generar cartas rasters

Dependencies
============

- python2.7
- libbsb (http://libbsb.sourceforge.net/)
    For debs: http://opencpn.org/ocpn/libbsb
- Imagemagick (http://www.imagemagick.org)
- mc2bsbh (http://www.dacust.com/inlandwaters/mapcal/mc2bsbh/mc2bsbh-beta09.zip)

Manual Installation
===================

Only copy ckap.py to your sbin path and give executable permission. For example:

$ sudo cp ckap.py /usr/sbin/ckap

$ sudo chmod a+x /usr/sbin/ckap

Syntax
======
ckap [image.png] [header.dir]

Use
===

First, You must change to the image and header folder. For ex:

cd chart-folder/

and then, execute ckap:

$ckap chartimage.png CHARTCAL.DIR

It's all done!
