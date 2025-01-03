import os
import time
from datetime import datetime
from pathlib import Path
import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import argparse

class ScreenshotCapture:
    def __init__(self, save_folder, window_title):
        self.save_folder = Path(save_folder)
        self.window_title = window_title
        
    def setup(self):
        if not self.save_folder.exists():
            self.save_folder.mkdir(parents=True)
            print(f"Created folder: {self.save_folder}")
            
    def capture_window(self, hwnd):
        # Get window dimensions
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        width = right - left
        height = bottom - top
        
        # Create device context
        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        
        # Create bitmap
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
        saveDC.SelectObject(saveBitMap)
        
        # Copy window content
        result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 3)
        
        # Convert to PIL Image
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)
        image = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)
            
        # Clean up
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwndDC)
        
        return image
            
    def capture_screenshots(self, interval_minutes=1):
        print(f"Starting screenshot capture every {interval_minutes} minute{'s' if interval_minutes != 1 else ''}...")
        print(f"Looking for window: {self.window_title}")
        print(f"Press Ctrl+C to stop")
        
        # Convert minutes to seconds for time.sleep()
        interval_seconds = interval_minutes * 60
        
        while True:
            try:
                # Find window handle
                hwnd = win32gui.FindWindow(None, self.window_title)
                
                if hwnd == 0:
                    print(f"Cannot find window: {self.window_title}")
                    time.sleep(interval_seconds)
                    continue
                
                # Capture window
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = self.save_folder / f"screenshot_{timestamp}.png"
                
                image = self.capture_window(hwnd)
                image.save(str(filename))
                print(f"Screenshot saved: {filename}")
                
                time.sleep(interval_seconds)
                
            except KeyboardInterrupt:
                print("\nStopping screenshot capture...")
                break
            except Exception as e:
                print(f"Error capturing screenshot: {e}")
                time.sleep(interval_seconds)

def list_windows():
    print("Available windows:")
    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                print(f"- {title}")
    win32gui.EnumWindows(callback, None)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Capture screenshots of a specific window periodically')
    
    parser.add_argument('-f', '--folder', 
                        type=str, 
                        required=True,
                        help='Folder path to save screenshots')
    
    parser.add_argument('-w', '--window', 
                        type=str, 
                        required=True,
                        help='Window title to capture')
    
    parser.add_argument('-p', '--period', 
                        type=float, 
                        default=1,
                        help='Time period between captures in minutes (default: 1)')
    
    parser.add_argument('-l', '--list', 
                        action='store_true',
                        help='List all visible windows and exit')

    args = parser.parse_args()

    if args.list:
        list_windows()
        exit()

    capture = ScreenshotCapture(args.folder, args.window)
    capture.setup()
    
    print("\nStarting capture...")
    capture.capture_screenshots(args.period)