DEBUG =

TARGET = ckw.exe
CXX = cl
RC = rc
LD = link
RM = del
INC =
CXXFLAGS = -nologo -MT -O2 -W3 -EHsc -DNDEBUG $(INC)
LDFLAGS = -nologo
LDLIBS = user32.lib gdi32.lib shell32.lib shlwapi.lib imm32.lib
RFLAGS = -nologo -l 0x409

SRCS = main.cpp \
       misc.cpp \
       option.cpp \
       selection.cpp
OBJS = $(SRCS:.cpp=.obj) rsrc.res ckwmanifest.res

!IF "$(DEBUG)" != ""
CXXFLAGS = -nologo -MTd -Od -W3 -EHsc -D_DEBUG $(INC)
!ENDIF

.SUFFIXES:
.SUFFIXES: .exe .obj .cpp .rc .res

################################################################
all: ver $(TARGET)

ver:
	version.bat > version.h

$(TARGET): $(OBJS)
	$(LD) $(LDFLAGS) -out:$@ $(OBJS) $(LDLIBS)

.cpp.obj:
	$(CXX) $(CXXFLAGS) -Fo$@ -c $<

.rc.res:
	$(RC) $(RFLAGS) -fo $@ $<

clean:
	$(RM) -f $(OBJS) $(TARGET)


################################################################
SLNDIR = vc2010
SLNFILE = $(SLNDIR)/ckw.sln
MSBFLAGS = -p:Configuration=Release

!IF "$(DEBUG)" != ""
MSBFLAGS = -p:Configuration=Debug
!ENDIF

msbuild:
	msbuild $(MSBFLAGS) $(SLNFILE)

msbuildclean:
	msbuild $(MSBFLAGS) -t:clean $(SLNFILE)
