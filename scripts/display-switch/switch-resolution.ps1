param(
    [ValidateSet("1080", "3440")]
    [string]$Resolution = "1080"
)

Add-Type @"
using System;
using System.Runtime.InteropServices;

[StructLayout(LayoutKind.Sequential, CharSet = CharSet.Auto)]
public struct DEVMODE {
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 32)]
    public string dmDeviceName;
    public ushort dmSpecVersion;
    public ushort dmDriverVersion;
    public ushort dmSize;
    public ushort dmDriverExtra;
    public uint dmFields;
    public int dmPositionX;
    public int dmPositionY;
    public uint dmDisplayOrientation;
    public uint dmDisplayFixedOutput;
    public short dmColor;
    public short dmDuplex;
    public short dmYResolution;
    public short dmTTOption;
    public short dmCollate;
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 32)]
    public string dmFormName;
    public ushort dmLogPixels;
    public uint dmBitsPerPel;
    public uint dmPelsWidth;
    public uint dmPelsHeight;
    public uint dmDisplayFlags;
    public uint dmDisplayFrequency;
}

public class NativeMethods {
    [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    public static extern int ChangeDisplaySettingsEx(string lpszDeviceName, ref DEVMODE lpDevMode, IntPtr hwnd, uint dwflags, IntPtr lParam);
}

public class DisplaySettings {
    public static int ChangeResolution(int width, int height) {
        DEVMODE dm = new DEVMODE();
        dm.dmSize = (ushort)Marshal.SizeOf(typeof(DEVMODE));
        dm.dmPelsWidth = (uint)width;
        dm.dmPelsHeight = (uint)height;
        dm.dmFields = 0x180000;
        return NativeMethods.ChangeDisplaySettingsEx(null, ref dm, IntPtr.Zero, 0, IntPtr.Zero);
    }
}
"@

switch ($Resolution) {
    "1080" {
        $result = [DisplaySettings]::ChangeResolution(1920, 1080)
        if ($result -eq 0) {
            Write-Host "Changed to 1920x1080 successfully"
        } else {
            Write-Host "Failed. Error code: $result"
        }
    }
    "3440" {
        $result = [DisplaySettings]::ChangeResolution(3440, 1440)
        if ($result -eq 0) {
            Write-Host "Changed to 3440x1440 successfully"
        } else {
            Write-Host "Failed. Error code: $result"
        }
    }
}
