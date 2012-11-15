rpmbuild-silk
=============

rpm build notes for silkv2.5.0
http://tools.netsa.cert.org/index.html

This project covers  rpm build process for silk. I'm creating binaries for Centos 5.7 64-bit. 
We'll use the resources below:
libfixbuf-1.2.0
netsa-python-1.3
silk-2.5.0
yaf-2.3.2

NOTE:  yaf won't work on Centos 5.7.  I'll update this later  for C6.


we'll also enable compression and the cisco asa hack to support v9 flows from the cisco asa until the   packetTotalCount
bug is fixed.

My information came from the following source.  Thanks for that!:D

http://tools.netsa.cert.org/silk/install-handbook.html
http://infosecmatters.blogspot.com/2012/10/netflow-analysis-with-silk-part-1.html

install.sh is not actually used in the build process.  It's just some notes as I go along.



RPM BUILD ENVIRONMENT
http://wiki.centos.org/HowTos/SetupRpmBuildEnvironment
http://www.lamolabs.org/blog/164/centos-rpm-tutorial-1/

*THIS IS THE BEST DOC*
https://tools.netsa.cert.org/confluence/plugins/viewsource/viewpagesrc.action?pageId=4980787

as root:
yum install -y rpm-build redhat-rpm-config make gcc

***do everything else as a non-root user***

mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS,tmp}
created ~/.rpmmacros  file with the contents:
%packager Nate Marks
%_topdir %(echo $HOME)/rpmbuild
%_tmppath %(echo $HOME)/rpmbuild/tmp


yum install -y rpm-build redhat-rpm-config make gcc

libfixbuf comes with it's own spec file, so copy the tarball to the SOURCES dir, unpack it, then copy the .spec file to SPECS
cd ~/rpmbuild/SOURCES
./configure

I also needed  to install glib2-devel before running 
cd ~/rpmbuild
rpmbuild -ba SPECS/libfixbuf.spec

that created 3 rpms for me (libfixbuf, debug and devel)
install libfixbuf and -devel

YAF:  doesn't work on Centos5 according to this link:
http://www.cert.org/forensics/tools/include/all_announcements.html
"  ...Note that this release of Yaf is not available for CentOS/RHEL 5 due to an outdated version of PCRE"
same as above except 
just before running the rpmbuild process, edit the spec file as noted  in the netsa link above
AND
yum install libtool-ltdl-devel pcre-devel

then rpmbuild -ba SPECS/yaf.spec

yum install libtool-ltdl-devel


NOw SilK:
yum install -y gcc make python-devel glib2-devel gnutls gnutls-devel lzo lzo-devel  libpcap libpcap-devel zlib zlib-devel


this configure command:
./configure --with-python --sysconfdir=/etc/sysconfig --enable-data-rootdir=/opt/silk/data --prefix=/opt/silk --enable-output-compression --enable-asa-zero-packet-hack

produced this summary:

    * Configured package:           SiLK 2.5.0
    * Host type:                    x86_64-unknown-linux-gnu
    * Source files ($top_srcdir):   .
    * Install directory:            /opt/silk
    * Root of packed data tree:     /opt/silk/data
    * Packing logic:                via run-time plugin
    * Timezone support:             UTC
    * Default compression method:   SK_COMPMETHOD_ZLIB
    * IPv6 flow-record support:     NO
    * IPFIX collection support:     YES (-pthread -L/lib64 -lfixbuf -lgthread-2.0 -lglib-2.0)
    * NetFlow9 collection support:  YES
    * ASA 0-packet work-around:     YES
    * Transport encryption support: YES (-lgnutls   -lgcrypt -ldl -lgpg-error)
    * IPA support:                  NO
    * LIBPCAP support:              YES (-lpcap)
    * ADNS support:                 NO
    * Python support:               YES (-L/usr/kerberos/lib64 -Xlinker -export-dynamic -ldl -lutil -lm -L/usr/lib64 -lpython2.4 -pthread)
    * Python package destination:   /usr/lib64/python2.4/site-packages
    * Build analysis tools:         YES
    * Build packing tools:          YES
    * Compiler (CC):                gcc
    * Compiler flags (CFLAGS):      -I$(srcdir) -I$(top_builddir)/src/include -I$(top_srcdir)/src/include -DNDEBUG -O3 -fno-strict-aliasing -Wall -W -Wmissing-prototypes -Wformat=2 -Wdeclaration-after-statement -Wpointer-arith
    * Linker flags (LDFLAGS):       
    * Libraries (LIBS):             -lz -ldl -lm 

the ./configure step also created the spec file .  copy that to the SPEC directory and use it to create the rpm
