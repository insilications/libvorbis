#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvorbis
Version  : 1.3.6
Release  : 18
URL      : http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.6.tar.xz
Source0  : http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.6.tar.xz
Summary  : Vorbis Library Development
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libvorbis-lib = %{version}-%{release}
Requires: libvorbis-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32ogg)
BuildRequires : pkgconfig(ogg)
Patch1: cve-2018-10392.patch
Patch2: cve-2018-10393.patch

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed 
and variable bitrates from 16 to 128 kbps/channel.

%package dev
Summary: dev components for the libvorbis package.
Group: Development
Requires: libvorbis-lib = %{version}-%{release}
Provides: libvorbis-devel = %{version}-%{release}

%description dev
dev components for the libvorbis package.


%package dev32
Summary: dev32 components for the libvorbis package.
Group: Default
Requires: libvorbis-lib32 = %{version}-%{release}
Requires: libvorbis-dev = %{version}-%{release}

%description dev32
dev32 components for the libvorbis package.


%package doc
Summary: doc components for the libvorbis package.
Group: Documentation

%description doc
doc components for the libvorbis package.


%package lib
Summary: lib components for the libvorbis package.
Group: Libraries
Requires: libvorbis-license = %{version}-%{release}

%description lib
lib components for the libvorbis package.


%package lib32
Summary: lib32 components for the libvorbis package.
Group: Default
Requires: libvorbis-license = %{version}-%{release}

%description lib32
lib32 components for the libvorbis package.


%package license
Summary: license components for the libvorbis package.
Group: Default

%description license
license components for the libvorbis package.


%prep
%setup -q -n libvorbis-1.3.6
%patch1 -p1
%patch2 -p1
pushd ..
cp -a libvorbis-1.3.6 build32
popd
pushd ..
cp -a libvorbis-1.3.6 buildavx2
popd
pushd ..
cp -a libvorbis-1.3.6 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541615945
export CFLAGS="$CFLAGS -ffast-math -fstack-protector-strong -ftree-loop-vectorize -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -ffast-math -fstack-protector-strong -ftree-loop-vectorize -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -ffast-math -fstack-protector-strong -ftree-loop-vectorize -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -ffast-math -fstack-protector-strong -ftree-loop-vectorize -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="$ASFLAGS --32"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export CXXFLAGS="$CXXFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export LDFLAGS="$LDFLAGS -m64 -march=skylake-avx512"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1541615945
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libvorbis
cp COPYING %{buildroot}/usr/share/package-licenses/libvorbis/COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx512/
%make_install_avx512
popd
pushd ../buildavx2/
%make_install_avx2
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/vorbis/codec.h
/usr/include/vorbis/vorbisenc.h
/usr/include/vorbis/vorbisfile.h
/usr/lib64/haswell/avx512_1/libvorbis.so
/usr/lib64/haswell/avx512_1/libvorbisenc.so
/usr/lib64/haswell/avx512_1/libvorbisfile.so
/usr/lib64/haswell/libvorbis.so
/usr/lib64/haswell/libvorbisenc.so
/usr/lib64/haswell/libvorbisfile.so
/usr/lib64/libvorbis.so
/usr/lib64/libvorbisenc.so
/usr/lib64/libvorbisfile.so
/usr/lib64/pkgconfig/vorbis.pc
/usr/lib64/pkgconfig/vorbisenc.pc
/usr/lib64/pkgconfig/vorbisfile.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libvorbis.so
/usr/lib32/libvorbisenc.so
/usr/lib32/libvorbisfile.so
/usr/lib32/pkgconfig/32vorbis.pc
/usr/lib32/pkgconfig/32vorbisenc.pc
/usr/lib32/pkgconfig/32vorbisfile.pc
/usr/lib32/pkgconfig/vorbis.pc
/usr/lib32/pkgconfig/vorbisenc.pc
/usr/lib32/pkgconfig/vorbisfile.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libvorbis/*
/usr/share/doc/libvorbis-1.3.6/doxygen-build.stamp
/usr/share/doc/libvorbis-1.3.6/eightphase.png
/usr/share/doc/libvorbis-1.3.6/fish_xiph_org.png
/usr/share/doc/libvorbis-1.3.6/floor1_inverse_dB_table.html
/usr/share/doc/libvorbis-1.3.6/floorval.png
/usr/share/doc/libvorbis-1.3.6/fourphase.png
/usr/share/doc/libvorbis-1.3.6/framing.html
/usr/share/doc/libvorbis-1.3.6/helper.html
/usr/share/doc/libvorbis-1.3.6/index.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/index.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/overview.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/reference.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/return.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/style.css
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis_blockout.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis_buffer.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis_headerout.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis_init.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis_wrote.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_bitrate_addblock.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_bitrate_flushpacket.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_block.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_block_clear.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_block_init.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_add.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_add_tag.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_clear.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_init.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_query.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_query_count.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_commentheader_out.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_dsp_clear.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_dsp_state.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_granule_time.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_info.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_info_blocksize.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_info_clear.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_info_init.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_packet_blocksize.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_blockin.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_halfrate.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_halfrate_p.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_headerin.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_idheader.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_init.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_lapout.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_pcmout.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_read.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_restart.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_trackonly.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_version_string.html
/usr/share/doc/libvorbis-1.3.6/oggstream.html
/usr/share/doc/libvorbis-1.3.6/programming.html
/usr/share/doc/libvorbis-1.3.6/rfc5215.txt
/usr/share/doc/libvorbis-1.3.6/rfc5215.xml
/usr/share/doc/libvorbis-1.3.6/squarepolar.png
/usr/share/doc/libvorbis-1.3.6/stereo.html
/usr/share/doc/libvorbis-1.3.6/stream.png
/usr/share/doc/libvorbis-1.3.6/v-comment.html
/usr/share/doc/libvorbis-1.3.6/vorbis-clip.txt
/usr/share/doc/libvorbis-1.3.6/vorbis-errors.txt
/usr/share/doc/libvorbis-1.3.6/vorbis-fidelity.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/changes.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/examples.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/index.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/ovectl_ratemanage2_arg.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/ovectl_ratemanage_arg.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/overview.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/reference.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/style.css
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_ctl.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_init.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_init_vbr.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_setup_init.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_setup_managed.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_setup_vbr.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/OggVorbis_File.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/callbacks.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/chaining_example_c.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/chainingexample.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/crosslap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/datastructures.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/decoding.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/example.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/exampleindex.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/fileinfo.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/index.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/initialization.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_bitrate.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_bitrate_instant.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_callbacks.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_clear.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_comment.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_crosslap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_fopen.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_info.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_open.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_open_callbacks.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_seek.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_seek_lap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_seek_page.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_seek_page_lap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_tell.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_total.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_raw_seek.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_raw_seek_lap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_raw_tell.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_raw_total.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_read.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_read_filter.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_read_float.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_seekable.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_serialnumber.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_streams.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_test.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_test_callbacks.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_test_open.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_seek.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_seek_lap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_seek_page.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_seek_page_lap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_tell.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_total.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/overview.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/reference.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/seekexample.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/seeking.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/seeking_example_c.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/seeking_test_c.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/seekingexample.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/style.css
/usr/share/doc/libvorbis-1.3.6/vorbisfile/threads.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/vorbisfile_example_c.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libvorbis.so.0
/usr/lib64/haswell/avx512_1/libvorbis.so.0.4.8
/usr/lib64/haswell/avx512_1/libvorbisenc.so.2
/usr/lib64/haswell/avx512_1/libvorbisenc.so.2.0.11
/usr/lib64/haswell/avx512_1/libvorbisfile.so.3
/usr/lib64/haswell/avx512_1/libvorbisfile.so.3.3.7
/usr/lib64/haswell/libvorbis.so.0
/usr/lib64/haswell/libvorbis.so.0.4.8
/usr/lib64/haswell/libvorbisenc.so.2
/usr/lib64/haswell/libvorbisenc.so.2.0.11
/usr/lib64/haswell/libvorbisfile.so.3
/usr/lib64/haswell/libvorbisfile.so.3.3.7
/usr/lib64/libvorbis.so.0
/usr/lib64/libvorbis.so.0.4.8
/usr/lib64/libvorbisenc.so.2
/usr/lib64/libvorbisenc.so.2.0.11
/usr/lib64/libvorbisfile.so.3
/usr/lib64/libvorbisfile.so.3.3.7

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libvorbis.so.0
/usr/lib32/libvorbis.so.0.4.8
/usr/lib32/libvorbisenc.so.2
/usr/lib32/libvorbisenc.so.2.0.11
/usr/lib32/libvorbisfile.so.3
/usr/lib32/libvorbisfile.so.3.3.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvorbis/COPYING
