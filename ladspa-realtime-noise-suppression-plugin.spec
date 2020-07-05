%define  commit 453a8af82a31a5361f6a13bf95c97686f0a2acd1

Name:           ladspa-realtime-noise-suppression-plugin
Version:        0.9.git.2.%{commit}
Release:        0%{?dist}
Summary:        Real-time Noise Suppression Plugin (LV2, LADSPA)
License:        GPLv3+
URL:            https://github.com/werman/noise-suppression-for-voice
#Source0:        https://github.com/werman/noise-suppression-for-voice/archive/v0.9.tar.gz
Source0:        https://github.com/werman/noise-suppression-for-voice/archive/%{commit}.tar.gz
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
Requires:       ladspa
Provides:       noise-suppression-for-voice = %{version}-%{release}

%description
A real-time noise suppression plugin for voice based on Xiph's RNNoise.


%prep
#%%setup -q -n noise-suppression-for-voice-%%{version}
%setup -q -n noise-suppression-for-voice-%{commit}

# use the system version of ladspa.h
%{__rm} ./src/ladspa_plugin/ladspa.h
ln -s /usr/include/ladspa.h ./src/ladspa_plugin/ladspa.h


%build
%cmake -DBUILD_VST_PLUGIN=OFF -DBUILD_LV2_PLUGIN=OFF .
%make_build


%install
%make_install


%files
%doc README.md
%license LICENSE
%{_libdir}/ladspa/*.so


%changelog
* Sun Jul 05 2020 Lars Kiesow <lkiesow@uos.de> - 0.9.git.2.453a8af82a31a5361f6a13bf95c97686f0a2acd1-0
- Update to git head
- Better control over which plugins are built

* Sat Jul 04 2020 Lars Kiesow <lkiesow@uos.de> - 0.9.git.1.cee9eda1cf0182aa4df3ed889eda4031078ef572-0
- Initial build
