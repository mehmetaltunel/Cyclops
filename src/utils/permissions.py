import sys
import os

def check_accessibility_permission() -> bool:
    """
    macOS icin erisilebilirlik iznini kontrol eder.
    Windows ve Linux icin her zaman True doner.
    """
    if sys.platform != 'darwin':
        return True

    try:
        # macOS'ta ctypes kullanarak ApplicationServices framework'une eriselim
        import ctypes
        # CoreGraphics/ApplicationServices framework'unu yukle
        app_services = ctypes.cdll.LoadLibrary('/System/Library/Frameworks/ApplicationServices.framework/ApplicationServices')
        
        # AXIsProcessTrusted fonksiyonunu cagir
        # Bu fonksiyon process'in trusted olup olmadigini doner
        is_trusted = app_services.AXIsProcessTrusted()
        return bool(is_trusted)
    except Exception as e:
        print(f"Izin kontrolu hatasi: {e}")
        # Hata durumunda (ornegin Windows'ta test edilirse) True donelim ki uygulama kapanmasin
        return True

def open_accessibility_settings():
    """
    macOS erisilebilirlik ayarlarini acar.
    """
    if sys.platform == 'darwin':
        try:
            import subprocess
            # Ayarlari ac
            cmd = "open 'x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility'"
            subprocess.run(cmd, shell=True)
        except:
            pass
