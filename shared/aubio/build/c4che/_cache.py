AR = ['/usr/bin/ar']
ARCH_ST = ['-arch']
ARFLAGS = ['rcs']
BINDIR = '/usr/local/bin'
CC = ['/usr/bin/clang']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'clang'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('12', '0', '5')
CFLAGS = ['-g', '-Wall', '-Wextra', '-O2', '-fPIC']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'clang'
CPPPATH_ST = '-I%s'
DATADIR = '/usr/local/share'
DATAROOTDIR = '/usr/local/share'
DEFINES = ['HAVE_CONFIG_H=1', 'AUBIO_PREFIX="/usr/local"', 'PACKAGE="aubio"']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'HAVE_ERRNO_H': '', 'HAVE_MEMCPY_HACKS': '', 'HAVE_STRING_H': '', 'HAVE_WAVWRITE': '', 'HAVE_WAVREAD': '', 'HAVE_SAMPLERATE': '', 'HAVE_SNDFILE': '', 'AUBIO_PREFIX': '', 'HAVE_C99_VARARGS_MACROS': '', 'HAVE_GETOPT_H': '', 'HAVE_SWRESAMPLE': '', 'HAVE_AVCODEC': '', 'HAVE_LIBAV': '', 'PACKAGE': '', 'HAVE_STDIO_H': '', 'HAVE_RUBBERBAND': '', 'HAVE_VORBISENC': '', 'HAVE_AVFORMAT': '', 'HAVE_STDLIB_H': '', 'HAVE_UNISTD_H': '', 'HAVE_LIMITS_H': '', 'HAVE_CONFIG_H': '', 'NDEBUG': '', 'HAVE_STDARG_H': '', 'HAVE_SINK_APPLE_AUDIO': '', 'HAVE_ACCELERATE': '', 'HAVE_FLAC': '', 'HAVE_MATH_H': '', 'HAVE_AVUTIL': '', 'HAVE_SOURCE_APPLE_AUDIO': ''}
DEST_BINFMT = 'mac-o'
DEST_CPU = 'aarch64'
DEST_OS = 'darwin'
DOCDIR = '/usr/local/share/doc/aubio'
DVIDIR = '/usr/local/share/doc/aubio'
EXEC_PREFIX = '/usr/local'
FRAMEWORK = ['CoreFoundation', 'AudioToolbox', 'Accelerate']
FRAMEWORKPATH_ST = '-F%s'
FRAMEWORK_RUBBERBAND = ['Accelerate']
FRAMEWORK_ST = ['-framework']
HAVE_AVCODEC = 1
HAVE_AVFORMAT = 1
HAVE_AVUTIL = 1
HAVE_ERRNO_H = 1
HAVE_FLAC = 1
HAVE_GETOPT_H = 1
HAVE_LIMITS_H = 1
HAVE_MATH_H = 1
HAVE_RUBBERBAND = 1
HAVE_SAMPLERATE = 1
HAVE_SNDFILE = 1
HAVE_STDARG_H = 1
HAVE_STDIO_H = 1
HAVE_STDLIB_H = 1
HAVE_STRING_H = 1
HAVE_SWRESAMPLE = 1
HAVE_UNISTD_H = 1
HAVE_VORBISENC = 1
HTMLDIR = '/usr/local/share/doc/aubio'
INCLUDEDIR = '/usr/local/include'
INCLUDES_AVCODEC = ['/opt/homebrew/Cellar/ffmpeg/4.4_2/include']
INCLUDES_AVFORMAT = ['/opt/homebrew/Cellar/ffmpeg/4.4_2/include']
INCLUDES_AVUTIL = ['/opt/homebrew/Cellar/ffmpeg/4.4_2/include']
INCLUDES_FLAC = ['/opt/homebrew/Cellar/flac/1.3.3/include', '/opt/homebrew/Cellar/libogg/1.3.5/include']
INCLUDES_RUBBERBAND = ['/opt/homebrew/Cellar/rubberband/1.9.2/include', '/opt/homebrew/Cellar/libsamplerate/0.1.9_1/include']
INCLUDES_SAMPLERATE = ['/opt/homebrew/Cellar/libsamplerate/0.1.9_1/include']
INCLUDES_SNDFILE = ['/opt/homebrew/Cellar/libsndfile/1.0.31/include', '/opt/homebrew/Cellar/flac/1.3.3/include', '/opt/homebrew/Cellar/libvorbis/1.3.7/include', '/opt/homebrew/Cellar/libogg/1.3.5/include', '/opt/homebrew/Cellar/opus/1.3.1/include/opus']
INCLUDES_SWRESAMPLE = ['/opt/homebrew/Cellar/ffmpeg/4.4_2/include']
INCLUDES_VORBISENC = ['/opt/homebrew/Cellar/libvorbis/1.3.7/include', '/opt/homebrew/Cellar/libogg/1.3.5/include']
INFODIR = '/usr/local/share/info'
LIBDIR = '/usr/local/lib'
LIBEXECDIR = '/usr/local/libexec'
LIBPATH_AVCODEC = ['/opt/homebrew/Cellar/ffmpeg/4.4_2/lib']
LIBPATH_AVFORMAT = ['/opt/homebrew/Cellar/ffmpeg/4.4_2/lib']
LIBPATH_AVUTIL = ['/opt/homebrew/Cellar/ffmpeg/4.4_2/lib']
LIBPATH_FLAC = ['/opt/homebrew/Cellar/flac/1.3.3/lib']
LIBPATH_RUBBERBAND = ['/opt/homebrew/Cellar/rubberband/1.9.2/lib', '/opt/homebrew/Cellar/libsamplerate/0.1.9_1/lib']
LIBPATH_SAMPLERATE = ['/opt/homebrew/Cellar/libsamplerate/0.1.9_1/lib']
LIBPATH_SNDFILE = ['/opt/homebrew/Cellar/libsndfile/1.0.31/lib']
LIBPATH_ST = '-L%s'
LIBPATH_SWRESAMPLE = ['/opt/homebrew/Cellar/ffmpeg/4.4_2/lib']
LIBPATH_VORBISENC = ['/opt/homebrew/Cellar/libvorbis/1.3.7/lib', '/opt/homebrew/Cellar/libogg/1.3.5/lib']
LIB_AVCODEC = ['avcodec']
LIB_AVFORMAT = ['avformat']
LIB_AVUTIL = ['avutil']
LIB_FLAC = ['FLAC']
LIB_M = ['m']
LIB_RUBBERBAND = ['rubberband', 'samplerate']
LIB_SAMPLERATE = ['samplerate']
LIB_SNDFILE = ['sndfile']
LIB_ST = '-l%s'
LIB_SWRESAMPLE = ['swresample']
LIB_VORBISENC = ['vorbisenc', 'vorbis', 'ogg']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-dynamiclib']
LINKFLAGS_cstlib = []
LINK_CC = ['/usr/bin/clang']
LOCALEDIR = '/usr/local/share/locale'
LOCALSTATEDIR = '/usr/local/var'
MANDIR = '/usr/local/share/man'
OLDINCLUDEDIR = '/usr/include'
PACKAGE = 'aubio'
PDFDIR = '/usr/local/share/doc/aubio'
PKGCONFIG = ['/opt/homebrew/bin/pkg-config']
PREFIX = '/usr/local'
PSDIR = '/usr/local/share/doc/aubio'
RPATH_ST = '-Wl,-rpath,%s'
SBINDIR = '/usr/local/sbin'
SHAREDSTATEDIR = '/usr/local/com'
SHLIB_MARKER = []
SONAME_ST = []
STLIBPATH_ST = '-L%s'
STLIB_MARKER = []
STLIB_ST = '-l%s'
SYSCONFDIR = '/usr/local/etc'
cfg_files = ['/Users/timschoen/aubio/build/src/config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.dylib'
cstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_CONFIG_H', 'AUBIO_PREFIX', 'PACKAGE']
macbundle_PATTERN = '%s.bundle'
