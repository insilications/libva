#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libva
Version  : 1.7.3
Release  : 10
URL      : https://www.freedesktop.org/software/vaapi/releases/libva/libva-1.7.3.tar.bz2
Source0  : https://www.freedesktop.org/software/vaapi/releases/libva/libva-1.7.3.tar.bz2
Summary  : Userspace Video Acceleration (VA) 3rd party interface
Group    : Development/Tools
License  : MIT
Requires: libva-bin
Requires: libva-lib
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xfixes)

%description
libva for Debian
----------------
This library implements the Video Acceleration (VA) API for Linux.
It will load a hardware dependendent video acceleration driver.

%package bin
Summary: bin components for the libva package.
Group: Binaries

%description bin
bin components for the libva package.


%package dev
Summary: dev components for the libva package.
Group: Development
Requires: libva-lib
Requires: libva-bin
Provides: libva-devel

%description dev
dev components for the libva package.


%package lib
Summary: lib components for the libva package.
Group: Libraries

%description lib
lib components for the libva package.


%prep
%setup -q -n libva-1.7.3

%build
export LANG=C
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/avcenc
/usr/bin/h264encode
/usr/bin/jpegenc
/usr/bin/loadjpeg
/usr/bin/mpeg2vaenc
/usr/bin/mpeg2vldemo
/usr/bin/putsurface
/usr/bin/putsurface_wayland
/usr/bin/vainfo

%files dev
%defattr(-,root,root,-)
/usr/include/va/va.h
/usr/include/va/va_backend.h
/usr/include/va/va_backend_egl.h
/usr/include/va/va_backend_glx.h
/usr/include/va/va_backend_tpi.h
/usr/include/va/va_backend_vpp.h
/usr/include/va/va_backend_wayland.h
/usr/include/va/va_compat.h
/usr/include/va/va_dec_hevc.h
/usr/include/va/va_dec_jpeg.h
/usr/include/va/va_dec_vp8.h
/usr/include/va/va_dec_vp9.h
/usr/include/va/va_dri2.h
/usr/include/va/va_dricommon.h
/usr/include/va/va_drm.h
/usr/include/va/va_drmcommon.h
/usr/include/va/va_egl.h
/usr/include/va/va_enc_h264.h
/usr/include/va/va_enc_hevc.h
/usr/include/va/va_enc_jpeg.h
/usr/include/va/va_enc_mpeg2.h
/usr/include/va/va_enc_vp8.h
/usr/include/va/va_enc_vp9.h
/usr/include/va/va_glx.h
/usr/include/va/va_tpi.h
/usr/include/va/va_version.h
/usr/include/va/va_vpp.h
/usr/include/va/va_wayland.h
/usr/include/va/va_x11.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/dri/dummy_drv_video.so
