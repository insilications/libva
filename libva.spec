#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libva
Version  : 2.12.0
Release  : 306
URL      : file:///aot/build/clearlinux/packages/libva/libva-v2.12.0.tar.gz
Source0  : file:///aot/build/clearlinux/packages/libva/libva-v2.12.0.tar.gz
Summary  : Userspace Video Acceleration (VA) core interface
Group    : Development/Tools
License  : LGPL-2.1+
Requires: libva-lib = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : libXScrnSaver
BuildRequires : libXScrnSaver-dev
BuildRequires : libXScrnSaver-lib
BuildRequires : libXau-dev
BuildRequires : libXau-lib
BuildRequires : libXcursor-dev
BuildRequires : libXcursor-lib
BuildRequires : libXdamage-dev
BuildRequires : libXdamage-lib
BuildRequires : libXdmcp-dev
BuildRequires : libXdmcp-lib
BuildRequires : libXext-dev
BuildRequires : libXext-lib
BuildRequires : libXfont2-dev
BuildRequires : libXft-dev
BuildRequires : libXft-lib
BuildRequires : libXi-dev
BuildRequires : libXi-lib
BuildRequires : libXrender-dev
BuildRequires : libXrender-lib
BuildRequires : libXtst-dev
BuildRequires : libXtst-lib
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-lib
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : libva-intel-driver
BuildRequires : libva-vdpau-driver-chromium
BuildRequires : libva-vdpau-driver-chromium-dev
BuildRequires : libvdpau
BuildRequires : libvdpau-dev
BuildRequires : libxcb-dev
BuildRequires : libxcb-lib
BuildRequires : libxkbcommon
BuildRequires : libxkbcommon-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt-bin
BuildRequires : libxslt-dev
BuildRequires : libxslt-staticdev
BuildRequires : mesa
BuildRequires : mesa-dev
BuildRequires : mesa-lib
BuildRequires : ninja
BuildRequires : pkgconfig(32gl)
BuildRequires : pkgconfig(32libdrm)
BuildRequires : pkgconfig(32wayland-client)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xfixes)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xfixes)
BuildRequires : sed
BuildRequires : wayland
BuildRequires : wayland-dev
BuildRequires : weston
BuildRequires : wmctrl
BuildRequires : xauth
BuildRequires : xcb-proto
BuildRequires : xcb-proto-dev
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
BuildRequires : xcb-util-xrm-dev
BuildRequires : xclip
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : xdotool
BuildRequires : xdpyinfo
BuildRequires : xf86-input-libinput
BuildRequires : xf86-video-amdgpu
BuildRequires : xf86-video-ati
BuildRequires : xf86-video-fbdev
BuildRequires : xf86-video-nouveau
BuildRequires : xf86-video-qxl
BuildRequires : xf86-video-vboxvideo
BuildRequires : xf86-video-vesa
BuildRequires : xf86-video-vmware
BuildRequires : xfontsel
BuildRequires : xhost
BuildRequires : xinit
BuildRequires : xinput
BuildRequires : xkbcomp
BuildRequires : xkeyboard-config
BuildRequires : xkill
BuildRequires : xmodmap
BuildRequires : xorg-server
BuildRequires : xorg-server-dev
BuildRequires : xorgproto
BuildRequires : xorgproto-dev
BuildRequires : xprop
BuildRequires : xrandr
BuildRequires : xrdb
BuildRequires : xrdp
BuildRequires : xrestop
BuildRequires : xscreensaver
BuildRequires : xsel
BuildRequires : xset
BuildRequires : xsetroot
BuildRequires : xvfb-run
BuildRequires : xwd
BuildRequires : xwininfo
BuildRequires : xz
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Enable-both_libraries-static-shared-build.patch

%description
[![Stories in Ready](https://badge.waffle.io/intel/libva.png?label=ready&title=Ready)](http://waffle.io/intel/libva)
[![Build Status](https://travis-ci.org/intel/libva.svg?branch=master)](https://travis-ci.org/intel/libva)
[![Coverity Scan Build Status](https://scan.coverity.com/projects/11605/badge.svg)](https://scan.coverity.com/projects/intel-libva)

%package dev
Summary: dev components for the libva package.
Group: Development
Requires: libva-lib = %{version}-%{release}
Provides: libva-devel = %{version}-%{release}
Requires: libva = %{version}-%{release}

%description dev
dev components for the libva package.


%package dev32
Summary: dev32 components for the libva package.
Group: Default
Requires: libva-lib32 = %{version}-%{release}
Requires: libva-dev = %{version}-%{release}

%description dev32
dev32 components for the libva package.


%package lib
Summary: lib components for the libva package.
Group: Libraries

%description lib
lib components for the libva package.


%package lib32
Summary: lib32 components for the libva package.
Group: Default

%description lib32
lib32 components for the libva package.


%package staticdev
Summary: staticdev components for the libva package.
Group: Default
Requires: libva-dev = %{version}-%{release}

%description staticdev
staticdev components for the libva package.


%package staticdev32
Summary: staticdev32 components for the libva package.
Group: Default
Requires: libva-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the libva package.


%prep
%setup -q -n libva
cd %{_builddir}/libva
%patch1 -p1
pushd %{_builddir}
cp -a %{_builddir}/libva build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630053094
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export CXXFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export CFFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags1 end
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both  -Ddisable_drm=false \
-Dwith_x11=yes \
-Dwith_glx=yes \
-Dwith_wayland=yes \
-Denable_docs=false builddir
ninja --verbose %{?_smp_mflags} -C builddir

pushd ../build32/
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
unset CPATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
unset ASFLAGS
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset CFFLAGS
unset LDFLAGS
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FCFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export CFFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib32 --prefix=/usr --buildtype=plain -Ddefault_library=both  -Denable_docs=false builddir
ninja --verbose %{?_smp_mflags} -C builddir
popd

%install
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/va/va.h
/usr/include/va/va_backend.h
/usr/include/va/va_backend_glx.h
/usr/include/va/va_backend_prot.h
/usr/include/va/va_backend_vpp.h
/usr/include/va/va_backend_wayland.h
/usr/include/va/va_compat.h
/usr/include/va/va_dec_av1.h
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
/usr/include/va/va_fei.h
/usr/include/va/va_fei_h264.h
/usr/include/va/va_fei_hevc.h
/usr/include/va/va_glx.h
/usr/include/va/va_prot.h
/usr/include/va/va_str.h
/usr/include/va/va_tpi.h
/usr/include/va/va_version.h
/usr/include/va/va_vpp.h
/usr/include/va/va_wayland.h
/usr/include/va/va_x11.h
/usr/lib64/libva-drm.so
/usr/lib64/libva-glx.so
/usr/lib64/libva-wayland.so
/usr/lib64/libva-x11.so
/usr/lib64/libva.so
/usr/lib64/pkgconfig/libva-drm.pc
/usr/lib64/pkgconfig/libva-glx.pc
/usr/lib64/pkgconfig/libva-wayland.pc
/usr/lib64/pkgconfig/libva-x11.pc
/usr/lib64/pkgconfig/libva.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libva-drm.so
/usr/lib32/libva-glx.so
/usr/lib32/libva-wayland.so
/usr/lib32/libva-x11.so
/usr/lib32/libva.so
/usr/lib32/pkgconfig/32libva-drm.pc
/usr/lib32/pkgconfig/32libva-glx.pc
/usr/lib32/pkgconfig/32libva-wayland.pc
/usr/lib32/pkgconfig/32libva-x11.pc
/usr/lib32/pkgconfig/32libva.pc
/usr/lib32/pkgconfig/libva-drm.pc
/usr/lib32/pkgconfig/libva-glx.pc
/usr/lib32/pkgconfig/libva-wayland.pc
/usr/lib32/pkgconfig/libva-x11.pc
/usr/lib32/pkgconfig/libva.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libva-drm.so.2
/usr/lib64/libva-drm.so.2.1300.0
/usr/lib64/libva-glx.so.2
/usr/lib64/libva-glx.so.2.1300.0
/usr/lib64/libva-wayland.so.2
/usr/lib64/libva-wayland.so.2.1300.0
/usr/lib64/libva-x11.so.2
/usr/lib64/libva-x11.so.2.1300.0
/usr/lib64/libva.so.2
/usr/lib64/libva.so.2.1300.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libva-drm.so.2
/usr/lib32/libva-drm.so.2.1300.0
/usr/lib32/libva-glx.so.2
/usr/lib32/libva-glx.so.2.1300.0
/usr/lib32/libva-wayland.so.2
/usr/lib32/libva-wayland.so.2.1300.0
/usr/lib32/libva-x11.so.2
/usr/lib32/libva-x11.so.2.1300.0
/usr/lib32/libva.so.2
/usr/lib32/libva.so.2.1300.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libva-drm.a
/usr/lib64/libva-glx.a
/usr/lib64/libva-wayland.a
/usr/lib64/libva-x11.a
/usr/lib64/libva.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libva-drm.a
/usr/lib32/libva-glx.a
/usr/lib32/libva-wayland.a
/usr/lib32/libva-x11.a
/usr/lib32/libva.a
