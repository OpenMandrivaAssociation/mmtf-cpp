Name:           mmtf-cpp       
Version:        1.0.0
Release:        1
Summary:        The pure C++ implementation of the MMTF API, decoder and encoder
License:        MIT
Group:          Development/C++
URL:            https://github.com/rcsb/mmtf-cpp
Source0:        https://github.com/rcsb/mmtf-cpp/archive/v1.0.0/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  ninja
BuildRequires:  doxygen

%description
The pure C++ implementation of the MMTF API, decoder and encoder.
A binary encoding of biological structures library.

%package        devel
Summary: The pure C++ implementation of the MMTF API, decoder and encoder

%description devel
The pure C++ implementation of the MMTF API, decoder and encoder.
A binary encoding of biological structures library.

%prep
%setup -q

%build

%cmake -G Ninja 
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_BUILD_TYPE=Release 

%ninja_build

%install
%ninja_install -C build

%files
#{_includedir}/mmtf/*

%files devel
%{_includedir}/mmtf*
