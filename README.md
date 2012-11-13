rpmbuild-silk
=============

rpm build notes for silkv2.5.0
http://tools.netsa.cert.org/index.html

This project covers  rpm build process for silk.  We'll use the resources below:
libfixbuf-1.2.0
netsa-python-1.3
silk-2.5.0
yaf-2.3.2


we'll also enable compression and the cisco asa hack to support v9 flows from the cisco asa until the   packetTotalCount
bug is fixed.

My information came from the following source.  Thanks for that!:D

http://tools.netsa.cert.org/silk/install-handbook.html
http://infosecmatters.blogspot.com/2012/10/netflow-analysis-with-silk-part-1.html

install.sh is not actually used in the build process.  It's just some notes as I go along.
