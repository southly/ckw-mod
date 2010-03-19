#ifndef __CKW_H__
#define __CKW_H__ 1

#define _WIN32_WINNT 0x0500
#define _UNICODE 1
#define  UNICODE 1
#include <windows.h>
#include <wchar.h>

#ifdef _MSC_VER
#define strcasecmp _stricmp
#endif
#ifndef COMMON_LVB_LEADING_BYTE
#define COMMON_LVB_LEADING_BYTE  0x0100
#endif
#ifndef COMMON_LVB_TRAILING_BYTE
#define COMMON_LVB_TRAILING_BYTE 0x0200
#endif

#define CSI_WndCols(csi) ((csi)->srWindow.Right - (csi)->srWindow.Left +1)
#define CSI_WndRows(csi) ((csi)->srWindow.Bottom - (csi)->srWindow.Top +1)

/* main.cpp */
extern HANDLE	gStdIn;
extern HANDLE	gStdOut;
extern DWORD	gFontW;
extern DWORD	gFontH;
extern DWORD	gBorderSize;
extern CONSOLE_SCREEN_BUFFER_INFO* gCSI;
extern CHAR_INFO*	gScreen;
BOOL WINAPI ReadConsoleOutput_Unicode(HANDLE,CHAR_INFO*,COORD,COORD,SMALL_RECT*);

/* selection.cpp */
BOOL	selectionGetArea(SMALL_RECT& sr);
void	selectionClear(HWND hWnd);
void	onLBtnDown(HWND hWnd, int x, int y);
void	onLBtnUp(HWND hWnd, int x, int y);
void	onMouseMove(HWND hWnd, int x, int y);

/* misc.cpp */
void	onPasteFromClipboard(HWND hWnd);
void	onDropFile(HDROP hDrop);
void	sysmenu_init(HWND hWnd);
BOOL	onSysCommand(HWND hWnd, DWORD id);

#endif /* __CKW_H__ */
