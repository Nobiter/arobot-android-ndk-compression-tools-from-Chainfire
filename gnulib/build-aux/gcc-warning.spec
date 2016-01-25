# options to filter out, and why
--all-warnings				alias for -Wall
--extra-warnings			alias for -Wextra
-Wabi-tag				c++
-Wabi=					c++
-Waggregate-return			obsolescent
-Waliasing				fortran
-Walign-commons				fortran
-Wampersand				fortran
-Warray-bounds				covered by -Warray-bounds=
-Warray-bounds=				handled specially by gl_MANYWARN_ALL_GCC
-Warray-temporaries			fortran
-Wassign-intercept			objc/objc++
-Wc++-compat				FIXME maybe? borderline.  some will want this
-Wc++0x-compat				c++
-Wc++11-compat				c++
-Wc++14-compat				c++
-Wc-binding-type			fortran
-Wc90-c99-compat			c compatibility
-Wc99-c11-compat			c compatibility
-Wcast-qual				FIXME maybe? too much noise; encourages bad changes
-Wcharacter-truncation			fortran
-Wcompare-reals				fortran
-Wconditionally-supported		c++ and objc++
-Wconversion				FIXME maybe? too much noise; encourages bad changes
-Wconversion-extra			fortran
-Wconversion-null			c++ and objc++
-Wctor-dtor-privacy			c++
-Wdeclaration-after-statement		FIXME: do not want.  others may
-Wdelete-incomplete			c++ and objc++
-Wdelete-non-virtual-dtor		c++
-Weffc++				c++
-Werror-implicit-function-declaration	deprecated
-Wfloat-equal				FIXME maybe? borderline.  some will want this
-Wformat				covered by -Wformat=2
-Wformat=				gcc --help=warnings artifact
-Wfunction-elimination			fortran
-Wimplicit-interface			fortran
-Wimplicit-procedure			fortran
-Winherited-variadic-ctor		c++
-Wintrinsic-shadow			fortran
-Wintrinsics-std			fortran
-Winvalid-offsetof			c++ and objc++
-Wlarger-than-				gcc --help=warnings artifact
-Wlarger-than=<number>			FIXME: choose something sane?
-Wline-truncation			fortran
-Wliteral-suffix			c++ and objc++
-Wlong-long				obsolescent
-Wnoexcept				c++
-Wnon-template-friend			c++
-Wnon-virtual-dtor			c++
-Wnormalized=<none|id|nfc|nfkc>		handled specially by gl_MANYWARN_ALL_GCC
-Wold-style-cast			c++ and objc++
-Woverloaded-virtual			c++
-Wpadded				FIXME maybe?  warns about "stabil" member in /usr/include/bits/timex.h
-Wpedantic				FIXME: too strict?
-Wpmf-conversions			c++ and objc++
-Wproperty-assign-default		objc++
-Wprotocol				objc++
-Wreal-q-constant			fortran
-Wrealloc-lhs				fortran
-Wrealloc-lhs-all			fortran
-Wredundant-decls			FIXME maybe? many _gl_cxxalias_dummy FPs
-Wreorder				c++ and objc++
-Wselector				objc and objc++
-Wshadow-ivar				objc
-Wsign-compare				FIXME maybe? borderline.  some will want this
-Wsign-conversion			FIXME maybe? borderline.  some will want this
-Wsign-promo				c++ and objc++
-Wsized-deallocation			c++ and objc++
-Wstack-usage=				FIXME: choose something sane?
-Wstrict-aliasing=			FIXME: choose something sane?
-Wstrict-null-sentinel			c++ and objc++
-Wstrict-overflow=			FIXME: choose something sane?
-Wstrict-selector-match			objc and objc++
-Wsuggest-override			c++ and objc++
-Wsurprising				fortran
-Wswitch-enum				FIXME maybe? borderline.  some will want this
-Wsynth					deprecated
-Wtabs					fortran
-Wtarget-lifetime			fortran
-Wtraditional				obsolescent
-Wtraditional-conversion		obsolescent
-Wundeclared-selector			objc and objc++
-Wundef					FIXME maybe? too many false positives
-Wunderflow				fortran
-Wunsuffixed-float-constants		triggers warning in gnulib's timespec.h
-Wunused-dummy-argument			fortran
-Wuse-without-only			fortran
-Wuseless-cast				c++ and objc++
-Wvirtual-move-assign			c++
-Wzero-as-null-pointer-constant		c++ and objc++
-Wzerotrip				fortran
-frequire-return-statement		go
