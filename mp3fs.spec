# Makefile manages to ignore hardened_build
#global _hardened_build 1

Summary: FUSE filesystem to transcode FLAC to MP3 on the fly
Name: mp3fs
Version: 0.91
Release: 4%{dist}
License: GPLv3+ and GFDL
Group: Applications/Multimedia
Source0: https://github.com/khenriks/mp3fs/releases/download/v%{version}/mp3fs-%{version}.tar.gz
#Patch0: mp3fs.patch
URL: http://khenriks.github.com/mp3fs/
#Provides: mp3encoder
# While mp3fs does not strictly require the fuse cli (which does not provide
# the fuse libraries), mp3fs is fairly useless without it.
Requires: fuse
BuildRequires: fuse-devel lame-devel flac-devel libid3tag-devel gcc-c++

%description
MP3FS is A read-only FUSE file-system which trans-codes audio formats (currently
FLAC) to MP3 on the fly when opened and read. This was written to enable me to
use my FLAC collection with software and/or hardware which only understands
MP3. e.g. "GMediaServer" to a Netgear MP101 mp3 player.

It is also a novel alternative to traditional mp3 encoder applications. Just
use your favorite file browser to select the files you want encoded and copy
them somewhere!

%prep
%setup -q 
#patch0 -p1 -b .sdg

%build
%configure
%{make_build} LDFLAGS="$RPM_LD_FLAGS -lm" V=1

%install
%make_install

%files
%{!?_licensedir:%global license %%doc}
%license COPYING COPYING.DOC
%doc NEWS ChangeLog README.md INSTALL.md
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Stuart Gathman <stuart@gathman.org> 0.91-3
- Remove space from Summary:
- Include $RPM_LD_FLAGS in LDFLAGS
- Removed mp3encoder provides, not useful apparently

* Tue Oct 18 2016 Stuart Gathman <stuart@gathman.org> 0.91-2
- Clean up to resubmit to rpmfusion.

* Sat Jan 24 2015 Stuart Gathman <stuart@gathman.org> 0.91-1
- Update to 0.91 on Fedora 19

* Wed Oct 10 2012 Stuart Gathman <stuart@gathman.org> 0.32-1
- Update to 0.32 on Fedora 16

* Tue Jun 29 2010 Stuart Gathman <stuart@gathman.org> 0.20-1
- Update to 0.20 on Fedora 12

* Fri Oct 19 2007 Stuart Gathman <stuart@gathman.org> 0.13-1
- Update to 0.13 on Centos5

* Fri Oct 19 2007 Stuart Gathman <stuart@gathman.org> 0.11-1
- Update to 0.11 on Centos5

* Wed Nov 22 2006 Stuart Gathman <stuart@gathman.org> 0.03-2
- Rebuild with fuse-2.6

* Wed Nov  1 2006 Stuart Gathman <stuart@gathman.org> 0.03-1
- RPM 
